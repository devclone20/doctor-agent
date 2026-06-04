"""
PROPOSTA-DOC-1 — Sanitização de metadata Word
Limpa metadata sensível de documentos .docx gerados pelo Doctor.
"""

import logging
import re
from pathlib import Path

logger = logging.getLogger(__name__)

# Padrões de credenciais que nunca devem aparecer em conteúdo de documentos
_SECRET_PATTERNS: list[tuple[str, str]] = [
    (r"sk-[A-Za-z0-9]{20,}", "sk-***"),
    (r"ANTHROPIC_API_KEY\s*=\s*\S+", "ANTHROPIC_API_KEY=***"),
    (r"(?i)api[_-]?key\s*[=:]\s*\S{8,}", "api_key=***"),
    (r"(?i)access[_-]?token\s*[=:]\s*\S{8,}", "access_token=***"),
    (r"(?i)secret[_-]?key\s*[=:]\s*\S{8,}", "secret_key=***"),
    (r"AKIA[0-9A-Z]{16}", "AKIAXXXX"),
    # Bearer tokens
    (r"(?i)Bearer\s+[A-Za-z0-9\-._~+/]{20,}", "Bearer ***"),
    # JWT: três segmentos base64 separados por ponto
    (r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}", "***jwt-redacted***"),
]

# Endereços de email a remover por default (qualquer email que não seja explicitamente preservado)
_EMAIL_PATTERN = re.compile(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}")


def sanitize_docx_metadata(path: Path) -> dict:
    """
    Abre um .docx e limpa metadata sensível:
      - Core properties: author, last_modified_by, company, manager
      - Comentários (w:comment / w:commentReference)
      - Track changes residuais (w:ins, w:del)
      - Custom XML parts corporativas

    Retorna dict com relatório do que foi alterado.
    """
    try:
        from docx import Document
        from docx.oxml.ns import qn
    except ImportError as exc:
        raise RuntimeError(
            "python-docx não está instalado. "
            "Instalar com: pip install python-docx"
        ) from exc

    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Ficheiro não encontrado: {path}")
    if path.suffix.lower() != ".docx":
        raise ValueError(f"Ficheiro não é .docx: {path}")

    doc = Document(str(path))
    report: dict = {
        "author_cleared": False,
        "last_modified_by_cleared": False,
        "company_cleared": False,
        "manager_cleared": False,
        "comments_removed": 0,
        "track_changes_removed": 0,
        "custom_xml_parts_removed": 0,
    }

    # --- Core properties ---
    props = doc.core_properties
    if props.author:
        props.author = "Doctor Agent"
        report["author_cleared"] = True
    if props.last_modified_by:
        props.last_modified_by = "Doctor Agent"
        report["last_modified_by_cleared"] = True

    # company e manager não têm setter nativo; editar directamente no XML
    try:
        from docx.oxml import parse_xml
        from lxml import etree

        ext_props = doc.part.package.part_related_by(
            "http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties"
        )
        tree = ext_props._element
        for tag in ("Company", "Manager"):
            el = tree.find(
                f"{{http://schemas.openxmlformats.org/officeDocument/2006/extended-properties}}{tag}"
            )
            if el is not None and el.text:
                if tag == "Company":
                    el.text = "IST Lisboa"
                    report["company_cleared"] = True
                else:
                    el.text = ""
                    report["manager_cleared"] = True
    except Exception as exc:
        logger.debug("Sem extended-properties ou erro ao limpar: %s", exc)

    # --- Comentários ---
    body = doc.element.body
    # Remover elementos w:comment do document.xml (raramente aqui, mas defensivo)
    for comment_ref in body.findall(f".//{qn('w:commentReference')}"):
        parent = comment_ref.getparent()
        if parent is not None:
            parent.remove(comment_ref)
            report["comments_removed"] += 1

    # Tentar aceder à part de comentários e limpar
    try:
        comments_part = doc.part.part_related_by(
            "http://schemas.openxmlformats.org/officeDocument/2006/relationships/comments"
        )
        comments_root = comments_part._element
        comment_elements = comments_root.findall(
            f"{{{qn('w:comment').split('}')[0].lstrip('{')}}}"
            f"comment"
        ) or comments_root.findall(f".//{qn('w:comment')}")
        for comment_el in list(comment_elements):
            comments_root.remove(comment_el)
            report["comments_removed"] += 1
    except Exception:
        pass  # Sem part de comentários — normal

    # --- Track changes (w:ins e w:del) ---
    for tag in (qn("w:ins"), qn("w:del")):
        for el in body.findall(f".//{tag}"):
            parent = el.getparent()
            if parent is not None:
                # Preservar o texto dentro de w:ins antes de remover o wrapper
                if tag == qn("w:ins"):
                    for child in list(el):
                        parent.insert(list(parent).index(el), child)
                parent.remove(el)
                report["track_changes_removed"] += 1

    # --- Custom XML parts ---
    try:
        pkg = doc.part.package
        custom_xml_rel_type = (
            "http://schemas.openxmlformats.org/officeDocument/2006/relationships/customXml"
        )
        to_remove = []
        for rel in pkg.rels.values():
            if rel.reltype == custom_xml_rel_type:
                to_remove.append(rel)
        for rel in to_remove:
            pkg.rels.pop(rel.rId, None)
            report["custom_xml_parts_removed"] += 1
    except Exception as exc:
        logger.debug("Sem custom XML parts ou erro: %s", exc)

    doc.save(str(path))
    logger.info("Metadata sanitizada em %s: %s", path.name, report)
    return report


def sanitize_docx_content(content: str, preserve_emails: list[str] | None = None) -> str:
    """
    Sanitiza conteúdo em texto puro antes de escrever num .docx:
      - Remove padrões de API keys, tokens, secrets
      - Remove endereços de email salvo os listados em `preserve_emails`

    Retorna o conteúdo limpo.
    """
    preserve_set = set(e.lower() for e in (preserve_emails or []))

    # Aplicar redacção de secrets
    for pattern, replacement in _SECRET_PATTERNS:
        content = re.sub(pattern, replacement, content)

    # Remover emails não preservados
    def _redact_email(match: re.Match) -> str:
        email = match.group(0)
        if email.lower() in preserve_set:
            return email
        return "[email redacted]"

    content = _EMAIL_PATTERN.sub(_redact_email, content)
    return content


def get_sanitization_prompt() -> str:
    """
    Instrução de sistema para o agente Doctor: nunca incluir credenciais,
    tokens, ou metadata pessoal nos documentos gerados.
    """
    return (
        "REGRA DE SEGURANÇA — DOCUMENTOS: "
        "Nunca incluas credenciais, API keys, tokens, palavras-passe, "
        "endereços de email pessoais, nomes de empresa internos, "
        "ou qualquer metadata sensível no conteúdo de documentos gerados. "
        "Documentos académicos devem conter apenas conteúdo científico. "
        "Se precisares de referenciar um endereço de email, usa apenas o "
        "endereço institucional explicitamente fornecido pelo utilizador. "
        "Qualquer string com padrão sk-***, AKIA***, Bearer *** é um secret "
        "e não deve aparecer em nenhum ficheiro de output."
    )
