# Rubrica de risco

| Nível | Condições típicas | Rota máxima |
|---|---|---|
| Baixo | Local, reversível, poucos arquivos, contrato e testes claros | MiMo, DeepSeek ou Laguna |
| Médio | Vários módulos, API pública, integração ou rollback não trivial | Worker delimitado, plano GPT e revisão Sol |
| Alto | Segurança, dados, migração, concorrência, regra jurídica ou impacto transversal | Sol controla; só partes mecânicas |
| Crítico | Produção, incidente, irreversibilidade, perda de dados ou impacto jurídico | Sol e revisão humana |

Forçar GPT para autenticação, autorização, multi-tenancy, segredos, migração, concorrência, idempotência, prazo processual, dados pessoais, arquitetura, incidente, ação destrutiva, ambiguidade, validação ausente ou escopo violado.

Somar um ponto por três ou mais comandos, navegação ampla, ciclo teste-correção, cinco ou mais arquivos, múltiplos módulos ou worktree. Selecionar Laguna ao atingir `terminal_score_threshold`; DeepSeek abaixo do limite. Recalibrar por benchmark. Desconhecido exige exploração somente leitura.

