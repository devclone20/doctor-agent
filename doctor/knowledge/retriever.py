"""
Retriever de conhecimento do Doctor.
Carrega wiki académico no SQLite e injeta contexto via FTS5.
"""

from pathlib import Path

from doctor.memory.db import init_db, upsert_wiki_page, search_wiki, get_connection


def get_wiki_dir() -> Path:
    return Path(__file__).parent / "wiki"


def load_wiki_into_db(db_path: Path) -> None:
    """
    Carrega os ficheiros markdown do wiki no SQLite.
    Usa mtime para evitar re-indexar ficheiros que não mudaram.
    """
    init_db(db_path)
    wiki_dir = get_wiki_dir()

    with get_connection(db_path) as conn:
        existing = {
            r["slug"]: r["updated_at"]
            for r in conn.execute(
                "SELECT slug, updated_at FROM wiki_pages WHERE tags='core-knowledge'"
            ).fetchall()
        }

    for md_file in wiki_dir.glob("*.md"):
        slug = md_file.stem
        mtime = str(md_file.stat().st_mtime)

        if slug in existing and existing[slug] == mtime:
            continue

        lines = md_file.read_text(encoding="utf-8").splitlines()
        title = lines[0].lstrip("# ").strip() if lines else slug
        body = "\n".join(lines[1:]).strip()
        upsert_wiki_page(db_path, slug, title, body, tags="core-knowledge")


def retrieve_relevant_context(db_path: Path, query: str, max_chars: int = 3000) -> str:
    """
    Busca no wiki os trechos mais relevantes para a query.
    Retorna texto formatado para injecção no system prompt.
    """
    if not query.strip():
        return ""

    results = search_wiki(db_path, query, limit=4)
    if not results:
        return ""

    parts: list[str] = []
    total_chars = 0

    for r in results:
        section = f"### {r['title']}\n{r['body']}"
        if total_chars + len(section) > max_chars:
            remaining = max_chars - total_chars
            if remaining > 150:
                parts.append(section[:remaining] + "...")
            break
        parts.append(section)
        total_chars += len(section)

    return "\n\n".join(parts)


def get_all_wiki_slugs(db_path: Path) -> list[str]:
    """Lista todos os slugs do wiki para debug."""
    with get_connection(db_path) as conn:
        rows = conn.execute("SELECT slug FROM wiki_pages ORDER BY slug").fetchall()
    return [r["slug"] for r in rows]
