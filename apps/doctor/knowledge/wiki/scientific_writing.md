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

---

## Rubrica IEEE de Avaliação de Abstracts (Night 3 — 2026-05-31)

Derivada de auto-avaliação com paper fictício FedAdaGrad (Federated Learning).
Testada e refinada em sessão de treino. Score mínimo IEEE: **8.0/10**.

### Os 4 Elementos Obrigatórios — Verificação Explícita

| # | Elemento | Frases | Critério de qualidade | Erro mais comum |
|---|----------|--------|----------------------|-----------------|
| 1 | **Problema/Contexto** | 1-2 | Problem claro + escala/impacto com número | "increasingly important" sem estatística |
| 2 | **Abordagem/Método** | 2-3 | Sistema nomeado + mecanismo chave identificado | Over-detail (deixar para Introduction) |
| 3 | **Resultados** | 1-2 | Benchmarks + métricas concretas + condição experimental | "competitive performance" sem número |
| 4 | **Impacto/Conclusão** | 1 | O que o campo pode agora fazer que antes não podia | **Ausente** — sacrificado para dar mais espaço a resultados |

**Checklist antes de finalizar qualquer abstract:**
- [ ] Elemento 1 presente com número de contexto ou citação de escala?
- [ ] Sistema/método tem nome próprio (searchable)?
- [ ] Resultados incluem: dataset(s), baseline, número(s), condição?
- [ ] **Elemento 4 presente?** (Verificação explícita — omissão mais frequente)
- [ ] Sem citações no abstract?
- [ ] Contagem de palavras dentro do limite do venue?

### Pesos para score ponderado:

```
Score = 0.20 × Problema + 0.25 × Método + 0.25 × Resultados + 0.20 × Impacto + 0.10 × Língua
```

Score < 7.5 → não submeter. Score 7.5–8.5 → revisar elementos fracos. Score > 8.5 → pronto.

---

## Regras de Melhoria — Padrões Fracos Identificados (Night 3)

### Regra 1 — O Impacto Nunca É Opcional
O quarto elemento (impacto/conclusão) é o mais frequentemente omitido e o mais valioso.
Aumentou o score do abstract de treino em +1.2 pontos com uma única frase.

**Fórmula:** "These results demonstrate that [X] is [a viable / the most effective] approach to [Y] for [domain]."

**Variações aceites:**
- "Our findings suggest that [technique] can reduce [cost] while preserving [quality] in [setting]."
- "FedAdaGrad demonstrates that importance-guided adaptive compression is a viable path toward production-ready federated systems for resource-constrained mobile environments."

### Regra 2 — Contexto com Escala Quantificada
**❌ Errado:** "FL faces challenges at scale"  
**✓ Correcto:** "FL deployments at production scale involve 10^6+ heterogeneous devices [X], where each training round transmits hundreds of megabytes per client [Y]."

### Regra 3 — Resultados Sem Hedging
**❌ Errado:** "matching or exceeding FedAvg accuracy"  
**✓ Correcto:** "exceeds FedAvg by 1.8 pp under 30% client dropout; matches FedAvg under full participation"

Quando o resultado é condicional, dar a condição, não hedging.

### Regra 4 — Léxico de Clichés Proibidos em Related Work

| Frase proibida | Substituição |
|----------------|--------------|
| "a rich body of research" | descrever estrutura: "three classes of compression: sparsification, quantisation, sketching" |
| "substantial attention" | "motivated X, Y, and Z [refs]" |
| "a growing body of work" | citar os papers directamente |
| "principled approach" | mecanismo específico: "importance-guided adaptive compression" |
| "it is clear that" | remover — nunca é "clear" |
| "we can see from" | "Figure X shows" |

### Regra 5 — Transições entre Grupos de Related Work
Cada transição entre grupos necessita de uma frase de ligação explícita que explique a relevância do próximo grupo.

**Padrão de transição:**  
"While [grupo anterior] addresses [problema A], [grupo seguinte] tackles [problema B], which remains unaddressed in [contexto]."

**Exemplo correcto:**  
"While the above approaches handle statistical heterogeneity, they leave the communication policy fixed across all clients, motivating work on per-client adaptive compression."

**Transição abrupt (❌):** Mudar de tema sem ligação → reviewer pergunta "porquê este grupo?"

### Regra 6 — Gap Statement Accionável

**❌ Genérico:** "Adaptive compression has not been systematically explored."

**✓ Específico (contraste duplo):**  
"Unlike prior *compression* approaches that apply static per-round budgets, and unlike *heterogeneity-handling* methods that leave communication policies unchanged, [proposed work] co-designs [X] and [Y] to simultaneously [objective 1] and [objective 2]."

O gap deve ser descrito em termos do que o seu trabalho faz que nenhum trabalho anterior faz, não apenas o que não existe.

---

## Estrutura Óptima de Related Work — Template de 5 Grupos

Identificada como superior ao template de 3 grupos (Night 3):

```
1. FOUNDATIONS
   Trabalho seminal + baseline. Uma limitação fundamental que motiva a área.
   Tipicamente 2-3 papers fundacionais.

2. ABORDAGEM A (e.g., Compressão)
   O que fazem, como funciona (específico), limitação partilhada.
   Citar 3-5 papers; terminar com: "A critical limitation shared by all X approaches is..."

3. ABORDAGEM B (e.g., Heterogeneidade)
   O que fazem, como funciona, limitação.
   [Transição explícita desde grupo anterior]
   Citar 3-5 papers.

4. ABORDAGEM C (e.g., Adaptação/Personalização)
   [Transição explícita] Porque é que este grupo é relevante para o trabalho.
   Limitação: "These approaches address X but leave Y unchanged."

5. POSICIONAMENTO (secção própria ou último parágrafo)
   Contraste com grupos anteriores: "Unlike A, and unlike B, o nosso trabalho..."
   "To the best of our knowledge, this is the first..."
   Nunca misturar com grupo 4.
```

### Verificação de qualidade de Related Work

| Critério | Indicador | Score mín. |
|----------|-----------|------------|
| Estrutura | 4-5 grupos temáticos com progressão lógica | 8/10 |
| Rigor científico | Sistemas nomeados, venues correctas, limitações específicas | 7.5/10 |
| Citações | Verificadas (fase 2) antes de submissão | 9/10 |
| Linguagem | Sem clichés; transições explícitas; contraste activo | 7.5/10 |

---

## Verificação de Citações em Duas Fases

Protocolo identificado em Night 3 para garantir integridade de referências:

### Fase 1 — Rascunho (estrutura suficiente)
- Nome do sistema + autores principais
- Venue provável + ano provável
- Contribuição principal
- Marcação: ⚠️ (a confirmar)

### Fase 2 — Submissão (completo e verificado)
- DOI confirmado
- Volume, número, páginas exactas
- Nome correcto do venue (conferência/journal, não abreviação genérica)
- Verificação em: Semantic Scholar, CrossRef, ACM DL, IEEE Xplore
- Marcação: ✅

**Regra absoluta:** Nunca apresentar uma referência Fase 1 como final num documento para submissão ou entrega académica.

*Fonte: Night 3 training (2026-05-31)*
