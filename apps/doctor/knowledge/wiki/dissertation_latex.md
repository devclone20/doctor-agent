# LaTeX para Dissertações IST

## Template Oficial IST v5.0

- URL: https://www.overleaf.com/latex/templates/ist-ul-msc-dissertation/wrhbmbvzpttw
- Engine: LuaLaTeX (não pdflatex)
- Versão: 5.0 (Outubro 2025)
- Autor: Prof. Dr. Rui Santos Cruz
- Licença: CC BY 4.0

## Estrutura do template:

```
main.tex              ← ficheiro principal (carrega o REAL MAIN)
ist_thesis.tex        ← ficheiro real de configuração
chapters/
    chapter1.tex      ← Introduction
    chapter2.tex      ← Background
    ...
figures/              ← figuras (PDF, PNG, SVG)
bibliography.bib      ← referências BibTeX
```

## Pacotes LaTeX Essenciais (incluídos no template IST)

```latex
% Lingua e encoding
\usepackage[utf8]{inputenc}     % apenas pdflatex
\usepackage[T1]{fontenc}
\usepackage[portuguese,english]{babel}

% Matemática
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}

% Figuras
\usepackage{graphicx}
\usepackage{subcaption}
\usepackage{float}

% Tabelas
\usepackage{booktabs}           % \toprule, \midrule, \bottomrule
\usepackage{multirow}
\usepackage{tabularx}

% Código fonte
\usepackage{listings}
\usepackage{minted}             % syntax highlight (requer Python pygments)

% Hiperlinks
\usepackage{hyperref}
\usepackage{cleveref}           % \cref{fig:x} → "Figure 1"

% Acrónimos e glossário
\usepackage{acronym}
\usepackage[toc]{glossaries}

% Algoritmos
\usepackage{algorithm}
\usepackage{algpseudocode}

% Citações IEEE
\usepackage[style=ieee]{biblatex}
% ou: \bibliographystyle{IEEEtran}
```

## Estrutura main.tex típica IST

```latex
\documentclass[12pt,a4paper,twoside]{report}

% --- Configuração ---
\newcommand{\thetitle}{Título da Dissertação}
\newcommand{\theauthor}{Nome Completo do Autor}
\newcommand{\theyear}{2025}
\newcommand{\thedegree}{Mestrado em Engenharia Informática e de Computadores}

% --- Pacotes ---
\input{packages}

\begin{document}

% --- Frente ---
\input{frontmatter/cover}
\input{frontmatter/abstract_pt}
\input{frontmatter/abstract_en}
\tableofcontents
\listoffigures
\listoftables
\input{frontmatter/acronyms}

% --- Capítulos ---
\input{chapters/chapter1_introduction}
\input{chapters/chapter2_background}
\input{chapters/chapter3_approach}
\input{chapters/chapter4_implementation}
\input{chapters/chapter5_evaluation}
\input{chapters/chapter6_conclusion}

% --- Referências ---
\printbibliography[heading=bibintoc]

% --- Apêndices ---
\appendix
\input{appendices/appendix_a}

\end{document}
```

## Comandos LaTeX Frequentes

### Figuras:
```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{figures/architecture.pdf}
    \caption{Arquitectura geral do sistema proposto. Os componentes principais são...}
    \label{fig:architecture}
\end{figure}
```

### Tabelas (estilo IEEE):
```latex
\begin{table}[htbp]
    \centering
    \caption{Comparação de resultados no dataset X.}
    \label{tab:results}
    \begin{tabular}{lccc}
        \toprule
        \textbf{Método} & \textbf{Accuracy (\%)} & \textbf{F1} & \textbf{Latência (ms)} \\
        \midrule
        Baseline [1] & 82.3 & 0.81 & 45 \\
        Método A [2] & 85.1 & 0.84 & 52 \\
        \textbf{Nosso método} & \textbf{88.7} & \textbf{0.87} & \textbf{38} \\
        \bottomrule
    \end{tabular}
\end{table}
```

### Equações:
```latex
% Inline
A função de atenção é definida como $\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$.

% Display com número
\begin{equation}
    \mathcal{L}(\theta) = -\frac{1}{N}\sum_{i=1}^{N} y_i \log \hat{y}_i
    \label{eq:cross_entropy}
\end{equation}
```

### Algoritmos:
```latex
\begin{algorithm}[htbp]
\caption{Algoritmo de treino}
\label{alg:training}
\begin{algorithmic}[1]
\Require Dataset $\mathcal{D}$, learning rate $\alpha$, epochs $E$
\For{$e = 1$ to $E$}
    \For{each batch $(X, y) \in \mathcal{D}$}
        \State $\hat{y} \leftarrow f_\theta(X)$
        \State $\mathcal{L} \leftarrow \text{CrossEntropy}(\hat{y}, y)$
        \State $\theta \leftarrow \theta - \alpha \nabla_\theta \mathcal{L}$
    \EndFor
\EndFor
\end{algorithmic}
\end{algorithm}
```

### Acrónimos:
```latex
% No preambulo:
\acrodef{CNN}{Convolutional Neural Network}
\acrodef{LSTM}{Long Short-Term Memory}
\acrodef{GAN}{Generative Adversarial Network}

% No texto (1ª vez expande; depois abrevia):
The \ac{CNN} architecture was first proposed...
% → "The Convolutional Neural Network (CNN) architecture..."
% → "The CNN architecture..." (nas seguintes)
```

## BibTeX Entries Comuns

```bibtex
% Artigo em conferência
@inproceedings{vaswani2017attention,
    title     = {Attention Is All You Need},
    author    = {Vaswani, Ashish and Shazeer, Noam and Parmar, Niki
                 and Uszkoreit, Jakob and Jones, Llion and Gomez, Aidan N.
                 and Kaiser, {\L}ukasz and Polosukhin, Illia},
    booktitle = {Advances in Neural Information Processing Systems},
    volume    = {30},
    year      = {2017},
    url       = {https://arxiv.org/abs/1706.03762}
}

% Artigo em journal
@article{lecun2015deep,
    title   = {Deep learning},
    author  = {LeCun, Yann and Bengio, Yoshua and Hinton, Geoffrey},
    journal = {Nature},
    volume  = {521},
    number  = {7553},
    pages   = {436--444},
    year    = {2015},
    doi     = {10.1038/nature14539}
}

% Dissertação IST
@mastersthesis{author2024title,
    title  = {Título da Dissertação},
    author = {Apelido, Nome},
    school = {Instituto Superior Técnico, Universidade de Lisboa},
    year   = {2024},
    url    = {https://scholar.tecnico.ulisboa.pt/...}
}

% Preprint arXiv
@misc{brown2020gpt3,
    title         = {Language Models are Few-Shot Learners},
    author        = {Brown, Tom and others},
    year          = {2020},
    eprint        = {2005.14165},
    archivePrefix = {arXiv},
    primaryClass  = {cs.CL}
}
```

## Compilação LuaLaTeX (ordem correcta):

```bash
lualatex main.tex
biber main        # ou bibtex main
lualatex main.tex
lualatex main.tex
```
