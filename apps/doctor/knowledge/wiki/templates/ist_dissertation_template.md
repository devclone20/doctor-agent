# Template de Dissertação IST-DEI — Mestrado em Engenharia Informática e de Computadores

> Baseado nas normas oficiais IST documentadas em `ist_standards.md` e no Regulamento de
> Dissertações IST 2022. Válido para o Departamento de Engenharia Informática (DEI),
> campus Alameda. Actualizado para o ano lectivo 2025/26.

---

## Estrutura Completa e Word Count por Secção

### Elementos Pré-Textuais

| Elemento | Páginas | Notas |
|---|---|---|
| Capa | 1 | Obrigatória — campos fixos |
| Página de Rosto | 1 | Orientador, co-orientador, júri |
| Dedicatória | 1 (opcional) | Opcional — máx. meia página |
| Agradecimentos | 1–2 | Obrigatório — modelo editável |
| Resumo (PT) | 1 | Máx. 250 palavras + 5–8 palavras-chave |
| Abstract (EN) | 1 | Máx. 250 palavras + 5–8 keywords |
| Índice Geral | 1–2 | Página separada obrigatória |
| Índice de Figuras | 1 | Página separada obrigatória |
| Índice de Tabelas | 1 | Página separada obrigatória |
| Lista de Acrónimos | 1 | Página separada obrigatória |

---

### Capítulo 1 — Introdução

**Word count recomendado: 1 500–2 500 palavras (8–12 páginas)**

#### 1.1 Motivação e Contexto (400–600 palavras)
- Enquadramento do problema no estado actual da área
- Por que é este problema relevante agora? (dados quantitativos sempre que possível)
- Impacto prático esperado da solução
- Conexão ao contexto IST/DEI e linhas de investigação do departamento

**Tópicos obrigatórios:**
- [ ] Problema concreto identificado (não genérico)
- [ ] Dados ou referências que justificam a relevância
- [ ] Âmbito: o que está dentro e fora do âmbito da dissertação

#### 1.2 Problema e Objectivos (300–500 palavras)
- Definição precisa e operacional do problema
- Questão de investigação principal (Research Question)
- Objectivos específicos numerados (3–5 objectivos concretos e verificáveis)
- Hipóteses de trabalho (se aplicável)

**Tópicos obrigatórios:**
- [ ] Research question formulada como pergunta
- [ ] Objectivos SMART (Specific, Measurable, Achievable, Relevant, Time-bound)
- [ ] Distinção entre objectivo principal e objectivos secundários

#### 1.3 Contribuições (200–400 palavras)
- Lista numerada e explícita de contribuições originais
- Cada contribuição com: o que é novo, como é diferente do estado da arte, onde é validado

**Tópicos obrigatórios:**
- [ ] Mínimo 2–3 contribuições técnicas concretas
- [ ] Cada contribuição ligada à secção onde é desenvolvida
- [ ] Distinção clara entre contribuição técnica e contribuição empírica

#### 1.4 Estrutura da Dissertação (100–200 palavras)
- Parágrafo por capítulo descrevendo o que contém
- Fluxo lógico entre capítulos explicitado

---

### Capítulo 2 — Background e Estado da Arte

**Word count recomendado: 4 000–7 000 palavras (20–35 páginas)**

#### 2.1 Conceitos Fundamentais (1 000–2 000 palavras)
- Definições precisas dos conceitos necessários para compreender a dissertação
- Fórmulas matemáticas relevantes com notação consistente
- Diagrams de arquitectura de sistemas base (Transformers, CNNs, etc. conforme o tema)

**Tópicos obrigatórios:**
- [ ] Cada conceito introduzido antes de ser usado
- [ ] Equações numeradas segundo o capítulo (2.1), (2.2)...
- [ ] Referências às fontes originais de cada conceito (não a textbooks)

#### 2.2 Trabalho Relacionado (2 000–3 500 palavras)
- Organizado por subtema, não por ordem cronológica ou alfabética
- Para cada trabalho relevante: método, resultado, limitação
- Tabela comparativa de abordagens existentes (obrigatória para dissertações DEI)

**Estrutura sugerida:**
```
2.2.1 [Subtema A — ex.: Load Balancing em Cloud]
2.2.2 [Subtema B — ex.: Multi-Agent Reinforcement Learning]
2.2.3 [Subtema C — ex.: Federated Learning para Cloud]
```

**Tópicos obrigatórios:**
- [ ] Mínimo 50 referências verificadas no estado da arte
- [ ] Tabela comparativa com pelo menos 5 trabalhos e 4 dimensões de comparação
- [ ] Identificação explícita das lacunas (research gaps) na literatura

#### 2.3 Análise Crítica e Posicionamento (500–1 000 palavras)
- Síntese das limitações do estado da arte
- Como a presente dissertação aborda essas limitações
- O que distingue esta abordagem das existentes

**Tópicos obrigatórios:**
- [ ] Cada gap mapeado a pelo menos uma contribuição da dissertação
- [ ] Referência cruzada com a lista de contribuições do Cap. 1.3

---

### Capítulo 3 — Abordagem / Arquitectura / Metodologia

**Word count recomendado: 3 000–5 000 palavras (15–25 páginas)**

#### 3.1 Visão Geral da Solução (400–700 palavras)
- Diagrama de arquitectura de alto nível (obrigatório)
- Descrição textual do fluxo de dados e decisões
- Decisões de design fundamentais e justificação

**Tópicos obrigatórios:**
- [ ] Figura de arquitectura geral com todos os componentes identificados
- [ ] Descrição de cada componente e responsabilidade
- [ ] Trade-offs considerados (e por que foi escolhida esta abordagem)

#### 3.2 Arquitectura Detalhada (1 500–2 500 palavras)
- Descrição técnica de cada componente
- Algoritmos principais em pseudocódigo (algoritmo numerado, não código-fonte)
- Estruturas de dados relevantes
- Protocolos de comunicação (se aplicável)

**Tópicos obrigatórios:**
- [ ] Pelo menos 1 algoritmo formal em pseudocódigo
- [ ] Diagramas de sequência ou de estados para fluxos complexos
- [ ] Fórmulas matemáticas do modelo proposto (se ML/DL)

#### 3.3 Decisões de Design e Justificação (600–1 000 palavras)
- Tabela de decisões de design: alternativa considerada vs. escolha feita vs. justificação
- Limitações conhecidas da abordagem escolhida
- Como as limitações são mitigadas

**Tópicos obrigatórios:**
- [ ] Tabela com pelo menos 3 decisões de design significativas
- [ ] Cada limitação da abordagem reconhecida explicitamente

---

### Capítulo 4 — Implementação

**Word count recomendado: 2 500–4 000 palavras (12–20 páginas)**

#### 4.1 Ambiente de Desenvolvimento (300–500 palavras)
- Hardware: CPU, GPU, RAM, armazenamento
- Software: OS, linguagem, frameworks, versões exactas
- Cloud: instância, região, configuração (se aplicável)

**Tópicos obrigatórios:**
- [ ] Tabela de especificações do ambiente (hardware + software)
- [ ] Versões exactas de todas as dependências principais
- [ ] Instruções de reprodução (ou referência ao repositório)

#### 4.2 Detalhes de Implementação (1 500–2 500 palavras)
- Estrutura do repositório de código
- Componentes implementados: módulos, classes, APIs
- Integrações externas (datasets, APIs, serviços cloud)
- Configurações de treino (se ML): hyperparâmetros, scheduler, optimizador

**Tópicos obrigatórios:**
- [ ] Diagrama de componentes ou UML (quando a implementação é complexa)
- [ ] Seeds fixos documentados (para reprodutibilidade)
- [ ] Decisões de engenharia divergentes da arquitectura proposta e porquê

#### 4.3 Desafios e Soluções (400–700 palavras)
- Problemas encontrados durante a implementação
- Como foram resolvidos
- O que seria feito de forma diferente

**Tópicos obrigatórios:**
- [ ] Pelo menos 2–3 desafios técnicos concretos descritos
- [ ] Solução implementada vs. soluções alternativas consideradas

---

### Capítulo 5 — Avaliação / Resultados Experimentais

**Word count recomendado: 3 000–5 000 palavras (15–25 páginas)**

#### 5.1 Setup Experimental (500–800 palavras)
- Datasets utilizados: nome, tamanho, split train/val/test, source
- Baselines: cada baseline descrita e justificada
- Métricas de avaliação: definição formal de cada métrica
- Protocolo experimental: como os experimentos foram conduzidos

**Tópicos obrigatórios:**
- [ ] Tabela de datasets com todas as estatísticas relevantes
- [ ] Justificação da escolha de cada baseline
- [ ] Definição matemática de cada métrica usada
- [ ] Seeds documentados para reprodutibilidade

#### 5.2 Resultados Principais (1 000–1 800 palavras)
- Tabela principal de resultados: método proposto vs. todas as baselines
- Gráficos de convergência / learning curves (para ML)
- Análise estatística: intervalos de confiança ou desvio padrão (obrigatório)

**Tópicos obrigatórios:**
- [ ] Tabela de resultados com negrito nos melhores resultados
- [ ] Teste estatístico de significância (t-test, Wilcoxon, etc.)
- [ ] Pelo menos 3 experimentos distintos

#### 5.3 Análise Ablation (500–1 000 palavras)
- Impacto de cada componente do sistema (remover/modificar um a um)
- Tabela de ablation com todas as variantes

**Tópicos obrigatórios:**
- [ ] Cada contribuição técnica do Cap. 1.3 avaliada individualmente
- [ ] Discussão do que acontece sem cada componente

#### 5.4 Discussão (500–900 palavras)
- Interpretação dos resultados: o que explicam os dados?
- Comparação com expectativas iniciais
- Casos de falha: onde o sistema não funciona bem e porquê
- Limitações experimentais

**Tópicos obrigatórios:**
- [ ] Análise de pelo menos 2 failure cases
- [ ] Limitações da avaliação reconhecidas explicitamente

---

### Capítulo 6 — Conclusão e Trabalho Futuro

**Word count recomendado: 1 000–1 800 palavras (5–8 páginas)**

#### 6.1 Sumário das Contribuições (400–600 palavras)
- Revisitar cada contribuição do Cap. 1.3 e confirmar como foi alcançada
- Síntese dos resultados mais relevantes com números concretos

**Tópicos obrigatórios:**
- [ ] Cada contribuição mapeada a um resultado quantitativo
- [ ] Research question do Cap. 1.2 respondida explicitamente

#### 6.2 Limitações (200–400 palavras)
- Limitações da abordagem proposta (técnicas e experimentais)
- O que não foi possível validar no âmbito desta dissertação

**Tópicos obrigatórios:**
- [ ] Pelo menos 3 limitações honestas e concretas
- [ ] Distinção entre limitações da abordagem e limitações da avaliação

#### 6.3 Trabalho Futuro (300–500 palavras)
- Extensões directas da dissertação (3–5 direcções concretas)
- Cada direcção com: motivação, abordagem sugerida, impacto esperado

**Tópicos obrigatórios:**
- [ ] Pelo menos 3 direcções de trabalho futuro concretas
- [ ] Cada direcção justificada pelas limitações identificadas em 6.2

---

### Bibliografia

**Mínimo recomendado: 60–100 referências para dissertações de Mestrado DEI**

- Formato IEEE (padrão IST Engenharia Informática)
- Todas as referências verificadas via DOI/CrossRef
- Máximo 10% de referências não peer-reviewed (blogs, GitHub, docs técnicas)
- Distribuição saudável: ≥70% artigos de conferências/journals top (IEEE, ACM, Springer)

---

### Apêndices

| Apêndice | Conteúdo típico |
|---|---|
| Apêndice A | Código-fonte relevante (não todo — só o essencial) |
| Apêndice B | Tabelas de resultados complementares |
| Apêndice C | Provas matemáticas auxiliares |
| Apêndice D | Detalhes de configuração e deployment |

---

## Checklist de Entrega IST-DEI

### Antes de entregar ao orientador:

**Estrutura:**
- [ ] Todos os capítulos obrigatórios presentes
- [ ] Cada capítulo começa numa nova página
- [ ] Índice Geral, Figuras, Tabelas e Acrónimos em páginas separadas
- [ ] Numeração de páginas correcta (romanas para pré-texto, árabes para capítulos)

**Conteúdo:**
- [ ] Research question respondida explicitamente na conclusão
- [ ] Todas as contribuições do Cap. 1.3 validadas no Cap. 5
- [ ] Todas as figuras referenciadas no texto antes de aparecerem
- [ ] Todas as tabelas com título acima e referenciadas no texto
- [ ] Nenhuma afirmação sem referência ou evidência

**Citações:**
- [ ] Todas as referências verificadas (CrossRef/DOI)
- [ ] Formato IEEE consistente em toda a bibliografia
- [ ] Nenhuma referência [NÃO VERIFICADO] no documento final
- [ ] Software/datasets citados correctamente

**Formatação:**
- [ ] Fonte: Arial 10pt ou Times New Roman 12pt (consultar orientador)
- [ ] Espaçamento: 1.5 linhas
- [ ] Margens: 2.5 cm todos os lados
- [ ] Equações numeradas (X.Y) alinhadas à direita
- [ ] Legendas de figuras abaixo, justificadas
- [ ] Legendas de tabelas acima, justificadas

**Submissão Fénix:**
- [ ] PDF final gerado com LuaLaTeX (sem erros de compilação)
- [ ] Resumo PT e Abstract EN prontos para o formulário Fénix (máx. 250 palavras cada)
- [ ] IST Scholar: metadados completos (título PT+EN, palavras-chave, orientador, DEI)
- [ ] Documento assinado pelo orientador

### Antes da defesa:

- [ ] Apresentação de 20–25 minutos preparada
- [ ] Demo funcional (se aplicável)
- [ ] Artigo submetido ou em preparação (recomendado para nota máxima)
- [ ] Repositório de código acessível ao júri
- [ ] Cópia encadernada para cada membro do júri (consultar DEI)

---

## Word Counts Totais por Tipo

| Tipo | Mínimo | Recomendado | Máximo |
|---|---|---|---|
| Dissertação de Mestrado DEI | 15 000 palavras | 20 000–30 000 palavras | 40 000 palavras |
| Relatório de Projecto Final (LEIC) | 8 000 palavras | 12 000–18 000 palavras | 25 000 palavras |
| Tese de Doutoramento DEI | 40 000 palavras | 60 000–80 000 palavras | 120 000 palavras |

---

## Referências Normativas

- Regulamento de Dissertações IST 2022 (PDF oficial — disponível no Fénix)
- Template LaTeX IST-UL MSc Dissertation v5.0 — https://www.overleaf.com/latex/templates/ist-ul-msc-dissertation/wrhbmbvzpttw
- Normas IEEE para Engenharia Informática — https://ieeeauthorcenter.ieee.org/
- IST Scholar — https://scholar.projects.dsi.tecnico.ulisboa.pt
