# Doctor — Skill Decomposition Architecture

> Como o Doctor decompõe tarefas académicas complexas em sub-skills encadeadas.
> Este documento define a arquitectura interna de orquestração do Doctor.

---

## Filosofia de Decomposição

Tarefas académicas complexas (dissertações, artigos, revisões) não são monolíticas.
O Doctor decompõe qualquer pedido numa pipeline de sub-skills especializadas, onde cada
uma produz um artefacto verificável que serve de input para a seguinte.

**Princípio:** nenhuma sub-skill produz output final sem validar o seu input.

---

## Pipeline Principal: Research → Outline → Draft → Review → Format → Export

```
┌──────────┐    ┌─────────┐    ┌───────┐    ┌────────┐    ┌────────┐    ┌────────┐
│ Research │───▶│ Outline │───▶│ Draft │───▶│ Review │───▶│ Format │───▶│ Export │
└──────────┘    └─────────┘    └───────┘    └────────┘    └────────┘    └────────┘
     │               │              │             │             │             │
  Papers          Estrutura      Texto        Anotações     IST style     .docx /
  verificados     validada       rascunho     críticas      aplicado      .pdf /
  + BibTeX        + word         por secção   + fixes       + formatação  .tex
                  counts                      sugeridas     completa
```

---

## Sub-Skills em Detalhe

### 1. Research

**Input:** tema, palavras-chave, tipo de documento, orientações do utilizador

**Processo:**
1. Pesquisar em arXiv, Semantic Scholar, CrossRef, IST Scholar, PubMed
2. Filtrar por relevância, ano (preferência: últimos 5 anos para estado da arte)
3. Verificar DOIs via CrossRef API
4. Identificar papers fundadores (alta citação) vs. trabalho recente (últimos 2 anos)
5. Extrair: autores, ano, venue, contribuição principal, limitações reportadas
6. Gerar BibTeX entries verificadas

**Output:** lista de referências verificadas + anotações de relevância por secção

**Regra crítica:** nunca fabrica referências. Se não encontrar via API, marca `[PESQUISA MANUAL NECESSÁRIA]`.

---

### 2. Outline

**Input:** tipo de documento, tema, referências da fase Research, requisitos do utilizador

**Processo:**
1. Seleccionar template correcto (dissertação IST / artigo IEEE / artigo ACM / relatório)
2. Adaptar estrutura ao tema específico
3. Atribuir word counts por secção
4. Identificar figuras e tabelas necessárias (placeholder com descrição)
5. Mapear referências a secções

**Output:** estrutura detalhada com secções, subsecções, word counts e referências alocadas

**Gate de qualidade:** o outline é validado antes de passar ao Draft. Se incompleto, volta ao Research.

---

### 3. Draft

**Input:** outline validado, referências, dados do utilizador (resultados, código, observações)

**Processo:**
1. Escrever secção por secção na ordem lógica (não necessariamente linear)
2. Inserir citações IEEE inline `[N]` em cada claim
3. Marcar placeholders para dados reais: `[PLACEHOLDER: inserir valor experimental aqui]`
4. Manter consistência de notação e terminologia entre secções
5. Gerar legendas de figuras e títulos de tabelas (mesmo sem as figuras)

**Output:** rascunho completo em Markdown estruturado, pronto para Review

**Regra:** cada parágrafo com claims técnicos tem pelo menos uma referência verificada.

---

### 4. Review

**Input:** rascunho completo

**Processo:**
1. **Revisão estrutural:** está a estrutura IST/IEEE correcta? Secções na ordem certa?
2. **Revisão de argumentação:** cada claim tem evidência? Lógica é coerente?
3. **Revisão de citações:** referências usadas correctamente? Formato IEEE correcto?
4. **Revisão de língua:** erros gramaticais, ortográficos, consistência de tempo verbal
5. **Revisão de formatação preliminar:** figuras referenciadas antes de aparecer? Equações numeradas?

**Output:** anotações por secção com três níveis:
- ⚠️ **Crítico** — impede submissão (claim sem evidência, citação fabricada, estrutura errada)
- 🟡 **Importante** — degrada qualidade significativamente (argumento fraco, dados omitidos)
- 💡 **Sugestão** — melhoria de estilo, clareza ou completude

**Regra:** o Doctor revê o seu próprio draft. Se detectar ⚠️ Críticos, volta ao Draft antes de avançar.

---

### 5. Format

**Input:** rascunho revisto e aprovado

**Processo:**
1. Aplicar estilo tipográfico correcto (IST / IEEE / ACM conforme target)
2. Configurar margens, fontes, espaçamentos
3. Formatar tabelas com estilo IST (cabeçalho IST_BLUE, linhas alternadas)
4. Aplicar legendas justificadas (figuras abaixo, tabelas acima)
5. Formatar equações numeradas
6. Gerar índice automático (Word field codes ou LaTeX `\tableofcontents`)
7. Inserir page breaks obrigatórios entre índices

**Output:** documento formatado pronto para Export

---

### 6. Export

**Input:** documento formatado

**Processo:**
1. Seleccionar formato de output: `.docx`, `.pdf`, `.tex`, ou todos
2. Para `.docx`: executar script python-docx, verificar que corre sem erros
3. Para `.tex`: validar que compila com LuaLaTeX sem warnings críticos
4. Para `.pdf`: gerar via LaTeX ou python-docx → LibreOffice headless
5. Verificar integridade do ficheiro output

**Output:** ficheiro(s) final(is) prontos a entregar

---

## Decision Tree — Escolher o Modo Correcto

```
Qual é o pedido do utilizador?
│
├── "dissertação" / "tese" / "MSc" / "Mestrado"
│     └── Modo: --style ist-dissertation
│           Pipeline completa: Research(50-100 refs) → Outline → Draft → Review → Format → Export(.docx + .tex)
│
├── "artigo" / "paper" / "conference" + IEEE venue
│     └── Modo: --style ieee-paper
│           Pipeline: Research(20-40 refs) → Outline(4-8 páginas) → Draft → Review → Format(IEEE 2-col) → Export(.pdf)
│
├── "artigo" / "paper" + ACM venue (SOSP, EuroSys, etc.)
│     └── Modo: --style acm-paper
│           Pipeline: Research(20-40 refs) → Outline(10-12 páginas) → Draft → Review → Format(ACM SIGPLAN) → Export(.pdf)
│
├── "relatório de laboratório" / "lab report"
│     └── Modo: relatório_lab
│           Pipeline simplificada: Outline(template IST lab) → Draft → Format → Export(.docx)
│           (Research não necessário a não ser que o utilizador peça estado da arte)
│
├── "revê isto" / "analisa" / "feedback" + documento existente
│     └── Modo: review-only
│           Pipeline: Review(documento fornecido) → output anotações + sugestões de fix
│           (sem Research, Outline, Draft ou Export a não ser que explicitamente pedido)
│
├── "pesquisa" / "encontra papers sobre" / "estado da arte"
│     └── Modo: research-only
│           Pipeline: Research → output lista de referências verificadas + síntese
│
└── "formata" / "converte para Word" / "gera .docx"
      └── Modo: format-export-only
            Pipeline: Format → Export (sem Research, Outline, Draft, Review)
```

---

## Encadeamento de Sub-Skills — Artefactos e Gates

```
Research ──[referências verificadas]──▶ Outline
                                              │
                                    [gate: outline completo?]
                                              │ sim
                                              ▼
                              Draft ──[rascunho por secção]──▶ Review
                                                                    │
                                                          [gate: zero ⚠️ Críticos?]
                                                                    │ sim
                                                                    ▼
                                                           Format ──▶ Export
```

**Gates explícitos:**
- Research → Outline: mínimo de referências atingido? (10 para lab, 50 para dissertação)
- Outline → Draft: todas as secções obrigatórias presentes?
- Draft → Review: nenhum placeholder crítico sem dados?
- Review → Format: zero anotações ⚠️ Críticas abertas?
- Format → Export: script de geração corre sem erro?

---

## Modos de Operação por Tipo de Documento

| Tipo | Sub-skills activas | Output |
|---|---|---|
| Dissertação IST Mestrado | Research + Outline + Draft + Review + Format + Export | `.docx` + `.tex` |
| Artigo IEEE | Research + Outline + Draft + Review + Format + Export | `.tex` (IEEE template) |
| Artigo ACM | Research + Outline + Draft + Review + Format + Export | `.tex` (ACM template) |
| Relatório de Laboratório | Outline + Draft + Format + Export | `.docx` |
| Revisão de documento | Review only | Anotações + fixes |
| Pesquisa bibliográfica | Research only | BibTeX + síntese |
| Formatação de documento | Format + Export | `.docx` / `.pdf` |
| Projecto incremental | Todos (sessão a sessão) | `projecto.json` + `.docx` |

---

## Regras de Composição

1. **Nunca saltar gates.** Se um gate falha, a sub-skill anterior é repetida com as correccções necessárias.
2. **Artefactos são verificáveis.** Cada output de uma sub-skill pode ser inspeccionado pelo utilizador antes de avançar.
3. **Research é assíncrona.** Pode ser executada em background enquanto o Outline é construído com as referências já disponíveis.
4. **Review é recursiva.** O Doctor pode executar Review sobre um Draft parcial (por capítulo) sem esperar o documento completo.
5. **Export é idempotente.** Pode ser re-executado a qualquer momento sobre o mesmo documento formatado sem alterar conteúdo.
