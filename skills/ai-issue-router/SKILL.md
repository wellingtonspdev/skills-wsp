---
name: ai-issue-router
description: Classifica uma ou várias issues, tickets, histórias ou tarefas de engenharia por tipo, complexidade, risco, qualidade e verificabilidade; recomenda workflow e modelos por papel e gera contratos de execução e revisão. Use antes de planejar, delegar ou revisar trabalho entre Codex/GPT e Antigravity/Gemini; não use como autorização automática para executar, aplicar labels ou alterar repositórios.
---

# AI Issue Router

Atue como control plane técnico. Compre raciocínio para triagem, investigação e revisão; compre execução para mudanças delimitadas e verificáveis. Não escolha um modelo apenas pelo tamanho aparente da alteração.

## Limites de autoridade

- Classificação e recomendação são read-only por padrão.
- Não implemente, delegue, crie agentes, aplique labels, escreva telemetria ou altere GitHub/repositório sem pedido ou autorização compatível.
- Trate nomes de modelos como preferências. Antes de executar, verifique o catálogo do runtime e registre `requested_model`, `effective_model` e `availability_status`; nunca simule disponibilidade.
- Preserve regras do projeto, privacidade, orçamento, worktrees e aprovações. Esta skill não relaxa nenhuma delas.
- Para issue sem evidência suficiente, produza classificação `preliminary`, explicite suposições e recomende a exploração mínima necessária.

## Entradas aceitas

Aceite uma issue, várias issues ou qualquer tarefa de engenharia, em texto, URL, objeto JSON ou dados coletados por ferramenta. Quando houver repositório disponível, leia primeiro as instruções do projeto e use exploração read-only proporcional ao risco.

Colete, quando disponíveis:

- título, corpo, labels, comentários, critérios de aceitação e reprodução;
- arquitetura relevante, caminhos críticos, comandos de teste e dependências;
- restrições de dados, segurança, prazo, orçamento e runtime/modelos disponíveis.

Não bloqueie a triagem porque faltam campos: pontue a qualidade baixa e separe fatos, inferências e lacunas.

## Workflow

1. Classifique o tipo `T` usando a taxonomia em [references/rubric.md](references/rubric.md).
2. Dê notas de 0 a 5 para `S`, `N`, `I`, `L`, `H` e `X`, sempre com evidência curta.
3. Calcule `C = 5S + 4N + 3I + 3L + 3H + 2X` e derive `C1–C5`.
4. Classifique risco `R0–R4` separadamente da complexidade.
5. Pontue qualidade `Q` pelos seis critérios da rubrica e identifique o nível de validação disponível `V0–V5`. Validação disponível não significa validação executada.
6. Detecte hard gates antes da matriz: auth, autorização, permissões, secrets, criptografia, migration destrutiva, dados de produção, isolamento/tenancy, concorrência crítica ou fronteira de segurança.
7. Selecione `W1–W5` pela política em [references/model-routing.md](references/model-routing.md). Hard gates, risco, baixa qualidade e baixa verificabilidade podem elevar o workflow.
8. Recomende planner, implementer, reviewer, esforço e escalonamento. Separe os papéis; o executor não é o único aprovador.
9. Gere a saída auditável. Para lote, acrescente uma tabela-resumo, dependências, conflitos e ordem sugerida; depois gere uma ficha por item.
10. Se o usuário pedir execução, gere antes o contrato em [references/contracts.md](references/contracts.md), confirme o runtime efetivo e reclassifique quando surgir nova evidência.

Use `scripts/classify_issue.py` para validar scores e obter roteamento determinístico. O agente faz a análise semântica; o script não substitui leitura da issue ou do repositório.

```powershell
python scripts/classify_issue.py issue.json --format both
python scripts/classify_issue.py issues.json --format json
python scripts/classify_issue.py --template
```

O input pode ser um objeto, uma lista ou `{ "items": [...] }`. Consulte [references/io-schema.md](references/io-schema.md) para os campos e formatos.

## Reclassificação durante a execução

Pare a improvisação e reclassifique se ocorrer qualquer um destes sinais:

- a mesma falha aparece em duas tentativas;
- root cause continua desconhecido;
- arquivos reais excedem aproximadamente 2x a estimativa;
- surge módulo, migration, auth, security ou dependência externa não previstos;
- o bug não é reproduzível ou faltam testes suficientes;
- o diff desvia do plano ou altera API pública/invariantes.

Promova auth/security/migration destrutiva/dados de produção diretamente para controle de Sol; W5 quando crítico ou irreversível. Não use confiança autodeclarada como evidência.

## Saída obrigatória

Para cada item, entregue:

1. `AI ROUTING CARD` legível por humano;
2. bloco JSON válido com o schema da referência;
3. justificativa baseada em evidências e lacunas;
4. validações esperadas e gatilhos de escalonamento;
5. labels sugeridas, sem aplicá-las automaticamente;
6. `Execution Contract` quando houver delegação solicitada.

Em lote, não reduza tudo a uma média. Classifique cada item, identifique acoplamento e proponha revisão agrupada somente para microtarefas independentes com testes confiáveis.

## Política resumida

- `W1`: Gemini direto para C1, R0/R1, Q alta e validação objetiva.
- `W2`: Terra faz microplano; Gemini executa tarefa simples/moderada.
- `W3`: GPT investiga/decompõe; Gemini executa subtarefas; GPT revisa.
- `W4`: Sol controla investigação, invariantes, plano e revisão; Gemini executa sob contrato.
- `W5`: Sol é dono do núcleo crítico; Gemini só recebe partes periféricas isoladas; revisão humana é obrigatória em R4.

Leia [references/model-routing.md](references/model-routing.md) sempre que escolher workflow/modelos. Leia [references/contracts.md](references/contracts.md) apenas quando produzir handoff, revisão ou telemetria.
