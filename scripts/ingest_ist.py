"""
Script de ingestão do IST Scholar e arXiv para a base de conhecimento do Doctor.
Indexa dissertações IST e papers de ML/AI/Cloud dos últimos anos.
"""

import os
import sys
import time
from pathlib import Path

import httpx

# Garantir que o package está no path
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
load_dotenv()


TOPICS_ML_AI = [
    "deep learning neural networks",
    "transformer attention mechanism",
    "federated learning privacy",
    "reinforcement learning optimization",
    "generative adversarial networks",
    "large language models",
    "computer vision image recognition",
    "natural language processing",
    "graph neural networks",
    "diffusion models generation",
]

TOPICS_CLOUD = [
    "cloud computing machine learning deployment",
    "MLOps machine learning operations",
    "kubernetes container orchestration",
    "serverless computing edge",
    "microservices architecture cloud",
]

TOPICS_IST = [
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "cloud computing",
    "neural networks",
    "computer vision",
    "natural language processing",
]


def ingest_arxiv_papers(
    db_path: Path,
    topics: list[str],
    limit_per_topic: int = 10,
    year_from: int = 2020,
    delay: float = 1.0,
) -> int:
    """Ingere papers do arXiv."""
    from doctor.core.academic_search import search_arxiv
    from doctor.memory.db import upsert_paper

    total = 0
    for topic in topics:
        print(f"  arXiv: {topic}")
        try:
            papers = search_arxiv(topic, limit=limit_per_topic)
            for p in papers:
                if (p.get("year") or 0) >= year_from:
                    upsert_paper(db_path, p)
                    total += 1
            print(f"    → {len(papers)} papers")
            time.sleep(delay)
        except Exception as e:
            print(f"    ⚠ Erro: {e}")

    return total


def ingest_semantic_scholar_papers(
    db_path: Path,
    topics: list[str],
    limit_per_topic: int = 10,
    delay: float = 1.5,
) -> int:
    """Ingere papers do Semantic Scholar."""
    from doctor.core.academic_search import search_semantic_scholar
    from doctor.memory.db import upsert_paper

    total = 0
    for topic in topics:
        print(f"  Semantic Scholar: {topic}")
        try:
            papers = search_semantic_scholar(topic, limit=limit_per_topic)
            for p in papers:
                upsert_paper(db_path, p)
                total += 1
            print(f"    → {len(papers)} papers")
            time.sleep(delay)
        except Exception as e:
            print(f"    ⚠ Erro: {e}")

    return total


def ingest_ist_dissertations(
    db_path: Path,
    topics: list[str],
    limit_per_topic: int = 10,
    delay: float = 1.0,
) -> int:
    """Ingere dissertações do IST Scholar."""
    from doctor.core.academic_search import search_ist_scholar
    from doctor.memory.db import upsert_paper

    total = 0
    for topic in topics:
        print(f"  IST Scholar: {topic}")
        try:
            papers = search_ist_scholar(topic, limit=limit_per_topic)
            for p in papers:
                upsert_paper(db_path, p)
                total += 1
            print(f"    → {len(papers)} dissertações")
            time.sleep(delay)
        except Exception as e:
            print(f"    ⚠ Erro: {e}")

    return total


def ingest_fundamental_papers(db_path: Path) -> int:
    """Ingere os papers fundamentais de ML/AI hardcoded."""
    from doctor.core.academic_search import lookup_doi, build_ieee_citation, build_apa_citation, build_bibtex
    from doctor.memory.db import upsert_paper

    FUNDAMENTAL_PAPERS = [
        # Transformers
        {"doi": "10.48550/arXiv.1706.03762", "arxiv_id": "1706.03762",
         "title": "Attention Is All You Need", "authors": "Vaswani, Ashish and Shazeer, Noam and others",
         "year": 2017, "venue": "NeurIPS"},
        {"doi": "10.48550/arXiv.1810.04805", "arxiv_id": "1810.04805",
         "title": "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
         "authors": "Devlin, Jacob and Chang, Ming-Wei and Lee, Kenton and Toutanova, Kristina",
         "year": 2019, "venue": "NAACL-HLT"},
        # ResNet
        {"doi": "10.48550/arXiv.1512.03385", "arxiv_id": "1512.03385",
         "title": "Deep Residual Learning for Image Recognition",
         "authors": "He, Kaiming and Zhang, Xiangyu and Ren, Shaoqing and Sun, Jian",
         "year": 2016, "venue": "CVPR"},
        # GPT-3
        {"doi": "10.48550/arXiv.2005.14165", "arxiv_id": "2005.14165",
         "title": "Language Models are Few-Shot Learners",
         "authors": "Brown, Tom and others", "year": 2020, "venue": "NeurIPS"},
        # Adam
        {"doi": "10.48550/arXiv.1412.6980", "arxiv_id": "1412.6980",
         "title": "Adam: A Method for Stochastic Optimization",
         "authors": "Kingma, Diederik P. and Ba, Jimmy", "year": 2015, "venue": "ICLR"},
        # ViT
        {"doi": "10.48550/arXiv.2010.11929", "arxiv_id": "2010.11929",
         "title": "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale",
         "authors": "Dosovitskiy, Alexey and others", "year": 2021, "venue": "ICLR"},
        # GAN
        {"doi": "10.48550/arXiv.1406.2661", "arxiv_id": "1406.2661",
         "title": "Generative Adversarial Networks",
         "authors": "Goodfellow, Ian and others", "year": 2014, "venue": "NeurIPS"},
        # Diffusion
        {"doi": "10.48550/arXiv.2006.11239", "arxiv_id": "2006.11239",
         "title": "Denoising Diffusion Probabilistic Models",
         "authors": "Ho, Jonathan and Jain, Ajay and Abbeel, Pieter",
         "year": 2020, "venue": "NeurIPS"},
        # PPO
        {"doi": "10.48550/arXiv.1707.06347", "arxiv_id": "1707.06347",
         "title": "Proximal Policy Optimization Algorithms",
         "authors": "Schulman, John and Wolski, Filip and others",
         "year": 2017, "venue": "arXiv"},
        # LeCun Deep Learning
        {"doi": "10.1038/nature14539",
         "title": "Deep Learning", "authors": "LeCun, Yann and Bengio, Yoshua and Hinton, Geoffrey",
         "year": 2015, "venue": "Nature"},
    ]

    total = 0
    for p in FUNDAMENTAL_PAPERS:
        if not p.get("citation_ieee"):
            p["citation_ieee"] = build_ieee_citation(p)
        if not p.get("citation_apa"):
            p["citation_apa"] = build_apa_citation(p)
        if not p.get("bibtex"):
            p["bibtex"] = build_bibtex(p)
        if not p.get("id"):
            p["id"] = f"fundamental_{p.get('arxiv_id', p.get('doi', '')).replace('.', '_').replace('/', '_')}"
        upsert_paper(db_path, p)
        total += 1

    return total


def ingest_all(
    db_path: Path,
    arxiv: bool = True,
    semantic: bool = True,
    ist: bool = True,
    fundamental: bool = True,
    limit: int = 10,
    delay: float = 1.0,
) -> None:
    """Ingestão completa."""
    from doctor.memory.db import init_db
    from doctor.knowledge.retriever import load_wiki_into_db

    print("=" * 60)
    print("Doctor — Ingestão de Conhecimento Académico")
    print("=" * 60)

    init_db(db_path)
    load_wiki_into_db(db_path)
    print("✓ Base de dados inicializada")

    total = 0

    if fundamental:
        print("\n[1/4] Papers fundamentais de ML/AI...")
        n = ingest_fundamental_papers(db_path)
        print(f"  → {n} papers fundamentais indexados")
        total += n

    if arxiv:
        print("\n[2/4] arXiv — ML/AI (2020-presente)...")
        n = ingest_arxiv_papers(db_path, TOPICS_ML_AI[:5], limit_per_topic=limit, delay=delay)
        print(f"  → {n} papers arXiv indexados")
        total += n

    if semantic:
        print("\n[3/4] Semantic Scholar — Cloud/MLOps...")
        n = ingest_semantic_scholar_papers(db_path, TOPICS_CLOUD[:3], limit_per_topic=limit, delay=delay)
        print(f"  → {n} papers Semantic Scholar indexados")
        total += n

    if ist:
        print("\n[4/4] IST Scholar — dissertações IST...")
        n = ingest_ist_dissertations(db_path, TOPICS_IST[:5], limit_per_topic=limit, delay=delay)
        print(f"  → {n} dissertações IST indexadas")
        total += n

    print(f"\n{'='*60}")
    print(f"✅ Ingestão completa: {total} itens indexados")
    print(f"{'='*60}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Ingerir conhecimento académico para o Doctor")
    parser.add_argument("--limit", type=int, default=10, help="Papers por tópico")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay entre requests")
    parser.add_argument("--no-arxiv", action="store_true")
    parser.add_argument("--no-semantic", action="store_true")
    parser.add_argument("--no-ist", action="store_true")
    parser.add_argument("--no-fundamental", action="store_true")
    args = parser.parse_args()

    memory_dir = Path(os.path.expanduser(os.environ.get("DOCTOR_MEMORY_DIR", "~/.doctor")))
    db_path = memory_dir / "doctor.db"

    ingest_all(
        db_path=db_path,
        arxiv=not args.no_arxiv,
        semantic=not args.no_semantic,
        ist=not args.no_ist,
        fundamental=not args.no_fundamental,
        limit=args.limit,
        delay=args.delay,
    )
