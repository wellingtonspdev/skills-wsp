---
name: ai-daily-radar
description: Pesquisa e sintetiza diariamente notícias, papers, releases, ferramentas, repositórios e sinais de comunidade sobre IA, tecnologia e programação. Use quando o usuário pedir radar diário de IA, briefing tecnológico, papers do dia, tendências de IA ou plano diário de estudos baseado em novidades recentes.
---

# Skill: AI Daily Radar

## Missão
Produzir um radar diário de alta precisão, com pesquisa web ao vivo, cobrindo as últimas 24 horas e estendendo para até 72 horas apenas quando um item importante não tiver aparecido em execuções anteriores.

## Entradas esperadas
- Data e hora atuais em `America/Sao_Paulo`.
- Arquivo `config/sources.yaml`.
- Relatórios recentes em `reports/`.
- Memória em `state/trend-ledger.md` e `state/seen-items.md`.

## Processo obrigatório

### 1. Preparação temporal
- Determine a janela principal: últimas 24 horas.
- Para segunda-feira ou período sem execução, cubra desde a última execução disponível, limitado a 72 horas.
- Registre horário de corte e horário da pesquisa.
- Use datas absolutas no formato `AAAA-MM-DD`.

### 2. Pesquisa por trilhas
Execute buscas independentes e depois consolide:

1. **Laboratórios e empresas**
   - anúncios de modelos, APIs, produtos, segurança, preços, disponibilidade e pesquisa;
   - changelogs e documentação oficial quando houver mudança técnica.

2. **Papers e pesquisa**
   - arXiv: `cs.AI`, `cs.LG`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.SE`, `stat.ML`;
   - Hugging Face Daily/Trending Papers;
   - OpenReview e páginas oficiais de conferências quando pertinente;
   - página do paper, PDF, código, dataset e projeto oficial.

3. **Programação e ferramentas**
   - releases e changelogs de ferramentas relevantes;
   - agentes, MCP, frameworks de LLM, inferência, avaliação, observabilidade, Python, web e DevOps.

4. **Open source**
   - repositórios em crescimento ou com release relevante;
   - valide atividade recente, documentação, licença quando disponível e utilidade real;
   - não ranqueie apenas por estrelas.

5. **Noticiário**
   - use veículos reconhecidos para contexto, mercado, política tecnológica, investimentos e incidentes;
   - encontre e cite a fonte primária correspondente sempre que possível.

6. **Comunidades e fóruns**
   - Hacker News, Reddit técnico, fóruns oficiais, GitHub Discussions e comunidades especializadas;
   - trate como sinal emergente, não como prova;
   - só destaque discussões com conteúdo técnico, evidência reproduzível ou forte impacto potencial.

### 3. Verificação e deduplicação
Para cada candidato:
- confirme título, autor/organização, data de publicação e URL;
- diferencie data da matéria e data do evento;
- procure a fonte primária;
- para alegações importantes, busque confirmação independente;
- agrupe matérias sobre o mesmo evento em um único item;
- consulte `state/seen-items.md` e relatórios anteriores;
- itens repetidos só retornam se houver atualização material, que deve ser explicitada.

### 4. Pontuação
Atribua de 0 a 5 para cada dimensão:
- impacto potencial;
- novidade real;
- qualidade da evidência;
- relevância para o perfil do projeto;
- aplicabilidade prática imediata.

Pontuação total: soma, máximo 25.

Classificação:
- 21–25: essencial hoje;
- 16–20: alta prioridade;
- 11–15: acompanhar;
- 0–10: omitir do relatório principal, podendo aparecer em “sinais fracos”.

### 5. Análise de papers
Para cada paper selecionado, informar:
- problema investigado;
- contribuição e método;
- resultados alegados pelos autores;
- benchmark/dataset usados;
- limitações, riscos e o que ainda não foi demonstrado;
- código, modelo ou dataset disponível;
- nível de dificuldade: introdutório, intermediário ou avançado;
- por que vale ou não vale estudar agora.

Nunca apresente resultado de preprint como consenso científico.

### 6. Síntese de tendências
Leia `state/trend-ledger.md` e relatórios dos últimos 7 e 30 dias. Identifique:
- temas acelerando;
- temas perdendo força;
- convergências entre papers, produtos e open source;
- possíveis mudanças de arquitetura ou ferramentas;
- hype sem evidência suficiente;
- oportunidades de projeto ou estudo.

### 7. Plano diário personalizado
Gere três rotas:
- **30 minutos:** leitura essencial e um conceito-chave;
- **60 minutos:** leitura + reprodução curta ou tutorial oficial;
- **2 horas:** mini-experimento prático com objetivo, passos e critério de sucesso.

Sempre conecte as sugestões, quando pertinente, a agentes, MCP, Python/FastAPI, React/Vite, Docker/PostgreSQL, DevOps/nuvem e construção de SaaS.

### 8. Atualização da memória
Atualize, sem apagar histórico útil:

`state/seen-items.md`
- data;
- título normalizado;
- URL canônica;
- categoria;
- motivo de inclusão;
- atualização material posterior, se houver.

`state/trend-ledger.md`
- tendência;
- evidências acumuladas;
- primeira e última observação;
- estágio: sinal fraco, emergente, consolidando, consolidada ou desacelerando;
- confiança: baixa, média ou alta.

Mantenha ambos compactos. Remova duplicações e preserve links.

## Estrutura obrigatória do relatório

# Radar Diário de IA — AAAA-MM-DD

## 1. Resumo executivo
- 5 a 8 pontos que realmente importam.
- Inclua “A mudança mais importante do dia”.

## 2. Top notícias e anúncios
Tabela com: prioridade, pontuação, título, categoria, data do evento, por que importa e fonte primária.
Depois da tabela, explique os itens essenciais com contexto, evidências, limitações e impacto.

## 3. Papers do dia
Selecione de 3 a 7 papers. Use a análise de papers definida nesta Skill.

## 4. Ferramentas, releases e open source
Inclua apenas novidades técnicas verificáveis e úteis.

## 5. Sinais das comunidades
Separe claramente opinião, relato reproduzível, demonstração e especulação.

## 6. Tendências de 7 e 30 dias
Mostre o que está acelerando, consolidando, desacelerando e o que ainda é hype.

## 7. O que estudar agora
Organize por prioridade: estudar hoje, explorar nesta semana e manter no radar.

## 8. Plano prático
Rotas de 30 minutos, 60 minutos e 2 horas.

## 9. Ideias de projetos e oportunidades
De 1 a 3 ideias concretas, pequenas o suficiente para validar, derivadas das tendências observadas.

## 10. Riscos, controvérsias e pontos de atenção
Segurança, privacidade, licenças, custos, dependência de fornecedor, benchmarks frágeis e alegações não verificadas.

## 11. Fontes e auditoria
- lista das fontes efetivamente consultadas;
- itens excluídos relevantes e motivo da exclusão;
- lacunas de cobertura ou páginas inacessíveis;
- horário de corte da pesquisa.

## Padrão de escrita
- Português do Brasil.
- Claro, detalhado e sem sensacionalismo.
- Links clicáveis em Markdown.
- Datas absolutas.
- Não use afirmações vagas como “está revolucionando” sem evidência concreta.
- Quando fizer uma inferência, sinalize explicitamente: `Análise:`.
- Quando a informação vier apenas de autor/empresa, sinalize: `Alegação da fonte:`.

## Saída final
A mensagem final deve conter somente o relatório completo em Markdown, sem comentários sobre o processo interno.
