"""
Síntese de sessão e construção de contexto de memória do Doctor.
"""

from pathlib import Path

import anthropic

from doctor.memory.db import (
    end_session,
    get_recent_sessions,
    get_session_observations,
    search_wiki,
    search_papers,
)

SYNTHESIS_MODEL = "claude-haiku-4-5-20251001"


def synthesize_session(
    client: anthropic.Anthropic,
    db_path: Path,
    session_id: str,
    project: str | None = None,
    doc_type: str | None = None,
) -> str:
    """
    Usa claude-haiku para sintetizar a sessão e guardar na memória.
    Retorna o resumo gerado.
    """
    obs = get_session_observations(db_path, session_id)
    if not obs:
        return ""

    # Formatar a conversa para síntese
    conv_text = "\n".join(
        f"[{o['role'].upper()}]: {o['content'][:500]}" for o in obs[:30]
    )

    proj_info = f" (projecto: {project})" if project else ""
    type_info = f" (tipo: {doc_type})" if doc_type else ""

    prompt = f"""Sintetiza esta sessão académica{proj_info}{type_info} em no máximo 300 palavras.
Foca em:
- Tema do trabalho / dissertação
- Decisões técnicas ou académicas tomadas
- Papers ou referências discutidos
- Progresso e próximos passos
- Qualquer informação útil para sessões futuras

Conversa:
{conv_text}

Síntese:"""

    try:
        response = client.messages.create(
            model=SYNTHESIS_MODEL,
            max_tokens=400,
            messages=[{"role": "user", "content": prompt}],
        )
        summary = response.content[0].text.strip()
        end_session(db_path, session_id, summary=summary)
        return summary
    except Exception:
        end_session(db_path, session_id, summary="")
        return ""


def build_memory_context(
    db_path: Path,
    query: str = "",
    max_sessions: int = 3,
) -> str:
    """
    Constrói contexto de memória para injecção no system prompt.
    Combina sessões recentes + wiki relevante + papers relevantes.
    """
    parts: list[str] = []

    # Sessões recentes com sumário
    sessions = get_recent_sessions(db_path, limit=max_sessions)
    session_parts = [
        s for s in sessions if s.get("summary")
    ]
    if session_parts:
        session_lines = []
        for s in session_parts:
            proj = f" [{s['project']}]" if s.get("project") else ""
            dtype = f" ({s['doc_type']})" if s.get("doc_type") else ""
            summary = (s.get("summary") or "")[:200]
            date = (s.get("started_at") or "")[:10]
            session_lines.append(f"- {date}{proj}{dtype}: {summary}")
        parts.append(
            "## Sessões Anteriores\n" + "\n".join(session_lines)
        )

    # Papers relevantes da KB local
    if query:
        papers = search_papers(db_path, query, limit=3)
        if papers:
            paper_lines = []
            for p in papers:
                authors = (p.get("authors") or "")[:60]
                title = p.get("title", "")
                year = p.get("year", "")
                venue = p.get("venue", "")
                paper_lines.append(f"- [{year}] {authors}. \"{title}\". {venue}")
            parts.append(
                "## Papers Relevantes na Base de Conhecimento\n" + "\n".join(paper_lines)
            )

    return "\n\n".join(parts)
