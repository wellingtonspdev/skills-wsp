# Provedores e integrações

Confirmar no ambiente: IDs GPT do Codex; slug e gratuidade do MiMo no OpenCode; slugs, disponibilidade, preço e limites de DeepSeek/Laguna no OpenRouter; CLI/API e artefatos do Traycer.

Manter valores em `config/orchestrator.json`. `TO_CONFIRM` bloqueia execução real. Não fixar preço pontual. Nunca imprimir credenciais.

## Preflight

1. Resolver executáveis e registrar caminho/versão.
2. Confirmar modelos por comando ou endpoint oficial.
3. Confirmar política de dados, retenção e disponibilidade.
4. Confirmar chave apenas por existência.
5. Fazer chamada sintética mínima descartável.
6. Validar worktree e artefatos.
7. Registrar data, fonte, resultado e expiração.

Adaptadores recebem contrato, worktree, modelo, limites e paths; retornam status, arquivos, comandos, validações, tokens, custo, tentativas e handoff; suportam cancelamento e falham fechados. Não presumir esquema nativo compartilhado.

