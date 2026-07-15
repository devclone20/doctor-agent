"""
Ingest all 87 developer-roadmap roadmaps into the Doctor wiki.

Idempotent: safe to run multiple times. Existing files are overwritten only
when content changes (compared by source mtime, stored in a sidecar index).

Output structure:
  doctor/knowledge/wiki/roadmaps/
    INDEX.md
    MASTER_KNOWLEDGE.md
    {category}/{roadmap}.md          (single file for small roadmaps)
    {category}/{roadmap}_part_N.md   (split files for roadmaps >400 content files)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Category mapping
# ---------------------------------------------------------------------------

CATEGORY_MAP: dict[str, str] = {
    # AI / ML
    "machine-learning": "ai-ml",
    "ai-engineer": "ai-ml",
    "ai-agents": "ai-ml",
    "ai-data-scientist": "ai-ml",
    "mlops": "ai-ml",
    "prompt-engineering": "ai-ml",
    "ai-product-builder": "ai-ml",
    "ai-red-teaming": "ai-ml",
    # Computer Science
    "computer-science": "computer-science",
    "datastructures-and-algorithms": "computer-science",
    "software-architect": "computer-science",
    "software-design-architecture": "computer-science",
    "system-design": "computer-science",
    # Infrastructure
    "devops": "infrastructure",
    "devops-beginner": "infrastructure",
    "docker": "infrastructure",
    "kubernetes": "infrastructure",
    "linux": "infrastructure",
    "aws": "infrastructure",
    "terraform": "infrastructure",
    "cloudflare": "infrastructure",
    "shell-bash": "infrastructure",
    "network-engineer": "infrastructure",
    # Development
    "python": "development",
    "backend": "development",
    "frontend": "development",
    "full-stack": "development",
    "typescript": "development",
    "nodejs": "development",
    "api-design": "development",
    "git-github": "development",
    "git-github-beginner": "development",
    "backend-beginner": "development",
    "frontend-beginner": "development",
    "javascript": "development",
    "html": "development",
    "css": "development",
    "graphql": "development",
    # Data
    "data-engineer": "data",
    "data-analyst": "data",
    "bi-analyst": "data",
    "postgresql-dba": "data",
    "mongodb": "data",
    "redis": "data",
    "elasticsearch": "data",
    "sql": "data",
    # Security
    "cyber-security": "security",
    "devsecops": "security",
    # Languages
    "cpp": "languages",
    "rust": "languages",
    "kotlin": "languages",
    "swift-ui": "languages",
    "scala": "languages",
    "ruby": "languages",
    "php": "languages",
    "golang": "languages",
    "java": "languages",
    # Frameworks
    "react": "frameworks",
    "angular": "frameworks",
    "vue": "frameworks",
    "nextjs": "frameworks",
    "django": "frameworks",
    "spring-boot": "frameworks",
    "laravel": "frameworks",
    "aspnet-core": "frameworks",
    "flutter": "frameworks",
    "react-native": "frameworks",
    "ruby-on-rails": "frameworks",
    "android": "frameworks",
    "ios": "frameworks",
}

# Anything not in CATEGORY_MAP falls into "other"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)

SPLIT_THRESHOLD = 400  # content files — split roadmaps larger than this


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text).strip()


def topic_name_from_filename(filename: str) -> str:
    """
    Convert 'basic-syntax@6xRncUs3_vxVbDur567QA.md' → 'Basic Syntax'
    """
    stem = Path(filename).stem
    # Remove the hash suffix after '@'
    name_part = stem.split("@")[0]
    return name_part.replace("-", " ").replace("_", " ").title()


def read_intro(roadmap_dir: Path, roadmap_name: str) -> str:
    """Read the top-level {name}.md intro file, stripping frontmatter."""
    intro_path = roadmap_dir / f"{roadmap_name}.md"
    if not intro_path.exists():
        return ""
    return strip_frontmatter(intro_path.read_text(encoding="utf-8"))


def collect_content_files(content_dir: Path) -> list[Path]:
    """Return all .md files in content/, sorted by name (stable ordering)."""
    if not content_dir.exists():
        return []
    return sorted(content_dir.glob("*.md"))


def build_roadmap_document(
    roadmap_name: str,
    intro: str,
    content_files: list[Path],
    part: int | None = None,
    part_files: list[Path] | None = None,
) -> str:
    """
    Build a single consolidated markdown document for a roadmap (or a part of it).
    """
    title_name = roadmap_name.replace("-", " ").title()
    part_suffix = f" — Part {part}" if part is not None else ""

    lines: list[str] = [f"# {title_name} Roadmap{part_suffix}", ""]

    if part is None and intro:
        lines += [intro, "", "---", ""]

    files_to_process = part_files if part_files is not None else content_files

    for cf in files_to_process:
        topic = topic_name_from_filename(cf.name)
        raw = cf.read_text(encoding="utf-8")
        body = strip_frontmatter(raw)
        if not body:
            continue
        lines += [f"## {topic}", "", body, ""]

    return "\n".join(lines)


def write_if_changed(path: Path, content: str) -> bool:
    """Write file only if content differs. Returns True if written."""
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# IST/MEIC relevance scoring
# ---------------------------------------------------------------------------

MEIC_HIGH_RELEVANCE = {
    "machine-learning", "ai-engineer", "ai-agents", "ai-data-scientist",
    "mlops", "prompt-engineering", "system-design", "software-design-architecture",
    "computer-science", "datastructures-and-algorithms", "python",
    "data-engineer", "postgresql-dba", "docker", "kubernetes",
}
MEIC_MED_RELEVANCE = {
    "software-architect", "devops", "aws", "terraform", "api-design",
    "backend", "typescript", "nodejs", "rust", "golang", "cpp",
    "ai-product-builder", "ai-red-teaming", "cyber-security", "devsecops",
    "sql", "redis", "elasticsearch", "mongodb", "data-analyst",
}


def relevance_stars(name: str) -> str:
    if name in MEIC_HIGH_RELEVANCE:
        return "⭐⭐⭐"
    if name in MEIC_MED_RELEVANCE:
        return "⭐⭐"
    return "⭐"


# ---------------------------------------------------------------------------
# INDEX.md builder
# ---------------------------------------------------------------------------

def build_index(
    roadmap_meta: list[dict],
) -> str:
    lines: list[str] = [
        "# Developer Roadmaps — Master Index",
        "",
        "Complete index of all ingested roadmaps from [roadmap.sh](https://roadmap.sh).",
        "",
        "## All Roadmaps",
        "",
        "| Roadmap | Category | Topics | IST MEIC Relevance |",
        "|---------|----------|--------|--------------------|",
    ]

    for m in sorted(roadmap_meta, key=lambda x: x["category"] + x["name"]):
        lines.append(
            f"| {m['name']} | {m['category']} | {m['topics']} | {m['stars']} |"
        )

    top15 = [
        m["name"] for m in roadmap_meta if m["stars"] == "⭐⭐⭐"
    ][:15]

    lines += [
        "",
        "## Roadmaps Essenciais para Dissertação MEIC IST",
        "",
        "Top roadmaps com relevância directa para investigação e dissertação em MEIC:",
        "",
    ]
    for name in top15:
        lines.append(f"- **{name}**")

    lines += [
        "",
        "## Roadmaps para Estado da Arte 2025",
        "",
        "Roadmaps mais relevantes para revisão de literatura e estado da arte:",
        "",
        "- **machine-learning** — fundamentos, algoritmos, avaliação de modelos",
        "- **ai-engineer** — LLMs, RAG, fine-tuning, deployment",
        "- **ai-agents** — agentes autónomos, ferramentas, orquestração",
        "- **mlops** — ciclo de vida de modelos em produção",
        "- **system-design** — arquitectura de sistemas de larga escala",
        "- **datastructures-and-algorithms** — fundamentos de CS",
        "- **prompt-engineering** — engenharia de prompts, chain-of-thought",
        "- **software-design-architecture** — padrões de design, DDD, CQRS",
        "- **data-engineer** — pipelines, data lakes, streaming",
        "- **computer-science** — base computacional transversal",
    ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# MASTER_KNOWLEDGE.md builder
# ---------------------------------------------------------------------------

MASTER_SECTIONS: list[tuple[str, str, list[str]]] = [
    (
        "AI & Machine Learning",
        "Núcleo de conhecimento para dissertações em IA, ML e sistemas inteligentes.",
        [
            "machine-learning", "ai-engineer", "ai-agents", "ai-data-scientist",
            "mlops", "prompt-engineering", "ai-product-builder", "ai-red-teaming",
        ],
    ),
    (
        "Computer Science Foundations",
        "Base matemática e computacional — transversal a todos os roadmaps.",
        [
            "computer-science", "datastructures-and-algorithms",
            "software-design-architecture", "software-architect", "system-design",
        ],
    ),
    (
        "Infrastructure & DevOps",
        "Deploy, escalabilidade, observabilidade e segurança operacional.",
        [
            "devops", "docker", "kubernetes", "linux", "aws",
            "terraform", "cloudflare", "shell-bash",
        ],
    ),
    (
        "Development & APIs",
        "Linguagens e frameworks de backend e frontend.",
        [
            "python", "backend", "frontend", "full-stack", "typescript",
            "nodejs", "api-design", "git-github",
        ],
    ),
    (
        "Data Engineering & Databases",
        "Pipelines de dados, bases de dados relacionais e NoSQL.",
        [
            "data-engineer", "data-analyst", "bi-analyst",
            "postgresql-dba", "mongodb", "redis", "elasticsearch", "sql",
        ],
    ),
    (
        "Security",
        "Segurança ofensiva e defensiva, DevSecOps.",
        ["cyber-security", "devsecops"],
    ),
    (
        "Languages",
        "Linguagens de sistemas e domínio específico.",
        ["cpp", "rust", "golang", "java", "kotlin", "scala", "swift-ui", "ruby", "php"],
    ),
    (
        "Frameworks & Platforms",
        "Ecosistemas de frameworks web e mobile.",
        [
            "react", "nextjs", "vue", "angular", "django",
            "spring-boot", "laravel", "aspnet-core", "flutter", "react-native",
        ],
    ),
]

ROADMAP_INTERLOCKS: list[tuple[str, list[str]]] = [
    ("ML Engineer / AI Researcher", [
        "python", "machine-learning", "mlops", "datastructures-and-algorithms",
        "docker", "kubernetes", "system-design",
    ]),
    ("AI Agent Developer", [
        "ai-agents", "ai-engineer", "prompt-engineering", "python",
        "api-design", "system-design",
    ]),
    ("Data Engineer", [
        "python", "sql", "data-engineer", "postgresql-dba",
        "docker", "kubernetes", "aws",
    ]),
    ("Backend / API Engineer", [
        "backend", "python", "nodejs", "api-design",
        "postgresql-dba", "redis", "docker", "system-design",
    ]),
    ("Dissertação MEIC — IA", [
        "machine-learning", "ai-engineer", "ai-agents",
        "mlops", "system-design", "python",
        "datastructures-and-algorithms", "computer-science",
    ]),
]

DISSERTATION_STACKS: list[tuple[str, str]] = [
    (
        "Dissertação em LLMs / NLP",
        "Python + machine-learning + ai-engineer + prompt-engineering + mlops + system-design",
    ),
    (
        "Dissertação em Sistemas Distribuídos",
        "system-design + software-design-architecture + docker + kubernetes + aws + backend",
    ),
    (
        "Dissertação em Segurança",
        "cyber-security + devsecops + system-design + software-architect",
    ),
    (
        "Dissertação em Engenharia de Dados",
        "data-engineer + postgresql-dba + sql + python + docker + aws",
    ),
    (
        "Dissertação em Agentes Autónomos",
        "ai-agents + ai-engineer + machine-learning + prompt-engineering + api-design + python",
    ),
]


def build_master_knowledge(roadmap_meta: list[dict]) -> str:
    meta_by_name = {m["name"]: m for m in roadmap_meta}

    lines: list[str] = [
        "# Master Knowledge — Developer Roadmaps",
        "",
        "Síntese estruturada de todos os roadmaps para consulta rápida pelo Doctor.",
        "Gerado automaticamente — não editar manualmente.",
        "",
        "---",
        "",
    ]

    for section_title, section_desc, roadmap_names in MASTER_SECTIONS:
        lines += [f"## {section_title}", "", section_desc, ""]
        for name in roadmap_names:
            m = meta_by_name.get(name)
            if not m:
                continue
            lines += [
                f"### {name}",
                f"- **Categoria:** {m['category']}",
                f"- **Tópicos:** {m['topics']}",
                f"- **IST MEIC:** {m['stars']}",
                f"- **Ficheiro(s):** {', '.join(m['files'])}",
                "",
            ]

    lines += [
        "---",
        "",
        "## Interligações entre Roadmaps",
        "",
        "Roadmaps que devem ser estudados em conjunto por perfil:",
        "",
    ]
    for profile, deps in ROADMAP_INTERLOCKS:
        lines.append(f"**{profile}:** " + " → ".join(deps))
        lines.append("")

    lines += [
        "---",
        "",
        "## Stack Recomendada por Tipo de Dissertação MEIC IST",
        "",
    ]
    for title, stack in DISSERTATION_STACKS:
        lines += [f"**{title}**", f"  {stack}", ""]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    roadmaps_src = Path("/tmp/developer-roadmap/src/data/roadmaps")
    wiki_out = Path(__file__).parent.parent / "doctor" / "knowledge" / "wiki" / "roadmaps"

    if not roadmaps_src.exists():
        print(f"ERROR: source directory not found: {roadmaps_src}", file=sys.stderr)
        sys.exit(1)

    wiki_out.mkdir(parents=True, exist_ok=True)

    roadmap_dirs = sorted(p for p in roadmaps_src.iterdir() if p.is_dir())

    total_roadmaps = 0
    total_files_written = 0
    total_bytes = 0
    roadmap_meta: list[dict] = []

    for roadmap_dir in roadmap_dirs:
        name = roadmap_dir.name
        category = CATEGORY_MAP.get(name, "other")
        category_dir = wiki_out / category
        category_dir.mkdir(parents=True, exist_ok=True)

        intro = read_intro(roadmap_dir, name)
        content_dir = roadmap_dir / "content"
        content_files = collect_content_files(content_dir)
        topic_count = len(content_files)

        written_files: list[str] = []

        if topic_count == 0:
            # Roadmap has no content files — write just the intro
            doc = f"# {name.replace('-', ' ').title()} Roadmap\n\n{intro}\n"
            out_path = category_dir / f"{name}.md"
            if write_if_changed(out_path, doc):
                total_files_written += 1
                total_bytes += len(doc.encode())
            written_files.append(out_path.name)

        elif topic_count <= SPLIT_THRESHOLD:
            doc = build_roadmap_document(name, intro, content_files)
            out_path = category_dir / f"{name}.md"
            if write_if_changed(out_path, doc):
                total_files_written += 1
                total_bytes += len(doc.encode())
            written_files.append(out_path.name)

        else:
            # Split into chunks of SPLIT_THRESHOLD
            chunk_size = SPLIT_THRESHOLD
            chunks = [
                content_files[i : i + chunk_size]
                for i in range(0, len(content_files), chunk_size)
            ]
            for part_idx, chunk in enumerate(chunks, start=1):
                doc = build_roadmap_document(
                    name, intro if part_idx == 1 else "",
                    content_files, part=part_idx, part_files=chunk,
                )
                out_path = category_dir / f"{name}_part{part_idx}.md"
                if write_if_changed(out_path, doc):
                    total_files_written += 1
                    total_bytes += len(doc.encode())
                written_files.append(out_path.name)

        total_roadmaps += 1
        roadmap_meta.append({
            "name": name,
            "category": category,
            "topics": topic_count,
            "stars": relevance_stars(name),
            "files": written_files,
        })

        print(f"  [{category}] {name} — {topic_count} topics → {len(written_files)} file(s)")

    # Write INDEX.md
    index_content = build_index(roadmap_meta)
    index_path = wiki_out / "INDEX.md"
    if write_if_changed(index_path, index_content):
        total_files_written += 1
        total_bytes += len(index_content.encode())
    print(f"\n  [index] INDEX.md written")

    # Write MASTER_KNOWLEDGE.md
    master_content = build_master_knowledge(roadmap_meta)
    master_path = wiki_out / "MASTER_KNOWLEDGE.md"
    if write_if_changed(master_path, master_content):
        total_files_written += 1
        total_bytes += len(master_content.encode())
    print(f"  [index] MASTER_KNOWLEDGE.md written")

    print(f"""
========================================
INGESTION COMPLETE
========================================
  Roadmaps processed : {total_roadmaps}
  Wiki files written : {total_files_written}
  Total KB ingested  : {total_bytes / 1024:.1f} KB
  Output dir         : {wiki_out}
========================================
""")


if __name__ == "__main__":
    main()
