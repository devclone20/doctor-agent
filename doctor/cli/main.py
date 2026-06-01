"""
CLI do Doctor — AI Academic Research & Dissertation Agent.
Comandos: chat, write, review, cite, search, ingest, status.
"""

import os
import sys
from pathlib import Path

import typer
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from rich.theme import Theme

load_dotenv()

app = typer.Typer(
    name="doctor",
    help="Doctor — AI Academic Research & Dissertation Agent. Padrão IST Lisboa.",
    add_completion=False,
)

DOCTOR_THEME = Theme({
    "doctor.name": "bold blue",
    "doctor.prompt": "bold cyan",
    "doctor.tool": "dim yellow",
    "doctor.memory": "dim green",
    "doctor.error": "bold red",
    "doctor.success": "green",
    "doctor.dim": "dim white",
    "doctor.academic": "bold magenta",
})

console = Console(theme=DOCTOR_THEME)

BANNER = """[doctor.name]
╔═══════════════════════════════════════════════════════╗
║  D O C T O R  —  AI Academic Research Agent          ║
║  Padrão IST Lisboa · ML/AI · Cloud · Dissertações    ║
║  IEEE · APA · arXiv · Scholar · Semantic Scholar     ║
╚═══════════════════════════════════════════════════════╝
[/doctor.name]"""


def _get_agent(
    project: str | None = None,
    doc_type: str | None = None,
    model: str | None = None,
    no_memory: bool = False,
) -> "DoctorAgent":  # type: ignore[name-defined]
    from doctor.core.agent import DoctorAgent

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        console.print("[doctor.error]ANTHROPIC_API_KEY não definida. Configure no .env[/doctor.error]")
        raise typer.Exit(1)

    return DoctorAgent(
        api_key=api_key,
        model=model,
        project=project,
        doc_type=doc_type,
        auto_synthesize=not no_memory,
    )


@app.command()
def chat(
    project: str = typer.Option(None, "--project", "-p", help="Nome da dissertação/projecto"),
    doc_type: str = typer.Option(None, "--type", "-t", help="Tipo: msc, phd, bsc, article"),
    model: str = typer.Option(None, "--model", "-m", help="Modelo Claude"),
    no_memory: bool = typer.Option(False, "--no-memory", help="Não usar memória persistente"),
) -> None:
    """
    Inicia sessão interactiva com o Doctor.
    """
    console.print(BANNER)
    if project:
        console.print(f"[doctor.dim]Projecto: {project}[/doctor.dim]")
    if doc_type:
        type_names = {"msc": "Dissertação de Mestrado", "phd": "Tese de Doutoramento",
                      "bsc": "Licenciatura", "article": "Artigo Científico"}
        console.print(f"[doctor.academic]Tipo: {type_names.get(doc_type, doc_type)}[/doctor.academic]")
    console.print("[doctor.dim]Escreve a tua pergunta. 'exit' ou Ctrl-C para sair.[/doctor.dim]\n")

    agent = _get_agent(project=project, doc_type=doc_type, model=model, no_memory=no_memory)
    agent.initialize()
    console.print(f"[doctor.memory]Memória carregada. Sessão: {agent.get_session_id()[:8]}[/doctor.memory]\n")

    try:
        while True:
            try:
                user_input = Prompt.ask("[doctor.prompt]você[/doctor.prompt]")
            except (EOFError, KeyboardInterrupt):
                break

            if user_input.strip().lower() in {"exit", "quit", "sair"}:
                break
            if not user_input.strip():
                continue

            console.print()
            console.print("[doctor.name]Doctor[/doctor.name]", end=" ")

            chunks: list[str] = []

            def on_chunk(text: str) -> None:
                chunks.append(text)
                console.print(text, end="", markup=False, highlight=False)

            agent.chat_stream(user_input, callback=on_chunk)
            console.print("\n")

    except KeyboardInterrupt:
        pass
    finally:
        console.print("\n[doctor.dim]A encerrar sessão...[/doctor.dim]")
        if not no_memory:
            with console.status("[doctor.memory]A sintetizar sessão académica...[/doctor.memory]"):
                summary = agent.end_session()
            if summary:
                console.print("[doctor.success]Sessão guardada na memória.[/doctor.success]")
        console.print("[doctor.dim]Até à próxima.[/doctor.dim]")


@app.command()
def write(
    topic: str = typer.Argument(..., help="Tema da dissertação/artigo"),
    doc_type: str = typer.Option("msc", "--type", "-t", help="Tipo: msc, phd, bsc, article"),
    spec: str = typer.Option("", "--spec", "-s", help="Ficheiro com especificações adicionais"),
    section: str = typer.Option("", "--section", help="Secção específica: introduction, background, methodology, evaluation, conclusion, abstract"),
    language: str = typer.Option("pt", "--lang", "-l", help="Idioma: pt ou en"),
    output: str = typer.Option(None, "--output", "-o", help="Ficheiro de saída"),
    project: str = typer.Option(None, "--project", "-p"),
    output_format: str = typer.Option("markdown", "--output-format", "-f", help="Formato de output: markdown ou latex"),
    style: str = typer.Option("", "--style", help="Estilo especial: ist-dissertation"),
) -> None:
    """
    Escreve uma dissertação completa ou secção específica.

    Exemplos:
      doctor write "Federated Learning para detecção de anomalias IoT" --type msc
      doctor write "Transformer architectures" --type article --section introduction --lang en
      doctor write "Redes Neuronais para Visão" --type msc --output-format latex
      doctor write "Federated Learning IoT" --type msc --style ist-dissertation
    """
    from doctor.skills.dissertation import get_dissertation_prompt, get_section_prompt

    console.print(BANNER)
    type_names = {"msc": "Dissertação de Mestrado", "phd": "Tese de Doutoramento",
                  "bsc": "Licenciatura", "article": "Artigo Científico"}
    type_name = type_names.get(doc_type, doc_type)

    if output_format not in ("markdown", "latex"):
        console.print("[doctor.error]--output-format deve ser 'markdown' ou 'latex'[/doctor.error]")
        raise typer.Exit(1)

    ist_style_active = style == "ist-dissertation"

    spec_content = ""
    if spec and Path(spec).exists():
        spec_content = Path(spec).read_text(encoding="utf-8")

    if section:
        console.print(f"[doctor.dim]Escrevendo secção '{section}' para {type_name}: {topic}[/doctor.dim]\n")
        prompt = get_section_prompt(section, topic, context=spec_content, doc_type=doc_type)
    else:
        console.print(f"[doctor.dim]Escrevendo {type_name} completa: {topic}[/doctor.dim]\n")
        prompt = get_dissertation_prompt(
            doc_type,
            topic,
            spec=spec_content,
            language=language,
            output_format=output_format,
            ist_style=ist_style_active,
        )

    if output_format == "latex" and not section:
        # Para LaTeX completo, pedir ao agente que exporte directamente em LaTeX
        from doctor.skills.dissertation import get_latex_export_prompt
        prompt = get_latex_export_prompt(prompt, doc_type=doc_type)

    agent = _get_agent(project=project or topic[:40], doc_type=doc_type)
    agent.initialize()

    with console.status(f"[doctor.tool]Doctor a escrever {type_name}...[/doctor.tool]", spinner="dots"):
        response = agent.chat(prompt)

    target = section or type_name
    console.print(Panel(
        Markdown(response) if output_format == "markdown" else Text(response[:3000]),
        title=f"[doctor.name]{target} — {topic[:50]}[/doctor.name]",
        border_style="blue",
        expand=False,
    ))

    # Determinar extensão e nome do ficheiro
    ext = ".tex" if output_format == "latex" else ".md"
    if output:
        out_path = Path(output)
        if output_format == "latex" and not output.endswith(".tex"):
            out_path = Path(output).with_suffix(".tex")
        out_path.write_text(response, encoding="utf-8")
        console.print(f"[doctor.success]Guardado em: {out_path}[/doctor.success]")
    else:
        work_dir = Path(os.path.expanduser("~/doctor-work"))
        work_dir.mkdir(exist_ok=True)
        safe_topic = "".join(c for c in topic[:40] if c.isalnum() or c in " -_").strip().replace(" ", "_")
        fname = f"{safe_topic}_{doc_type}_{section or 'full'}{ext}"
        out_path = work_dir / fname
        out_path.write_text(response, encoding="utf-8")
        console.print(f"[doctor.dim]Auto-guardado em: {out_path}[/doctor.dim]")

    agent.end_session()


@app.command()
def template(
    doc_type: str = typer.Option("msc", "--type", "-t", help="Tipo: msc, phd, bsc"),
    output: str = typer.Option(None, "--output", "-o", help="Ficheiro onde guardar o template"),
) -> None:
    """
    Imprime ou guarda o template IST-DEI com todas as secções obrigatórias.

    Exemplos:
      doctor template --type msc
      doctor template --type msc --output template.md
      doctor template --type phd --output phd_template.md
    """
    from doctor.skills.dissertation import get_ist_dei_template

    console.print(BANNER)
    console.print(f"[doctor.dim]Template IST-DEI — {doc_type.upper()}[/doctor.dim]\n")

    content = get_ist_dei_template(doc_type=doc_type)

    if output:
        Path(output).write_text(content, encoding="utf-8")
        console.print(f"[doctor.success]Template guardado em: {output}[/doctor.success]")
    else:
        work_dir = Path(os.path.expanduser("~/doctor-work"))
        work_dir.mkdir(exist_ok=True)
        out_path = work_dir / f"template_ist_dei_{doc_type}.md"
        out_path.write_text(content, encoding="utf-8")
        console.print(Panel(
            Markdown(content[:4000] + "\n\n*[...template truncado para visualização — ficheiro completo guardado]*"),
            title=f"[doctor.name]Template IST-DEI — {doc_type.upper()}[/doctor.name]",
            border_style="blue",
        ))
        console.print(f"[doctor.dim]Template completo em: {out_path}[/doctor.dim]")


@app.command()
def review(
    path: str = typer.Argument(..., help="Ficheiro a rever (.md, .txt, .tex, .pdf)"),
    review_type: str = typer.Option("full", "--type", "-t", help="Tipo: full, structure, citations, language, technical"),
    doc_type: str = typer.Option("dissertation", "--doc", "-d", help="Tipo de documento: dissertation, article, abstract"),
    focus: str = typer.Option("", "--focus", "-f", help="Aspecto específico a focar"),
    output: str = typer.Option(None, "--output", "-o", help="Ficheiro para guardar a revisão"),
    project: str = typer.Option(None, "--project", "-p"),
) -> None:
    """
    Revê e anota um trabalho académico.

    Exemplos:
      doctor review dissertation.md
      doctor review chapter2.tex --type citations
      doctor review abstract.md --type language
    """
    from doctor.skills.review import get_review_prompt

    p = Path(path)
    if not p.exists():
        console.print(f"[doctor.error]Ficheiro não encontrado: {path}[/doctor.error]")
        raise typer.Exit(1)

    console.print(BANNER)
    console.print(f"[doctor.dim]Revendo: {path} (tipo: {review_type})[/doctor.dim]\n")

    content = p.read_text(encoding="utf-8", errors="replace")
    prompt = get_review_prompt(content, doc_type=doc_type, review_type=review_type, focus=focus)

    agent = _get_agent(project=project, doc_type=doc_type)
    agent.initialize()

    with console.status("[doctor.tool]Doctor a rever o trabalho...[/doctor.tool]", spinner="dots"):
        response = agent.chat(prompt)

    console.print(Panel(
        Markdown(response),
        title=f"[doctor.name]Revisão — {p.name}[/doctor.name]",
        border_style="blue",
    ))

    if output:
        Path(output).write_text(response, encoding="utf-8")
        console.print(f"[doctor.success]Revisão guardada em: {output}[/doctor.success]")

    agent.end_session()


@app.command()
def cite(
    query: str = typer.Option("", "--query", "-q", help="Tema para pesquisar referências"),
    doi: str = typer.Option("", "--doi", help="DOI específico para formatar"),
    style: str = typer.Option("ieee", "--style", "-s", help="Estilo: ieee, apa, bibtex"),
    sources: str = typer.Option("arxiv,semantic,ist", "--sources", help="Fontes: arxiv,semantic,ist,openalex,pubmed"),
    limit: int = typer.Option(10, "--limit", "-n", help="Número de resultados"),
) -> None:
    """
    Pesquisa e formata citações bibliográficas.

    Exemplos:
      doctor cite --query "transformer neural networks"
      doctor cite --doi "10.1038/nature14539" --style bibtex
      doctor cite --query "federated learning IoT" --sources arxiv,semantic --limit 15
    """
    console.print(BANNER)

    if doi:
        # Lookup directo por DOI
        from doctor.core.academic_search import lookup_doi
        console.print(f"[doctor.dim]Lookup DOI: {doi}[/doctor.dim]\n")
        with console.status("[doctor.tool]A procurar...[/doctor.tool]"):
            paper = lookup_doi(doi)
        if paper:
            content = f"**{paper.get('title')}**\n\n"
            content += f"IEEE: `{paper.get('citation_ieee')}`\n\n"
            content += f"APA: `{paper.get('citation_apa')}`\n\n"
            content += f"**BibTeX:**\n```bibtex\n{paper.get('bibtex')}\n```"
            console.print(Panel(Markdown(content), title="[doctor.name]Citação[/doctor.name]", border_style="blue"))
        else:
            console.print(f"[doctor.error]DOI não encontrado: {doi}[/doctor.error]")

    elif query:
        from doctor.core.academic_search import search_academic, format_results_for_agent
        src_list = [s.strip() for s in sources.split(",")]
        console.print(f"[doctor.dim]Pesquisando: {query} em {src_list}[/doctor.dim]\n")
        with console.status("[doctor.tool]A pesquisar nas bases académicas...[/doctor.tool]"):
            results = search_academic(query, sources=src_list, limit_per_source=limit // len(src_list))
        formatted = format_results_for_agent(results, style=style)
        console.print(Panel(Markdown(formatted), title=f"[doctor.name]Referências — {query[:40]}[/doctor.name]", border_style="blue"))
    else:
        console.print("[doctor.error]Usa --query 'tema' ou --doi '10.xxx/xxx'[/doctor.error]")


@app.command()
def search(
    query: str = typer.Argument(..., help="Query de pesquisa"),
    source: str = typer.Option("all", "--source", "-s", help="Fonte: ist, arxiv, semantic, openalex, pubmed, all"),
    limit: int = typer.Option(10, "--limit", "-n", help="Número de resultados"),
    year_min: int = typer.Option(None, "--from", help="Ano mínimo (ex: 2020)"),
) -> None:
    """
    Pesquisa directa em bases de dados académicas.

    Exemplos:
      doctor search "deep learning time series" --source arxiv
      doctor search "dissertações IST machine learning" --source ist
      doctor search "federated learning privacy" --from 2022
    """
    from doctor.core.academic_search import search_academic, format_results_for_agent

    console.print(BANNER)
    src_list = None if source == "all" else [s.strip() for s in source.split(",")]
    console.print(f"[doctor.dim]Pesquisando: {query}[/doctor.dim]\n")

    with console.status("[doctor.tool]A pesquisar...[/doctor.tool]"):
        results = search_academic(query, sources=src_list, limit_per_source=max(limit, 5))

    if year_min:
        results = [r for r in results if (r.get("year") or 0) >= year_min]

    if not results:
        console.print("[doctor.error]Nenhum resultado encontrado.[/doctor.error]")
        return

    formatted = format_results_for_agent(results[:limit])
    console.print(Panel(
        Markdown(formatted),
        title=f"[doctor.name]{len(results[:limit])} resultados — {query[:40]}[/doctor.name]",
        border_style="blue",
    ))


@app.command()
def ingest(
    url: str = typer.Option(None, "--url", "-u", help="URL específico a ingerir"),
    query: str = typer.Option(None, "--query", "-q", help="Pesquisar e ingerir papers sobre um tema"),
    source: str = typer.Option("arxiv,semantic", "--source", "-s", help="Fontes a ingerir"),
    limit: int = typer.Option(10, "--limit", "-n", help="Número de papers a ingerir"),
) -> None:
    """
    Ingere papers e artigos na base de conhecimento permanente.

    Exemplos:
      doctor ingest --query "transformer attention mechanism" --limit 20
      doctor ingest --url "https://arxiv.org/abs/1706.03762"
    """
    import os as _os
    from pathlib import Path as P

    console.print(BANNER)
    console.print("[doctor.dim]A ingerir conhecimento académico...[/doctor.dim]\n")

    api_key = _os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        console.print("[doctor.error]ANTHROPIC_API_KEY não definida.[/doctor.error]")
        raise typer.Exit(1)

    memory_dir = P(_os.path.expanduser(_os.environ.get("DOCTOR_MEMORY_DIR", "~/.doctor")))
    db_path = memory_dir / "doctor.db"

    from doctor.memory.db import init_db, upsert_paper, upsert_wiki_page
    from doctor.knowledge.retriever import load_wiki_into_db
    init_db(db_path)
    load_wiki_into_db(db_path)

    if url:
        from doctor.core.tools import _fetch_paper
        console.print(f"[doctor.dim]A ingerir: {url}[/doctor.dim]")
        with console.status("[doctor.tool]A processar...[/doctor.tool]"):
            content = _fetch_paper({"url": url, "extract": "full"})

        # Tentar extrair metadados básicos
        from doctor.core.academic_search import search_academic
        title = url.split("/")[-1].replace("-", " ").replace("_", " ")

        slug = "ingested_" + url[-20:].replace("/", "_").replace(".", "_")
        upsert_wiki_page(db_path, slug, title, content[:3000], tags="ingested")
        console.print(f"[doctor.success]Ingerido: {title}[/doctor.success]")

    elif query:
        from doctor.core.academic_search import search_academic
        src_list = [s.strip() for s in source.split(",")]
        console.print(f"[doctor.dim]Pesquisando: {query} em {src_list}[/doctor.dim]")

        with console.status("[doctor.tool]A pesquisar e indexar...[/doctor.tool]"):
            results = search_academic(query, sources=src_list, limit_per_source=limit)

        count = 0
        for paper in results:
            if paper.get("title"):
                upsert_paper(db_path, paper)
                count += 1

        console.print(f"[doctor.success]{count} artigos indexados na base de conhecimento.[/doctor.success]")
    else:
        console.print("[doctor.error]Usa --url ou --query[/doctor.error]")


@app.command()
def status() -> None:
    """Mostra o estado actual do Doctor e da base de conhecimento."""
    import os as _os
    from pathlib import Path as P

    db_path = P(_os.path.expanduser("~/.doctor/doctor.db"))

    console.print(BANNER)

    if not db_path.exists():
        console.print("[doctor.error]Base de dados não existe. Execute: doctor chat[/doctor.error]")
        return

    from doctor.memory.db import get_connection, get_wiki_count, get_paper_count, get_recent_sessions

    wiki_count = get_wiki_count(db_path)
    paper_count = get_paper_count(db_path)

    with get_connection(db_path) as conn:
        session_count = conn.execute("SELECT COUNT(*) FROM sessions").fetchone()[0]
        obs_count = conn.execute("SELECT COUNT(*) FROM observations").fetchone()[0]

    console.print(f"\n[doctor.name]Estado do Doctor[/doctor.name]\n")
    console.print(f"  [doctor.dim]Wiki académico:[/doctor.dim]    [cyan]{wiki_count}[/cyan] páginas")
    console.print(f"  [doctor.dim]Papers indexados:[/doctor.dim]  [cyan]{paper_count}[/cyan] artigos")
    console.print(f"  [doctor.dim]Sessões de chat:[/doctor.dim]   [cyan]{session_count}[/cyan]")
    console.print(f"  [doctor.dim]Observações log:[/doctor.dim]   [cyan]{obs_count}[/cyan]")
    console.print(f"  [doctor.dim]DB em:[/doctor.dim]             [dim]{db_path}[/dim]")
    console.print(f"  [doctor.dim]Work dir:[/doctor.dim]          [dim]{_os.path.expanduser('~/doctor-work')}[/dim]")

    sessions = get_recent_sessions(db_path, limit=5)
    if sessions:
        console.print(f"\n[doctor.name]Sessões recentes:[/doctor.name]")
        for s in sessions:
            proj = f" [{s['project']}]" if s.get("project") else ""
            dtype = f" ({s['doc_type']})" if s.get("doc_type") else ""
            summary = (s.get("summary") or "sem resumo")[:70]
            date = (s.get("started_at") or "")[:10]
            console.print(f"  [doctor.dim]{date}{proj}{dtype}[/doctor.dim] — {summary}")

    console.print()


@app.command()
def memory(
    action: str = typer.Argument("list", help="Acção: list, search, papers"),
    query: str = typer.Option("", "--query", "-q"),
) -> None:
    """Gere a memória do Doctor."""
    import os as _os
    from pathlib import Path as P

    db_path = P(_os.path.expanduser("~/.doctor/doctor.db"))

    if action == "list":
        from doctor.memory.db import get_recent_sessions
        sessions = get_recent_sessions(db_path, limit=10)
        console.print(f"\n[doctor.name]Sessões ({len(sessions)}):[/doctor.name]\n")
        for s in sessions:
            proj = f" [{s['project']}]" if s.get("project") else ""
            dtype = f" ({s['doc_type']})" if s.get("doc_type") else ""
            summary = (s.get("summary") or "sem resumo")[:80]
            console.print(f"  [doctor.dim]{(s.get('started_at') or '')[:10]}{proj}{dtype}[/doctor.dim] — {summary}")

    elif action == "search":
        if not query:
            console.print("[doctor.error]Usa --query[/doctor.error]")
            return
        from doctor.memory.db import search_wiki, search_papers
        wiki = search_wiki(db_path, query)
        papers = search_papers(db_path, query)
        for r in wiki:
            console.print(Panel(Markdown(r["body"][:500]), title=f"[doctor.name]{r['title']}[/doctor.name]", border_style="dim"))
        for p in papers:
            console.print(f"  [{p.get('year')}] {p.get('authors', '')[:60]}. \"{p.get('title')}\"")

    elif action == "papers":
        from doctor.memory.db import get_paper_count, get_connection
        with get_connection(db_path) as conn:
            papers = conn.execute("SELECT title, authors, year, source FROM papers ORDER BY year DESC LIMIT 20").fetchall()
        console.print(f"\n[doctor.name]Papers indexados (últimos 20):[/doctor.name]\n")
        for p in papers:
            console.print(f"  [{p['year']}] {(p['authors'] or '')[:50]}. \"{p['title'][:60]}\"")

    console.print()


def main() -> None:
    app()


if __name__ == "__main__":
    main()
