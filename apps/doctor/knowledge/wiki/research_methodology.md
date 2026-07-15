# Metodologia de Investigação Científica

## Tipos de Investigação

### Investigação Básica (Fundamental):
- Geração de novo conhecimento sem aplicação imediata
- Publicado em journals de alto impacto (Nature, Science, JMLR, TPAMI)
- Exemplo: nova arquitectura de rede neuronal

### Investigação Aplicada:
- Resolver problemas específicos usando conhecimento existente
- Publicado em conferências de topo (NeurIPS, ICML, CVPR)
- Exemplo: aplicar transformers para diagnóstico médico

### Investigação de Desenvolvimento:
- Construir sistemas funcionais (prototipagem, engenharia)
- Dissertações de mestrado frequentemente aqui
- Exemplo: sistema MLOps para produção

---

## O Processo Científico

### 1. Definição do Problema
- O que está errado ou em falta? (research gap)
- Porque é importante resolver?
- Quem beneficia da solução?

### 2. Revisão de Literatura
- State-of-the-art: quem fez o quê?
- Identificar limitações dos trabalhos existentes
- Posicionar o trabalho em relação ao existente

### 3. Formulação de Hipóteses
- H0 (hipótese nula) vs H1 (hipótese alternativa)
- Hipóteses verificáveis e falsificáveis
- Exemplo: "A arquitectura X supera o baseline Y em Z dataset"

### 4. Design Experimental
- Variáveis independentes (o que se controla)
- Variáveis dependentes (o que se mede)
- Grupos de controlo e experimentais
- Reproducibilidade: seed, hardware, versões

### 5. Recolha e Processamento de Dados
- Datasets públicos preferidos (reproducibilidade)
- Data splits: train / validation / test (nunca contaminar o test set)
- Preprocessing: normalização, augmentation, balanceamento

### 6. Implementação e Execução
- Versão controlada (git)
- Logging de experimentos (MLflow, W&B)
- Checkpoints e early stopping

### 7. Análise de Resultados
- Comparação com baselines
- Testes estatísticos quando aplicável
- Análise de erros (error analysis, failure cases)
- Ablation study

### 8. Conclusões e Limitações
- O que foi provado?
- O que não foi provado?
- Quando a solução não funciona?
- Trabalho futuro

---

## Qualidade da Investigação

### Validade Interna:
- Os resultados são causados pelo que pensamos que causam?
- Confounding variables eliminados?
- Reproducible experiments?

### Validade Externa:
- Os resultados generalizam para outros contextos?
- Apenas um dataset é insuficiente para claims gerais

### Reproducibilidade (crise de reprodutibilidade):
- Código público (GitHub)
- Dados públicos ou disponíveis sob pedido
- Hyperparameters e setup completamente documentados
- Hardware especificado (GPU, memória, CUDA version)
- Random seeds fixados

---

## Datasets Públicos Importantes em CS/AI

### Computer Vision:
- **ImageNet** (1.2M imagens, 1000 classes) — classificação
- **COCO** (328K imagens) — detecção, segmentação
- **CIFAR-10/100** — benchmark clássico
- **Open Images** — detecção large-scale

### NLP:
- **GLUE/SuperGLUE** — benchmark NLP multitarefa
- **SQuAD 2.0** — question answering
- **Common Crawl / C4** — pretraining LLMs
- **HumanEval** — code generation benchmark

### Tabular:
- **UCI ML Repository** — >500 datasets
- **Kaggle** — competições e datasets
- **OpenML** — benchmark suite

### Time Series:
- **ETTh1/ETTm1** — electricity transformer
- **Traffic, Weather** — forecasting benchmarks

---

## Como Fazer uma Revisão de Literatura Eficaz

### Fontes primárias:
1. **arXiv** — cs.LG, cs.AI, cs.CV, cs.CL para ML/AI (preprints, rápido)
2. **Semantic Scholar** — gratuito, boas recomendações
3. **Google Scholar** — abrangente mas não filtra qualidade
4. **IST Scholar** — dissertações do IST
5. **ACM Digital Library** — CS papers
6. **IEEE Xplore** — engenharia, sistemas
7. **PubMed** — biomédico

### Estratégia de pesquisa:
1. Começar com papers de survey/review do tema
2. Identificar papers fundadores (muito citados)
3. Seguir "cited by" para papers recentes
4. Usar Google Scholar Alerts para novos papers

### Gestão de literatura:
- Usar Zotero ou Mendeley
- Criar pasta por tema
- Anotar: problema, método, resultado, limitação
- BibTeX export para LaTeX

### Quantos papers citar?
- Dissertação de mestrado: 50-100 referências típico
- Paper de conferência (8 pág.): 25-50
- Review paper: 100-300+

---

## Research Questions vs. Objectives vs. Contributions

### Research Questions (RQ):
- Formuladas como perguntas
- RQ1: "Does approach X outperform Y on task Z?"
- RQ2: "What is the impact of hyperparameter H on performance?"

### Objectives:
- O que vai ser feito (accionável)
- "Implement and evaluate X on dataset Y"
- "Compare X against baselines A, B, C"

### Contributions:
- O que é novo no mundo (não apenas para o autor)
- "We propose X, a novel approach that..."
- "We present the first study of X in context Y"
- "We release a dataset of X" (contribuição de recurso)
- "We identify that X leads to Y" (contribuição empírica)

---

## Ética na Investigação

### Conflito de interesses:
- Declarar funding e afiliações
- Não esconder resultados negativos

### Investigação com humanos:
- RGPD (GDPR) compliance
- Anonimização de dados
- Consentimento informado

### IA e ética:
- Fairness e bias em modelos
- Transparência e explicabilidade
- Impacto ambiental (carbon footprint de treino de LLMs)
- Dual-use concerns (modelos que podem ser usados para mal)
