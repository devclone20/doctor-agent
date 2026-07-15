"""
Skill de revisão e anotação de trabalhos académicos.
"""


def get_review_prompt(
    content: str,
    doc_type: str = "dissertation",
    review_type: str = "full",
    focus: str = "",
) -> str:
    """
    Gera prompt para revisão completa de um trabalho académico.

    content: texto do trabalho a rever
    doc_type: "dissertation", "article", "abstract", "introduction", etc.
    review_type: "full", "structure", "language", "citations", "technical"
    focus: aspecto específico a focar
    """
    review_guides = {
        "full": """
Faz uma revisão completa e estruturada, organizada nas seguintes categorias:

## 1. Estrutura e Organização
- A estrutura segue o padrão IST/IEEE?
- Os capítulos/secções têm a extensão adequada?
- O fluxo lógico está correcto?
- Há secções em falta?

## 2. Conteúdo Técnico
- Os conceitos estão correctamente explicados?
- As afirmações têm suporte bibliográfico?
- A metodologia está suficientemente detalhada?
- Os resultados são apresentados com rigor?

## 3. Citações e Referências
- As citações estão no formato IEEE correcto?
- Todas as afirmações relevantes têm citação?
- A bibliografia está completa e correctamente formatada?
- Há referências em falta ou incorrectas?

## 4. Qualidade da Escrita
- A linguagem é precisa e não ambígua?
- Há erros gramaticais ou de estilo académico?
- As frases são demasiado longas ou complexas?
- O tom é adequado para trabalho académico?

## 5. Figuras, Tabelas e Equações
- As figuras têm legenda adequada?
- As tabelas têm título e são referenciadas no texto?
- As equações estão numeradas?
- O material visual suporta o texto?

## 6. Resumo da Revisão
- ⚠️ Crítico (deve ser corrigido antes de submeter)
- 🟡 Importante (melhoria significativa)
- 💡 Sugestão (opcional mas recomendado)
- ✅ Pontos fortes
""",
        "structure": """
Revê especificamente a estrutura e organização:
- A estrutura segue o padrão IST?
- Os capítulos têm a extensão e profundidade adequadas?
- A progressão lógica está correcta?
- O que está em falta ou fora de lugar?
""",
        "citations": """
Faz uma auditoria completa das citações e referências:
- Identifica todas as afirmações sem citação que deveriam ter
- Verifica o formato IEEE de cada referência
- Identifica referências incorrectas ou incompletas
- Sugere referências adicionais relevantes para os temas abordados
""",
        "language": """
Revê especificamente a qualidade da escrita:
- Identifica erros gramaticais, de sintaxe ou estilo
- Sugere reformulações mais precisas ou académicas
- Identifica linguagem imprecisa ou ambígua
- Verifica consistência terminológica
""",
        "technical": """
Faz uma revisão técnica profunda:
- Os conceitos técnicos estão correctamente explicados?
- A metodologia é sound e reproduzível?
- Os resultados são apresentados com rigor estatístico adequado?
- Há erros técnicos ou simplificações excessivas?
""",
    }

    guide = review_guides.get(review_type, review_guides["full"])
    focus_part = f"\n\nFoco especial em: {focus}" if focus else ""
    type_map = {
        "dissertation": "Dissertação de Mestrado IST",
        "article": "Artigo Científico",
        "abstract": "Abstract",
        "introduction": "Secção de Introdução",
        "background": "Estado da Arte",
    }
    type_name = type_map.get(doc_type, doc_type)

    return f"""Revê este {type_name} de acordo com os padrões IST e IEEE:

{guide}
{focus_part}

---
## Trabalho a rever:

{content[:8000]}
---

Para cada ponto de revisão, indica:
- Localização no texto (secção, parágrafo, ou citar directamente)
- Problema identificado
- Sugestão concreta de correcção

Termina com um julgamento global: está pronto para submeter? O que é urgente?
"""


def get_annotation_prompt(content: str, annotation_style: str = "academic") -> str:
    """
    Gera prompt para anotações inline num texto académico.
    Retorna o texto com comentários inseridos.
    """
    return f"""Adiciona anotações académicas ao texto seguinte.

Para cada parágrafo ou frase que precisar de atenção, insere um comentário no formato:
> **[DOCTOR]** Observação: ... | Sugestão: ...

Tipos de anotações:
- **[DOCTOR - CITAÇÃO]** Falta referência bibliográfica aqui
- **[DOCTOR - ESTRUTURA]** Este parágrafo deveria ir para outra secção
- **[DOCTOR - TÉCNICO]** Afirmação imprecisa — explicar melhor
- **[DOCTOR - LÍNGUA]** Reformular: ...
- **[DOCTOR - BOM]** Esta parte está bem escrita/fundamentada

---
{content[:6000]}
---

Retorna o texto original intercalado com as tuas anotações.
"""
