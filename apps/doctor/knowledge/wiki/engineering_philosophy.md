# Filosofia de Engenharia — Fabio Akita para Investigadores

## Por que isto importa para o Doctor

Investigadores que constroem sistemas (dissertações de desenvolvimento, protótipos, pipelines MLOps)
frequentemente cometem erros de engenharia que invalidam ou enfraquecem os resultados.
Entender a filosofia de engenharia de Fabio Akita ajuda a construir sistemas mais credíveis,
mais reproducíveis, e mais honestos sobre as suas limitações.

---

## O Princípio Central: Pragmatismo sobre Dogma

"A gente geralmente faz assim" nunca é uma razão técnica.
Toda decisão de arquitectura precisa de uma razão explícita e verificável.

Aplicado à investigação:
- "Usámos PyTorch porque é o standard em investigação" — razão fraca
- "Usámos PyTorch porque a nossa arquitectura requer autograd dinâmico e os benchmarks de performance para o nosso caso de uso favorecem PyTorch sobre JAX" — razão forte

---

## Anti-Hype Sistemático — O Ciclo que se Repete

O hype tecnológico segue sempre o mesmo padrão:
```
Entusiasmo inicial → Adopção acrítica → Desilusão → Síntese madura
```

Já aconteceu com: cloud (2010), big data (2012), blockchain (2017), microservices (2018), NoSQL (2015), IA generativa (2023–...).

**A relação entre entusiasmo e conhecimento é inversamente proporcional.**
Quem entende profundamente uma tecnologia raramente faz claims absolutos sobre ela.

### Aplicado à investigação académica em ML:

Perguntas que um investigador com mentalidade Akita faz:

1. **"Este paper compara com baselines adequados?"** — Um modelo SOTA que bate apenas baselines de 3 anos atrás não prova muito.
2. **"Qual é o custo de treino?"** — Papers que não reportam custo computacional são incompletos.
3. **"Os resultados reproduzem noutro hardware?"** — Benchmark em TPU específica do Google não generaliza.
4. **"Existe deployment real ou apenas protótipo?"** — "Funciona em Jupyter" é diferente de "funciona em produção".

---

## O "Chef de Miojo" vs. Engenheiro Real — Aplicado a ML

**Chef de Miojo** (em ML/investigação): segue tutoriais do Hugging Face sem entender o que está a fazer.
Produz notebooks que funcionam no dataset do tutorial. Falha quando o dataset real é diferente.

**Engenheiro real**: entende por que a arquitectura funciona, não apenas como configurar os parâmetros.
Sabe o que quebra, quando quebra, e como diagnosticar.

### Indicadores de "chef de Miojo" em dissertações:
- "Usámos BERT porque é estado da arte" (sem justificação para o task específico)
- Sem análise de erros — apenas tabela de accuracy
- Sem ablation study
- Sem discussion de quando o modelo falha
- Resultados apenas no split de test, sem análise de casos difíceis

### Indicadores de engenheiro real em dissertações:
- Escolha de arquitectura justificada para o problema específico
- Análise de erros: quais exemplos o modelo erra e porquê
- Ablation study: cada componente justificado com dados
- Limitações honestas e específicas
- Reproducibilidade documentada (seeds, hardware, versões)

---

## Experiência como Autoridade — O Padrão da Prova

Akita sobre teoria vs. prática:
"Teoria sem prática é decoração intelectual. O padrão é quem viveu o problema, não quem leu sobre ele."

Para investigadores, isto significa:
- Resultados experimentais superam claims teóricos não testados
- Um sistema que funciona em produção real é mais valioso que um protótipo em notebook
- Limitações descobertas empiricamente são contribuições legítimas (não falhas)

---

## Decisões Técnicas — O Framework ADR (Architecture Decision Record)

Para cada decisão técnica não óbvia numa dissertação, documentar:

```
Decisão: [O que foi decidido]
Contexto: [Por que esta decisão era necessária]
Decisão: [O que foi escolhido]
Consequências: [Trade-offs aceites]
Alternativas consideradas: [O que foi rejeitado e porquê]
```

Exemplo em contexto de dissertação:

```
Decisão: PostgreSQL como base de dados para feature store
Contexto: Precisávamos de armazenar e recuperar features para 50k exemplos
          com latência < 10ms para serving online.
Decisão: PostgreSQL com índices B-tree em feature_id e timestamp.
Consequências: Simples de operar, ACID, sem overhead de sistema dedicado.
               Não escala para >10M features sem sharding.
Alternativas: Redis (demasiado volátil para dados de treino),
              Feast (overhead operacional injustificado para escala do projecto).
```

---

## Independência Intelectual na Investigação

Akita: "Nunca aceitar sponsorship. Nunca publicar o que não se acredita."

Para investigadores:
- Declarar conflitos de interesses (funding, afiliações)
- Não omitir resultados negativos — são contribuições legítimas
- Não inflar claims para aumentar probabilidade de aceitação
- O paper que diz "X não funciona para Y" pode ser mais valioso que o que diz "X funciona"

---

## Estimativas — Ranges com Probabilidade, Não Datas Fixas

Akita sobre estimativas de prazo:
"50% de chance de terminar em 2 semanas, 90% em 6 semanas."

Aplicado a investigação:
- Timelines de dissertações devem ter buffers explícitos
- "Espero terminar implementação em Março" → "Implementação: melhor caso Março, provável Abril, limite Maio"
- Experimentos falham, datasets têm problemas, infra tem downtime — planear para isto

---

## Escolha de Tecnologia — Melhor, Não Popular

Akita: "Toda escolha técnica é a melhor escolha disponível. Não a padrão. Não a popular. A melhor."

Em investigação, isto significa:
- PyTorch é padrão em investigação — mas é a melhor para o seu caso?
- Para modelos muito pequenos em edge: TensorFlow Lite pode ser superior
- Para matemática pura e diferenciação automática avançada: JAX é genuinamente superior
- Para produção enterprise: TensorFlow/Keras tem deployment mais maduro

A escolha correcta depende do problema. Não do que o orientador usa.

---

## "Construído para Durar" vs. "Funciona para o Paper"

A maioria dos protótipos de dissertação são construídos para funcionar enquanto se escreve o paper.
O Akita acrescentaria: vale a pena construir melhor, mesmo em dissertações, porque:

1. **Reproducibilidade real** — o code é revisto pelo júri e pela comunidade
2. **Credibilidade técnica** — code limpo sugere resultados limpos
3. **Reutilização** — código de dissertação que outros podem usar tem impacto real

Checklist mínima de qualidade de engenharia para dissertações:
- [ ] README com setup em < 5 comandos
- [ ] Requirements.txt / environment.yml com versões fixadas
- [ ] Seeds fixados em todos os ficheiros de treino
- [ ] Hardware e software stack documentados
- [ ] Testes unitários para data preprocessing (onde mais ocorrem bugs silenciosos)
- [ ] Sem credenciais no repositório (usar .env, documentado em .env.example)

---

## Segurança em Sistemas de Investigação

Investigadores frequentemente ignoram segurança porque "é só investigação".
Mas sistemas de investigação frequentemente:
- Correm em servidores universitários partilhados
- Processam dados sensíveis (médicos, financeiros, pessoais)
- Usam APIs com custos reais (OpenAI, AWS)

Mínimo aceitável (princípio least privilege do Akita):
- Variáveis de ambiente para API keys — nunca hardcoded
- `.gitignore` cobre `.env`, credenciais, dados sensíveis, checkpoints grandes
- Dados pessoais anonimizados antes de qualquer processamento
- Acesso a servidores GPU via SSH keys, não passwords

---

## Long-Term Thinking — Décadas, Não Sprints

Akita: "Penso em décadas, não em sprints."

Para investigadores:
- A dissertação que vale é a que contribui genuinamente para o campo, não a que passa na defesa
- Trabalho de investigação honesto sobre limitações é mais durável que claims inflados
- A reputação científica constrói-se ao longo de anos — um paper desonesto é difícil de esquecer
- Escolher problemas de investigação com durabilidade: fundamentos de ML duram décadas; frameworks específicos ficam obsoletos em anos
