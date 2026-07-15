# Machine Learning e Deep Learning — Conhecimento Core

## Fundamentos de Machine Learning

### Paradigmas:
- **Supervised Learning** — classificação, regressão (labels conhecidas)
- **Unsupervised Learning** — clustering, dimensionality reduction (sem labels)
- **Semi-supervised** — combina dados com e sem labels
- **Reinforcement Learning** — agente aprende por recompensas (Q-learning, PPO, SAC)
- **Self-supervised** — labels geradas automaticamente (contrastive, masked prediction)

### Algoritmos Clássicos:
- Linear/Logistic Regression, SVM, Decision Trees, Random Forest, Gradient Boosting
- XGBoost, LightGBM, CatBoost (estado da arte em dados tabulares)
- k-NN, k-Means, DBSCAN, PCA, t-SNE, UMAP

### Avaliação de Modelos:
- Classification: Accuracy, Precision, Recall, F1, ROC-AUC, PR-AUC
- Regression: MSE, RMSE, MAE, R², MAPE
- Cross-validation: k-fold, stratified k-fold, time-series split
- Bias-variance tradeoff; overfitting vs underfitting

---

## Deep Learning — Arquitecturas Fundamentais

### Feedforward Neural Networks (MLP):
- Backpropagation, gradient descent, SGD, Adam, AdamW
- Activations: ReLU, GELU, Swish, Tanh, Sigmoid
- Regularization: Dropout, Batch Norm, Layer Norm, Weight Decay

### Convolutional Neural Networks (CNN):
- LeNet, AlexNet, VGG, ResNet, DenseNet, EfficientNet
- Convolution, pooling, feature maps, receptive field
- Aplicações: image classification, object detection (YOLO, Faster R-CNN), segmentation

### Recurrent Networks (RNN/LSTM/GRU):
- Vanishing gradient problem → LSTM gates, GRU
- Seq2Seq, encoder-decoder
- Aplicações: NLP antes dos transformers, time series

### Transformers — Arquitectura Dominante (2017–presente):
- Paper fundamental: "Attention Is All You Need" (Vaswani et al., 2017), arXiv:1706.03762
- Multi-head self-attention, positional encoding
- Encoder-only (BERT), decoder-only (GPT), encoder-decoder (T5, BART)
- Vision Transformers (ViT), Swin Transformer
- BERT, GPT-2/3/4, T5, LLaMA, Mistral, Claude, Gemini

### Large Language Models (LLMs):
- Pre-training (next token prediction / masked LM)
- Fine-tuning, RLHF, DPO, ORPO
- Prompt engineering, in-context learning, chain-of-thought
- RAG (Retrieval Augmented Generation)
- Parameter-efficient fine-tuning: LoRA, QLoRA, adapters

### Graph Neural Networks (GNN):
- GCN, GAT, GraphSAGE
- Aplicações: molecular property prediction, social networks, recommendation

### Diffusion Models:
- DDPM, DDIM, Score-based models
- Aplicações: image generation (Stable Diffusion, DALL-E), audio, video

---

## Frameworks e Ferramentas

### Deep Learning Frameworks:
- **PyTorch** — padrão em investigação (dinâmico, flexible)
- **TensorFlow/Keras** — produção, deployment (TFServing, TFLite)
- **JAX** — high-performance, XLA, funcional (Google)
- **Hugging Face Transformers** — modelos pré-treinados, fine-tuning

### MLOps & Experiment Tracking:
- **MLflow** — tracking, model registry, deployment
- **Weights & Biases (W&B)** — visualização de runs
- **DVC** — versioning de dados e modelos
- **Hydra** — configuração de experimentos
- **Ray Tune** — hyperparameter optimization

### Data Engineering:
- **Pandas, Polars** — manipulação tabular
- **NumPy, SciPy** — álgebra linear, estatística
- **Apache Spark** — big data processing
- **Dask** — parallelismo em Python

---

## Papers Fundamentais (Must-Know)

### Transformers & Attention:
- Vaswani et al. (2017) — "Attention Is All You Need" — arXiv:1706.03762
- Devlin et al. (2019) — "BERT: Pre-training of Deep Bidirectional Transformers" — arXiv:1810.04805
- Brown et al. (2020) — "Language Models are Few-Shot Learners" (GPT-3) — arXiv:2005.14165

### Computer Vision:
- He et al. (2016) — "Deep Residual Learning for Image Recognition" (ResNet) — arXiv:1512.03385
- Dosovitskiy et al. (2021) — "An Image is Worth 16x16 Words" (ViT) — arXiv:2010.11929

### Reinforcement Learning:
- Mnih et al. (2015) — "Human-level control through deep RL" (DQN) — Nature 518
- Schulman et al. (2017) — "Proximal Policy Optimization" — arXiv:1707.06347

### Generative Models:
- Goodfellow et al. (2014) — "Generative Adversarial Networks" — arXiv:1406.2661
- Ho et al. (2020) — "Denoising Diffusion Probabilistic Models" — arXiv:2006.11239

### Optimization:
- Kingma & Ba (2015) — "Adam: A Method for Stochastic Optimization" — arXiv:1412.6980
- Loshchilov & Hutter (2019) — "Decoupled Weight Decay Regularization" (AdamW) — arXiv:1711.05101

---

## Métricas de Avaliação em Deep Learning

### Visão Computacional:
- mAP (mean Average Precision) — detecção
- IoU (Intersection over Union) — segmentação
- FID (Fréchet Inception Distance) — qualidade generativa

### NLP:
- BLEU, ROUGE — tradução e sumarização
- Perplexity — modelos de linguagem
- BERTScore, METEOR

### Fairness & Robustness:
- Calibration (ECE), Adversarial robustness
- Out-of-distribution detection

---

## Engenharia Informática e Computadores @ IST

Tópicos de dissertação frequentes em ML/AI:
- Federated Learning (privacidade + distribuição)
- Explainable AI (XAI) — SHAP, LIME, attention maps
- Edge AI / TinyML — deployment em dispositivos IoT
- Neural Architecture Search (NAS)
- Continual Learning / Lifelong Learning
- Anomaly Detection
- Multimodal Learning (vision + language)
- Time Series Forecasting com Transformers

---

## Estado da Arte 2025 — Top 10 Papers ML/DL/AI

*Secção adicionada na Night 2 do ciclo de treino. Todos os papers verificados via arXiv,
Semantic Scholar e fontes primárias. Citações reportadas em Maio 2026.*

*Nota metodológica: inclui papers publicados em Dez 2024 que circularam e foram massivamente
citados ao longo de 2025, bem como papers publicados ao longo de 2025.*

---

### [P1] DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

| Campo | Detalhe |
|-------|---------|
| **Autores** | DeepSeek-AI (Guo, D. et al.) |
| **Venue** | arXiv:2501.12948 (Jan 2025); publicado em *Nature* (2025) |
| **Citações** | ~5,517 (Semantic Scholar, Maio 2026) |

**Contribuição principal:** Prova que raciocínio de ponta pode emergir de Reinforcement
Learning puro, sem trajectórias de raciocínio supervisionadas por humanos. Introduz
DeepSeek-R1-Zero (RL puro) e DeepSeek-R1 (RL + SFT mínimo de arranque).

**Metodologia:** GRPO (Group Relative Policy Optimization) — variante de PPO que elimina a
rede crítica e usa a recompensa média do grupo de saídas como baseline. Recompensas baseadas
em regras (correcção formal verificável). Treinado sobre DeepSeek-V3 como modelo base.

**Resultados chave:**
- AIME 2024: pass@1 sobe de 15.6% → **71.0%** (86.7% com majority voting)
- Desempenho comparable ao OpenAI o1 em raciocínio matemático e código
- Destilação do R1 para modelos 1.5B–70B mantém ganhos substanciais

**Impacto:** Paper mais citado de Jan 2025. Democratizou RL para raciocínio; lançou vaga de
reproduções (QwQ, s1, etc.) e consolidou GRPO como algoritmo de referência em 2025.

---

### [P2] DeepSeek-V3 Technical Report

| Campo | Detalhe |
|-------|---------|
| **Autores** | DeepSeek-AI |
| **Venue** | arXiv:2412.19437 (Dez 2024 / Jan 2025) |

**Contribuição principal:** Modelo MoE (Mixture-of-Experts) aberto com 671B parâmetros
totais / 37B activos por token, treinado com eficiência de custo sem precedentes no segmento
open-source.

**Metodologia:**
- Multi-head Latent Attention (MLA) para reduzir KV cache
- DeepSeekMoE com estratégia de balanceamento sem auxiliary loss (bias dinâmico por expert)
- Multi-Token Prediction (MTP) como objectivo auxiliar de treino
- Apenas **2.788M horas de GPU H800** para treino completo (~$5.5M vs. dezenas de M$ de rivais)

**Resultados chave:**
- Supera todos os modelos open-source no lançamento
- Desempenho comparável a modelos closed-source líderes (GPT-4o, Claude 3.5 Sonnet)
- Benchmarks: HumanEval 65.2%, MATH 61.6%, MMLU 88.5%

**Impacto:** Confirmou que a arquitectura MoE com optimizações de sistema pode colapsar a
vantagem de custo dos modelos proprietários. Base de treino do DeepSeek-R1.

---

### [P3] Qwen2.5 Technical Report

| Campo | Detalhe |
|-------|---------|
| **Autores** | Qwen Team, Alibaba Group |
| **Venue** | arXiv:2412.15115 (Jan 2025) |

**Contribuição principal:** Família de LLMs open-weight com escalamento de dados pré-treino
de 7T → 18T tokens, acompanhada de modelos especializados (Qwen2.5-Math, Qwen2.5-Coder).

**Metodologia:** Curadoria massiva de dados com filtros de qualidade, pós-treino com RLHF,
DPO, e instruction tuning. Pipeline de post-training multi-stage.

**Resultados chave:**
- Qwen2.5-72B-Instruct compete com **Llama-3-405B-Instruct** (5× maior)
- Qwen2.5-Turbo e Qwen2.5-Plus competitivos com GPT-4o-mini e GPT-4o respectivamente
- Qwen2.5-Math-72B estado da arte em benchmarks matemáticos open-source

**Impacto:** Estabeleceu novo patamar de eficiência paramétrica para LLMs open-weight.
A família Qwen tornou-se base para numerosas investigações e fine-tunings em 2025.

---

### [P4] s1: Simple Test-Time Scaling

| Campo | Detalhe |
|-------|---------|
| **Autores** | Muennighoff, N., Yang, Z., Shi, W. et al. (Stanford) |
| **Venue** | arXiv:2501.19393 (Jan 2025); EMNLP 2025 |

**Contribuição principal:** Primeira reprodução aberta e verificável de test-time scaling
(escalamento de compute em inferência), usando apenas 1,000 exemplos de treino.

**Metodologia:**
- Dataset s1K: 1,000 pares (pergunta, trace de raciocínio) seleccionados por 3 critérios:
  dificuldade, diversidade, qualidade
- Supervised fine-tuning do Qwen2.5-32B-Instruct sobre s1K
- **Budget forcing**: forçar ou interromper o pensamento do modelo em inferência para
  controlar compute usado, reproduzindo a curva de escalamento do o1

**Resultados chave:**
- Matches OpenAI o1-preview em AIME e MATH com apenas 1K exemplos de treino
- Primeira reprodução das curvas de test-time scaling do o1
- Código e dados publicados open-source

**Impacto:** Desmistificou o "segredo" do o1. Prova que test-time scaling é acessível
sem recursos proprietários massivos. Gerou vaga de trabalhos de reprodução e extensão.

---

### [P5] Scaling LLM Test-Time Compute Optimally

| Campo | Detalhe |
|-------|---------|
| **Autores** | Snell, C., Lee, J., Xu, K., Kumar, A. (Google DeepMind) |
| **Venue** | arXiv:2408.03314 (Ago 2024 — massivamente citado em 2025) |

**Contribuição principal:** Demonstra que escalar compute em inferência pode ser mais eficaz
do que escalar parâmetros do modelo, desde que se use a estratégia óptima.

**Metodologia:** Compara estratégias de compute em inferência: best-of-N sampling, beam
search com Process Reward Models (PRMs), revision iterativa. Define noção de
"compute-optimal test-time strategy".

**Resultados chave:**
- Para um dado orçamento de compute, test-time scaling bem optimizado supera scaling de parâmetros
- PRMs como verifiers são componente chave para orientar busca em raciocínio
- Resultados em MATH e GSM8K validam as curvas teóricas

**Impacto:** Paper fundacional para a vaga de reasoning models de 2025 (o1, R1, QwQ, s1).
Define o vocabulário conceptual do campo: "compute-optimal inference", "process reward model".

---

### [P6] The Llama 3 Herd of Models

| Campo | Detalhe |
|-------|---------|
| **Autores** | Meta AI Research (Dubey, A. et al., ~100 autores) |
| **Venue** | arXiv:2407.21783 (Jul 2024 — um dos mais citados em 2025) |

**Contribuição principal:** Família de LLMs multilingues e multimodais open-weight, com o
maior modelo de 405B parâmetros densos — o modelo aberto mais capaz no lançamento.

**Metodologia:** Dense Transformer com contexto de 128K tokens. Pré-treino em 15T+ tokens.
Multi-stage post-training: SFT → RLHF → DPO. Suporte nativo a code, reasoning, tool use.
Versões multimodais com visão integrada.

**Resultados chave:**
- Llama-3.1-405B compara favoravelmente com GPT-4 em múltiplos benchmarks
- Llama-3.2-11B-Vision compete com modelos multimodais proprietários de menor escala
- Base para centenas de fine-tunings académicos e industriais em 2025

**Impacto:** O modelo open-weight de referência em 2025. Tornou-se base para a maioria dos
estudos académicos de PEFT, alinhamento, e eficiência em 2025.

---

### [P7] InternVL2.5: Expanding Performance Boundaries of Open-Source Multimodal Models

| Campo | Detalhe |
|-------|---------|
| **Autores** | Chen, J. et al. (OpenGVLab / Shanghai AI Lab) |
| **Venue** | arXiv:2412.05271 (Dez 2024 — amplamente citado em 2025) |

**Contribuição principal:** Primeiro modelo multimodal open-source a superar 70% no
benchmark MMMU (Massive Multidisciplinary Multimodal Understanding).

**Metodologia:** Escalamento sistemático de: encoder visual, modelo de linguagem base,
tamanho do dataset e estratégias test-time. Vision-language co-training. Grandes encoders
visuais reduzem dependência de dados de treino.

**Resultados chave:**
- InternVL2.5-78B: **>70% no MMMU** (primeiro open-source a cruzar esta barreira)
- Competitivo com GPT-4o e Claude 3.5 Sonnet em document understanding e visual grounding
- InternVL2.5-78B obtém melhor performance que modelos comparáveis com apenas 1/10 dos tokens

**Impacto:** Fechou o gap entre modelos multimodais abertos e fechados. Tornou-se
referência para dissertações sobre multimodal learning em 2025.

---

### [P8] Gold-medalist Performance in Solving Olympiad Geometry with AlphaGeometry2

| Campo | Detalhe |
|-------|---------|
| **Autores** | Google DeepMind Team |
| **Venue** | arXiv:2502.03544 (Fev 2025); *Nature* (Nov 2025) |

**Contribuição principal:** Sistema neuro-simbólico que resolve 84% dos problemas de
geometria IMO (2000–2024), superando o desempenho médio de um medalhista de ouro.

**Metodologia:** Sistema híbrido simbólico + neural. Extensão da linguagem geométrica
para incluir equações lineares de ângulos, razões e distâncias. Knowledge-guided search
com modelos neurais de linguagem treinados em provas formalizadas. Integração com AlphaProof
para outras categorias matemáticas.

**Resultados chave:**
- Resolve 42/50 problemas de geometria IMO (2000-2024)
- Taxa de cobertura geométrica: 66% → 88% vs. versão anterior
- AlphaProof (sistema complementar): medalha de prata no IMO 2024

**Impacto:** Demonstra que AI pode resolver raciocínio matemático formal ao nível de elite
humana. Abre caminho para AI como ferramenta de investigação matemática. Publicado na
*Nature*, o que sinaliza reconhecimento da importância fora da comunidade de ML.

---

### [P9] Gemma 3 Technical Report

| Campo | Detalhe |
|-------|---------|
| **Autores** | Gemma Team, Google DeepMind |
| **Venue** | arXiv:2503.19786 (Mar 2025) |

**Contribuição principal:** Família de modelos open-weight multimodais leves (1B–27B) com
visão nativa, contexto de 128K tokens, e suporte multilíngue alargado.

**Metodologia:** Destilação de conhecimento de modelos Gemini maiores. Vision encoder
integrado para compreensão de imagem nativa. Pré-treino multilíngue. Instruction tuning e
alinhamento com RLHF.

**Resultados chave:**
- Gemma3-27B-IT ≈ Gemini-1.5-Pro em benchmarks gerais
- Gemma3-4B-IT competitivo com Gemma2-27B-IT (7× mais pequeno, desempenho equivalente)
- Capacidade de visão com compreensão de imagem e texto interligados

**Impacto:** Tornou modelos de alta capacidade acessíveis para hardware de consumo. O
Gemma3-4B é o modelo de referência para edge deployment e investigação com recursos
limitados em 2025.

---

### [P10] Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities

| Campo | Detalhe |
|-------|---------|
| **Autores** | Gemini Team, Google DeepMind |
| **Venue** | arXiv:2507.06261 (Jul 2025) |

**Contribuição principal:** Modelo multimodal de topo com raciocínio nativo ("thinking model"),
processamento de vídeo até 3 horas, e contexto de 1M+ tokens, com capacidades agénticas.

**Metodologia:** Arquitectura "thinking model" que permite raciocínio interno antes da
resposta. Multimodalidade nativa (texto, imagem, áudio, vídeo). Tool use integrado.
Contexto de mais de 1 milhão de tokens.

**Resultados chave:**
- Estado da arte em USAMO 2025 (matemática olímpica)
- Estado da arte em LiveCodeBench (código competitivo)
- Estado da arte em MMMU (compreensão multimodal)
- LMArena score: +120 pontos vs. Gemini 1.5 Pro

**Impacto:** Estabelece o novo patamar de capacidades de modelos frontier em 2025. A
combinação de raciocínio, multimodalidade e contexto ultra-longo define o paradigma de
modelos "de segunda geração" após os primeiros LLMs de raciocínio.

---

### Tendências Transversais — 2025

| Tendência | Papers exemplares | Implicação para dissertações IST |
|-----------|------------------|----------------------------------|
| **Test-Time Scaling** | P4 (s1), P5 (Snell et al.) | Compute em inferência como dimensão de escalamento; PRMs como verifiers |
| **RL para Raciocínio** | P1 (DeepSeek-R1) | GRPO substituindo PPO em fine-tuning; recompensas verificáveis |
| **Eficiência MoE** | P2 (DeepSeek-V3) | MoE como arquitectura padrão para LLMs de grande escala |
| **Multimodalidade Open** | P7 (InternVL2.5), P9 (Gemma 3) | Modelos multimodais acessíveis para investigação académica |
| **AI + Matemática Formal** | P8 (AlphaGeometry2) | Sistemas neuro-simbólicos para raciocínio verificável |
| **Destilação + Escalamento de Dados** | P3 (Qwen2.5), P9 (Gemma 3) | Qualidade de dados > quantidade bruta; destilação eficaz |

### BibTeX IEEE para os Top 10 Papers (2025)

```bibtex
@article{deepseek_r1_2025,
  author  = {{DeepSeek-AI} and Guo, Daya and others},
  title   = {{DeepSeek-R1}: Incentivizing Reasoning Capability in {LLMs} via Reinforcement Learning},
  journal = {arXiv preprint arXiv:2501.12948},
  year    = {2025}
}

@article{deepseek_v3_2025,
  author  = {{DeepSeek-AI}},
  title   = {{DeepSeek-V3} Technical Report},
  journal = {arXiv preprint arXiv:2412.19437},
  year    = {2025}
}

@article{qwen25_2025,
  author  = {{Qwen Team}},
  title   = {{Qwen2.5} Technical Report},
  journal = {arXiv preprint arXiv:2412.15115},
  year    = {2025}
}

@inproceedings{muennighoff_s1_2025,
  author    = {Muennighoff, Niklas and Yang, Zitong and Shi, Weijia and others},
  title     = {s1: Simple Test-Time Scaling},
  booktitle = {Proceedings of EMNLP 2025},
  year      = {2025}
}

@article{snell_tts_2024,
  author  = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},
  title   = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},
  journal = {arXiv preprint arXiv:2408.03314},
  year    = {2024}
}

@article{meta_llama3_2024,
  author  = {Dubey, Abhimanyu and others},
  title   = {The {Llama} 3 Herd of Models},
  journal = {arXiv preprint arXiv:2407.21783},
  year    = {2024}
}

@article{internvl25_2024,
  author  = {Chen, Jiaqi and others},
  title   = {Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling},
  journal = {arXiv preprint arXiv:2412.05271},
  year    = {2024}
}

@article{alphageometry2_2025,
  author  = {{Google DeepMind Team}},
  title   = {Gold-medalist Performance in Solving Olympiad Geometry with {AlphaGeometry2}},
  journal = {arXiv preprint arXiv:2502.03544},
  year    = {2025}
}

@article{gemma3_2025,
  author  = {{Gemma Team}},
  title   = {{Gemma 3} Technical Report},
  journal = {arXiv preprint arXiv:2503.19786},
  year    = {2025}
}

@article{gemini25_2025,
  author  = {{Gemini Team}},
  title   = {{Gemini 2.5}: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities},
  journal = {arXiv preprint arXiv:2507.06261},
  year    = {2025}
}
```

---

## Engenharia Informática e Computadores @ IST
