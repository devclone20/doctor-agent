# IST Scholar — Plataforma de Publicação Institucional

## O que é

**URL:** https://scholar.projects.dsi.tecnico.ulisboa.pt

Scholar é o **repositório institucional do Instituto Superior Técnico** (Técnico Lisboa, Universidade de Lisboa). O seu propósito é recolher, preservar e disseminar a produção científica do IST. Funciona num modelo de *self-archiving*: os investigadores depositam individualmente os seus trabalhos.

**Quem tem acesso:**
> "All users linked to IST (with Técnico ID and completed admission process) have an account in Scholar."

Todos os estudantes e docentes do IST com Técnico ID têm conta automática. Não é necessário criar conta.

---

## Como Publicar — Passo a Passo

### Acesso
1. Vai a https://scholar.projects.dsi.tecnico.ulisboa.pt
2. Clica no botão azul **Login** (canto superior direito)
3. Autentica com as credenciais institucionais do Técnico (Fénix/IST ID)

### Submissão
4. Clica na tua **foto de perfil** (canto superior direito) → **"Create publication"**
5. **Selecciona o tipo de publicação** (ver lista abaixo)
6. **Preenche o formulário de metadados** (8 passos guiados):
   - Título
   - Autores
   - Resumo/Abstract
   - Identificadores: DOI, ISBN, ISSN (se aplicável)
   - Informação de financiamento
   - Direitos de acesso (Open Access, Restrito, Embargado)
7. **Upload do documento** digital quando possível (PDF recomendado)
8. **Submete** — a publicação fica disponível no repositório

---

## Tipos de Publicação Aceites (8 categorias)

| Tipo | Quando usar |
|------|-------------|
| **Article** | Artigos em revistas científicas (journals) |
| **Thesis** | Dissertações de Mestrado e Doutoramento |
| **Book** | Livros e capítulos de livros |
| **Conference Paper** | Artigos em conferências (IEEE, ACM, Springer) |
| **Poster** | Posters científicos |
| **Dataset** | Conjuntos de dados de investigação |
| **Software** | Código e ferramentas de software |
| **Other** | Relatórios técnicos, preprints, etc. |

---

## Campos Obrigatórios por Tipo

### Para Dissertação de Mestrado (Thesis):
- **Título** (em Português e Inglês)
- **Autor** (nome completo como no Fénix)
- **Orientador(es)** — docente(s) do IST
- **Resumo** — Português (obrigatório) + Inglês
- **Palavras-chave** — mínimo 5, separadas por vírgula
- **Departamento** — ex: Departamento de Engenharia Informática (DEI)
- **Data de defesa**
- **Grau** — Mestre em Engenharia Informática e de Computadores
- **Ficheiro PDF** — versão final aprovada pelo júri
- **Direitos de acesso** — geralmente Open Access após defesa

### Para Artigo Científico (Article/Conference Paper):
- **Título**
- **Autores** (todos, por ordem)
- **Abstract**
- **DOI** (se publicado) ou preprint ID
- **Venue** — nome da revista/conferência
- **Ano e volume/número** (para journals)
- **ISBN/ISSN**
- **PDF** (versão aceite pelo autor, respeitando políticas do publisher)

---

## Integração com Repositórios Externos

O Scholar importa automaticamente publicações de:
- **ORCID** — ligando o ORCID ID à conta
- **DBLP** — para publicações em CS/Informática
- **Scopus** — para publicações indexadas

**Dica prática:** Se já tens um ORCID, linka-o na conta Scholar e as publicações importam automaticamente.

---

## Política de Acesso Aberto

O IST segue a política de Open Access da Universidade de Lisboa:
- Dissertações: **Open Access** após defesa (por defeito)
- Artigos: respeitar as políticas dos publishers (Sherpa/RoMEO)
- Embargo: possível por até 1-2 anos em casos excepcionais (ex: patente pendente)

---

## Repositório Alternativo — Fenix/ULisboa

Dissertações IST também estão no **Catálogo Colectivo da Universidade de Lisboa**:
- https://catalog.ulisboa.pt
- Indexado pela OpenAlex (institution ID: I141596103)
- Pesquisável via API OpenAlex: `filter=institutions.id:I141596103`

---

## Notas para o Doctor

1. **Para publicar uma dissertação:** o estudante faz login com Técnico ID → Create publication → Thesis → preenche metadados → upload PDF final aprovado
2. **Após a defesa:** o júri aprova → o estudante submete a versão final no Scholar + no Fénix
3. **Prazo típico:** versão final até 5-7 dias úteis após a defesa
4. **Formato preferido:** PDF/A (archival), gerado do LaTeX com `pdflatex` ou `lualatex`
5. **O orientador deve estar registado** no Scholar/Fénix para ser adicionado como supervisor
