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
