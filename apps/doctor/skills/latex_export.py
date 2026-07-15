"""
Skill de exportação LaTeX para dissertações IST.
Converte conteúdo Markdown em estrutura LaTeX IST-compatível.
"""

import re

# Preâmbulo LaTeX fixo — construído como string literal para evitar conflitos
# com f-string e raw-string (backslashes + chaves LaTeX).
_PREAMBLE_TEMPLATE = r"""% IST-DEI Dissertation Template — gerado por Doctor Agent
% Padrão: Instituto Superior Técnico, Universidade de Lisboa
% Tipo: __TYPE_LABEL__

\documentclass[12pt,a4paper]{article}

% --- Pacotes base -------------------------------------------------------------
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[portuguese,english]{babel}
\usepackage{helvet}           % Helvetica ~ Arial (norma IST)
\renewcommand{\familydefault}{\sfdefault}

% --- Layout -------------------------------------------------------------------
\usepackage[
  top=2.5cm, bottom=2.5cm,
  left=2.5cm, right=2.5cm
]{geometry}
\usepackage{setspace}
\onehalfspacing               % 1.5 linhas (norma IST)

% --- Tipografia ---------------------------------------------------------------
\usepackage{microtype}
\usepackage{parskip}
\usepackage{titlesec}
\titleformat{\section}{\large\bfseries}{\thesection}{1em}{}
\titleformat{\subsection}{\normalsize\bfseries}{\thesubsection}{1em}{}

% --- Figuras e tabelas --------------------------------------------------------
\usepackage{graphicx}
\usepackage{float}
\usepackage{booktabs}
\usepackage{caption}
\usepackage{subcaption}
\usepackage{array}

% --- Matemática ---------------------------------------------------------------
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}

% --- Algoritmos ---------------------------------------------------------------
\usepackage{algorithm}
\usepackage{algpseudocode}

% --- Código fonte -------------------------------------------------------------
\usepackage{listings}
\usepackage{xcolor}
\lstset{
  basicstyle=\ttfamily\small,
  breaklines=true,
  frame=single,
  numbers=left,
  numberstyle=\tiny,
  keywordstyle=\color{blue},
  commentstyle=\color{gray},
  stringstyle=\color{teal},
}

% --- Hiperligações ------------------------------------------------------------
\usepackage[
  colorlinks=true,
  linkcolor=black,
  citecolor=black,
  urlcolor=blue,
  bookmarks=true,
]{hyperref}

% --- Citações IEEE ------------------------------------------------------------
\usepackage[
  style=ieee,
  backend=biber,
  sorting=none,
]{biblatex}
\addbibresource{references.bib}

% --- Metadados (preencher) ----------------------------------------------------
\newcommand{\dissertationtitle}{Título da Dissertação}
\newcommand{\authorname}{Nome do Autor}
\newcommand{\supervisorname}{Nome do Orientador}
\newcommand{\degreename}{__TYPE_LABEL__}
\newcommand{\coursename}{Mestrado em Engenharia Informática e de Computadores}
\newcommand{\thesisyear}{\the\year}
"""

_COVER_PAGE = r"""% --- Capa IST ----------------------------------------------------------------
\begin{titlepage}
  \centering
  \vspace*{1cm}
  {\large\textbf{Instituto Superior Técnico}\\
   Universidade de Lisboa\par}
  \vspace{2cm}
  {\LARGE\textbf{\dissertationtitle}\par}
  \vspace{2cm}
  {\large\authorname\par}
  \vspace{1.5cm}
  {\normalsize\degreename\par}
  {\normalsize\coursename\par}
  \vfill
  {\normalsize Orientador: \supervisorname\par}
  \vspace{1cm}
  {\normalsize Lisboa, \thesisyear\par}
\end{titlepage}
\clearpage

"""


def get_ist_latex_preamble(doc_type: str = "msc") -> str:
    """
    Retorna o preâmbulo LaTeX padrão IST para o tipo de documento.
    doc_type: "msc", "phd", "bsc", "article"
    """
    type_labels = {
        "msc": "Dissertação de Mestrado",
        "phd": "Tese de Doutoramento",
        "bsc": "Trabalho de Licenciatura",
        "article": "Artigo Científico",
    }
    type_label = type_labels.get(doc_type, "Dissertação")
    return _PREAMBLE_TEMPLATE.replace("__TYPE_LABEL__", type_label)


def markdown_to_latex_structure(content: str) -> str:
    """
    Converte Markdown em corpo LaTeX.
    Trata: headings, bold, italic, código inline, listas, citações [N].
    """
    lines = content.split("\n")
    out: list[str] = []

    for line in lines:
        # Headings
        if line.startswith("#### "):
            out.append(r"\paragraph{" + _escape_latex(line[5:]) + "}")
            continue
        if line.startswith("### "):
            out.append(r"\subsubsection{" + _escape_latex(line[4:]) + "}")
            continue
        if line.startswith("## "):
            out.append(r"\subsection{" + _escape_latex(line[3:]) + "}")
            continue
        if line.startswith("# "):
            out.append(r"\section{" + _escape_latex(line[2:]) + "}")
            continue

        # Blocos de código (fenced — marcador de abertura e fecho separados)
        if line.startswith("```"):
            lang = line[3:].strip() or "text"
            if lang:
                out.append(r"\begin{lstlisting}" + f"[language={lang}]")
            else:
                out.append(r"\end{lstlisting}")
            continue

        # Listas não ordenadas (emitir ambiente por item — simplificado)
        if line.startswith("- ") or line.startswith("* "):
            out.append(r"\begin{itemize}")
            out.append(r"  \item " + _inline_latex(line[2:]))
            out.append(r"\end{itemize}")
            continue

        # Listas numeradas
        if re.match(r"^\d+\. ", line):
            text = re.sub(r"^\d+\. ", "", line)
            out.append(r"\begin{enumerate}")
            out.append(r"  \item " + _inline_latex(text))
            out.append(r"\end{enumerate}")
            continue

        # Linha em branco
        if not line.strip():
            out.append("")
            continue

        out.append(_inline_latex(line))

    return "\n".join(out)


def wrap_in_latex_document(body: str, doc_type: str = "msc") -> str:
    """
    Envolve o corpo numa estrutura LaTeX IST completa com capa e estrutura de documento.
    """
    preamble = get_ist_latex_preamble(doc_type)
    return (
        preamble
        + "\n\\begin{document}\n\n"
        + _COVER_PAGE
        + "\\tableofcontents\n\\newpage\n\n"
        + body
        + "\n\n\\printbibliography[heading=bibintoc,title={Referências Bibliográficas}]\n\n"
        + "\\end{document}\n"
    )


# --- Auxiliares internos ------------------------------------------------------

_LATEX_SPECIAL: dict[str, str] = {
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}


def _escape_latex(text: str) -> str:
    """Escapa caracteres especiais LaTeX num texto simples."""
    result: list[str] = []
    for ch in text:
        result.append(_LATEX_SPECIAL.get(ch, ch))
    return "".join(result)


def _inline_latex(text: str) -> str:
    """Converte markdown inline (bold, italic, código, citações) para LaTeX."""
    # Citações IEEE [1], [2,3]
    text = re.sub(
        r"\[(\d+(?:,\s*\d+)*)\]",
        lambda m: r"\cite{" + m.group(1).replace(" ", "") + "}",
        text,
    )
    # Bold
    text = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", text)
    # Italic
    text = re.sub(r"\*(.+?)\*", r"\\textit{\1}", text)
    # Inline code
    text = re.sub(r"`(.+?)`", r"\\texttt{\1}", text)
    return text
