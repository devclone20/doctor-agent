# ML em Produção Real — O Que as Dissertações Não Ensinam

## A Lacuna Academia–Produção

Dissertações ensinam a construir modelos. Produção exige operar modelos.
São problemas fundamentalmente diferentes. Este wiki cobre o segundo.

Fonte: filosofia de engenharia de Fabio Akita, 30+ anos de experiência em sistemas reais.

---

## O que "Funciona" Significa em Produção

Em investigação: "o modelo atinge X% de accuracy no test set"
Em produção: "o modelo serve 10.000 requests/dia com P99 < 100ms, 99.9% uptime, custo < $0.01/request, e não degrada ao longo do tempo"

São cinco dimensões diferentes. Optimizar apenas uma é insuficiente.

---

## Os 7 Problemas Que Ninguém Conta nas Dissertações

### 1. Data Drift — O Modelo Degrada Silenciosamente

O test set é uma foto do passado. O mundo muda.

- **Covariate shift**: a distribuição de input muda (ex: utilizadores novos comportam-se diferente)
- **Label drift**: a distribuição de output muda (ex: o que era spam há 2 anos já não é spam hoje)
- **Concept drift**: a relação entre input e output muda (ex: padrões de fraude evoluem)

**O que fazer:**
- Monitorizar distribuição dos inputs em produção vs. distribuição de treino
- Alertas automáticos quando KL divergence ultrapassa threshold
- Retraining schedule: não esperar que o modelo quebre para retreinar
- Ferramentas: Evidently AI, NannyML, WhyLabs

**Exemplo real**: modelo de detecção de fraude treinado em 2022 começa a degradar em 2023 porque os padrões de fraude evoluíram. Sem monitorização, o degradação passa despercebida durante meses.

### 2. The "Works in Jupyter" Problem

Jupyter notebooks escondem estado global, ordem de execução, e dependências implícitas.

Sintomas:
- "Funciona no meu computador" (diferenças de versão)
- "Só funciona se correr as células nesta ordem" (estado implícito)
- "Não sei porque funcionou antes e agora não" (mutabilidade de estado)

**O que fazer:**
- Pipeline scripts em vez de notebooks para código de produção
- `requirements.txt` ou `pyproject.toml` com versões fixadas
- Docker para reproducibilidade garantida
- CI/CD que corre o pipeline de ponta a ponta em cada commit

```python
# Mau: estado global em notebook
df = pd.read_csv("data.csv")  # célula 1
# ... muitas células depois...
model.fit(df)  # assume df ainda está em memória, não transformado

# Bom: pipeline com estado explícito
def run_training_pipeline(data_path: str, config: TrainingConfig) -> TrainedModel:
    df = load_and_validate(data_path)
    features = engineer_features(df)
    model = train(features, config)
    return model
```

### 3. Latência de Inferência — O Problema Mais Subestimado

Em investigação, mede-se accuracy. Em produção, o utilizador mede latência.

**Ordens de grandeza (guia prático):**
- Modelo clássico (XGBoost, sklearn): < 1ms por predição
- CNN pequena (MobileNet): 5–20ms CPU, < 1ms GPU
- BERT-base: 20–50ms CPU, 5–10ms GPU
- GPT-2 (117M): 50–200ms CPU, 10–30ms GPU
- LLM 7B (geração): 500ms–5s dependendo do hardware
- LLM 70B (geração): 5–60s sem optimização

**O que fazer para reduzir latência:**
- Quantization: INT8 reduz ~4x tamanho e ~2x latência
- ONNX Runtime: optimiza grafos de computação
- Batching: agrupar requests aumenta throughput mas aumenta latência individual
- Caching: resultados determinísticos para inputs repetidos (embeddings, por exemplo)
- vLLM / TGI: PagedAttention para LLMs — reduz latência até 10x vs. HuggingFace naive

### 4. Custo Real — O Elefante na Sala dos Papers

Papers não reportam custo de inferência. Produção vive e morre pelo custo.

**Benchmark de custo (2026, ordem de grandeza):**
- 1M tokens (GPT-4): ~$10–30
- 1M tokens (GPT-3.5): ~$1–2
- 1M tokens (Claude 3 Haiku): ~$0.25
- Self-hosted Llama 70B (A100 spot): ~$0.50/hora → ~$0.001 por request de 500 tokens

**Regra de Akita**: nunca use um modelo maior do que o necessário para o task.
Classificação de sentimento não precisa de GPT-4. Precisa de um modelo BERT fine-tuned.

### 5. Logging e Debugging em Produção

Um modelo que falha silenciosamente em produção é o pior cenário.

**O que logar (obrigatório):**
```python
# Cada request de inferência deve logar:
{
    "timestamp": "2026-05-28T14:23:01Z",
    "request_id": "uuid-xxx",
    "model_version": "v2.3.1",
    "input_hash": "sha256:...",  # nunca o input completo se tiver PII
    "prediction": {...},
    "confidence": 0.87,
    "latency_ms": 45,
    "error": null
}
```

**O que NÃO logar:**
- Dados pessoais (GDPR — mesmo que "só para debug")
- API keys, tokens (mesmo que "só para teste")
- Inputs completos de utilizadores sem anonimização

### 6. Versionamento de Modelos — Mais Complexo do Que Parece

Git faz versionamento de código. Modelos precisam de mais:

- **Código** — versionado em git
- **Dados de treino** — versionados em DVC, Delta Lake, ou similar
- **Hyperparameters** — registados em MLflow, W&B
- **Artefacto do modelo** (pesos) — versionados em MLflow Registry, S3 com versionamento
- **Métricas de avaliação** — associadas a cada versão

**Por que importa**: se um modelo degrada em produção, precisas de saber exactamente o que mudou. Sem versionamento de dados + modelo + código, é impossível fazer root cause analysis.

```bash
# Exemplo: MLflow tracking
import mlflow

with mlflow.start_run():
    mlflow.log_params({"learning_rate": 1e-4, "batch_size": 32, "epochs": 10})
    mlflow.log_metrics({"accuracy": 0.923, "f1": 0.918, "latency_ms": 45})
    mlflow.sklearn.log_model(model, "model", registered_model_name="fraud-detector")
```

### 7. A/B Testing de Modelos — Como Validar Mudanças Sem Quebrar Produção

Nunca fazer big bang deployment de um novo modelo.

**Estratégia canónica:**
1. Shadow mode: novo modelo recebe requests mas os resultados não são usados — só logados
2. Canary: 5% do tráfego para novo modelo, 95% para modelo antigo
3. Gradual rollout: 5% → 20% → 50% → 100%, com alertas automáticos de regressão
4. Rollback automático: se métricas caem X% em Y minutos, reverter automaticamente

---

## MLOps — O Que É Real vs. O Que É Hype

### O que funciona em equipas pequenas (1–5 pessoas):
- MLflow local para tracking de experimentos
- DVC para versionamento de dados
- Docker para reproducibilidade
- GitHub Actions para CI/CD
- FastAPI para serving
- PostgreSQL ou SQLite para feature store simples

### O que é overkill para a maioria dos projectos:
- Kubeflow (complexidade de K8s sem necessidade)
- Feast (feature store dedicada — só justificado com 50+ features em produção)
- Ray distributed training (só para modelos que não cabem numa GPU)
- Seldon/KFServing (overkill para < 1M requests/dia)

**Regra de Akita para MLOps**: adicionar um componente apenas quando consegues identificar o problema específico que resolve e quando o custo de operar esse componente é inferior ao custo do problema que resolve.

---

## Arquitectura de Referência — Sistema ML Simples e Robusto

Para dissertações com componente de deployment (avaliação em produção real):

```
[Data Source] → [Preprocessing Pipeline] → [Feature Store (PostgreSQL)]
                                                       ↓
                                              [Training Pipeline]
                                                       ↓
                                              [MLflow Model Registry]
                                                       ↓
                                        [FastAPI Serving (Docker)]
                                                       ↓
                                              [Prediction Logs]
                                                       ↓
                                        [Drift Monitoring (Evidently)]
                                                       ↓
                                           [Retraining Trigger]
```

Esta arquitectura cobre os 7 problemas listados acima. É simples, operável por uma pessoa, e honesta sobre as suas limitações.

---

## Debugging de Modelos em Produção — Checklist

Quando um modelo se comporta de forma inesperada em produção:

```
1. Verificar logs de inferência — há erros silenciosos?
2. Comparar distribuição de inputs produção vs. treino (data drift?)
3. Verificar versão do modelo em deployment (foi feito rollback acidental?)
4. Verificar versão das dependências (numpy, torch, sklearn mudaram?)
5. Analisar exemplos de erros específicos — há padrão?
6. Correr o modelo em modo de debug com exemplos reais que falharam
7. Comparar métricas de produção com métricas de test set
```

---

## O Que Reportar numa Dissertação com Componente de Produção

Se a dissertação inclui deployment real (mesmo que experimental):

**Secção de avaliação deve incluir:**
- Latência P50, P95, P99 (não só média — a média esconde outliers)
- Throughput máximo testado (requests/segundo)
- Custo estimado para escala de produção hipotética
- Comportamento sob carga (degradação graciosa ou falha catastrófica?)
- Resultado de teste de data drift com dados sintéticos ou reais

**O que NÃO fazer:**
- Reportar apenas accuracy no test set e chamar de "avaliação completa"
- "O sistema foi deployado com sucesso" sem métricas de produção
- Ignorar latência por ser "investigação, não produção"

---

## Ceticismo Saudável sobre Ferramentas MLOps

O ecosistema MLOps tem mais ferramentas do que problemas.
Antes de adoptar qualquer ferramenta, responder:

1. **Qual é o problema específico que esta ferramenta resolve?**
2. **O problema existe no meu caso?** (escala, equipa, complexidade)
3. **Qual é o custo de operar esta ferramenta?** (tempo de setup, manutenção, curva de aprendizagem)
4. **Existe solução mais simples?** (um script Python bem escrito pode substituir Airflow para pipelines simples)

Ferramentas que vale sempre a pena:
- `git` — versionamento de código (universal)
- `docker` — reproducibilidade de ambiente (universal)
- `mlflow` (local) — tracking de experimentos (baixo custo, alto valor)

Ferramentas que só valem acima de certa escala:
- Kubernetes (>50 serviços ou >100k requests/hora)
- Feature stores dedicadas (>50 features computadas em tempo real)
- Distributed training (>1 GPU necessária para treinar no tempo disponível)
