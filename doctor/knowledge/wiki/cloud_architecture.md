# Cloud Architecture e MLOps — Conhecimento Core

## Cloud Providers Principais

### AWS (Amazon Web Services)
- **Compute**: EC2 (VMs), Lambda (serverless), ECS/EKS (containers)
- **Storage**: S3 (object), EBS (block), EFS (file), Glacier (archival)
- **ML**: SageMaker (treino, deploy, pipelines), Bedrock (LLMs managed)
- **Data**: Redshift (DW), RDS/Aurora, DynamoDB (NoSQL), Kinesis (streaming)
- **Networking**: VPC, CloudFront (CDN), Route 53, ALB/NLB

### GCP (Google Cloud Platform)
- **Compute**: Compute Engine, Cloud Run (serverless containers), GKE
- **Storage**: Cloud Storage (GCS), Bigtable, Firestore, BigQuery (analytics)
- **ML**: Vertex AI (end-to-end MLOps), AutoML, TPU v4/v5
- **Data**: Dataflow (Apache Beam), Pub/Sub (messaging), Dataproc (Spark)

### Azure (Microsoft)
- **Compute**: Azure VMs, Azure Functions, AKS, Container Instances
- **Storage**: Blob Storage, Azure SQL, Cosmos DB
- **ML**: Azure Machine Learning, Azure OpenAI Service
- **Data**: Synapse Analytics, Event Hub, HDInsight

---

## MLOps — Machine Learning Operations

### Definição:
MLOps = DevOps + ML. Práticas para levar modelos de investigação para produção de forma reproduzível, monitorizada e escalável.

### Pipeline MLOps (ciclo completo):
1. **Data Ingestion** — colecção, validação, versioning (DVC, Delta Lake)
2. **Feature Engineering** — feature stores (Feast, Tecton, Hopsworks)
3. **Model Training** — distributed training (Horovod, DeepSpeed, FSDP)
4. **Experiment Tracking** — MLflow, W&B, Comet
5. **Model Registry** — MLflow Registry, SageMaker Model Registry
6. **CI/CD for ML** — GitHub Actions, GitLab CI, automated testing
7. **Model Deployment** — REST API, batch, streaming, edge
8. **Monitoring** — data drift, model drift, performance degradation
9. **Feedback Loop** — retraining triggers, active learning

### Tools Ecosystem:
- **Orchestration**: Kubeflow Pipelines, Apache Airflow, Prefect, Metaflow, ZenML
- **Serving**: TorchServe, TF Serving, Triton Inference Server, BentoML, Seldon
- **Feature Store**: Feast, Hopsworks, Tecton
- **Data Quality**: Great Expectations, Evidently AI, NannyML
- **Containerization**: Docker, containerd, BuildKit

---

## Kubernetes e Containerization

### Conceitos Core:
- **Pod** — unidade mínima (1+ containers)
- **Deployment** — declarative pod management, rolling updates
- **Service** — expose pods (ClusterIP, NodePort, LoadBalancer)
- **Ingress** — HTTP routing, TLS termination
- **ConfigMap / Secret** — configuração e segredos
- **PersistentVolume (PV/PVC)** — armazenamento persistente
- **Namespace** — isolamento lógico

### ML on Kubernetes:
- **Kubeflow** — ML workflows no K8s
- **Ray Cluster** — distributed Python, Ray Serve para deployment
- **Spark on K8s** — big data processing
- **GPU Scheduling** — NVIDIA device plugin, GPU sharing

### Helm:
- Package manager para Kubernetes
- Charts para instalar aplicações complexas

---

## Deployment de Modelos ML

### REST API (padrão mais comum):
```python
# FastAPI + uvicorn
from fastapi import FastAPI
app = FastAPI()

@app.post("/predict")
async def predict(request: PredictRequest):
    result = model.predict(request.features)
    return {"prediction": result}
```

### Padrões de Serving:
- **Online serving** — low-latency (<100ms), single request
- **Batch prediction** — high throughput, processar grandes volumes
- **Streaming** — Kafka, Kinesis, Pub/Sub para real-time
- **Edge/On-device** — ONNX, CoreML, TFLite, OpenVINO

### Optimização de Inferência:
- **Quantization** — INT8, FP16, GGUF (reduz tamanho e latência)
- **Pruning** — remoção de pesos não essenciais
- **Distillation** — modelo pequeno aprende de modelo grande
- **TensorRT, ONNX Runtime** — optimização de grafo de computação
- **vLLM, TGI** — serving eficiente de LLMs (PagedAttention, continuous batching)

---

## Infrastructure as Code (IaC)

### Terraform:
- Declarativo, multi-cloud, state management
- Providers: AWS, GCP, Azure, Kubernetes, Datadog

### Pulumi:
- IaC em linguagens reais (Python, TypeScript)

### CloudFormation / ARM / Deployment Manager:
- IaC nativo dos respectivos cloud providers

---

## Segurança em Cloud ML

### Princípios:
- **Zero Trust** — verificar sempre, nunca confiar implicitamente
- **Least Privilege** — IAM roles mínimas necessárias
- **Encryption at rest + in transit** — AES-256, TLS 1.3
- **Secrets Management** — AWS Secrets Manager, HashiCorp Vault, GCP Secret Manager
- **Network isolation** — VPC, private subnets, security groups

### ML-specific Security:
- Model poisoning attacks
- Data privacy (GDPR compliance, differential privacy)
- Model IP protection (watermarking, obfuscation)
- Adversarial examples defense

---

## Cost Optimization

### Estratégias:
- **Spot/Preemptible instances** — até 90% mais barato para treino
- **Auto-scaling** — scale to zero quando não há tráfego
- **Reserved instances** — desconto para workloads previsíveis
- **Multi-region** — seleccionar regiões mais baratas
- **Data lifecycle** — tiering automático S3 (Standard → IA → Glacier)

### GPU Cost Management:
- AWS: p3.2xlarge (V100), p4d (A100), g5 (A10G)
- GCP: a2-highgpu (A100), g2 (L4)
- Spot training com checkpointing para tolerância a falhas

---

## Arquitecturas de Referência para Dissertações

### LLM Fine-tuning Pipeline:
Data → Preprocessing → LoRA Training (A100) → Evaluation → Model Registry → Serving (vLLM) → Monitoring

### Real-time ML System:
API → Feature Store → Online Model → Prediction → Logging → Batch Retraining → Model Update

### Federated Learning System:
Central Server ↔ Edge Clients (privacy-preserving aggregation, FedAvg, FedProx)
