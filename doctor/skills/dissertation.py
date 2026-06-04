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


def get_meic_ist_2024_template(topic: str = "") -> str:
    """
    Retorna o template estrutural completo para dissertações MEIC IST 2024.

    Baseado na estrutura real dos papers MEIC IST 2024 (dissertações de mestrado
    em Engenharia Informática e de Computadores do Instituto Superior Técnico).
    Campos marcados [MEIC-IST-2024] são obrigatórios segundo as normas do programa.

    topic: tema da dissertação (pré-preenche campos relevantes)
    """
    topic_line = f"**{topic}**" if topic else "**[MEIC-IST-2024: Título da Dissertação]**"

    return f"""# Template MEIC IST 2024 — Dissertação de Mestrado
# Mestrado Integrado em Engenharia Informática e de Computadores

> Gerado por Doctor Agent · Instituto Superior Técnico, Universidade de Lisboa
> Departamento de Engenharia Informática (DEI) · Normas MEIC 2024
> Mínimo: 40 referências IEEE · Abstract EN+PT ≤ 250 palavras · 5–8 keywords EN

---

## CAPA [MEIC-IST-2024: obrigatório]

**[Logótipo IST — canto superior esquerdo]**

{topic_line}
*[Subtítulo opcional]*

**[MEIC-IST-2024: Nome completo do Autor]**

Dissertação para obtenção do Grau de Mestre em
**Engenharia Informática e de Computadores**

**Júri [MEIC-IST-2024: obrigatório]**
- Presidente: Prof. Dr. [Nome], [Instituição]
- Orientador: Prof. Dr. [Nome], IST, Universidade de Lisboa
- Vogal: Prof. Dr. [Nome], [Instituição]

**Orientador:** Prof. Dr. [MEIC-IST-2024: Nome do Orientador], IST
**Co-orientador:** Prof. Dr. [Nome do Co-orientador] *(se aplicável)*

[MEIC-IST-2024: Mês] [MEIC-IST-2024: Ano]

---

## ACKNOWLEDGEMENTS [MEIC-IST-2024: em inglês para dissertações EN]

*(Opcional — máx. 1 página)*

[Text of acknowledgements. Dissertações submetidas em inglês devem ter os
agradecimentos também em inglês. Dissertações em português: "Agradecimentos".]

---

## RESUMO [MEIC-IST-2024: obrigatório — máx. 250 palavras]

[Contextualização e motivação do problema. Abordagem e metodologia proposta.
Resultados principais com métricas quando possível. Conclusão e impacto.]

**Palavras-chave [MEIC-IST-2024: 5–8 em português]:**
palavra1, palavra2, palavra3, palavra4, palavra5

---

## ABSTRACT [MEIC-IST-2024: obrigatório — máx. 250 words]

[Context and motivation. Proposed approach and methodology.
Main results with quantitative metrics. Conclusion and contribution.]

**Keywords [MEIC-IST-2024: 5–8 in English]:**
keyword1, keyword2, keyword3, keyword4, keyword5

---

## TABLE OF CONTENTS

*(Gerado automaticamente — `\\tableofcontents` em LaTeX)*

---

## LIST OF FIGURES

*(Gerado automaticamente — `\\listoffigures` em LaTeX)*

---

## LIST OF TABLES

*(Gerado automaticamente — `\\listoftables` em LaTeX)*

---

## LIST OF ABBREVIATIONS

*(Se aplicável)*

| Abbreviation | Meaning |
|-------------|---------|
| IST  | Instituto Superior Técnico |
| MEIC | Mestrado Integrado em Engenharia Informática e de Computadores |
| ML   | Machine Learning |

---

# 1. INTRODUCTION [MEIC-IST-2024: obrigatório]

## 1.1 Motivation

[Contextualização ampla do domínio. Porque é que este problema é relevante agora?
Que tendências actuais — industriais, científicas, sociais — o tornam urgente?
Impacto real se resolvido. 1–2 parágrafos de abertura fortes.]

## 1.2 Problem Statement

[Definição precisa e formal do problema. O que exactamente se quer resolver?
Porque é que é difícil? Que limitações têm as abordagens actuais?
O que ainda não existe que este trabalho vai criar?]

## 1.3 Proposed Approach

[Overview de alto nível da solução proposta — sem detalhes técnicos (esse é o cap. 4).
Intuição, arquitectura geral, insight principal.]

## 1.4 Contributions [MEIC-IST-2024: lista explícita obrigatória]

The main contributions of this work are:

- **[C1]** [Contribuição 1 — específica, verificável, diferenciadora]
- **[C2]** [Contribuição 2 — específica, verificável, diferenciadora]
- **[C3]** [Contribuição 3 — específica, verificável, diferenciadora]

## 1.5 Dissertation Structure

The remainder of this dissertation is organized as follows.
Chapter 2 introduces the necessary background concepts.
Chapter 3 reviews and positions related work.
Chapter 4 presents the proposed [system/method/architecture].
Chapter 5 evaluates the approach experimentally.
Chapter 6 concludes and discusses future work.

---

# 2. BACKGROUND [MEIC-IST-2024: análise crítica, não apenas survey]

## 2.1 [Fundamental Concept 1]

### 2.1.1 [Sub-concept]

[Explicação com citações [N]. Fórmulas LaTeX quando relevante: $f(x) = \\sigma(Wx + b)$.]

### 2.1.2 [Sub-concept]

[...]

## 2.2 [Fundamental Concept 2]

[...]

## 2.3 [Fundamental Concept 3]

[...]

## 2.4 Chapter Summary

[Síntese dos conceitos cobertos e como preparam o leitor para o capítulo seguinte.]

---

# 3. RELATED WORK [MEIC-IST-2024: tabela comparativa obrigatória]

## 3.1 [Approach Family 1]

[Análise crítica dos trabalhos desta categoria — não lista, mas argumento.
O que funciona bem? Onde falham? Como se relacionam com esta proposta?]

## 3.2 [Approach Family 2]

[...]

## 3.3 [Approach Family 3]

[...]

## 3.4 Comparison Table [MEIC-IST-2024: obrigatória]

| Work | Venue | Method | Metric A | Metric B | Key Limitation |
|------|-------|--------|----------|----------|----------------|
| [1]  | ...   | ...    | ...      | ...      | ...            |
| [2]  | ...   | ...    | ...      | ...      | ...            |
| **This work** | — | ... | **XX.X** | **XX.X** | — |

## 3.5 Positioning

[Como este trabalho se diferencia de cada família. Por que as limitações identificadas
justificam a abordagem proposta. Ligação directa às contribuições do cap. 1.]

---

# 4. [SYSTEM/METHOD NAME] — ARCHITECTURE [MEIC-IST-2024: cap. central]

## 4.1 Overview

[Descrição de alto nível com referência à figura de arquitectura.]

**Figure 4.1:** [MEIC-IST-2024: Arquitectura geral do sistema proposto.]
*(Criar figura — diagrama de blocos com fluxo de dados e componentes principais)*

## 4.2 [Component 1]

[Descrição detalhada. Justificação das escolhas de design vs. alternativas.
Trade-offs explícitos. Equações quando necessário (eq. numeradas).]

$$f(x) = \\text{{[MEIC-IST-2024: equação do componente]}}  \\tag{{4.1}}$$

## 4.3 [Component 2]

[...]

## 4.4 [Component 3]

[...]

## 4.5 Algorithm

```
Algorithm 1: [MEIC-IST-2024: Nome do Algoritmo Principal]
Input:  [inputs com tipos]
Output: [outputs com tipos]
 1: [Passo 1]
 2: [Passo 2]
 3: for each [item] in [collection] do
 4:   [operação]
 5: end for
 6: return [resultado]
```

**Complexity:** Time $O(\\text{...})$, Space $O(\\text{...})$.

## 4.6 Implementation Details

**Stack:**

| Component  | Technology | Version | Rationale |
|-----------|------------|---------|-----------|
| Language   | Python     | 3.11    | [justificação] |
| Framework  | ...        | ...     | [justificação] |

**Environment:** [CPU/GPU, RAM, OS, principais dependências]

---

# 5. EVALUATION [MEIC-IST-2024: RQs explícitas, setup completo, ablation]

## 5.1 Research Questions [MEIC-IST-2024: obrigatório]

- **RQ1:** [Questão 1 — focada, verificável]
- **RQ2:** [Questão 2 — focada, verificável]
- **RQ3:** [Questão 3 — focada, verificável]

## 5.2 Experimental Setup

### 5.2.1 Datasets

| Dataset | Size | Domain | Split (train/val/test) |
|---------|------|--------|------------------------|
| [DS1]   | ...  | ...    | .../.../.../          |

### 5.2.2 Baselines

| Baseline | Reference | Rationale for inclusion |
|---------|-----------|------------------------|
| [B1]    | [N]       | [por que é o SOTA relevante] |

### 5.2.3 Evaluation Metrics

[Definição formal de cada métrica. Equações quando relevante. Justificação da escolha.]

### 5.2.4 Hardware & Reproducibility

**Hardware:** [CPU/GPU, RAM]
**Random seeds:** [valores para reprodutibilidade]
**Code:** [link para repositório / instruções]

## 5.3 Results

### 5.3.1 RQ1 — [Título da questão]

| Method       | Metric A ↑ | Metric B ↑ | Metric C ↓ |
|-------------|-----------|-----------|-----------|
| Baseline 1   | XX.X ± X.X | XX.X ± X.X | XX.X ± X.X |
| Baseline 2   | XX.X ± X.X | XX.X ± X.X | XX.X ± X.X |
| **Proposed** | **XX.X ± X.X** | **XX.X ± X.X** | **XX.X ± X.X** |

[MEIC-IST-2024: DADOS REAIS NECESSÁRIOS — substituir XX.X pelos resultados experimentais]

### 5.3.2 RQ2 — [Título da questão]

[...]

### 5.3.3 RQ3 — [Título da questão]

[...]

## 5.4 Ablation Study [MEIC-IST-2024: obrigatório para dissertações com componentes múltiplos]

| Variant            | Metric A ↑ | Delta vs. Full |
|-------------------|-----------|----------------|
| Full model         | XX.X      | —              |
| w/o [Component 1]  | XX.X      | -X.X           |
| w/o [Component 2]  | XX.X      | -X.X           |

## 5.5 Analysis and Discussion

[Interpretação dos resultados. Resposta directa a cada RQ com evidência.
Casos de sucesso e casos de falha. Análise de erros. Limitações visíveis nos dados.]

---

# 6. CONCLUSION [MEIC-IST-2024: obrigatório]

## 6.1 Summary of Contributions

[Em retrospectiva — o que foi efectivamente construído, avaliado e provado.
Ligar de volta às contribuições declaradas no cap. 1.]

## 6.2 Answers to Research Questions

- **RQ1:** [Resposta directa com evidência dos resultados]
- **RQ2:** [Resposta directa com evidência dos resultados]
- **RQ3:** [Resposta directa com evidência dos resultados]

## 6.3 Limitations

[Limitações honestas do trabalho. O que não está coberto. O que foi assumido.
Condições de validade dos resultados.]

## 6.4 Future Work

- **[FW1]:** [Direcção específica e accionável — não "melhorar o sistema"]
- **[FW2]:** [Direcção específica e accionável]
- **[FW3]:** [Direcção específica e accionável]

## 6.5 Final Remarks

[Impacto esperado. Contribuição para a comunidade. Posicionamento no panorama actual.]

---

# REFERENCES [MEIC-IST-2024: mínimo 40 referências, formato IEEE]

*(Numeradas por ordem de aparecimento no texto — IEEE style)*

[1] [Autor(es)], "[Título]," *[Venue — journal ou proceedings]*, vol. X, no. Y, pp. Z–W, [Ano]. doi: [DOI].

[2] ...

*[MEIC-IST-2024: mínimo 40 referências. Preferencialmente: 60% conference/journal papers,
20% books/theses, 20% technical reports/preprints. Verificar com `doctor cite --doi ...`]*

---

# APPENDICES *(Opcional)*

## Appendix A — [Title]

[Conteúdo adicional: provas, código, datasets detalhados, tabelas extensas —
material que suporta reprodutibilidade mas não cabe no corpo principal.]

---

*Template MEIC IST 2024 gerado por Doctor Agent*
*Normas: DEI/IST, Universidade de Lisboa — MEIC 2024*
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
