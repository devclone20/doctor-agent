"""
Base de dados SQLite para o Doctor.
FTS5 para busca semântica. WAL mode para performance.
"""

import re
import sqlite3
from contextlib import contextmanager
from datetime import UTC, datetime
from pathlib import Path


@contextmanager
def get_connection(db_path: Path):
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_db(db_path: Path) -> None:
    """Inicializa o schema da base de dados."""
    with get_connection(db_path) as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS sessions (
                id          TEXT PRIMARY KEY,
                started_at  TEXT NOT NULL,
                ended_at    TEXT,
                project     TEXT,
                doc_type    TEXT,
                summary     TEXT
            );

            CREATE TABLE IF NOT EXISTS observations (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id  TEXT NOT NULL REFERENCES sessions(id),
                role        TEXT NOT NULL,
                content     TEXT NOT NULL,
                created_at  TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS wiki_pages (
                slug        TEXT PRIMARY KEY,
                title       TEXT NOT NULL,
                body        TEXT NOT NULL,
                tags        TEXT DEFAULT '',
                updated_at  TEXT NOT NULL
            );

            CREATE VIRTUAL TABLE IF NOT EXISTS wiki_fts USING fts5(
                slug UNINDEXED,
                title,
                body,
                content=wiki_pages,
                content_rowid=rowid,
                tokenize='unicode61 remove_diacritics 2'
            );

            CREATE TRIGGER IF NOT EXISTS wiki_ai AFTER INSERT ON wiki_pages BEGIN
                INSERT INTO wiki_fts(rowid, slug, title, body)
                VALUES (new.rowid, new.slug, new.title, new.body);
            END;

            CREATE TRIGGER IF NOT EXISTS wiki_ad AFTER DELETE ON wiki_pages BEGIN
                INSERT INTO wiki_fts(wiki_fts, rowid, slug, title, body)
                VALUES ('delete', old.rowid, old.slug, old.title, old.body);
            END;

            CREATE TRIGGER IF NOT EXISTS wiki_au AFTER UPDATE ON wiki_pages BEGIN
                INSERT INTO wiki_fts(wiki_fts, rowid, slug, title, body)
                VALUES ('delete', old.rowid, old.slug, old.title, old.body);
                INSERT INTO wiki_fts(rowid, slug, title, body)
                VALUES (new.rowid, new.slug, new.title, new.body);
            END;

            CREATE TABLE IF NOT EXISTS papers (
                id          TEXT PRIMARY KEY,
                title       TEXT NOT NULL,
                authors     TEXT,
                year        INTEGER,
                venue       TEXT,
                doi         TEXT,
                arxiv_id    TEXT,
                abstract    TEXT,
                url         TEXT,
                citation_ieee TEXT,
                citation_apa  TEXT,
                bibtex      TEXT,
                tags        TEXT DEFAULT '',
                added_at    TEXT NOT NULL
            );

            CREATE VIRTUAL TABLE IF NOT EXISTS papers_fts USING fts5(
                id UNINDEXED,
                title,
                authors,
                abstract,
                content=papers,
                content_rowid=rowid,
                tokenize='unicode61 remove_diacritics 2'
            );

            CREATE TRIGGER IF NOT EXISTS papers_ai AFTER INSERT ON papers BEGIN
                INSERT INTO papers_fts(rowid, id, title, authors, abstract)
                VALUES (new.rowid, new.id, new.title, new.authors, new.abstract);
            END;

            CREATE TRIGGER IF NOT EXISTS papers_ad AFTER DELETE ON papers BEGIN
                INSERT INTO papers_fts(papers_fts, rowid, id, title, authors, abstract)
                VALUES ('delete', old.rowid, old.id, old.title, old.authors, old.abstract);
            END;

            CREATE TRIGGER IF NOT EXISTS papers_au AFTER UPDATE ON papers BEGIN
                INSERT INTO papers_fts(papers_fts, rowid, id, title, authors, abstract)
                VALUES ('delete', old.rowid, old.id, old.title, old.authors, old.abstract);
                INSERT INTO papers_fts(rowid, id, title, authors, abstract)
                VALUES (new.rowid, new.id, new.title, new.authors, new.abstract);
            END;
        """)


def _sanitize_fts_query(query: str) -> str:
    """Extrai palavras válidas e junta com OR para FTS5 seguro."""
    words = re.findall(r"[a-zA-ZÀ-ÿ\d]{2,}", query)
    if not words:
        return ""
    return " OR ".join(words[:10])


def create_session(
    db_path: Path,
    project: str | None = None,
    doc_type: str | None = None,
) -> str:
    import uuid
    session_id = str(uuid.uuid4())
    now = datetime.now(UTC).isoformat()
    with get_connection(db_path) as conn:
        conn.execute(
            "INSERT INTO sessions (id, started_at, project, doc_type) VALUES (?,?,?,?)",
            (session_id, now, project, doc_type),
        )
    return session_id


def end_session(db_path: Path, session_id: str, summary: str = "") -> None:
    now = datetime.now(UTC).isoformat()
    with get_connection(db_path) as conn:
        conn.execute(
            "UPDATE sessions SET ended_at=?, summary=? WHERE id=?",
            (now, summary, session_id),
        )


def log_observation(
    db_path: Path,
    session_id: str,
    role: str,
    content: str,
) -> None:
    now = datetime.now(UTC).isoformat()
    with get_connection(db_path) as conn:
        conn.execute(
            "INSERT INTO observations (session_id, role, content, created_at) VALUES (?,?,?,?)",
            (session_id, role, content, now),
        )


def get_session_observations(db_path: Path, session_id: str) -> list[dict]:
    with get_connection(db_path) as conn:
        rows = conn.execute(
            "SELECT role, content FROM observations WHERE session_id=? ORDER BY id",
            (session_id,),
        ).fetchall()
    return [dict(r) for r in rows]


def upsert_wiki_page(
    db_path: Path,
    slug: str,
    title: str,
    body: str,
    tags: str = "",
) -> None:
    now = datetime.now(UTC).isoformat()
    with get_connection(db_path) as conn:
        existing = conn.execute(
            "SELECT rowid FROM wiki_pages WHERE slug=?", (slug,)
        ).fetchone()
        if existing:
            conn.execute(
                "UPDATE wiki_pages SET title=?, body=?, tags=?, updated_at=? WHERE slug=?",
                (title, body, tags, now, slug),
            )
        else:
            conn.execute(
                "INSERT INTO wiki_pages (slug, title, body, tags, updated_at) VALUES (?,?,?,?,?)",
                (slug, title, body, tags, now),
            )


def search_wiki(db_path: Path, query: str, limit: int = 5) -> list[dict]:
    safe_query = _sanitize_fts_query(query)
    if not safe_query:
        return []
    with get_connection(db_path) as conn:
        try:
            rows = conn.execute(
                """SELECT w.slug, w.title, w.body
                   FROM wiki_fts f
                   JOIN wiki_pages w ON f.slug = w.slug
                   WHERE wiki_fts MATCH ?
                   ORDER BY rank
                   LIMIT ?""",
                (safe_query, limit),
            ).fetchall()
            return [dict(r) for r in rows]
        except sqlite3.OperationalError:
            return []


def upsert_paper(db_path: Path, paper: dict) -> None:
    """Guarda ou actualiza um artigo científico."""
    now = datetime.now(UTC).isoformat()
    with get_connection(db_path) as conn:
        conn.execute(
            """INSERT INTO papers
               (id, title, authors, year, venue, doi, arxiv_id, abstract,
                url, citation_ieee, citation_apa, bibtex, tags, added_at)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
               ON CONFLICT(id) DO UPDATE SET
               title=excluded.title, abstract=excluded.abstract,
               citation_ieee=excluded.citation_ieee,
               citation_apa=excluded.citation_apa,
               bibtex=excluded.bibtex""",
            (
                paper.get("id", ""),
                paper.get("title", ""),
                paper.get("authors", ""),
                paper.get("year"),
                paper.get("venue", ""),
                paper.get("doi", ""),
                paper.get("arxiv_id", ""),
                paper.get("abstract", ""),
                paper.get("url", ""),
                paper.get("citation_ieee", ""),
                paper.get("citation_apa", ""),
                paper.get("bibtex", ""),
                paper.get("tags", ""),
                now,
            ),
        )


def search_papers(db_path: Path, query: str, limit: int = 10) -> list[dict]:
    """Pesquisa artigos na base de dados local."""
    safe_query = _sanitize_fts_query(query)
    if not safe_query:
        return []
    with get_connection(db_path) as conn:
        try:
            rows = conn.execute(
                """SELECT p.id, p.title, p.authors, p.year, p.venue,
                          p.doi, p.arxiv_id, p.abstract, p.url,
                          p.citation_ieee, p.citation_apa, p.bibtex
                   FROM papers_fts f
                   JOIN papers p ON f.id = p.id
                   WHERE papers_fts MATCH ?
                   ORDER BY rank
                   LIMIT ?""",
                (safe_query, limit),
            ).fetchall()
            return [dict(r) for r in rows]
        except sqlite3.OperationalError:
            return []


def get_recent_sessions(db_path: Path, limit: int = 10) -> list[dict]:
    with get_connection(db_path) as conn:
        rows = conn.execute(
            """SELECT id, started_at, ended_at, project, doc_type, summary
               FROM sessions ORDER BY started_at DESC LIMIT ?""",
            (limit,),
        ).fetchall()
    return [dict(r) for r in rows]


def get_paper_count(db_path: Path) -> int:
    with get_connection(db_path) as conn:
        return conn.execute("SELECT COUNT(*) FROM papers").fetchone()[0]


def get_wiki_count(db_path: Path) -> int:
    with get_connection(db_path) as conn:
        return conn.execute("SELECT COUNT(*) FROM wiki_pages").fetchone()[0]
