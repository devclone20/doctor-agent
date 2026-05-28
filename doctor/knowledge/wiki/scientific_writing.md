# Escrita Científica — Metodologia e Padrões

## Princípios da Escrita Científica

### Clareza antes de tudo:
- Uma frase = uma ideia
- Evitar ambiguidade: o leitor não deve adivinhar
- Usar terminologia consistente — não variar o nome do mesmo conceito
- Definir acrónimos na primeira utilização: "Convolutional Neural Network (CNN)"

### Precisão e rigor:
- Claims devem ser suportados por evidência (citações ou resultados próprios)
- Distinguir factos de opinião
- Quantificar sempre que possível: "melhora 15%" > "melhora significativamente"
- Não fazer afirmações que os dados não suportam

### Objectividade:
- Evitar linguagem emotiva
- Apresentar limitações e trabalho relacionado crítico de forma justa
- Voz passiva é comum em PT científico; activa em EN moderno (ACM/IEEE recomendam activa)

---

## Estrutura de um Artigo Científico (IEEE/ACM)

### Short paper (4-6 páginas):
1. **Abstract** (150-250 palavras) — problema, método, resultados-chave, contribuição
2. **Introduction** — contexto, problema, contribuições, paper structure
3. **Related Work** — estado da arte, como o trabalho se posiciona
4. **Approach/Method** — o que foi feito e porquê
5. **Evaluation** — setup, métricas, resultados, comparação
6. **Conclusion** — sumário e trabalho futuro
7. **References**

### Full paper (8-12 páginas):
Igual ao short paper mas com secções mais desenvolvidas e possível apêndice.

---

## Como Escrever Cada Secção

### Abstract:
- 4 elementos obrigatórios: (1) contexto/problema, (2) abordagem, (3) resultados, (4) conclusão/impacto
- Não citar referências no abstract
- Evitar jargão excessivo — o abstract é lido por pessoas fora da área
- Tempo presente para factos gerais; passado para o que foi feito

### Introduction:
- Parágrafo 1: Contexto geral e relevância do problema
- Parágrafo 2-3: Definição precisa do problema e por que é difícil
- Parágrafo 4: Overview do que foi proposto (sem detalhes técnicos)
- Parágrafo 5: Lista bullet de contribuições ("The main contributions of this work are:")
- Parágrafo final: "The remainder of this paper is organized as follows: Section 2..."

### Related Work:
- NÃO é uma lista de "X fez Y". É análise crítica.
- Agrupar trabalhos por abordagem/problema
- Para cada grupo: o que fazem, qual a limitação, como o seu trabalho é diferente
- Usar comparação directa: "Unlike [5], our approach..."

### Methodology/Approach:
- Começar com visão geral (diagrama de arquitectura é obrigatório)
- Descer ao detalhe progressivamente
- Justificar escolhas de design: "We chose X over Y because..."
- Pseudocódigo para algoritmos (Algorithm environment em LaTeX)

### Evaluation:
- Research questions claras: "RQ1: Does X outperform Y?"
- Setup: dataset, hardware, hyperparameters, baselines
- Métricas: justificar a escolha
- Resultados em tabela + discussão
- Análise estatística quando relevante (significance tests, confidence intervals)
- Ablation study: mostrar contribuição de cada componente

### Conclusion:
- Não repetir verbatim o abstract
- Sumário das contribuições (em retrospectiva, não em futuro)
- Limitações honestas
- Future work específico e accionável

---

## Figuras e Tabelas — Regras de Ouro

### Figuras:
- Cada figura conta uma história — se não, cortar
- Legenda deve ser auto-suficiente (lida sem o texto)
- Resolução: ≥300 DPI para print; vectorial (PDF, SVG) é melhor
- Linha de referência no texto ANTES da figura: "Figure 3 shows..."
- Não usar screenshots de baixa qualidade

### Tabelas:
- Título acima (IEEE standard)
- Melhor resultado em bold
- Unidades no cabeçalho, não nas células
- Evitar linhas verticais (plain tabular style é mais legível)
- Baseline destacada (linha horizontal separadora)

---

## Língua Inglesa em Papers IEEE

### Expressões técnicas úteis:
- "We propose/present/introduce..." — contribuição
- "To the best of our knowledge, this is the first..." — novidade
- "Empirical results demonstrate that..." — evidência
- "This approach achieves a X% improvement over..." — comparação
- "We evaluate on [dataset] and show that..." — avaliação
- "The key insight is that..." — contribuição conceptual
- "Despite its simplicity, the method..." — understatement elegante

### Erros comuns a evitar:
- "In this paper, we will..." → "In this paper, we..."
- "The results shows" → "The results show"
- "As we can see from the figure" → "Figure X shows"
- "It is clear that" → remover (nunca é "clear")
- "Very", "quite", "rather" → substituir por quantificação

---

## Processo de Revisão Científica

### Como submeter um paper:
1. Escolher conferência/journal adequado (verificar ranking: CORE, Qualis, SJR)
2. Ler o Call for Papers com atenção
3. Formatar correctamente segundo o template
4. Double-blind review: remover nomes e referências próprias identificáveis
5. Submeter antes do deadline (sistemas caem no último dia)

### Rankings de Conferências (CS/AI):
- **A*** (top): NeurIPS, ICML, ICLR, CVPR, ACL, SOSP, OSDI
- **A**: AAAI, IJCAI, ECCV, ICCV, EMNLP, EuroSys, USENIX ATC
- **B**: AISTATS, CoNLL, ICASSP, Middleware
- **Journals top**: TPAMI, JMLR, AIJ, TOIS, TKDE

### Resposta a revisores:
- Agradecer o feedback (mesmo o mau)
- Responder a CADA ponto dos revisores
- "We thank Reviewer 2 for this observation. We have added..."
- Mostrar diferenças com diff markup

---

## Plágio e Integridade Académica

### Regras IST:
- Citação obrigatória para toda ideia não original
- Paráfrase não é plágio se citada correctamente
- Autoplágio existe — citar trabalho anterior próprio
- Uso de IA (ChatGPT, Claude): verificar política do venue

### Ferramentas anti-plágio:
- Turnitin (usado pelo IST)
- iThenticate
- Grammarly (também detecção básica)
