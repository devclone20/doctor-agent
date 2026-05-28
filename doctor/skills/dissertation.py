"""
Skill de escrita de dissertações IST.
Gera prompts estruturados para cada tipo de trabalho académico.
"""


def get_dissertation_prompt(
    doc_type: str,
    topic: str,
    spec: str = "",
    language: str = "pt",
    output_format: str = "markdown",
) -> str:
    """
    Gera prompt para escrita de dissertação completa.

    doc_type: "msc", "phd", "bsc", "article"
    topic: tema da dissertação
    spec: especificações adicionais (tópicos, subtópicos, requisitos)
    language: "pt" ou "en"
    output_format: "markdown" ou "latex"
    """
    type_names = {
        "msc": "Dissertação de Mestrado",
        "phd": "Tese de Doutoramento",
        "bsc": "Trabalho de Licenciatura",
        "article": "Artigo Científico",
    }
    type_name = type_names.get(doc_type, doc_type)
    lang_name = "Português" if language == "pt" else "English"
    fmt_name = "Markdown (com indicações para LaTeX)" if output_format == "markdown" else "LaTeX"

    spec_section = f"\n\n## Especificações do utilizador:\n{spec}" if spec else ""

    return f"""Escreve uma **{type_name}** completa sobre o tema: **{topic}**

Língua: {lang_name}
Formato de output: {fmt_name}
Padrão: Instituto Superior Técnico (IST), Universidade de Lisboa
Área: Engenharia Informática e de Computadores — Machine Learning / AI / Cloud Architecture
{spec_section}

## Instruções de escrita:

1. Segue rigorosamente a estrutura obrigatória IST para {type_name}
2. Cada secção deve ser substancial e académicamente rigorosa
3. Inclui citações bibliográficas reais e relevantes em formato IEEE no texto [1], [2], etc.
4. Para figuras: inclui descrição e legenda completa — eu adicionarei as imagens reais
5. Para tabelas: inclui estrutura completa com dados realistas ou placeholders claros
6. Para equações: formato LaTeX correcto, numeradas
7. Pesquisa artigos relevantes para suportar cada afirmação importante
8. O estado da arte deve ser crítico — não apenas listar trabalhos, mas posicionar o trabalho
9. A metodologia deve ser suficientemente detalhada para ser reproduzível
10. Identifica claramente onde preciso de dados experimentais reais com [DADOS REAIS NECESSÁRIOS: ...]
11. No final, apresenta a bibliografia completa em formato IEEE

Começa com a estrutura completa e depois desenvolve cada secção.
"""


def get_section_prompt(section: str, topic: str, context: str = "", doc_type: str = "msc") -> str:
    """
    Gera prompt para escrever uma secção específica da dissertação.

    section: "introduction", "background", "methodology", "evaluation", "conclusion", etc.
    """
    section_guides = {
        "introduction": """
Escreve a secção de Introdução. Deve incluir:
- Contextualização do problema (parágrafo amplo)
- Definição precisa do problema e porque é difícil/importante
- Overview da abordagem proposta
- Lista explícita de contribuições (bullet points): "As principais contribuições deste trabalho são:"
- Estrutura da dissertação: "O restante desta dissertação está organizado da seguinte forma:"
Extensão: 3-5 páginas (1500-2500 palavras)
""",
        "background": """
Escreve o capítulo de Background / Estado da Arte. Deve incluir:
- Secção de conceitos fundamentais necessários (com citações)
- Análise crítica dos trabalhos relacionados (agrupados por abordagem)
- Para cada grupo: limitações e como o trabalho actual as endereça
- Tabela comparativa dos trabalhos mais relevantes (se aplicável)
- Sumário do posicionamento do trabalho
Extensão: 5-10 páginas (2500-5000 palavras)
""",
        "methodology": """
Escreve o capítulo de Metodologia / Arquitectura / Abordagem. Deve incluir:
- Visão geral com diagrama de arquitectura (descrever para criar figura)
- Justificação das escolhas de design
- Cada componente do sistema em detalhe
- Algoritmos em pseudocódigo (formato LaTeX algorithm)
- Decisões de implementação e trade-offs
Extensão: 5-8 páginas (2500-4000 palavras)
""",
        "implementation": """
Escreve o capítulo de Implementação. Deve incluir:
- Stack tecnológico e justificação
- Ambiente de desenvolvimento (hardware, versões de software)
- Detalhes de implementação dos componentes principais
- Desafios encontrados e soluções
- Snippets de código relevantes (não exaustivos)
Extensão: 3-6 páginas (1500-3000 palavras)
""",
        "evaluation": """
Escreve o capítulo de Avaliação / Resultados Experimentais. Deve incluir:
- Research questions (RQ1, RQ2, ...)
- Setup experimental (datasets, baselines, métricas, hardware)
- Resultados em tabelas com comparação a baselines
- Análise e discussão dos resultados
- Ablation study (se aplicável)
- Análise de limitações e casos de falha
Nota: usa [RESULTADOS REAIS NECESSÁRIOS: ...] onde precisas de dados reais.
Extensão: 5-8 páginas (2500-4000 palavras)
""",
        "conclusion": """
Escreve o capítulo de Conclusão e Trabalho Futuro. Deve incluir:
- Sumário das contribuições (em retrospectiva)
- Resposta directa às research questions
- Limitações honestas do trabalho
- Trabalho futuro específico e accionável (não vago)
- Reflexão final sobre o impacto do trabalho
Extensão: 2-3 páginas (1000-1500 palavras)
""",
        "abstract": """
Escreve o Resumo em Português (máx. 250 palavras) e o Abstract em Inglês (máx. 250 palavras).
Cada um deve conter os 4 elementos obrigatórios:
1. Contexto e motivação do problema
2. Abordagem e metodologia
3. Resultados principais (com métricas quando possível)
4. Conclusão e impacto/contribuição

Keywords: 5-8 palavras-chave relevantes (em inglês para o abstract).
""",
    }

    section_guide = section_guides.get(section, f"Escreve a secção de {section}.")
    context_part = f"\n\nContexto adicional:\n{context}" if context else ""

    return f"""Escreve a seguinte secção para uma {doc_type.upper()} sobre: **{topic}**

{section_guide}
{context_part}

Segue o padrão IST. Usa citações IEEE reais pesquisando nas bases de dados académicas.
Apresenta o texto directamente, pronto a usar.
"""


def get_abstract_evaluation(abstract: str) -> str:
    """Gera prompt para avaliar um abstract."""
    return f"""Avalia este abstract de acordo com os padrões IST e IEEE:

---
{abstract}
---

Verifica:
1. Tem os 4 elementos obrigatórios? (contexto, método, resultados, conclusão)
2. Está dentro do limite de 250 palavras?
3. Há claims sem suporte?
4. A linguagem é precisa e não ambígua?
5. As keywords são adequadas?

Apresenta a avaliação e uma versão melhorada se necessário.
"""
