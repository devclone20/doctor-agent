# Normas e Padrões IST — Instituto Superior Técnico, Lisboa

## Sobre o IST

O Instituto Superior Técnico (IST) da Universidade de Lisboa, campus de Alameda, é a principal escola de engenharia e tecnologia de Portugal. Os seus padrões académicos estão entre os mais exigentes da Europa.

## Estrutura de uma Dissertação de Mestrado IST

### Ordem obrigatória dos elementos:
1. **Capa** — Título, autor, grau, curso, data, logótipo IST
2. **Página de rosto** — Título, autor, orientador, co-orientador, júri
3. **Dedicatória** (opcional)
4. **Agradecimentos** (Acknowledgements)
5. **Resumo** (Português — máx. 250 palavras)
6. **Abstract** (Inglês — máx. 250 palavras) + **Keywords** (5-8 palavras)
7. **Índice** (Table of Contents)
8. **Lista de Figuras** (List of Figures)
9. **Lista de Tabelas** (List of Tables)
10. **Lista de Acrónimos** (List of Acronyms)
11. **Capítulos** (ver estrutura padrão abaixo)
12. **Bibliografia** (References)
13. **Apêndices** (Appendices) — material suplementar

### Estrutura padrão de capítulos:

#### Capítulo 1 — Introdução
- 1.1 Motivação
- 1.2 Problema e Objectivos
- 1.3 Contribuições
- 1.4 Estrutura da Dissertação

#### Capítulo 2 — Background e Estado da Arte
- 2.1 Conceitos fundamentais
- 2.2 Trabalho relacionado
- 2.3 Comparação crítica

#### Capítulo 3 — Abordagem / Arquitectura / Metodologia
- 3.1 Visão geral da solução
- 3.2 Arquitectura do sistema
- 3.3 Decisões de design

#### Capítulo 4 — Implementação
- 4.1 Ambiente de desenvolvimento
- 4.2 Detalhes de implementação
- 4.3 Desafios e soluções

#### Capítulo 5 — Avaliação / Resultados Experimentais
- 5.1 Setup experimental
- 5.2 Métricas e benchmarks
- 5.3 Resultados e discussão

#### Capítulo 6 — Conclusão e Trabalho Futuro
- 6.1 Sumário das contribuições
- 6.2 Limitações
- 6.3 Trabalho futuro

## Formatação IST

### Texto:
- Fonte: 12pt (body text)
- Margens: 2.5 cm em todos os lados
- Espaçamento: 1.5 linhas (ou duplo em versão prévia)
- Idiomas aceites: Português ou Inglês

### Figuras e Tabelas:
- Todas as figuras têm legenda abaixo: "Figura X.Y: Descrição."
- Todas as tabelas têm título acima: "Tabela X.Y: Descrição."
- Todas as figuras e tabelas devem ser referenciadas no texto

### Equações:
- Numeradas: (X.Y) à direita
- Variáveis em itálico
- Vectores/matrizes a bold

## Template LaTeX Oficial IST

- Template: IST-UL MSc Dissertation v5.0 (Outubro 2025)
- Engine: LuaLaTeX
- Autor: Prof. Dr. Rui Santos Cruz
- Disponível: https://www.overleaf.com/latex/templates/ist-ul-msc-dissertation/wrhbmbvzpttw
- Suporta: draft/final mode, PT/EN, track changes, glossários, acrónimos

## Estilo de Citações IST (Engenharia)

Engenharia Informática e de Computadores usa o estilo **IEEE**:
- Referências numeradas: [1], [2], [3], ...
- No texto: "segundo [1], ...", "como proposto em [1][2]"
- Na bibliography: autores, título, conferência/journal, volume, páginas, ano

## Processo de Submissão

1. Submeter via Fénix (plataforma académica IST)
2. Aprovação do orientador
3. Defesa perante júri
4. Disponibilização no repositório Scholar IST

## Repositório IST Scholar

- URL: https://scholar.tecnico.ulisboa.pt
- API: https://scholar.tecnico.ulisboa.pt/api/
- Contém: ~24.000 dissertações de mestrado + ~8.000 teses de doutoramento
- Formato de busca: ?q=QUERY&domain=records&sort=_score:desc&page=1&perPage=10
