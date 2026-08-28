# Política de workflow e modelos

Leia esta referência após concluir T/C/R/Q/V. A rota é uma recomendação por papel; não prova que o modelo está disponível no runtime.

## Matriz base

| Complexidade | R0–R1 | R2 | R3 | R4 |
|---|---|---|---|---|
| C1 | W1 | W2 | W4 | W5 |
| C2 | W1/W2 | W2 | W4 | W5 |
| C3 | W2/W3 | W3 | W4 | W5 |
| C4 | W3 | W3/W4 | W4 | W5 |
| C5 | W3/W4 | W4 | W5 | W5 |

Resolva células ambíguas assim:

- `C2 + R0/R1`: W1 somente com `Q>=80` e `V>=V2`; caso contrário W2.
- `C3 + R0/R1`: W2 somente com `Q>=70`, `V>=V2`, causa/escopo conhecidos e tarefa decomponível; caso contrário W3.
- `C4 + R2`: W3 somente com `Q>=60`, `V>=V3`, escopo decomponível e sem hard gate; caso contrário W4.
- `C5 + R0/R1`: W3 somente quando decomponível e `V>=V3`; caso contrário W4.

Elevações obrigatórias:

- `Q<60`: no mínimo W3.
- `V0/V1`: no mínimo W3; W4 se também houver `R2+`, `C4+` ou root cause desconhecida.
- hard gate confirmado: no mínimo W4.
- hard gate crítico/irreversível ou `R4`: W5.
- `SECURITY`/`AUTH`: W4 por padrão; W5 para núcleo crítico, autorização, permissões, secrets, crypto ou `R4`.
- `ARCH` central, incidente crítico, migration destrutiva e concorrência crítica: W5.

## Papéis por workflow

| Workflow | Planner | Implementer | Reviewer | Escalation |
|---|---|---|---|---|
| `W1` | nenhum | Gemini 3.7 Flash Medium | self-check ou Terra em revisão agrupada | Terra Medium |
| `W2` | GPT-5.6 Terra Medium | Gemini 3.7 Flash Medium/High | Terra Medium | Terra High/Sol High |
| `W3` | Terra High; Sol High para C4, ARCH ou BUG-X difícil | Gemini 3.7 Flash High | Terra High; Sol para C4/R2 importante | Sol High |
| `W4` | GPT-5.6 Sol High/XHigh | Gemini 3.7 Flash High sob contrato | Sol High em sessão independente | Sol XHigh/humano |
| `W5` | GPT-5.6 Sol High/XHigh | Sol no núcleo; Gemini apenas periférico | Sol independente + humano em R4 | humano/owner técnico |

Gemini 3.1 Pro é fallback de execução para lógica excepcional ou após uma tentativa bem instrumentada do Flash. Gemini 3.6/3.5 são fallbacks de quota/compatibilidade, não padrão.

## Responsabilidades

- Terra: dispatcher, triagem, exploração intermediária, planejamento C2/C3 e revisão convencional.
- Sol: arquitetura, C4/C5, root cause difícil, segurança, auth, migrations críticas, concorrência e auditoria adversarial.
- Gemini Flash: execução principal de planos delimitados, testes, frontend, CRUD, automação e refactors localizados.
- Humano: aprovação final de R4, irreversibilidade, produção e decisões materiais.

Antes de reservar Sol para uma implementação grande, tente decompor a issue em subtarefas C1–C3 que Gemini consiga executar sob contrato. Não decomponha de forma a esconder uma invariante crítica.

## Verificação de runtime

Antes da execução:

1. liste modelos/agentes suportados pelo harness atual;
2. preserve o nome recomendado em `requested_model`;
3. registre o modelo realmente selecionado em `effective_model`;
4. se indisponível, marque `availability_status=unavailable` e proponha fallback; não declare delegação concluída;
5. não confunda harness, agente, provedor, modelo e reasoning effort.

## Reviewer independente

Forneça ao reviewer issue original, critérios de aceite, plano, diff, resultados brutos de testes e arquitetura relevante. Peça que tente falsificar a solução e procure regressões, edge cases, inconsistência schema/ORM, mudança fora do escopo, testes falsamente positivos, security issues, tratamento incompleto de erros e breaking changes.
