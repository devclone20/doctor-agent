"""
PROPOSTA-DOC-5 — Pipeline anti-alucinação de citações
Verificação tripla de citações via CrossRef, OpenAlex e Semantic Scholar.
"""

import logging
import re
import time
from typing import Any

import requests

logger = logging.getLogger(__name__)

# Rate limiting: 1 req/s por fonte (partilhado via timestamps)
_LAST_CALL: dict[str, float] = {}
_RATE_LIMIT_SECONDS = 1.0

_HEADERS = {
    "User-Agent": (
        "DoctorAgent/1.0 (academic citation verification; "
        "contact: doctor-agent@ist.ulisboa.pt)"
    )
}


# ---------------------------------------------------------------------------
# Helpers internos
# ---------------------------------------------------------------------------

def _throttle(source: str) -> None:
    """Garante no mínimo 1 segundo entre chamadas à mesma fonte."""
    now = time.monotonic()
    last = _LAST_CALL.get(source, 0.0)
    wait = _RATE_LIMIT_SECONDS - (now - last)
    if wait > 0:
        time.sleep(wait)
    _LAST_CALL[source] = time.monotonic()


def _word_overlap_score(query: str, result_title: str) -> float:
    """
    Score simples de sobreposição de palavras entre títulos (0.0–1.0).
    Remove stop words e pontuação básica para um matching mais robusto.
    """
    stop = {
        "a", "an", "the", "of", "in", "on", "at", "to", "for",
        "and", "or", "with", "by", "from", "is", "are", "was",
    }

    def tokenise(text: str) -> set[str]:
        words = re.sub(r"[^a-z0-9\s]", "", text.lower()).split()
        return {w for w in words if w not in stop and len(w) > 2}

    q_words = tokenise(query)
    r_words = tokenise(result_title)
    if not q_words or not r_words:
        return 0.0
    intersection = q_words & r_words
    return len(intersection) / max(len(q_words), len(r_words))


def _year_matches(expected: int | None, found: int | None) -> bool | None:
    """
    Retorna True se anos coincidem, False se discrepância confirmada,
    None se um dos valores é desconhecido.
    """
    if expected is None or found is None:
        return None
    return abs(expected - found) <= 1  # tolerar 1 ano (preprint vs publicado)


# ---------------------------------------------------------------------------
# Clientes por fonte
# ---------------------------------------------------------------------------

def _query_crossref(title: str) -> list[dict]:
    """CrossRef Works API — retorna até 3 resultados."""
    _throttle("crossref")
    try:
        resp = requests.get(
            "https://api.crossref.org/works",
            params={"query.title": title, "rows": 3, "select": "title,author,published,DOI"},
            headers=_HEADERS,
            timeout=10,
        )
        resp.raise_for_status()
        items = resp.json().get("message", {}).get("items", [])
        results = []
        for item in items:
            title_parts = item.get("title", [])
            found_title = title_parts[0] if title_parts else ""
            authors = item.get("author", [])
            author_str = "; ".join(
                f"{a.get('family', '')} {a.get('given', '')[:1]}".strip()
                for a in authors[:3]
            )
            pub = item.get("published", {}).get("date-parts", [[None]])
            year = pub[0][0] if pub and pub[0] else None
            results.append({
                "source": "crossref",
                "title": found_title,
                "authors": author_str,
                "year": year,
                "doi": item.get("DOI"),
                "score": _word_overlap_score(title, found_title),
            })
        return results
    except Exception as exc:
        logger.warning("CrossRef query falhou para '%s': %s", title[:60], exc)
        return []


def _query_openalex(title: str) -> list[dict]:
    """OpenAlex API — retorna até 3 resultados."""
    _throttle("openalex")
    try:
        resp = requests.get(
            "https://api.openalex.org/works",
            params={"search": title, "per-page": 3, "select": "title,authorships,publication_year,doi"},
            headers=_HEADERS,
            timeout=10,
        )
        resp.raise_for_status()
        items = resp.json().get("results", [])
        results = []
        for item in items:
            found_title = item.get("title") or ""
            authorships = item.get("authorships", [])
            author_str = "; ".join(
                a.get("author", {}).get("display_name", "")
                for a in authorships[:3]
            )
            doi = item.get("doi") or ""
            if doi.startswith("https://doi.org/"):
                doi = doi[len("https://doi.org/"):]
            results.append({
                "source": "openalex",
                "title": found_title,
                "authors": author_str,
                "year": item.get("publication_year"),
                "doi": doi or None,
                "score": _word_overlap_score(title, found_title),
            })
        return results
    except Exception as exc:
        logger.warning("OpenAlex query falhou para '%s': %s", title[:60], exc)
        return []


def _query_semantic_scholar(title: str) -> list[dict]:
    """Semantic Scholar Graph API — retorna até 3 resultados."""
    _throttle("semantic_scholar")
    try:
        resp = requests.get(
            "https://api.semanticscholar.org/graph/v1/paper/search",
            params={
                "query": title,
                "limit": 3,
                "fields": "title,authors,year,externalIds",
            },
            headers=_HEADERS,
            timeout=10,
        )
        resp.raise_for_status()
        items = resp.json().get("data", [])
        results = []
        for item in items:
            found_title = item.get("title") or ""
            authors = item.get("authors", [])
            author_str = "; ".join(a.get("name", "") for a in authors[:3])
            ext = item.get("externalIds", {})
            doi = ext.get("DOI")
            results.append({
                "source": "semantic_scholar",
                "title": found_title,
                "authors": author_str,
                "year": item.get("year"),
                "doi": doi,
                "score": _word_overlap_score(title, found_title),
            })
        return results
    except Exception as exc:
        logger.warning("Semantic Scholar query falhou para '%s': %s", title[:60], exc)
        return []


# ---------------------------------------------------------------------------
# API pública
# ---------------------------------------------------------------------------

def verify_citation(
    title: str,
    authors: str = "",
    year: int | None = None,
) -> dict:
    """
    Pipeline de tripla verificação de uma citação.

    Consulta CrossRef, OpenAlex e Semantic Scholar.
    Para cada fonte, calcula score de confiança por sobreposição de palavras.

    Retorna:
        {
            "verified": bool,           # True se score >= 0.7 em >= 2 fontes
            "confidence": float,        # Score médio das fontes com melhor resultado
            "sources_found": int,       # Número de fontes com score >= 0.5
            "best_match": dict,         # Melhor resultado encontrado
            "discrepancies": list[str], # Divergências detectadas (ano, autores)
        }
    """
    if not title or not title.strip():
        return {
            "verified": False,
            "confidence": 0.0,
            "sources_found": 0,
            "best_match": {},
            "discrepancies": ["Título vazio — não verificável"],
        }

    all_results: list[dict] = []
    all_results.extend(_query_crossref(title))
    all_results.extend(_query_openalex(title))
    all_results.extend(_query_semantic_scholar(title))

    if not all_results:
        return {
            "verified": False,
            "confidence": 0.0,
            "sources_found": 0,
            "best_match": {},
            "discrepancies": ["Nenhuma fonte respondeu"],
        }

    # Melhor resultado por score
    best = max(all_results, key=lambda r: r["score"])
    scores_per_source = {}
    for r in all_results:
        src = r["source"]
        if r["score"] > scores_per_source.get(src, 0.0):
            scores_per_source[src] = r["score"]

    sources_with_match = [s for s, sc in scores_per_source.items() if sc >= 0.5]
    sources_found = len(sources_with_match)
    confidence = (
        sum(scores_per_source[s] for s in sources_with_match) / len(sources_with_match)
        if sources_with_match else 0.0
    )
    verified = confidence >= 0.7 and sources_found >= 2

    discrepancies: list[str] = []
    if best["score"] < 0.5:
        discrepancies.append(f"Título não coincide com nenhum resultado (melhor score: {best['score']:.2f})")

    if year is not None and best.get("year"):
        year_ok = _year_matches(year, int(best["year"]))
        if year_ok is False:
            discrepancies.append(
                f"Ano discrepante: passado={year}, encontrado={best['year']}"
            )

    if authors and best.get("authors"):
        # Comparar apelido do primeiro autor
        first_passed = authors.split()[0].lower().rstrip(",;")
        first_found = best["authors"].split()[0].lower().rstrip(",;")
        if first_passed and first_found and first_passed not in first_found and first_found not in first_passed:
            discrepancies.append(
                f"Primeiro autor discrepante: passado='{first_passed}', encontrado='{first_found}'"
            )

    return {
        "verified": verified,
        "confidence": round(confidence, 3),
        "sources_found": sources_found,
        "best_match": best,
        "discrepancies": discrepancies,
    }


def batch_verify_citations(citations: list[dict]) -> list[dict]:
    """
    Verifica uma lista de citações com rate limiting (1 req/s por fonte).

    Cada elemento da lista pode ser:
      - str: tratado como título
      - dict com chaves "title" (obrigatório), "authors" (opcional), "year" (opcional)

    Retorna lista com os resultados de verify_citation para cada item,
    acrescentando o campo "input" com a citação original.
    """
    results = []
    for item in citations:
        if isinstance(item, str):
            citation_dict = {"title": item}
        elif isinstance(item, dict):
            citation_dict = item
        else:
            results.append({
                "input": item,
                "verified": False,
                "confidence": 0.0,
                "sources_found": 0,
                "best_match": {},
                "discrepancies": ["Formato inválido — esperado str ou dict"],
            })
            continue

        title = citation_dict.get("title", "")
        authors = citation_dict.get("authors", "")
        year = citation_dict.get("year")
        if isinstance(year, str) and year.isdigit():
            year = int(year)

        result = verify_citation(title, authors=authors, year=year)
        result["input"] = citation_dict
        results.append(result)

    return results


def citation_hallucination_report(citations: list[dict]) -> str:
    """
    Formata relatório de verificação de citações.

    Aceita a lista de resultados de batch_verify_citations.
    Usa prefixos de texto: [OK], [WARN], [FAIL] para compatibilidade universal.
    """
    if not citations:
        return "Nenhuma citação para verificar."

    verified_count = sum(1 for c in citations if c.get("verified"))
    warn_count = sum(
        1 for c in citations if not c.get("verified") and c.get("sources_found", 0) > 0
    )
    fail_count = len(citations) - verified_count - warn_count

    lines = [
        "=== Relatorio de Verificacao de Citacoes ===",
        f"Total: {len(citations)} | Verificadas: {verified_count} | "
        f"Nao encontradas: {warn_count} | Discrepancias: {fail_count}",
        "",
    ]

    for i, c in enumerate(citations, 1):
        inp = c.get("input", {})
        title = inp.get("title", str(inp)) if isinstance(inp, dict) else str(inp)
        short_title = title[:80] + ("..." if len(title) > 80 else "")

        confidence = c.get("confidence", 0.0)
        sources = c.get("sources_found", 0)
        discrepancies = c.get("discrepancies", [])

        if c.get("verified"):
            status = "[OK] Verificada"
        elif sources > 0:
            status = "[WARN] Nao encontrada com confianca suficiente"
        else:
            status = "[FAIL] Discrepancia ou nao encontrada"

        lines.append(f"{i}. {status}")
        lines.append(f"   Titulo: {short_title}")
        lines.append(f"   Confianca: {confidence:.1%} | Fontes com resultado: {sources}/3")

        best = c.get("best_match", {})
        if best.get("title"):
            lines.append(f"   Melhor resultado: \"{best['title'][:70]}\" ({best.get('year', '?')})")
            lines.append(f"   Fonte: {best.get('source', '?')} | Score: {best.get('score', 0):.2f}")

        if discrepancies:
            for d in discrepancies:
                lines.append(f"   ! {d}")

        lines.append("")

    return "\n".join(lines)
