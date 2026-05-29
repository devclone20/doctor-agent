# Normas e Padrões IST — Instituto Superior Técnico, Lisboa

## Sobre o IST

O Instituto Superior Técnico (IST) da Universidade de Lisboa, campus de Alameda, é a principal escola de engenharia e tecnologia de Portugal. Os seus padrões académicos estão entre os mais exigentes da Europa.

## Estrutura de uma Dissertação de Mestrado IST

### Ordem obrigatória dos elementos:
1. **Capa** — Título, autor, grau, curso, data, logótipo IST
2. **Página de rosto** — Título, autor, orientador, co-orientador, júri
3. **Dedicatória** (opcional)
4. **Agradecimentos** (Acknowledgements)
5. **Resumo** (Português — máx. 250 palavras)
6. **Abstract** (Inglês — máx. 250 palavras) + **Keywords** (5-8 palavras)
7. **Índice** (Table of Contents)
8. **Lista de Figuras** (List of Figures)
9. **Lista de Tabelas** (List of Tables)
10. **Lista de Acrónimos** (List of Acronyms)
11. **Capítulos** (ver estrutura padrão abaixo)
12. **Bibliografia** (References)
13. **Apêndices** (Appendices) — material suplementar

### Estrutura padrão de capítulos:

#### Capítulo 1 — Introdução
- 1.1 Motivação
- 1.2 Problema e Objectivos
- 1.3 Contribuições
- 1.4 Estrutura da Dissertação

#### Capítulo 2 — Background e Estado da Arte
- 2.1 Conceitos fundamentais
- 2.2 Trabalho relacionado
- 2.3 Comparação crítica

#### Capítulo 3 — Abordagem / Arquitectura / Metodologia
- 3.1 Visão geral da solução
- 3.2 Arquitectura do sistema
- 3.3 Decisões de design

#### Capítulo 4 — Implementação
- 4.1 Ambiente de desenvolvimento
- 4.2 Detalhes de implementação
- 4.3 Desafios e soluções

#### Capítulo 5 — Avaliação / Resultados Experimentais
- 5.1 Setup experimental
- 5.2 Métricas e benchmarks
- 5.3 Resultados e discussão

#### Capítulo 6 — Conclusão e Trabalho Futuro
- 6.1 Sumário das contribuições
- 6.2 Limitações
- 6.3 Trabalho futuro

## Formatação IST

### Texto:
- Fonte: 12pt (body text)
- Margens: 2.5 cm em todos os lados
- Espaçamento: 1.5 linhas (ou duplo em versão prévia)
- Idiomas aceites: Português ou Inglês

### Figuras e Tabelas:
- Todas as figuras têm legenda abaixo: "Figura X.Y: Descrição."
- Todas as tabelas têm título acima: "Tabela X.Y: Descrição."
- Todas as figuras e tabelas devem ser referenciadas no texto

### Equações:
- Numeradas: (X.Y) à direita
- Variáveis em itálico
- Vectores/matrizes a bold

## Template LaTeX Oficial IST

- Template: IST-UL MSc Dissertation v5.0 (Outubro 2025)
- Engine: LuaLaTeX
- Autor: Prof. Dr. Rui Santos Cruz
- Disponível: https://www.overleaf.com/latex/templates/ist-ul-msc-dissertation/wrhbmbvzpttw
- Suporta: draft/final mode, PT/EN, track changes, glossários, acrónimos

## Estilo de Citações IST (Engenharia)

Engenharia Informática e de Computadores usa o estilo **IEEE**:
- Referências numeradas: [1], [2], [3], ...
- No texto: "segundo [1], ...", "como proposto em [1][2]"
- Na bibliography: autores, título, conferência/journal, volume, páginas, ano

## Processo de Submissão

1. Submeter via Fénix (plataforma académica IST)
2. Aprovação do orientador
3. Defesa perante júri
4. Disponibilização no repositório Scholar IST

## Repositório IST Scholar

- URL: https://scholar.tecnico.ulisboa.pt
- API: https://scholar.tecnico.ulisboa.pt/api/
- Contém: ~24.000 dissertações de mestrado + ~8.000 teses de doutoramento
- Formato de busca: ?q=QUERY&domain=records&sort=_score:desc&page=1&perPage=10

---

## Templates LaTeX para IST — Comparação (2025/2026)

Existem dois templates LaTeX distintos para dissertações IST:

### Template A — IST-UL MSc Dissertation (oficial)
- **Versão:** v5.0 (Outubro 2025)
- **Autor:** Prof. Dr. Rui Santos Cruz
- **Engine:** LuaLaTeX
- **Disponível:** Overleaf (template IST-UL MSc Dissertation)
- **Status:** Template "oficial" criado especificamente para o IST
- **Funcionalidades:**
  - Modos draft/final com watermark automático
  - Suporte PT/EN (estrutura adapta-se à língua)
  - Track Changes integrado
  - Acrónimos e glossário
  - Clever Referencing (`cleveref`)
  - Algoritmos (`algorithm2e`, `algorithmicx`)
  - Syntax highlighting para código (`minted`, `listings`)
  - Lista de Símbolos
  - Citações IEEE com `biblatex` + `biber`

### Template B — NOVAthesis (multi-institucional, recomendado)
- **Versão:** v7.10.1 (2026-02-10)
- **Autor:** Prof. João Lourenço (FCT-NOVA)
- **Engine:** LuaLaTeX (suporta também pdfLaTeX/XeLaTeX)
- **Disponível:** GitHub (joaomlourenco/novathesis) + Overleaf
- **Status:** Mais feature-rich; suporta 20+ escolas portuguesas incluindo IST/ULisboa
- **Configuração para IST:**
  ```latex
  \documentclass[
    school=ul/ist,       % Instituto Superior Técnico, ULisboa
    doctype=msc,         % Mestrado (ou phd)
    lang=en,             % Inglês (ou pt)
    biblatex/style=ieee, % Citações IEEE
  ]{novathesis}
  ```

### Funcionalidades novas NOVAthesis v7.x (2025-2026)

| Versão | Data | Novidade |
|--------|------|----------|
| v7.10.1 | 2026-02-10 | Estabilidade ("Let's make it work") |
| v7.10.0 | 2026-02-04 | AI Disclosure Statement (`aidisclose`) + suporte CJK |
| v7.8+ | 2025 | Migração para package `geometry` para layout de página |
| v7.6+ | 2025 | 17 ícones SDG (Sustainable Development Goals) |

### Package `aidisclose` — IMPORTANTE para 2026
A partir de 2026, universidades portuguesas (incluindo IST) exigem declaração formal do uso de IA na dissertação. O NOVAthesis v7.8+ inclui o package `aidisclose` para este fim:
```latex
% No preâmbulo — declarar quais ferramentas de IA foram usadas
\aiToolUsed{GitHub Copilot}{code completion in Chapter 4}
\aiToolUsed{ChatGPT}{grammar checking of English text}
```

### Recomendação para alunos IST
- **Para conformidade máxima:** IST-UL v5.0 (template do próprio IST)
- **Para funcionalidades máximas:** NOVAthesis v7.10+ com `school=ul/ist`
- **Ambos usam:** LuaLaTeX + Biber + BibLaTeX (estilo IEEE)

---

## Critérios de Avaliação de uma Introdução IST (Night 1 — Night 6)

Com base na auto-avaliação da sessão de treino Night 1, os critérios para avaliar a qualidade de uma Introdução de dissertação IST são:

| Critério | Peso | Indicadores de excelência |
|----------|------|---------------------------|
| Estrutura IST (1.1-1.4) | 20% | Todas as subsecções presentes, completas, na ordem correcta |
| Motivação | 15% | Contexto do problema, escala, relevância prática, impacto ambiental/societal |
| Problema e objectivos | 20% | Research question clara, objectivos numerados com métricas específicas |
| Contribuições | 20% | Contribuições com nomes próprios, verificáveis, gap vs estado da arte explícito |
| Linguagem académica | 15% | Formal, terminologia correcta, sem coloquialismos, sem hedging excessivo |
| Fluxo e coerência | 10% | Progressão lógica entre subsecções, anaphoric references correctas |

**Score mínimo IST:** 7.0/10 em todos os critérios  
**Score excelência IST:** 9.0+/10 na média

### Padrões fracos comuns (identificados em Night 1)
1. Falta de contexto energético/ambiental em dissertações de ML (tendência 2025)
2. Objectivos sem métricas específicas (F1, BLEU, pass@k, latência, throughput)
3. Contribuições sem referência ao gap vs surveys/trabalho anterior
4. Palavra "compelling" — informal para dissertações IST (substituir por "promising" ou "compelling evidence")

---

## Docling — Ingestão Estrutural de PDFs Académicos

**Docling** (IBM Research, DS4SD) é a ferramenta de referência para processar PDFs académicos em 2025/2026.

- **Paper:** arXiv:2501.17887 — "Docling: An Efficient Open-Source Toolkit for AI-driven Document Conversion" (Jan 2025)
- **Technical Report:** arXiv:2408.09869 (Ago 2024, v4)
- **Stars:** 37,000+ (cresceu de ~14k — 2.6× em poucos meses)
- **Licença:** Apache 2.0

### Modelos AI core

| Modelo | Função |
|--------|---------|
| DocLayNet | Layout analysis — detecta texto, tabelas, figuras, títulos, notas de rodapé |
| TableFormer | Table structure recognition — células, cabeçalhos, merged cells |
| Granite-Docling (Jan 2026) | Modelo end-to-end: backbone Granite 3 + SigLIP2 visual encoder |

### Uso do Doctor — workflow recomendado
```python
from docling.document_converter import DocumentConverter

converter = DocumentConverter()
result = converter.convert("dissertacao.pdf")

doc = result.document
# Export estruturado
markdown = doc.export_to_markdown()        # Para edição
json_doc = doc.export_to_dict()           # Para processamento programático
sections = json_doc["body"]
tables = [e for e in sections if e["type"] == "table"]
references = [e for e in sections if e["type"] == "reference"]
```

### Capacidades para documentos académicos
- Preserva hierarquia de secções (H1/H2/H3)
- Extrai referências como entidades estruturadas
- Reconhece equações (como imagens ou via OCR especializado)
- Ordena blocos por reading order (não por posição geométrica bruta)
- Integra com LangChain e LlamaIndex para pipelines RAG
- Execução 100% local (compatível com ambientes air-gapped)

*Fonte: Night 1 training (2026-05-29)*
