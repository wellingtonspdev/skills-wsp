# Contratos, revisão e telemetria

Leia esta referência apenas quando houver handoff, revisão ou registro de resultado.

## Execution Contract

Entregue ao executor um contrato completo:

```markdown
# EXECUTION CONTRACT

## Identidade
- Task/issue:
- Harness:
- Requested model:
- Effective model:
- Worktree/repository:

## Objetivo

## Escopo permitido
- arquivos/componentes:

## Fora de escopo

## Plano aprovado

## Invariantes

## Critérios de aceitação

## Validações obrigatórias
- comandos e resultados esperados:

## Condições de escalonamento
- mesma falha duas vezes;
- escopo real >2x estimativa;
- módulo/migration/auth/security/dependência inesperada;
- desvio do plano;
- validação impossível.

## Relatório final exigido
- arquivos alterados e motivo;
- diff resumido;
- comandos executados e saída;
- falhas/retries;
- riscos ou lacunas restantes;
- requested/effective model.
```

O contrato delimita execução; não concede permissões externas nem autoriza alterações irreversíveis.

## Review Contract

O reviewer deve receber artefatos primários, não somente o resumo do executor:

```markdown
# REVIEW CONTRACT

Considere a implementação não confiável e tente falsificá-la.

Entradas:
- issue e critérios de aceite originais;
- plano/contrato aprovado;
- diff completo;
- resultados brutos de testes/checks;
- arquitetura e invariantes relevantes.

Verifique:
- aderência ao escopo e ao plano;
- regressões, edge cases e breaking changes;
- segurança, auth, privacidade e isolamento;
- concorrência, idempotência e integridade;
- consistência ORM/schema/API;
- testes falsamente positivos ou ausentes;
- tratamento de erros e rollback.

Saída: PASS, FAIL ou NEEDS_EVIDENCE, com achados por severidade e evidência reproduzível.
```

## Telemetria opcional

Somente salve quando o usuário/projeto autorizar. Use JSONL, um objeto por execução, sem segredos, payloads privados ou conteúdo desnecessário:

```json
{
  "issue_id": "#184",
  "task_type": "FEATURE-X",
  "complexity_score": 57,
  "risk": "R2",
  "issue_quality": 82,
  "validation_level": "V4",
  "workflow": "W3",
  "planner_model": "gpt-5.6-terra-high",
  "implementer_model": "gemini-3.7-flash-high",
  "reviewer_model": "gpt-5.6-terra-high",
  "requested_model": "gemini-3.7-flash-high",
  "effective_model": null,
  "turns": null,
  "retries": 0,
  "estimated_files": null,
  "actual_files": null,
  "validation": {},
  "outcome": "classified",
  "review_findings": []
}
```

Calibre a política apenas depois de amostras comparáveis e verificadas. Benchmark interno pode superar benchmarks públicos, mas não deve remover hard gates sem decisão humana explícita.
