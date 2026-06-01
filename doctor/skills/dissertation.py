"""
Skill de escrita de dissertações IST.
Gera prompts estruturados para cada tipo de trabalho académico.
"""

# ─── Normas IST para dissertação ─────────────────────────────────────────────

IST_DISSERTATION_STYLE: dict[str, object] = {
    "font_family": "Arial (corpo) / Helvetica em LaTeX",
    "font_size_pt": 10,
    "line_spacing": "1.5 linhas",
    "margins_cm": {
        "top": 2.5,
        "bottom": 2.5,
        "left": 2.5,
        "right": 2.5,
    },
    "citation_style": "IEEE (numeradas, [N] no texto, lista no final por ordem de aparecimento)",
    "cover_elements": [
        "Logótipo IST (canto superior esquerdo)",
        "Título em bold, centrado",
        "Nome do autor",
        "Tipo de dissertação (ex: Dissertação de Mestrado)",
        "Nome do curso",
        "Nome do orientador",
        "Mês e ano",
    ],
    "mandatory_sections": [
        "Capa",
        "Declaração de Honra",
        "Agradecimentos (opcional)",
        "Resumo (português, máx. 250 palavras + keywords)",
        "Abstract (inglês, máx. 250 palavras + keywords)",
        "Índice",
        "Lista de Figuras",
        "Lista de Tabelas",
        "Lista de Abreviaturas (se aplicável)",
        "Capítulos (Introdução, Background, Metodologia, Implementação, Avaliação, Conclusão)",
        "Referências Bibliográficas",
        "Anexos (se aplicável)",
    ],
    "language": "Português (Brasil ou Europeu — consistente)",
    "figures": "Numeradas (Figura N.M), legenda em baixo, referenciadas no texto antes de aparecerem",
    "tables": "Numeradas (Tabela N.M), legenda em cima, referenciadas no texto",
    "equations": "Numeradas à direita, centradas, formato LaTeX",
    "page_numbering": "Preliminares em romano (i, ii, ...), capítulos em árabe (1, 2, ...)",
}


def get_dissertation_prompt(
    doc_type: str,
    topic: str,
    spec: str = "",
    language: str = "pt",
    output_format: str = "markdown",
    ist_style: bool = False,
) -> str:
    """
    Gera prompt para escrita de dissertação completa.

    doc_type: "msc", "phd", "bsc", "article"
    topic: tema da dissertação
    spec: especificações adicionais (tópicos, subtópicos, requisitos)
    language: "pt" ou "en"
    output_format: "markdown" ou "latex"
    ist_style: aplicar normas IST completas (fonte, margens, citações IEEE obrigatórias)
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

    ist_style_section = ""
    if ist_style:
        style = IST_DISSERTATION_STYLE
        ist_style_section = f"""

## Normas IST obrigatórias (seguir rigorosamente):
- Fonte: {style["font_family"]}, {style["font_size_pt"]}pt
- Espaçamento: {style["line_spacing"]}
- Margens: {style["margins_cm"]}
- Citações: {style["citation_style"]}
- Secções obrigatórias: {", ".join(str(s) for s in style["mandatory_sections"])}
- Numeração de páginas: {style["page_numbering"]}
- Figuras: {style["figures"]}
- Tabelas: {style["tables"]}
- Equações: {style["equations"]}
"""

    return f"""Escreve uma **{type_name}** completa sobre o tema: **{topic}**

Língua: {lang_name}
Formato de output: {fmt_name}
Padrão: Instituto Superior Técnico (IST), Universidade de Lisboa
Área: Engenharia Informática e de Computadores — Machine Learning / AI / Cloud Architecture
{ist_style_section}{spec_section}

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


def get_latex_export_prompt(content: str, doc_type: str = "msc") -> str:
    """
    Gera prompt para o agente converter um rascunho Markdown numa estrutura LaTeX IST.
    O agente deve retornar um documento LaTeX completo e compilável.
    """
    type_labels = {
        "msc": "Dissertação de Mestrado",
        "phd": "Tese de Doutoramento",
        "bsc": "Trabalho de Licenciatura",
        "article": "Artigo Científico",
    }
    type_label = type_labels.get(doc_type, doc_type)

    return f"""Converte o seguinte rascunho Markdown numa estrutura LaTeX IST completa e compilável.

Tipo de documento: **{type_label}**

## Requisitos obrigatórios do output LaTeX:
1. Usar `\\documentclass[12pt,a4paper]{{article}}`
2. Pacotes: `fontenc`, `inputenc`, `babel` (portuguese,english), `helvet` (Arial equiv.), `geometry` (margens 2.5cm), `setspace` (1.5 linhas), `biblatex` (style=ieee, backend=biber)
3. Capa IST com: título, autor, tipo, curso, orientador, ano
4. Estrutura: `\\tableofcontents`, `\\listoffigures`, `\\listoftables` antes dos capítulos
5. Citações no formato IEEE: `\\cite{{key}}` no texto, `\\printbibliography` no final
6. Equações numeradas com `equation` environment
7. Figuras com `\\begin{{figure}}[htbp]`, `\\caption{{}}`, `\\label{{}}`
8. Tabelas com `booktabs` (`\\toprule`, `\\midrule`, `\\bottomrule`)
9. Numeração de páginas: `\\pagenumbering{{roman}}` nas preliminares, `\\pagenumbering{{arabic}}` nos capítulos
10. Ficheiro deve compilar com: `lualatex main.tex && biber main && lualatex main.tex`

## Rascunho Markdown a converter:

{content}

Retorna APENAS o código LaTeX completo, sem explicações, pronto a guardar como `.tex`.
"""


def get_ist_dei_template(doc_type: str = "msc") -> str:
    """
    Retorna a estrutura completa de uma dissertação IST-DEI com todas as secções obrigatórias.
    doc_type: "msc" ou "phd"
    """
    type_labels = {
        "msc": "Dissertação de Mestrado",
        "phd": "Tese de Doutoramento",
        "bsc": "Trabalho de Licenciatura",
    }
    type_label = type_labels.get(doc_type, "Dissertação de Mestrado")

    return f"""# Template IST-DEI — {type_label}

> Gerado por Doctor Agent · Padrão Instituto Superior Técnico, Universidade de Lisboa
> Departamento de Engenharia Informática (DEI)

---

## CAPA

**[Logótipo IST — canto superior esquerdo]**

**Título da Dissertação**
*Subtítulo (se aplicável)*

Nome do Autor

{type_label}
Mestrado em Engenharia Informática e de Computadores

Orientador: Prof. Dr. [Nome do Orientador]
Co-orientador: Prof. Dr. [Nome do Co-orientador] *(se aplicável)*

[Mês] [Ano]

---

## DECLARAÇÃO DE HONRA

Declaro que o presente documento é de minha autoria e que não recorri para a sua elaboração
a qualquer forma de ajuda externa, para além das fontes bibliográficas referenciadas
e do apoio do meu orientador.

[Local], [data]
Assinatura: ______________________________

---

## AGRADECIMENTOS

*(Opcional — máx. 1 página)*

[Texto de agradecimentos...]

---

## RESUMO

*(Máx. 250 palavras)*

[Contextualização do problema e motivação. Abordagem e metodologia proposta.
Resultados principais com métricas quando possível. Conclusão e impacto do trabalho.]

**Palavras-chave:** palavra1, palavra2, palavra3, palavra4, palavra5

---

## ABSTRACT

*(Max. 250 words)*

[Context and motivation. Proposed approach and methodology.
Main results with quantitative metrics when possible. Conclusion and impact.]

**Keywords:** keyword1, keyword2, keyword3, keyword4, keyword5

---

## ÍNDICE

*(Gerado automaticamente em LaTeX com `\\tableofcontents`)*

---

## LISTA DE FIGURAS

*(Gerada automaticamente em LaTeX com `\\listoffigures`)*

---

## LISTA DE TABELAS

*(Gerada automaticamente em LaTeX com `\\listoftables`)*

---

## LISTA DE ABREVIATURAS E ACRÓNIMOS

*(Se aplicável)*

| Acrónimo | Significado |
|----------|-------------|
| AI       | Artificial Intelligence |
| ML       | Machine Learning |
| IST      | Instituto Superior Técnico |

---

# 1. INTRODUÇÃO

## 1.1 Contextualização e Motivação

[Contextualização ampla do domínio. Porque é que este problema é relevante?
Que impacto tem na área? Que tendências actuais o tornam oportuno?]

## 1.2 Definição do Problema

[Definição precisa e formal do problema. O que se quer resolver?
Porque é que é difícil? Que limitações têm as abordagens actuais?]

## 1.3 Abordagem Proposta

[Overview da solução proposta. Não entrar em detalhes técnicos — isso vai na metodologia.]

## 1.4 Contribuições

As principais contribuições deste trabalho são:

- **Contribuição 1:** [Descrição precisa]
- **Contribuição 2:** [Descrição precisa]
- **Contribuição 3:** [Descrição precisa]

## 1.5 Estrutura da Dissertação

O restante desta dissertação está organizado da seguinte forma:
o Capítulo 2 apresenta o background e estado da arte;
o Capítulo 3 descreve a metodologia proposta;
o Capítulo 4 detalha a implementação;
o Capítulo 5 apresenta a avaliação experimental;
o Capítulo 6 conclui e identifica trabalho futuro.

---

# 2. BACKGROUND E ESTADO DA ARTE

## 2.1 Conceitos Fundamentais

### 2.1.1 [Conceito Base 1]

[Explicação com citações [N]. Fórmulas quando relevante.]

### 2.1.2 [Conceito Base 2]

[...]

## 2.2 Trabalhos Relacionados

### 2.2.1 [Abordagem/Família 1]

[Análise crítica dos trabalhos desta categoria. Limitações.]

### 2.2.2 [Abordagem/Família 2]

[...]

## 2.3 Comparação de Abordagens

| Trabalho | Método | Métrica A | Métrica B | Limitação Principal |
|----------|--------|-----------|-----------|---------------------|
| [Ref 1]  | ...    | ...       | ...       | ...                 |
| [Ref 2]  | ...    | ...       | ...       | ...                 |
| **Proposta** | ... | ...    | ...       | —                   |

## 2.4 Sumário e Posicionamento

[Como o presente trabalho se diferencia e supera as limitações identificadas.]

---

# 3. METODOLOGIA

## 3.1 Visão Geral

[Diagrama de arquitectura — descrever para criar figura]

**Figura 3.1:** Arquitectura geral do sistema proposto.

## 3.2 [Componente Principal 1]

[Descrição detalhada. Justificação das escolhas. Trade-offs.]

## 3.3 [Componente Principal 2]

[...]

## 3.4 Algoritmo Principal

```
Algorithm 1: [Nome do Algoritmo]
Input: [...]
Output: [...]
1: [Passo 1]
2: [Passo 2]
...
```

## 3.5 Análise de Complexidade

[Complexidade temporal e espacial. Provas quando necessário.]

---

# 4. IMPLEMENTAÇÃO

## 4.1 Stack Tecnológico

| Componente | Tecnologia | Versão | Justificação |
|------------|------------|--------|--------------|
| Linguagem  | Python     | 3.11   | ...          |
| Framework  | ...        | ...    | ...          |

## 4.2 Arquitectura do Sistema

[Estrutura de directorias, módulos principais, interfaces.]

## 4.3 Detalhes de Implementação

### 4.3.1 [Módulo 1]

[Decisões de implementação. Desafios e soluções.]

## 4.4 Ambiente de Desenvolvimento

**Hardware:** [CPU, RAM, GPU se aplicável]
**Sistema Operativo:** [...]
**Dependências principais:** ver `requirements.txt`

---

# 5. AVALIAÇÃO EXPERIMENTAL

## 5.1 Questões de Investigação

- **RQ1:** [Questão 1]
- **RQ2:** [Questão 2]

## 5.2 Setup Experimental

### 5.2.1 Datasets

[Descrição dos datasets. Estatísticas. Splits treino/validação/teste.]

### 5.2.2 Baselines

[Métodos de comparação e justificação da sua escolha.]

### 5.2.3 Métricas de Avaliação

[Definição formal das métricas. Porque são as adequadas?]

## 5.3 Resultados

### 5.3.1 Comparação com Baselines

| Método       | Métrica A ↑ | Métrica B ↑ | Métrica C ↓ |
|--------------|-------------|-------------|-------------|
| Baseline 1   | XX.X        | XX.X        | XX.X        |
| Baseline 2   | XX.X        | XX.X        | XX.X        |
| **Proposta** | **XX.X**    | **XX.X**    | **XX.X**    |

[DADOS REAIS NECESSÁRIOS: substituir XX.X pelos resultados experimentais reais]

### 5.3.2 Ablation Study

[Análise do contributo de cada componente.]

## 5.4 Análise e Discussão

[Interpretação dos resultados. Casos de sucesso. Casos de falha. Limitações.]

---

# 6. CONCLUSÃO

## 6.1 Sumário das Contribuições

[Em retrospectiva: o que foi efectivamente feito e provado.]

## 6.2 Resposta às Questões de Investigação

- **RQ1:** [Resposta directa com evidência]
- **RQ2:** [Resposta directa com evidência]

## 6.3 Limitações

[Limitações honestas do trabalho. O que não está coberto.]

## 6.4 Trabalho Futuro

- [Direcção 1 — específica e accionável]
- [Direcção 2 — específica e accionável]

## 6.5 Reflexão Final

[Impacto do trabalho. Contribuição para a área.]

---

# REFERÊNCIAS BIBLIOGRÁFICAS

*(Formato IEEE — numeradas por ordem de aparecimento no texto)*

[1] [Autor(es)], "[Título]," *[Venue]*, [Ano]. doi: [DOI].

[2] ...

---

# ANEXOS

## Anexo A — [Título]

*(Se aplicável)*

[Conteúdo adicional que não cabe no corpo principal mas é relevante para reprodutibilidade.]

---

*Template IST-DEI gerado por Doctor Agent · github.com/ist-doctor*
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
