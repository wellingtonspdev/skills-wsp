# Gates operacionais

A ordem é bloqueante: configuração ativa → preflight → classificação → decisão de rota → sanitização externa → contrato → escopo/worktree → orçamento → métricas → registro Traycer → worker → validações → revisão independente.

Cada etapa deve gerar JSON com `*_status=valid`. Ausência, erro ou divergência interrompe o pipeline. O agente não pode pular scripts por conveniência. O único fallback seguro é `codex_only`.

Estados de validação: `working`, `not_working`, `not_exercised`, `not_applicable`, `not_verifiable`. `not_applicable` só é válido quando justificado no review; não é falha automática.

