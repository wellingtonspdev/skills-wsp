# Rubrica T/C/R/Q/V

Use esta referência ao analisar semanticamente cada issue. Registre uma evidência curta por nota; números sem justificativa não são auditáveis.

## T — Task Type

Escolha o tipo dominante e, se necessário, tipos secundários:

| Código | Tipo |
|---|---|
| `DOC` | documentação |
| `TEST` | testes |
| `UI` | frontend/interface |
| `BUG-L` | bug localizado, causa conhecida |
| `BUG-X` | bug de causa desconhecida |
| `FEATURE-L` | feature localizada |
| `FEATURE-X` | feature transversal |
| `REFACTOR-L` | refactor localizado |
| `REFACTOR-X` | refactor arquitetural |
| `PERF` | performance |
| `CI` | CI/CD ou build |
| `INFRA` | infraestrutura, Docker ou deployment |
| `DB` | banco, schema ou migrations |
| `ARCH` | arquitetura |
| `INTEGRATION` | API, MCP ou serviço externo |
| `ALGO` | algoritmo ou lógica complexa |
| `SECURITY` | segurança |
| `AUTH` | autenticação ou autorização |
| `REVIEW` | revisão ou auditoria |
| `RESEARCH` | pesquisa ou análise técnica |

O tipo influencia a rota antes do score. `C2 + UI + R1` pode ir para Gemini; `C2 + AUTH + R4` vai para Sol.

## C — Complexity

Pontue cada fator de 0 a 5.

| Fator | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| `S` escopo/fragmentação | trivial | 1 arquivo/local | 2–3 relacionados | vários no módulo | vários módulos | cross-repository |
| `N` navegação | local óbvio | componente conhecido | pouca navegação | múltiplos componentes | arquitetura espalhada | compreensão ampla |
| `I` integrações | isolado | dependência local | poucas dependências | banco ou API | vários serviços | banco + APIs + auth + externos |
| `L` lógica | mecânica | simples | regra clara | negócio | invariantes complexas | concorrência/algoritmo/arquitetura |
| `H` horizonte | uma edição | edição + teste | poucas etapas | investigar + implementar | várias etapas/ferramentas | ciclo longo de observar/corrigir |
| `X` validação difícil | determinística | teste direto | unit tests | integração | E2E/ambiente | difícil reproduzir/externa |

Fórmula:

```text
C = 5S + 4N + 3I + 3L + 3H + 2X
```

| Score | Classe |
|---:|---|
| 0–20 | `C1` |
| 21–40 | `C2` |
| 41–60 | `C3` |
| 61–80 | `C4` |
| 81–100 | `C5` |

## R — Risk / Blast Radius

| Classe | Interpretação |
|---|---|
| `R0` | irrelevante |
| `R1` | baixo, localizado e reversível |
| `R2` | moderado, regressão possível mas controlável |
| `R3` | alto, grande blast radius ou rollback difícil |
| `R4` | crítico, dano grave/irreversível ou fronteira sensível |

Considere dados pessoais, produção, pagamentos, compatibilidade pública, isolamento entre tenants, integridade, rollback, concorrência e dependências externas. Complexidade não reduz risco.

## Hard gates

Confirme explicitamente qualquer toque direto em:

- autenticação, autorização, permissões ou fronteiras de segurança;
- secrets, criptografia ou credenciais;
- migration destrutiva ou dados de produção;
- isolamento/tenancy ou dados pessoais sensíveis;
- concorrência crítica ou alteração irreversível.

Hard gate confirmado impõe no mínimo `W4`; use `W5` quando for crítico, irreversível, central ou `R4`. Menção documental ou incidental deve virar `possible_hard_gate`, não confirmação automática.

## Q — Issue Quality

Pontue de 0 a 5 cada critério:

1. problema claramente descrito;
2. comportamento esperado;
3. critérios de aceitação;
4. evidências ou reprodução;
5. componentes/contexto relevantes;
6. definição objetiva de pronto.

Normalize: `Q = round(soma / 30 * 100)`.

| Q | Estado |
|---:|---|
| 80–100 | pronta para agente |
| 60–79 | utilizável |
| 40–59 | requer planejamento/exploração |
| 0–39 | não implementar diretamente |

## V — Validation disponível

| Nível | Capacidade objetiva disponível |
|---|---|
| `V0` | nenhuma |
| `V1` | somente manual |
| `V2` | testes unitários |
| `V3` | integração |
| `V4` | integração + E2E |
| `V5` | suíte completa + checks especializados aplicáveis |

Não marque `V4` porque alguém prometeu executar E2E. Registre o que existe e é executável. Resultados efetivamente rodados ficam em `validation_evidence`.

## Estado da classificação

- `confirmed`: issue e contexto do repositório sustentam as notas.
- `preliminary`: faltam exploração, reprodução, arquitetura ou evidência de validação.
- `blocked`: a decisão segura depende de informação material indisponível.

Uma classificação preliminar ainda pode recomendar planejamento; ela não autoriza implementação.
