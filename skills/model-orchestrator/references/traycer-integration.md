# Integração Traycer

Mapear cada execução para um objeto nativo: `Task` para trabalho executável, `Spec` para definição, `Ticket` para issue, `Story` para entrega de produto e `Review` para aprovação.

O contexto Traycer deve fornecer `traycer_status=connected`, `traycer_task_id`, `traycer_object_type`, `traycer_worktree`, agente, permissões e, para rotas delegadas, `child_agent_id`. O bridge recusa rota externa sem agente-filho.

Handoffs, classificação, rota, preflight, escopo, orçamento, métricas e review são artefatos versionados; conversas entre Codex e OpenCode não são fonte de verdade.

