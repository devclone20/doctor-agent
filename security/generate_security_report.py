"""
Gerador de relatório de segurança consolidado — PROPOSTA-HACK-1.

Combina os outputs de Gitleaks e pip-audit num único relatório Markdown
com sumário executivo, findings por severidade e recomendações.

Uso:
    python security/generate_security_report.py \\
        --gitleaks gitleaks-report.json \\
        --pip-audit pip-audit-report.json \\
        --output security-report.md

Exit codes:
    0 — sem findings críticos
    1 — um ou mais findings CRITICAL detectados
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

@dataclass
class SecretFinding:
    rule_id: str
    description: str
    file: str
    line_start: int
    author: str
    commit: str
    severity: str = "CRITICAL"


@dataclass
class VulnFinding:
    package: str
    installed_version: str
    vuln_id: str
    description: str
    fix_version: str
    severity: str


@dataclass
class SecurityReport:
    generated_at: str
    secrets: list[SecretFinding] = field(default_factory=list)
    vulns: list[VulnFinding] = field(default_factory=list)

    @property
    def critical_count(self) -> int:
        return sum(1 for s in self.secrets if s.severity == "CRITICAL") + \
               sum(1 for v in self.vulns if v.severity.upper() == "CRITICAL")

    @property
    def high_count(self) -> int:
        return sum(1 for v in self.vulns if v.severity.upper() == "HIGH")

    @property
    def medium_count(self) -> int:
        return sum(1 for v in self.vulns if v.severity.upper() == "MEDIUM")

    @property
    def low_count(self) -> int:
        return sum(1 for v in self.vulns if v.severity.upper() in ("LOW", "UNKNOWN"))


# ---------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------

def _parse_gitleaks(path: Path) -> list[SecretFinding]:
    """
    Lê gitleaks-report.json e converte para SecretFinding.

    Gitleaks pode gerar null (sem findings) ou uma lista de objectos.
    Tolerante a ficheiros ausentes.
    """
    if not path.exists():
        return []

    raw = path.read_text(encoding="utf-8").strip()
    if not raw or raw == "null":
        return []

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return []

    if not isinstance(data, list):
        return []

    findings: list[SecretFinding] = []
    for item in data:
        findings.append(SecretFinding(
            rule_id=item.get("RuleID", item.get("ruleID", "unknown")),
            description=item.get("Description", item.get("description", "")),
            file=item.get("File", item.get("file", "")),
            line_start=int(item.get("StartLine", item.get("startLine", 0))),
            author=item.get("Author", item.get("author", "")),
            commit=str(item.get("Commit", item.get("commit", "")))[:12],
            severity="CRITICAL",
        ))
    return findings


def _severity_from_aliases(aliases: list[str]) -> str:
    """
    Infere severidade a partir de CVE aliases ou fallback para 'UNKNOWN'.

    pip-audit não expõe sempre a severidade directamente — usamos a
    presença de CVE IDs como proxy (todos são tratados como HIGH por defeito).
    """
    for alias in aliases:
        if alias.startswith("GHSA"):
            # GitHub Advisory — assume HIGH (conservador sem chamar a API)
            return "HIGH"
        if alias.startswith("CVE"):
            return "HIGH"
        if alias.startswith("PYSEC"):
            return "MEDIUM"
    return "UNKNOWN"


def _parse_pip_audit(path: Path) -> list[VulnFinding]:
    """
    Lê pip-audit-report.json e converte para VulnFinding.

    pip-audit --output=json gera:
    {"dependencies": [{"name": ..., "version": ..., "vulns": [...]}, ...]}
    """
    if not path.exists():
        return []

    raw = path.read_text(encoding="utf-8").strip()
    if not raw:
        return []

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return []

    findings: list[VulnFinding] = []

    # pip-audit pode gerar lista directa ou wrapper {"dependencies": [...]}
    deps: list[dict] = []
    if isinstance(data, list):
        deps = data
    elif isinstance(data, dict):
        deps = data.get("dependencies", [])

    for dep in deps:
        vulns = dep.get("vulns", [])
        for vuln in vulns:
            aliases: list[str] = vuln.get("aliases", [])
            fix_versions = vuln.get("fix_versions", [])
            fix_str = ", ".join(fix_versions) if fix_versions else "no fix available"
            severity = _severity_from_aliases(aliases)
            findings.append(VulnFinding(
                package=dep.get("name", "unknown"),
                installed_version=dep.get("version", "?"),
                vuln_id=vuln.get("id", aliases[0] if aliases else "UNKNOWN"),
                description=vuln.get("description", "")[:300],
                fix_version=fix_str,
                severity=severity,
            ))

    return findings


# ---------------------------------------------------------------------------
# Report renderer
# ---------------------------------------------------------------------------

def _render_markdown(report: SecurityReport) -> str:
    has_critical = report.critical_count > 0
    status_badge = "FAIL" if has_critical else "PASS"

    lines: list[str] = [
        "# Security Audit Report",
        f"",
        f"**Generated:** {report.generated_at}",
        f"**Status:** `{status_badge}`",
        f"",
        "---",
        "",
        "## Executive Summary",
        "",
        "| Category              | Count |",
        "|----------------------|-------|",
        f"| Secrets / leaked keys | {len(report.secrets)} |",
        f"| CRITICAL CVEs         | {report.critical_count - len(report.secrets)} |",
        f"| HIGH CVEs             | {report.high_count} |",
        f"| MEDIUM CVEs           | {report.medium_count} |",
        f"| LOW / UNKNOWN CVEs    | {report.low_count} |",
        f"| **Total findings**    | **{len(report.secrets) + len(report.vulns)}** |",
        "",
    ]

    # --- Secrets section ---
    lines += ["---", "", "## Secrets Found (Gitleaks)", ""]
    if not report.secrets:
        lines.append("No secrets detected.")
    else:
        lines.append(
            "| Severity | Rule | File | Line | Author | Commit |"
        )
        lines.append(
            "|----------|------|------|------|--------|--------|"
        )
        for s in report.secrets:
            lines.append(
                f"| **{s.severity}** | `{s.rule_id}` | `{s.file}` "
                f"| {s.line_start} | {s.author} | `{s.commit}` |"
            )
        lines.append("")
        lines.append(
            "> **Action required:** rotate any exposed credentials immediately, "
            "then remove from git history using `git filter-repo` or BFG."
        )
    lines.append("")

    # --- Vulnerable dependencies section ---
    lines += ["---", "", "## Vulnerable Dependencies (pip-audit)", ""]
    if not report.vulns:
        lines.append("No vulnerable dependencies detected.")
    else:
        lines.append(
            "| Severity | Package | Installed | Vulnerability | Fix Version | Description |"
        )
        lines.append(
            "|----------|---------|-----------|---------------|-------------|-------------|"
        )
        for v in report.vulns:
            short_desc = v.description[:120].replace("|", "/")
            lines.append(
                f"| **{v.severity}** | `{v.package}` | `{v.installed_version}` "
                f"| [{v.vuln_id}](https://osv.dev/vulnerability/{v.vuln_id}) "
                f"| `{v.fix_version}` | {short_desc} |"
            )
    lines.append("")

    # --- Recommendations ---
    lines += ["---", "", "## Recommendations", ""]
    if report.secrets:
        lines += [
            "### Secrets",
            "- Rotate all exposed credentials immediately.",
            "- Add patterns to `.gitleaksignore` only after confirming false positives.",
            "- Enable pre-commit hook: `gitleaks protect --staged`.",
            "",
        ]
    if report.vulns:
        critical_pkgs = {v.package for v in report.vulns if v.severity.upper() == "CRITICAL"}
        high_pkgs = {v.package for v in report.vulns if v.severity.upper() == "HIGH"}
        lines += [
            "### Dependencies",
        ]
        if critical_pkgs:
            lines.append(f"- **Immediate:** update {', '.join(f'`{p}`' for p in sorted(critical_pkgs))}.")
        if high_pkgs:
            lines.append(f"- **This sprint:** update {', '.join(f'`{p}`' for p in sorted(high_pkgs))}.")
        lines += [
            "- Run `pip-audit --fix` in a branch, review changes, then merge.",
            "- Pin transitive dependencies in `pyproject.toml` to prevent silent upgrades.",
            "",
        ]
    if not report.secrets and not report.vulns:
        lines.append("No action required. Continue running audits on every push.")

    lines += [
        "---",
        "",
        "*Generated by Doctor Agent security pipeline.*",
    ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate consolidated Markdown security report from Gitleaks and pip-audit JSON outputs.",
    )
    parser.add_argument(
        "--gitleaks",
        default="gitleaks-report.json",
        help="Path to gitleaks JSON report (default: gitleaks-report.json)",
    )
    parser.add_argument(
        "--pip-audit",
        dest="pip_audit",
        default="pip-audit-report.json",
        help="Path to pip-audit JSON report (default: pip-audit-report.json)",
    )
    parser.add_argument(
        "--output",
        default="security-report.md",
        help="Output Markdown file (default: security-report.md)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)

    secrets = _parse_gitleaks(Path(args.gitleaks))
    vulns = _parse_pip_audit(Path(args.pip_audit))

    report = SecurityReport(
        generated_at=datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        secrets=secrets,
        vulns=vulns,
    )

    markdown = _render_markdown(report)
    Path(args.output).write_text(markdown, encoding="utf-8")

    print(f"Security report written to: {args.output}")
    print(
        f"Summary — Secrets: {len(secrets)} | "
        f"CRITICAL: {report.critical_count} | HIGH: {report.high_count} | "
        f"MEDIUM: {report.medium_count} | LOW: {report.low_count}"
    )

    return 1 if report.critical_count > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
