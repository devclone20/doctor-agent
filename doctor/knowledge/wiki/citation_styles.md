# Estilos de Citação Científica

## IEEE (Padrão IST Engenharia Informática)

### Formato no texto:
- Referência simples: [1]
- Múltiplas: [1], [2], [3] ou [1]–[3]
- Com página: [1, p. 45]
- Integrado: "Smith et al. [1] demonstraram que..."

### Formato na bibliografia:

#### Artigo em conferência (IEEE):
[N] A. B. Sobrenome, "Título do artigo," in *Proc. Nome da Conferência (SIGLA)*, Cidade, País, Ano, pp. XX–YY.

Exemplo:
[1] Y. LeCun, Y. Bengio, and G. Hinton, "Deep learning," *Nature*, vol. 521, pp. 436–444, May 2015.

#### Artigo em journal:
[N] A. B. Sobrenome, "Título," *Nome do Journal*, vol. X, no. Y, pp. XX–YY, Mês Ano.

#### Livro:
[N] A. B. Sobrenome, *Título do Livro*, Xª ed. Cidade: Editora, Ano.

#### Capítulo de livro:
[N] A. B. Sobrenome, "Título do capítulo," in *Título do Livro*, A. Editor, Ed. Cidade: Editora, Ano, pp. XX–YY.

#### Dissertação/Tese:
[N] A. B. Sobrenome, "Título," Ph.D. dissertation / M.S. thesis, Dept. Nome, Universidade, Cidade, País, Ano.

#### Relatório técnico:
[N] A. B. Sobrenome, "Título," Nome da Empresa/Inst., Cidade, Rep. Técnico N.º XX, Ano.

#### Recurso online:
[N] A. B. Sobrenome, "Título," *Nome do Site*, Data publicação. [Online]. Disponível: URL. [Acedido: DD Mês AAAA].

#### Preprint (arXiv):
[N] A. B. Sobrenome, "Título," arXiv preprint arXiv:XXXX.XXXXX, Ano.

---

## APA 7ª Edição

### Formato no texto:
- (Sobrenome, Ano)
- (Sobrenome & Sobrenome, Ano)
- (Sobrenome et al., Ano) — 3+ autores
- Integrado: Smith e Jones (2023) demonstraram...

### Formato na bibliografia:

#### Artigo:
Sobrenome, A. B., & Sobrenome, C. D. (Ano). Título do artigo. *Nome do Journal*, *Volume*(Número), pp–pp. https://doi.org/XXXX

#### Livro:
Sobrenome, A. B. (Ano). *Título do livro* (Xª ed.). Editora.

#### Capítulo:
Sobrenome, A. B. (Ano). Título do capítulo. In A. Editor & B. Editor (Eds.), *Título do livro* (pp. XX–YY). Editora.

#### Recurso online:
Sobrenome, A. B. (Ano, Mês DD). Título. *Nome do Site*. URL

---

## Vancouver (Biomédico)

### Formato no texto:
- Número sobrescrito: texto¹, texto¹˒²
- Numeração por ordem de aparecimento

### Formato na bibliografia:
1. Sobrenome AB, Sobrenome CD. Título do artigo. Nome Journal. Ano;Volume(Número):pp-pp.

---

## Identificadores Importantes

### DOI (Digital Object Identifier):
- Formato: https://doi.org/10.XXXX/XXXXXX
- Exemplo: https://doi.org/10.1038/nature14539
- CrossRef API para lookup: https://api.crossref.org/works/10.XXXX/XXXXXX

### arXiv ID:
- Formato: arXiv:YYMM.NNNNN
- Exemplo: arXiv:1706.03762 (Attention Is All You Need)
- URL: https://arxiv.org/abs/1706.03762

### PubMed ID (PMID):
- Lookup: https://pubmed.ncbi.nlm.nih.gov/PMID/

---

## Como Citar Tipos Especiais

### Dataset:
[N] A. B. Sobrenome, "Nome do Dataset," Repositório, Ano. [Online]. Disponível: URL.

### Software/GitHub:
[N] A. B. Sobrenome, *Nome do Software* (versão X.Y). GitHub, Ano. [Online]. Disponível: https://github.com/...

### Standard/Norma:
[N] Nome da Organização, *Título da Norma*, Standard N.º XXXX, Ano.

### Comunicação pessoal:
(Não se usa em IEEE — citar apenas fontes publicadas)

---

## Ferramentas de Gestão Bibliográfica

- **Zotero** — gratuito, exporta IEEE/APA/BibTeX
- **Mendeley** — gratuito com limites
- **BibTeX** — formato padrão LaTeX
- **JabRef** — GUI para BibTeX

### Exemplo BibTeX (IEEE):
```bibtex
@article{vaswani2017attention,
  title={Attention is all you need},
  author={Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and others},
  journal={Advances in neural information processing systems},
  volume={30},
  year={2017}
}
```
