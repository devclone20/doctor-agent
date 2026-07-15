"""
Skill de gestão bibliográfica.
Pesquisa, formata e gere citações em IEEE, APA, BibTeX.
"""


def get_citation_search_prompt(topic: str, style: str = "ieee") -> str:
    """Gera prompt para pesquisar e formatar citações sobre um tema."""
    return f"""Pesquisa artigos científicos relevantes sobre: **{topic}**

Usa as ferramentas de pesquisa académica (search_academic) para encontrar:
1. Os papers mais citados e fundamentais sobre o tema
2. Papers recentes (últimos 3 anos)
3. Dissertações do IST se relevante

Para cada paper encontrado, apresenta:
- Citação em formato {style.upper()} (numerada para IEEE)
- Entrada BibTeX
- 1-2 frases sobre o que o paper contribui e quando citar

No final, apresenta a lista completa de referências pronta a copiar para a bibliografia.
"""


def get_bibliography_from_text(text: str, style: str = "ieee") -> str:
    """Gera prompt para extrair e completar referências de um texto."""
    return f"""Analisa este texto académico e faz o seguinte:

1. Identifica todas as citações no texto (ex: [1], [2], ou (Autor, Ano))
2. Para cada citação, pesquisa o paper real que corresponde ao contexto
3. Verifica se o formato das citações inline está correcto para {style.upper()}
4. Gera a secção de Bibliografia completa no formato {style.upper()}
5. Indica se alguma citação parece incorrecta ou não encontrada

---
Texto:
{text[:5000]}
---

Apresenta:
- Lista das referências identificadas
- Status de cada uma (✅ encontrada / ⚠️ não verificada / ❌ incorrecta)
- Secção de Referências completa em formato {style.upper()}
"""


def get_bibtex_from_papers(papers: list[str]) -> str:
    """Gera prompt para obter entradas BibTeX de uma lista de papers."""
    papers_list = "\n".join(f"{i+1}. {p}" for i, p in enumerate(papers))
    return f"""Para cada paper na lista, pesquisa os metadados completos e gera a entrada BibTeX:

{papers_list}

Para cada um:
1. Pesquisa usando search_academic ou lookup_doi
2. Verifica os metadados (autores, ano, venue)
3. Gera a entrada BibTeX correcta

Apresenta todas as entradas BibTeX juntas, prontas a copiar para o ficheiro .bib.
"""


def format_references_section(
    references: list[dict],
    style: str = "ieee",
) -> str:
    """
    Formata uma lista de referências numa secção de bibliografia.

    references: lista de dicts com campos title, authors, year, venue, doi, etc.
    """
    if not references:
        return "Nenhuma referência fornecida."

    from doctor.core.academic_search import build_ieee_citation, build_apa_citation, build_bibtex

    lines = []

    if style == "ieee":
        lines.append("## Referências\n")
        for i, ref in enumerate(references, 1):
            lines.append(build_ieee_citation(ref, ref_num=i))
    elif style == "apa":
        lines.append("## References\n")
        for ref in references:
            lines.append(build_apa_citation(ref))
    elif style == "bibtex":
        for ref in references:
            lines.append(build_bibtex(ref))
            lines.append("")

    return "\n".join(lines)
