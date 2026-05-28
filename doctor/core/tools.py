"""
Ferramentas do Doctor.
10 tools: academic search, fetch paper, cite, write/read file, memory, web search.
"""

import os
from pathlib import Path

TOOL_DEFINITIONS = [
    {
        "name": "search_academic",
        "description": (
            "Pesquisa artigos científicos em múltiplas bases de dados académicas: "
            "IST Scholar, arXiv, Semantic Scholar, OpenAlex, PubMed. "
            "Retorna títulos, autores, anos, abstracts e citações formatadas em IEEE. "
            "Usar para encontrar referências bibliográficas, estado da arte, ou papers específicos."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Query de pesquisa (em inglês para melhores resultados). Ex: 'transformer architecture image classification'",
                },
                "sources": {
                    "type": "array",
                    "items": {"type": "string", "enum": ["ist", "arxiv", "semantic", "openalex", "pubmed"]},
                    "description": "Fontes a pesquisar. Default: ['arxiv', 'semantic', 'ist', 'openalex']. Usar 'pubmed' para biomédico.",
                },
                "limit": {
                    "type": "integer",
                    "description": "Número de resultados por fonte (default: 5, max: 10)",
                },
                "citation_style": {
                    "type": "string",
                    "enum": ["ieee", "apa", "bibtex"],
                    "description": "Estilo de citação a retornar (default: ieee)",
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "fetch_paper",
        "description": (
            "Descarrega e analisa o conteúdo de um artigo científico ou página web académica. "
            "Extrai título, abstract, secções principais, e metadata. "
            "Usar quando se fornece uma URL de paper para estudar ou citar."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "URL do artigo (arXiv, IST Scholar, DOI, ou qualquer página).",
                },
                "extract": {
                    "type": "string",
                    "enum": ["full", "abstract", "metadata"],
                    "description": "O que extrair: 'full' (tudo), 'abstract' (só resumo), 'metadata' (título, autores, ano). Default: 'full'",
                },
            },
            "required": ["url"],
        },
    },
    {
        "name": "lookup_doi",
        "description": (
            "Procura metadados completos de um artigo pelo seu DOI (Digital Object Identifier). "
            "Retorna título, autores, ano, journal, e citação formatada. "
            "Usar quando se tem um DOI e se quer a citação correcta."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "doi": {
                    "type": "string",
                    "description": "DOI do artigo. Ex: '10.1038/nature14539' ou 'https://doi.org/10.1038/nature14539'",
                },
                "citation_style": {
                    "type": "string",
                    "enum": ["ieee", "apa", "bibtex", "all"],
                    "description": "Estilo de citação (default: 'all' — retorna todos)",
                },
            },
            "required": ["doi"],
        },
    },
    {
        "name": "write_file",
        "description": (
            "Guarda conteúdo num ficheiro — secções de dissertação, capítulos LaTeX, "
            "bibliografias, rascunhos de artigos. "
            "Usar para persistir trabalho gerado."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Caminho relativo ao directório de trabalho. Ex: 'dissertation/chapter2.md' ou 'bibliography.bib'",
                },
                "content": {
                    "type": "string",
                    "description": "Conteúdo a escrever no ficheiro.",
                },
                "mode": {
                    "type": "string",
                    "enum": ["write", "append"],
                    "description": "Modo: 'write' (substituir) ou 'append' (adicionar ao final). Default: 'write'",
                },
            },
            "required": ["path", "content"],
        },
    },
    {
        "name": "read_file",
        "description": (
            "Lê o conteúdo de um ficheiro existente para revisão ou análise. "
            "Usar para ler dissertações, artigos, ou código submetido para revisão."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Caminho do ficheiro a ler.",
                },
                "max_chars": {
                    "type": "integer",
                    "description": "Máximo de caracteres a retornar (default: 8000).",
                },
            },
            "required": ["path"],
        },
    },
    {
        "name": "list_files",
        "description": "Lista ficheiros num directório do projecto.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Directório a listar. Default: directório actual.",
                },
                "pattern": {
                    "type": "string",
                    "description": "Padrão glob. Ex: '*.tex', '*.md', '*.bib'",
                },
            },
            "required": [],
        },
    },
    {
        "name": "search_memory",
        "description": (
            "Pesquisa na base de conhecimento local do Doctor: wiki académico, "
            "papers indexados, normas IST, guias de escrita científica. "
            "Usar quando se precisa de informação específica sobre normas, citações, ou conhecimento guardado."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Query de pesquisa em português ou inglês.",
                },
                "source": {
                    "type": "string",
                    "enum": ["wiki", "papers", "all"],
                    "description": "Onde pesquisar: 'wiki' (normas/guias), 'papers' (artigos indexados), 'all' (tudo). Default: 'all'",
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "save_learning",
        "description": (
            "Guarda novo conhecimento académico na base de dados permanente do Doctor. "
            "Usar para memorizar papers importantes, normas específicas, ou descobertas de investigação."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "Título do conhecimento a guardar.",
                },
                "content": {
                    "type": "string",
                    "description": "Conteúdo a guardar (artigo, norma, descoberta, etc.)",
                },
                "tags": {
                    "type": "string",
                    "description": "Tags separadas por vírgula. Ex: 'ml,transformers,ist,dissertação'",
                },
            },
            "required": ["title", "content"],
        },
    },
    {
        "name": "search_web",
        "description": (
            "Pesquisa na web por informação geral. Usar como fallback quando as bases "
            "académicas não têm o que se precisa, ou para verificar factos recentes."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Query de pesquisa.",
                },
                "max_results": {
                    "type": "integer",
                    "description": "Número máximo de resultados (default: 5).",
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "run_command",
        "description": (
            "Executa um comando no terminal — para compilar LaTeX, verificar ficheiros, "
            "ou tarefas de sistema. Comandos perigosos são bloqueados."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "command": {
                    "type": "string",
                    "description": "Comando a executar. Ex: 'lualatex main.tex', 'biber main', 'ls dissertation/'",
                },
                "working_dir": {
                    "type": "string",
                    "description": "Directório de trabalho (opcional).",
                },
            },
            "required": ["command"],
        },
    },
]

# Comandos perigosos bloqueados
BLOCKED_COMMANDS = {
    "rm -rf", "sudo rm", "drop table", "drop database",
    "format c:", "mkfs", "dd if=", "> /dev/", "chmod 777",
    "curl | sh", "wget | sh", ":(){:|:&};:", "fork bomb",
}


def execute_tool(tool_name: str, tool_input: dict, db_path: Path) -> str:
    """Dispatcher principal de ferramentas."""
    try:
        if tool_name == "search_academic":
            return _search_academic(tool_input)
        elif tool_name == "fetch_paper":
            return _fetch_paper(tool_input)
        elif tool_name == "lookup_doi":
            return _lookup_doi(tool_input)
        elif tool_name == "write_file":
            return _write_file(tool_input)
        elif tool_name == "read_file":
            return _read_file(tool_input)
        elif tool_name == "list_files":
            return _list_files(tool_input)
        elif tool_name == "search_memory":
            return _search_memory(tool_input, db_path)
        elif tool_name == "save_learning":
            return _save_learning(tool_input, db_path)
        elif tool_name == "search_web":
            return _search_web(tool_input)
        elif tool_name == "run_command":
            return _run_command(tool_input)
        else:
            return f"Ferramenta desconhecida: {tool_name}"
    except Exception as e:
        return f"Erro na ferramenta {tool_name}: {e}"


def _search_academic(inp: dict) -> str:
    from doctor.core.academic_search import search_academic, format_results_for_agent
    query = inp.get("query", "")
    sources = inp.get("sources")
    limit = min(int(inp.get("limit", 5)), 10)
    style = inp.get("citation_style", "ieee")
    results = search_academic(query, sources=sources, limit_per_source=limit)
    return format_results_for_agent(results, style=style)


def _fetch_paper(inp: dict) -> str:
    import httpx
    from bs4 import BeautifulSoup

    url = inp.get("url", "")
    extract = inp.get("extract", "full")

    try:
        with httpx.Client(timeout=20.0, follow_redirects=True) as client:
            resp = client.get(url, headers={"User-Agent": "DoctorAgent/1.0"})
            resp.raise_for_status()

        # arXiv: redirigir para abstract page
        if "arxiv.org/pdf" in url:
            abs_url = url.replace("/pdf/", "/abs/").replace(".pdf", "")
            with httpx.Client(timeout=20.0) as client:
                resp = client.get(abs_url, headers={"User-Agent": "DoctorAgent/1.0"})

        soup = BeautifulSoup(resp.text, "lxml")

        # Remover scripts, styles, nav
        for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()

        if extract == "abstract":
            # Procurar campo abstract
            for selector in ["#abstract", ".abstract", "[class*=abstract]", "blockquote"]:
                el = soup.select_one(selector)
                if el:
                    return f"Abstract:\n{el.get_text(separator=' ', strip=True)[:1000]}"
            return soup.get_text(separator=" ", strip=True)[:500]

        elif extract == "metadata":
            title = soup.find("title")
            title_text = title.get_text(strip=True) if title else "N/A"
            meta_desc = soup.find("meta", {"name": "description"})
            description = meta_desc.get("content", "")[:300] if meta_desc else ""
            return f"Título: {title_text}\nDescrição: {description}\nURL: {url}"

        else:  # full
            text = soup.get_text(separator="\n", strip=True)
            lines = [l for l in text.splitlines() if len(l.strip()) > 20]
            return "\n".join(lines[:100])[:6000]

    except Exception as e:
        return f"Erro ao buscar {url}: {e}"


def _lookup_doi(inp: dict) -> str:
    from doctor.core.academic_search import lookup_doi, search_arxiv
    doi = inp.get("doi", "")
    style = inp.get("citation_style", "all")
    paper = lookup_doi(doi)

    # Fallback: se CrossRef falhar, tentar arXiv directamente
    if not paper:
        # Detectar arXiv ID: 10.48550/arXiv.XXXX ou XXXX.XXXXX
        arxiv_id = ""
        if "arXiv." in doi:
            arxiv_id = doi.split("arXiv.")[-1]
        elif doi.replace(".", "").replace("/", "").isalnum() and len(doi) < 20:
            arxiv_id = doi  # pode ser um arXiv ID directo
        if arxiv_id:
            results = search_arxiv(f"id:{arxiv_id}", limit=1)
            if results:
                paper = results[0]
    if not paper:
        return f"DOI/ID não encontrado: {doi}"
    lines = [
        f"Título: {paper.get('title')}",
        f"Autores: {paper.get('authors')}",
        f"Ano: {paper.get('year')} | Venue: {paper.get('venue')}",
        f"DOI: {paper.get('doi')}",
        "",
    ]
    if style in ("ieee", "all"):
        lines.append(f"IEEE: {paper.get('citation_ieee')}")
    if style in ("apa", "all"):
        lines.append(f"APA: {paper.get('citation_apa')}")
    if style in ("bibtex", "all"):
        lines.append(f"\nBibTeX:\n{paper.get('bibtex')}")
    return "\n".join(lines)


def _write_file(inp: dict) -> str:
    path = Path(inp.get("path", "output.md"))
    content = inp.get("content", "")
    mode = inp.get("mode", "write")

    # Segurança: apenas dentro do directório actual ou ~/doctor-work
    work_dir = Path(os.path.expanduser("~/doctor-work"))
    work_dir.mkdir(parents=True, exist_ok=True)

    if not path.is_absolute():
        full_path = work_dir / path
    else:
        full_path = path

    full_path.parent.mkdir(parents=True, exist_ok=True)

    file_mode = "a" if mode == "append" else "w"
    with open(full_path, file_mode, encoding="utf-8") as f:
        f.write(content)

    return f"Ficheiro guardado: {full_path} ({len(content)} caracteres)"


def _read_file(inp: dict) -> str:
    path = Path(inp.get("path", ""))
    max_chars = int(inp.get("max_chars", 8000))

    work_dir = Path(os.path.expanduser("~/doctor-work"))
    if not path.is_absolute():
        full_path = work_dir / path
    else:
        full_path = path

    if not full_path.exists():
        return f"Ficheiro não encontrado: {full_path}"

    try:
        content = full_path.read_text(encoding="utf-8", errors="replace")
        if len(content) > max_chars:
            return content[:max_chars] + f"\n\n[... truncado. Total: {len(content)} chars ...]"
        return content
    except Exception as e:
        return f"Erro ao ler {full_path}: {e}"


def _list_files(inp: dict) -> str:
    path_str = inp.get("path", ".")
    pattern = inp.get("pattern", "*")

    work_dir = Path(os.path.expanduser("~/doctor-work"))
    path = Path(path_str)
    if not path.is_absolute():
        path = work_dir / path_str if path_str != "." else work_dir

    if not path.exists():
        return f"Directório não encontrado: {path}"

    files = list(path.glob(pattern))
    if not files:
        return f"Nenhum ficheiro encontrado em {path} com padrão '{pattern}'"

    lines = [f"Ficheiros em {path}:"]
    for f in sorted(files)[:50]:
        size = f.stat().st_size if f.is_file() else 0
        lines.append(f"  {'[DIR]' if f.is_dir() else '[FIC]'} {f.name} ({size} bytes)")
    return "\n".join(lines)


def _search_memory(inp: dict, db_path: Path) -> str:
    from doctor.memory.db import search_wiki, search_papers
    query = inp.get("query", "")
    source = inp.get("source", "all")
    results_parts = []

    if source in ("wiki", "all"):
        wiki_results = search_wiki(db_path, query, limit=3)
        if wiki_results:
            results_parts.append("=== Wiki Académico ===")
            for r in wiki_results:
                results_parts.append(f"\n### {r['title']}\n{r['body'][:600]}...")

    if source in ("papers", "all"):
        paper_results = search_papers(db_path, query, limit=5)
        if paper_results:
            results_parts.append("\n=== Papers Indexados ===")
            for p in paper_results:
                results_parts.append(
                    f"\n[{p.get('year')}] {p.get('authors', '')[:60]}. \"{p.get('title')}\"\n"
                    f"  {p.get('citation_ieee', '')}"
                )

    if not results_parts:
        return f"Nenhum resultado encontrado para: {query}"
    return "\n".join(results_parts)


def _save_learning(inp: dict, db_path: Path) -> str:
    from doctor.memory.db import upsert_wiki_page
    import hashlib
    title = inp.get("title", "")
    content = inp.get("content", "")
    tags = inp.get("tags", "learned")
    slug = "learned_" + hashlib.md5(title.encode()).hexdigest()[:8]
    upsert_wiki_page(db_path, slug, title, content, tags=tags)
    return f"Conhecimento guardado: '{title}' (slug: {slug})"


def _search_web(inp: dict) -> str:
    query = inp.get("query", "")
    max_results = int(inp.get("max_results", 5))
    try:
        from ddgs import DDGS
    except ImportError:
        try:
            from duckduckgo_search import DDGS
        except ImportError:
            return "Web search não disponível (instalar ddgs)."
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
        if not results:
            return "Sem resultados web."
        lines = []
        for r in results:
            lines.append(f"**{r.get('title', '')}**")
            lines.append(r.get("body", "")[:200])
            lines.append(r.get("href", ""))
            lines.append("")
        return "\n".join(lines)
    except Exception as e:
        return f"Erro na pesquisa web: {e}"


def _run_command(inp: dict) -> str:
    import subprocess
    command = inp.get("command", "")
    working_dir = inp.get("working_dir", os.path.expanduser("~/doctor-work"))

    # Verificar comandos bloqueados
    command_lower = command.lower()
    for blocked in BLOCKED_COMMANDS:
        if blocked in command_lower:
            return f"Comando bloqueado por segurança: '{blocked}'"

    # Apenas comandos permitidos para LaTeX e navegação
    allowed_prefixes = (
        "lualatex", "pdflatex", "xelatex", "biber", "bibtex",
        "ls", "cat", "head", "tail", "echo", "pwd", "find", "grep",
        "python", "python3", "pip", "pip3", "wc",
    )
    cmd_name = command.strip().split()[0] if command.strip() else ""
    if not any(command.strip().startswith(p) for p in allowed_prefixes):
        return f"Comando não permitido: '{cmd_name}'. Apenas LaTeX, ls, cat, python."

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=60,
            cwd=working_dir,
        )
        output = result.stdout[:2000] + (result.stderr[:500] if result.stderr else "")
        return output.strip() or "Comando executado sem output."
    except subprocess.TimeoutExpired:
        return "Timeout: comando demorou mais de 60 segundos."
    except Exception as e:
        return f"Erro ao executar: {e}"
