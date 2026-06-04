"""
Gestão de ficheiros BibTeX persistentes — PROPOSTA-DOC-2.

Centraliza a criação, deduplicação e exportação de entradas bibliográficas
num único ficheiro .bib, integrando com o pipeline de citações do Doctor.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Helpers de parsing / serialização BibTeX
# ---------------------------------------------------------------------------

def _bibtex_key_from_paper(paper: dict[str, Any]) -> str:
    """
    Gera uma chave BibTeX no formato AuthorANO (ex: Vaswani2017attention).

    Usa o apelido do primeiro autor + ano + primeira palavra do título.
    Garante que a chave é válida para LaTeX: apenas [a-zA-Z0-9_-].
    """
    authors_str: str = paper.get("authors", "")
    year: str | int = paper.get("year", "0000")
    title: str = paper.get("title", "")

    first_author_last = ""
    if authors_str:
        # Primeiro autor — último token do nome
        first_author = authors_str.split(",")[0].strip()
        first_author_last = first_author.split()[-1] if first_author else "Unknown"

    title_words = re.findall(r"[a-zA-Z]+", title)
    key_word = title_words[0].capitalize() if title_words else "paper"

    raw = f"{first_author_last}{year}{key_word}"
    # Sanitizar para LaTeX: apenas alfanumérico + underscore
    return re.sub(r"[^a-zA-Z0-9_]", "", raw)


def _parse_bib_entries(bib_text: str) -> dict[str, str]:
    """
    Extrai entradas BibTeX existentes num ficheiro .bib.

    Retorna {key: full_entry_text}. Parsing tolerante a formatações variadas.
    """
    entries: dict[str, str] = {}
    # Encontrar todas as entradas @type{key, ...}
    pattern = re.compile(
        r"(@\w+\s*\{\s*([^,\s]+)\s*,.*?\n\})",
        re.DOTALL,
    )
    for match in pattern.finditer(bib_text):
        full_entry = match.group(1)
        key = match.group(2).strip()
        entries[key] = full_entry
    return entries


# ---------------------------------------------------------------------------
# BibliographyManager
# ---------------------------------------------------------------------------

class BibliographyManager:
    """
    Gestor de ficheiro BibTeX persistente.

    Carrega um .bib existente (ou cria um vazio), permite adicionar entradas
    via DOI, título ou manualmente, e exporta o ficheiro actualizado.

    Usage::

        bm = BibliographyManager(Path("~/doctor-work/bibliography.bib"))
        key = bm.add_from_doi("10.1145/3295500.3356196")
        bm.save()
        print(bm.export_bib())
    """

    def __init__(self, bib_path: Path) -> None:
        self._path = bib_path.expanduser().resolve()
        # {key: bibtex_entry_string}
        self._entries: dict[str, str] = {}
        self._load()

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def _load(self) -> None:
        """Carrega entradas do ficheiro .bib existente (se existir)."""
        if self._path.exists():
            content = self._path.read_text(encoding="utf-8", errors="replace")
            self._entries = _parse_bib_entries(content)

    def save(self, path: Path | None = None) -> None:
        """Guarda o ficheiro .bib no disco.

        path: destino alternativo (default: path passado no __init__)
        """
        target = (path.expanduser().resolve() if path else self._path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(self.export_bib(), encoding="utf-8")

    # ------------------------------------------------------------------
    # Mutators
    # ------------------------------------------------------------------

    def _add_entry(self, paper: dict[str, Any]) -> str:
        """
        Adiciona uma entrada derivada de um paper dict.

        Gera a chave, verifica duplicados por DOI/título, e insere no dicionário
        interno. Retorna a chave gerada.
        """
        # Deduplicar por DOI quando disponível
        doi = (paper.get("doi") or "").strip()
        if doi:
            for key, entry in self._entries.items():
                if doi in entry:
                    return key  # já existe — retornar key existente

        bibtex: str = paper.get("bibtex", "")
        if not bibtex:
            # Gerar BibTeX mínimo se a fonte não o forneceu
            from doctor.core.academic_search import build_bibtex
            bibtex = build_bibtex(paper)

        key = _bibtex_key_from_paper(paper)

        # Garantir unicidade da chave (evitar colisão)
        if key in self._entries:
            suffix = 2
            base_key = key
            while key in self._entries:
                key = f"{base_key}_{suffix}"
                suffix += 1
            # Substituir a chave no texto BibTeX gerado
            bibtex = re.sub(
                r"(@\w+\{)\s*[^,\s]+",
                lambda m: f"{m.group(1)}{key}",
                bibtex,
                count=1,
            )

        self._entries[key] = bibtex
        return key

    def add_from_doi(self, doi: str) -> str:
        """
        Adiciona uma entrada bibliográfica pelo DOI.

        Consulta a CrossRef para obter metadados completos.
        Retorna a chave BibTeX gerada (formato AuthorANOtítulo).
        Lança ValueError se o DOI não for encontrado.
        """
        from doctor.core.academic_search import lookup_doi

        paper = lookup_doi(doi)
        if not paper:
            raise ValueError(f"DOI não encontrado: {doi!r}")
        return self._add_entry(paper)

    def add_from_title(self, title: str) -> str:
        """
        Adiciona uma entrada bibliográfica pelo título do artigo.

        Pesquisa na CrossRef e selecciona o resultado com maior sobreposição
        de palavras. Retorna a chave BibTeX gerada.
        Lança ValueError se nenhuma correspondência for encontrada.
        """
        from doctor.core.academic_search import cite_from_title

        paper = cite_from_title(title, style="all")
        if not paper:
            raise ValueError(f"Artigo não encontrado para título: {title!r}")
        return self._add_entry(paper)

    def add_manual(self, entry: dict[str, Any]) -> str:
        """
        Adiciona uma entrada bibliográfica manualmente.

        entry deve conter pelo menos "title" e idealmente "authors", "year",
        "venue" (ou "journal"/"booktitle"). Opcionalmente "bibtex" pré-formatado.

        Retorna a chave BibTeX gerada.
        """
        return self._add_entry(entry)

    # ------------------------------------------------------------------
    # Queries
    # ------------------------------------------------------------------

    def get_all_keys(self) -> list[str]:
        """Retorna todas as chaves BibTeX no ficheiro, por ordem de inserção."""
        return list(self._entries.keys())

    def export_bib(self) -> str:
        """
        Retorna o conteúdo completo do ficheiro .bib como string.

        Inclui cabeçalho de identificação e todas as entradas separadas por
        linha em branco.
        """
        header = (
            "% Bibliography managed by Doctor Agent\n"
            "% Do not edit manually — use: doctor bibliography add-doi / add-title\n"
            f"% Entries: {len(self._entries)}\n\n"
        )
        return header + "\n\n".join(self._entries.values()) + "\n"

    def to_ieee_list(self) -> str:
        """
        Formata todas as entradas como lista IEEE numerada.

        Útil para copiar directamente para um documento Markdown ou verificar
        as referências sem compilar LaTeX.
        """
        from doctor.core.academic_search import build_ieee_citation, build_bibtex
        import re as _re

        lines: list[str] = []
        for i, (key, entry) in enumerate(self._entries.items(), start=1):
            # Extrair campos básicos do BibTeX para reconstruir citação IEEE
            def _field(name: str) -> str:
                m = _re.search(rf"{name}\s*=\s*\{{([^}}]*)\}}", entry, _re.IGNORECASE)
                return m.group(1).strip() if m else ""

            paper: dict[str, Any] = {
                "title":   _field("title"),
                "authors": _field("author"),
                "year":    _field("year"),
                "venue":   _field("booktitle") or _field("journal"),
                "doi":     _field("doi"),
                "url":     _field("url"),
            }
            ieee = build_ieee_citation(paper, ref_num=i)
            lines.append(ieee)

        return "\n".join(lines)
