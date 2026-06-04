# Doctor Skills — Architecture

## What a skill is

A skill is a **pure prompt module**: a Python module that exports one or more functions
returning strings. Skills have no state, no I/O, no side effects.

They are called by:
1. The CLI (`doctor/cli/main.py`) — builds a prompt then calls `agent.chat(prompt)`
2. The agent loop (`doctor/core/agent.py`) — passes the prompt to the LLM

```
User → CLI command → Skill (prompt builder) → Agent → LLM → Response
```

## Modules

| Module | Purpose |
|---|---|
| `dissertation.py` | Prompts for full dissertations, individual sections, LaTeX export, IST-DEI template |
| `review.py` | Prompts for academic review (structure, citations, language, technical) |
| `citation.py` | Citation formatting helpers (delegated to `academic_search.py`) |
| `latex_export.py` | Programmatic Markdown→LaTeX conversion, IST preamble, document wrapping |

## Skills in `dissertation.py`

| Function | What it does |
|---|---|
| `get_dissertation_prompt(doc_type, topic, …)` | Full dissertation prompt. Supports `output_format="latex"` and `ist_style=True` |
| `get_section_prompt(section, topic, …)` | Single section (introduction, methodology, etc.) |
| `get_latex_export_prompt(content, doc_type)` | Asks the LLM to convert Markdown draft to IST LaTeX |
| `get_ist_dei_template(doc_type)` | Returns the complete IST-DEI skeleton with all mandatory sections |
| `get_abstract_evaluation(abstract)` | Review prompt for an abstract |
| `IST_DISSERTATION_STYLE` | Dict with all IST formatting norms (font, margins, spacing, citation style) |

## Skills in `latex_export.py`

Programmatic conversion (no LLM needed). Used as fallback or preprocessing.

| Function | What it does |
|---|---|
| `get_ist_latex_preamble(doc_type)` | Full LaTeX preamble (packages, geometry, biblatex IEEE) |
| `markdown_to_latex_structure(content)` | Converts Markdown headings, lists, bold/italic, citations to LaTeX |
| `wrap_in_latex_document(body, doc_type)` | Wraps body in full document with IST cover page and bibliography |

## Adding a new skill

1. Create `doctor/skills/my_skill.py`
2. Export functions with signature `(…) -> str`
3. No imports from `doctor.core` or `doctor.memory` — skills are pure
4. Call from CLI or pass the returned string directly to `agent.chat()`

## Invariants

- Skills never call the LLM directly
- Skills never read or write files
- Skills never have module-level state
- All exported functions are pure (same input → same output)
