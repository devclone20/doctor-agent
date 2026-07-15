"""
Sanitização de outputs LaTeX gerados pelo Doctor Agent.

Bloqueia comandos que permitem execução de código externo, path traversal,
e redefinição perigosa de primitivas TeX — vectores documentados no LaTeX Security Guide.
"""

from __future__ import annotations

import re

# ---------------------------------------------------------------------------
# Padrões de comandos perigosos
# ---------------------------------------------------------------------------

# Comandos que requerem --shell-escape (execução de processos externos)
_SHELL_ESCAPE_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("\\write18",        re.compile(r"\\write18\b")),
    ("\\immediate\\write18", re.compile(r"\\immediate\\write18\b")),
    # minted requer pygmentize via shell
    ("\\begin{minted}", re.compile(r"\\begin\{minted\}")),
    # gnuplottex executa gnuplot via shell
    ("\\begin{gnuplot}", re.compile(r"\\begin\{gnuplot\}")),
    # svg com inkscape converter
    ("\\includesvg",    re.compile(r"\\includesvg\b")),
    # epstopdf em modo auto-convert
    ("\\epstopdf",      re.compile(r"\\epstopdf\b")),
]

# Comandos que são removidos por serem perigosos mesmo sem shell-escape
_DANGEROUS_COMMAND_PATTERNS: list[re.Pattern[str]] = [
    # Escrita directa de ficheiros do sistema
    re.compile(r"\\immediate\\write\s*\{[^}]*\}"),
    # \input com paths não-literais (detecta variáveis ou paths absolutos)
    re.compile(r"\\input\s*\{[^}]*(?:\.\.|/etc|/proc|/sys|/dev|C:\\\\|~)[^}]*\}"),
    # \include com paths suspeitos (path traversal)
    re.compile(r"\\include\s*\{[^}]*(?:\.\.|/etc|/proc|/sys|/dev|C:\\\\|~)[^}]*\}"),
    # \includegraphics com paths absolutos ou traversal
    re.compile(r"\\includegraphics(?:\[[^\]]*\])?\s*\{[^}]*(?:\.\.|/etc|/proc|C:\\\\)[^}]*\}"),
    # Redefinição de \catcode (altera tokenização — vector de injecção avançado)
    re.compile(r"\\catcode\s*`"),
    # \openout abre ficheiros arbitrários para escrita
    re.compile(r"\\openout\s*\d+\s*="),
    # \special com src= pode executar código em alguns drivers DVI
    re.compile(r"\\special\s*\{[^}]*src\s*="),
]


# ---------------------------------------------------------------------------
# API pública
# ---------------------------------------------------------------------------


def sanitize_latex_content(content: str) -> str:
    """
    Remove ou neutraliza comandos LaTeX perigosos de *content*.

    Comandos removidos:
    - ``\\write18`` e ``\\immediate\\write18`` (shell execution)
    - ``\\immediate\\write`` com handles de ficheiros do sistema
    - ``\\input`` / ``\\include`` com paths de path-traversal
    - ``\\includegraphics`` com paths absolutos ou de traversal
    - ``\\catcode`` alterações (vector de injecção de tokenização)
    - ``\\openout`` (escrita de ficheiros arbitrários)
    - ``\\special{src=...}`` (execução via drivers DVI)

    Não remove:
    - ``\\input{chapters/intro}`` — path relativo sem traversal (seguro)
    - ``\\includegraphics{figures/fig1.pdf}`` — path relativo dentro do projecto
    - ``\\write`` com ficheiro de output definido pelo utilizador (aviso gerado externamente)

    Returns the sanitised string. The caller is responsible for logging
    which patterns were matched — use ``check_latex_shell_escape`` for that.
    """
    result = content

    # Remove shell-escape triggers primeiro (mais críticos)
    result = re.sub(r"\\write18\b[^\n]*", r"% [SANITIZED: \\write18 removed]", result)
    result = re.sub(r"\\immediate\\write18\b[^\n]*", r"% [SANITIZED: \\immediate\\write18 removed]", result)

    # Remove cada padrão perigoso, substituindo pela linha comentada
    for pattern in _DANGEROUS_COMMAND_PATTERNS:
        result = pattern.sub(lambda m: f"% [SANITIZED: {m.group(0)[:60].strip()}]", result)

    return result


def check_latex_shell_escape(content: str) -> list[str]:
    """
    Retorna lista de strings descrevendo comandos que requerem ``--shell-escape``.

    Uma lista não vazia significa que o documento NÃO deve ser compilado
    com um compilador LaTeX standard sem sandboxing adicional.

    Each entry is a human-readable description of the match found, including
    the command name and the approximate location (line number).
    """
    findings: list[str] = []
    lines = content.splitlines()

    for line_no, line in enumerate(lines, start=1):
        for command_name, pattern in _SHELL_ESCAPE_PATTERNS:
            if pattern.search(line):
                findings.append(
                    f"Line {line_no}: requires --shell-escape → `{command_name}` "
                    f"(found: {line.strip()[:80]})"
                )

    return findings


def get_safe_latex_preamble() -> str:
    """
    Retorna um preâmbulo LaTeX seguro para dissertações IST.

    Inclui apenas pacotes que:
    - Não executam código externo
    - Não requerem ``--shell-escape``
    - Não abrem ficheiros arbitrários do sistema

    Pacotes explicitamente excluídos e porquê:
    - ``minted``        — requer pygmentize via shell
    - ``gnuplottex``    — executa gnuplot via shell
    - ``svg``           — modo inkscape requer shell
    - ``epstopdf``      — auto-convert requer Ghostscript via shell (usar ``epsfig`` em vez)
    - ``pythontex``     — executa Python via shell
    - ``sagetex``       — executa SageMath via shell
    """
    return r"""\documentclass[12pt,a4paper]{article}

% ── Encoding & Language ────────────────────────────────────────────────────
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[portuguese,english]{babel}

% ── Typography ─────────────────────────────────────────────────────────────
\usepackage{helvet}          % Arial equivalent (Helvetica)
\renewcommand{\familydefault}{\sfdefault}
\usepackage{microtype}       % Microtypography — no shell escape required

% ── Page Layout ────────────────────────────────────────────────────────────
\usepackage[
  top=2.5cm,
  bottom=2.5cm,
  left=2.5cm,
  right=2.5cm
]{geometry}
\usepackage{setspace}
\setstretch{1.5}

% ── Mathematics ────────────────────────────────────────────────────────────
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}

% ── Figures & Tables ───────────────────────────────────────────────────────
% NOTE: \includegraphics paths must be relative and within the project tree.
% Absolute paths and path-traversal sequences are blocked by latex_sanitizer.
\usepackage{graphicx}
\usepackage{booktabs}        % Professional table rules
\usepackage{tabularx}
\usepackage{longtable}
\usepackage{float}
\usepackage{caption}
\usepackage{subcaption}

% ── Code Listings (safe alternative to minted) ─────────────────────────────
% listings does NOT require --shell-escape
\usepackage{listings}
\usepackage{xcolor}
\lstset{
  basicstyle=\ttfamily\small,
  breaklines=true,
  frame=single,
  numbers=left,
  numberstyle=\tiny,
  captionpos=b,
}

% ── References (IEEE style) ────────────────────────────────────────────────
\usepackage[
  backend=biber,
  style=ieee,
  sorting=none
]{biblatex}

% ── Hyperlinks ─────────────────────────────────────────────────────────────
\usepackage[
  colorlinks=true,
  linkcolor=black,
  citecolor=black,
  urlcolor=blue,
  pdfauthor={},         % Leave blank — fill at document level, not here
  pdftitle={},
]{hyperref}
\usepackage{url}

% ── Algorithms (no shell-escape required) ──────────────────────────────────
\usepackage{algorithm}
\usepackage{algpseudocode}

% ── Miscellaneous ──────────────────────────────────────────────────────────
\usepackage{enumitem}
\usepackage{multirow}
\usepackage{array}
\usepackage{pdfpages}   % Include external PDFs (safe — no shell execution)

% ── Explicitly NOT included (require --shell-escape or external processes) ──
% minted, gnuplottex, svg (inkscape mode), epstopdf (auto), pythontex, sagetex
"""
