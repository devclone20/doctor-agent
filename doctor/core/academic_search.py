"""
Motor de busca académica multi-fonte do Doctor.
Integra: IST Scholar, arXiv, Semantic Scholar, PubMed, OpenAlex, CrossRef.
"""

import hashlib
import re
import time
from typing import Any

import httpx


# ─── Formatação de citações ───────────────────────────────────────────────────

def _format_authors_ieee(authors_str: str, max_authors: int = 6) -> str:
    """Formata lista de autores para IEEE."""
    if not authors_str:
        return "Unknown Author"
    authors = [a.strip() for a in authors_str.split(",") if a.strip()]
    if len(authors) > max_authors:
        return ", ".join(authors[:max_authors]) + ", et al."
    return ", ".join(authors)


def _format_authors_apa(authors_str: str) -> str:
    """Formata lista de autores para APA 7th."""
    if not authors_str:
        return "Unknown Author"
    authors = [a.strip() for a in authors_str.split(",") if a.strip()]

    def fmt_author(name: str) -> str:
        parts = name.split()
        if len(parts) >= 2:
            last = parts[-1]
            initials = ". ".join(p[0] for p in parts[:-1] if p) + "."
            return f"{last}, {initials}"
        return name

    formatted = [fmt_author(a) for a in authors]
    if len(formatted) > 20:
        return ", ".join(formatted[:19]) + ", ... " + formatted[-1]
    if len(formatted) > 1:
        return ", ".join(formatted[:-1]) + ", & " + formatted[-1]
    return formatted[0] if formatted else "Unknown Author"


def build_ieee_citation(paper: dict, ref_num: int = 1) -> str:
    """Gera citação IEEE completa."""
    authors = _format_authors_ieee(paper.get("authors", ""))
    title = paper.get("title", "Unknown Title")
    year = paper.get("year", "n.d.")
    venue = paper.get("venue", "")
    doi = paper.get("doi", "")
    arxiv_id = paper.get("arxiv_id", "")
    url = paper.get("url", "")

    if doi:
        source = f"doi: {doi}"
    elif arxiv_id:
        source = f"arXiv:{arxiv_id}"
    elif url:
        source = f"[Online]. Available: {url}"
    else:
        source = ""

    if venue:
        citation = f"[{ref_num}] {authors}, \"{title},\" *{venue}*, {year}"
    else:
        citation = f"[{ref_num}] {authors}, \"{title},\" {year}"

    if source:
        citation += f". {source}."
    else:
        citation += "."

    return citation


def build_apa_citation(paper: dict) -> str:
    """Gera citação APA 7th."""
    authors = _format_authors_apa(paper.get("authors", ""))
    title = paper.get("title", "Unknown Title")
    year = paper.get("year", "n.d.")
    venue = paper.get("venue", "")
    doi = paper.get("doi", "")
    url = paper.get("url", "")

    citation = f"{authors} ({year}). {title}."
    if venue:
        citation += f" *{venue}*."
    if doi:
        citation += f" https://doi.org/{doi}"
    elif url:
        citation += f" {url}"
    return citation


def build_bibtex(paper: dict) -> str:
    """Gera entrada BibTeX."""
    # Gerar chave
    first_author = ""
    authors_str = paper.get("authors", "")
    if authors_str:
        first_author = authors_str.split(",")[0].strip().split()[-1].lower()
    year = paper.get("year", "0000")
    title_words = re.findall(r"[a-zA-Z]+", paper.get("title", ""))
    key_word = title_words[0].lower() if title_words else "paper"
    key = f"{first_author}{year}{key_word}"

    # Tipo de entrada
    venue = paper.get("venue", "").lower()
    if any(w in venue for w in ["proceedings", "conference", "workshop", "symposium", "icml", "nips", "iclr", "cvpr", "aaai"]):
        entry_type = "inproceedings"
        venue_field = f"  booktitle = {{{paper.get('venue', '')}}}"
    elif any(w in venue for w in ["journal", "transactions", "letters", "arxiv"]):
        entry_type = "article"
        venue_field = f"  journal   = {{{paper.get('venue', '')}}}"
    elif paper.get("arxiv_id"):
        entry_type = "misc"
        venue_field = f"  archivePrefix = {{arXiv}},\n  eprint    = {{{paper.get('arxiv_id', '')}}}"
    else:
        entry_type = "misc"
        venue_field = ""

    doi_field = f"  doi       = {{{paper.get('doi', '')}}}," if paper.get("doi") else ""
    url_field = f"  url       = {{{paper.get('url', '')}}}," if paper.get("url") else ""

    bibtex = f"""@{entry_type}{{{key},
  title     = {{{paper.get('title', '')}}},
  author    = {{{paper.get('authors', '')}}},
  year      = {{{year}}},
{venue_field},
{doi_field}
{url_field}
}}"""
    return bibtex.strip()


# ─── IST Scholar (via OpenAlex — University of Lisbon) ───────────────────────

# Universidade de Lisboa em OpenAlex: I141596103
_ULISBOA_OPENALEX_ID = "I141596103"


def search_ist_scholar(query: str, limit: int = 10) -> list[dict]:
    """
    Pesquisa artigos de IST/ULisboa via OpenAlex institution filter.
    Filtra pela Universidade de Lisboa (que inclui o IST).
    """
    params = {
        "search": query,
        "per-page": min(limit, 25),
        "sort": "relevance_score:desc",
        "filter": f"institutions.id:{_ULISBOA_OPENALEX_ID}",
        "mailto": "doctor-agent@ist.pt",
    }
    try:
        with httpx.Client(timeout=15.0) as client:
            resp = client.get("https://api.openalex.org/works", params=params)
            if resp.status_code != 200:
                return []
            data = resp.json()
    except Exception:
        return []

    results = []
    for item in data.get("results", [])[:limit]:
        authorships = item.get("authorships", [])
        authors = ", ".join(
            a.get("author", {}).get("display_name", "")
            for a in authorships[:8]
        )
        doi = (item.get("doi") or "").replace("https://doi.org/", "")
        pub_year = item.get("publication_year")
        venue_info = (item.get("primary_location") or {})
        source_info = (venue_info.get("source") or {})
        venue = source_info.get("display_name", "IST Lisboa")
        url = (venue_info.get("pdf_url") or
               f"https://doi.org/{doi}" if doi else item.get("id", ""))
        abstract = _reconstruct_abstract(item.get("abstract_inverted_index") or {})

        paper = {
            "id": f"ist_{(item.get('id') or '').split('/')[-1]}",
            "title": item.get("title", ""),
            "authors": authors,
            "year": pub_year,
            "venue": venue or "IST Lisboa",
            "doi": doi,
            "abstract": abstract[:500],
            "url": url,
            "source": "IST Scholar",
        }
        paper["citation_ieee"] = build_ieee_citation(paper)
        paper["citation_apa"] = build_apa_citation(paper)
        paper["bibtex"] = build_bibtex(paper)
        results.append(paper)

    return results


# ─── arXiv ───────────────────────────────────────────────────────────────────

def search_arxiv(query: str, limit: int = 10, categories: str = "cs.LG,cs.AI,cs.CV,cs.CL,cs.DC") -> list[dict]:
    """Pesquisa no arXiv (cs.LG, cs.AI, cs.CV, cs.CL, cs.DC)."""
    import xml.etree.ElementTree as ET

    search_query = f"({query}) AND (cat:{categories.replace(',', ' OR cat:')})"
    params = {
        "search_query": search_query,
        "max_results": limit,
        "sortBy": "relevance",
        "sortOrder": "descending",
    }
    try:
        with httpx.Client(timeout=20.0) as client:
            resp = client.get("https://export.arxiv.org/api/query", params=params)
            if resp.status_code != 200:
                return []
            root = ET.fromstring(resp.text)
    except Exception:
        return []

    ns = {"atom": "http://www.w3.org/2005/Atom"}
    results = []

    for entry in root.findall("atom:entry", ns)[:limit]:
        title_el = entry.find("atom:title", ns)
        title = (title_el.text if title_el is not None else "") or ""
        title = title.strip().replace("\n", " ")

        summary_el = entry.find("atom:summary", ns)
        abstract = (summary_el.text if summary_el is not None else "") or ""
        abstract = abstract.strip().replace("\n", " ")[:500]

        id_el = entry.find("atom:id", ns)
        arxiv_url = (id_el.text if id_el is not None else "") or ""
        arxiv_id = arxiv_url.split("/abs/")[-1].strip() if "/abs/" in arxiv_url else ""

        authors_els = entry.findall("atom:author", ns)
        authors_list = []
        for a in authors_els:
            name_el = a.find("atom:name", ns)
            if name_el is not None and name_el.text:
                authors_list.append(name_el.text)
        authors = ", ".join(authors_list)

        published_el = entry.find("atom:published", ns)
        published = (published_el.text if published_el is not None else "") or ""
        year = int(published[:4]) if published[:4].isdigit() else None

        doi_el = entry.find("{http://arxiv.org/schemas/atom}doi")
        doi = doi_el.text.strip() if doi_el is not None else ""

        paper = {
            "id": f"arxiv_{arxiv_id.replace('.', '_').replace('/', '_')}",
            "title": title,
            "authors": authors,
            "year": year,
            "venue": "arXiv",
            "arxiv_id": arxiv_id,
            "doi": doi,
            "abstract": abstract,
            "url": f"https://arxiv.org/abs/{arxiv_id}",
            "source": "arXiv",
        }
        paper["citation_ieee"] = build_ieee_citation(paper)
        paper["citation_apa"] = build_apa_citation(paper)
        paper["bibtex"] = build_bibtex(paper)
        results.append(paper)

    return results


# ─── Semantic Scholar ─────────────────────────────────────────────────────────

def search_semantic_scholar(query: str, limit: int = 10) -> list[dict]:
    """Pesquisa no Semantic Scholar (gratuito, sem API key)."""
    params = {
        "query": query,
        "limit": min(limit, 100),
        "fields": "title,authors,year,venue,abstract,externalIds,openAccessPdf,url",
    }
    try:
        with httpx.Client(timeout=15.0) as client:
            resp = client.get(
                "https://api.semanticscholar.org/graph/v1/paper/search",
                params=params,
                headers={"User-Agent": "DoctorAgent/1.0 (academic research)"},
            )
            if resp.status_code != 200:
                return []
            data = resp.json()
    except Exception:
        return []

    results = []
    for item in data.get("data", [])[:limit]:
        authors = ", ".join(
            a.get("name", "") for a in item.get("authors", [])
        )
        ext_ids = item.get("externalIds", {}) or {}
        doi = ext_ids.get("DOI", "")
        arxiv_id = ext_ids.get("ArXiv", "")
        paper_id = item.get("paperId", "")
        url = item.get("url") or (
            f"https://www.semanticscholar.org/paper/{paper_id}" if paper_id else ""
        )
        pdf_info = item.get("openAccessPdf") or {}
        pdf_url = pdf_info.get("url", "") if isinstance(pdf_info, dict) else ""

        paper = {
            "id": f"s2_{paper_id[:12]}" if paper_id else f"s2_{hashlib.md5(item.get('title', '').encode()).hexdigest()[:8]}",
            "title": item.get("title", ""),
            "authors": authors,
            "year": item.get("year"),
            "venue": item.get("venue", ""),
            "doi": doi,
            "arxiv_id": arxiv_id,
            "abstract": (item.get("abstract") or "")[:500],
            "url": pdf_url or url,
            "source": "Semantic Scholar",
        }
        paper["citation_ieee"] = build_ieee_citation(paper)
        paper["citation_apa"] = build_apa_citation(paper)
        paper["bibtex"] = build_bibtex(paper)
        results.append(paper)

    return results


# ─── OpenAlex ────────────────────────────────────────────────────────────────

def search_openalex(query: str, limit: int = 10) -> list[dict]:
    """Pesquisa no OpenAlex (base aberta multi-disciplinar)."""
    params = {
        "search": query,
        "per-page": min(limit, 25),
        "sort": "relevance_score:desc",
        "filter": "type:article",
        "mailto": "doctor-agent@ist.pt",
    }
    try:
        with httpx.Client(timeout=15.0) as client:
            resp = client.get("https://api.openalex.org/works", params=params)
            if resp.status_code != 200:
                return []
            data = resp.json()
    except Exception:
        return []

    results = []
    for item in data.get("results", [])[:limit]:
        authorships = item.get("authorships", [])
        authors = ", ".join(
            a.get("author", {}).get("display_name", "")
            for a in authorships[:10]
        )
        doi = (item.get("doi") or "").replace("https://doi.org/", "")
        pub_date = item.get("publication_date") or item.get("publication_year") or ""
        year = int(str(pub_date)[:4]) if str(pub_date)[:4].isdigit() else None
        venue_info = item.get("primary_location") or {}
        source_info = (venue_info.get("source") or {})
        venue = source_info.get("display_name", "")
        url = item.get("primary_location", {}).get("pdf_url") or item.get("id", "")

        paper = {
            "id": f"oa_{(item.get('id') or '').split('/')[-1]}",
            "title": item.get("title", ""),
            "authors": authors,
            "year": year,
            "venue": venue,
            "doi": doi,
            "abstract": (item.get("abstract_inverted_index") and _reconstruct_abstract(item["abstract_inverted_index"]) or "")[:500],
            "url": url,
            "source": "OpenAlex",
        }
        paper["citation_ieee"] = build_ieee_citation(paper)
        paper["citation_apa"] = build_apa_citation(paper)
        paper["bibtex"] = build_bibtex(paper)
        results.append(paper)

    return results


def _reconstruct_abstract(inverted_index: dict) -> str:
    """Reconstrói o abstract do formato inverted index do OpenAlex."""
    if not inverted_index:
        return ""
    word_positions: list[tuple[int, str]] = []
    for word, positions in inverted_index.items():
        for pos in positions:
            word_positions.append((pos, word))
    word_positions.sort()
    return " ".join(w for _, w in word_positions)


# ─── CrossRef (DOI lookup) ────────────────────────────────────────────────────

def lookup_doi(doi: str) -> dict | None:
    """Lookup de metadados por DOI via CrossRef."""
    doi_clean = doi.replace("https://doi.org/", "").strip()
    try:
        with httpx.Client(timeout=15.0) as client:
            resp = client.get(
                f"https://api.crossref.org/works/{doi_clean}",
                headers={"User-Agent": "DoctorAgent/1.0 (mailto:doctor@ist.pt)"},
            )
            if resp.status_code != 200:
                return None
            data = resp.json().get("message", {})
    except Exception:
        return None

    authors_list = data.get("author", [])
    authors = ", ".join(
        f"{a.get('given', '')} {a.get('family', '')}".strip()
        for a in authors_list
    )
    title_list = data.get("title", [])
    title = title_list[0] if title_list else ""
    year_parts = data.get("published", {}).get("date-parts", [[]])
    year = year_parts[0][0] if year_parts and year_parts[0] else None
    container = data.get("container-title", [""])
    venue = container[0] if container else ""
    volume = data.get("volume", "")
    issue = data.get("issue", "")
    pages = data.get("page", "")

    venue_full = venue
    if volume:
        venue_full += f", vol. {volume}"
    if issue:
        venue_full += f", no. {issue}"
    if pages:
        venue_full += f", pp. {pages}"

    paper = {
        "id": f"doi_{doi_clean.replace('/', '_')}",
        "title": title,
        "authors": authors,
        "year": year,
        "venue": venue_full,
        "doi": doi_clean,
        "abstract": "",
        "url": f"https://doi.org/{doi_clean}",
        "source": "CrossRef",
    }
    paper["citation_ieee"] = build_ieee_citation(paper)
    paper["citation_apa"] = build_apa_citation(paper)
    paper["bibtex"] = build_bibtex(paper)
    return paper


# ─── PubMed ──────────────────────────────────────────────────────────────────

def search_pubmed(query: str, limit: int = 10) -> list[dict]:
    """Pesquisa no PubMed (biomedical)."""
    try:
        with httpx.Client(timeout=15.0) as client:
            # Step 1: search IDs
            search_resp = client.get(
                "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
                params={
                    "db": "pubmed",
                    "term": query,
                    "retmax": limit,
                    "retmode": "json",
                    "tool": "DoctorAgent",
                    "email": "doctor@ist.pt",
                },
            )
            ids = search_resp.json().get("esearchresult", {}).get("idlist", [])
            if not ids:
                return []

            # Step 2: fetch summaries
            summary_resp = client.get(
                "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi",
                params={
                    "db": "pubmed",
                    "id": ",".join(ids),
                    "retmode": "json",
                    "tool": "DoctorAgent",
                    "email": "doctor@ist.pt",
                },
            )
            summaries = summary_resp.json().get("result", {})
    except Exception:
        return []

    results = []
    for pmid in ids:
        item = summaries.get(pmid, {})
        if not item:
            continue
        authors_list = item.get("authors", [])
        authors = ", ".join(a.get("name", "") for a in authors_list[:10])
        title = item.get("title", "")
        year_raw = item.get("pubdate", "")
        year = int(year_raw[:4]) if year_raw[:4].isdigit() else None
        venue = item.get("fulljournalname") or item.get("source", "")

        paper = {
            "id": f"pmid_{pmid}",
            "title": title,
            "authors": authors,
            "year": year,
            "venue": venue,
            "doi": item.get("elocationid", "").replace("doi: ", ""),
            "abstract": "",
            "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            "source": "PubMed",
        }
        paper["citation_ieee"] = build_ieee_citation(paper)
        paper["citation_apa"] = build_apa_citation(paper)
        paper["bibtex"] = build_bibtex(paper)
        results.append(paper)

    return results


# ─── Interface principal ──────────────────────────────────────────────────────

def search_academic(
    query: str,
    sources: list[str] | None = None,
    limit_per_source: int = 5,
) -> list[dict]:
    """
    Pesquisa académica multi-fonte.
    sources: ["ist", "arxiv", "semantic", "openalex", "pubmed"] ou None (todas)
    """
    if sources is None:
        sources = ["arxiv", "semantic", "ist", "openalex"]

    all_results: list[dict] = []
    seen_titles: set[str] = set()

    source_fns = {
        "ist": lambda: search_ist_scholar(query, limit_per_source),
        "arxiv": lambda: search_arxiv(query, limit_per_source),
        "semantic": lambda: search_semantic_scholar(query, limit_per_source),
        "openalex": lambda: search_openalex(query, limit_per_source),
        "pubmed": lambda: search_pubmed(query, limit_per_source),
    }

    for source in sources:
        if source not in source_fns:
            continue
        try:
            results = source_fns[source]()
            for r in results:
                title_key = r.get("title", "").lower().strip()
                if title_key and title_key not in seen_titles:
                    seen_titles.add(title_key)
                    all_results.append(r)
            time.sleep(0.3)  # rate limit gentil
        except Exception:
            continue

    return all_results


def format_results_for_agent(results: list[dict], style: str = "ieee") -> str:
    """Formata resultados de pesquisa para o agente."""
    if not results:
        return "Nenhum resultado encontrado."

    lines = [f"Encontrados {len(results)} artigos:\n"]
    for i, r in enumerate(results, 1):
        title = r.get("title", "Untitled")
        authors = (r.get("authors") or "")[:80]
        year = r.get("year", "n.d.")
        venue = r.get("venue", "")
        source = r.get("source", "")
        abstract = (r.get("abstract") or "")[:200]
        url = r.get("url", "")

        lines.append(f"[{i}] {title}")
        lines.append(f"    Autores: {authors}")
        lines.append(f"    Ano: {year} | Fonte: {source} | Venue: {venue}")
        if abstract:
            lines.append(f"    Abstract: {abstract}...")
        if url:
            lines.append(f"    URL: {url}")

        if style == "ieee":
            lines.append(f"    IEEE: {r.get('citation_ieee', '')}")
        elif style == "apa":
            lines.append(f"    APA: {r.get('citation_apa', '')}")

        lines.append("")

    return "\n".join(lines)
