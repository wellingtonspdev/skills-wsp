# Política de privacidade e sanitização

- `public` e `synthetic`: envio externo permitido.
- `sanitized`: permitido após relatório sem bloqueios.
- `internal`: bloqueado por padrão; exigir política e aprovação.
- `sensitive` e `secret`: envio externo proibido.

Bloquear `.env`, chaves, tokens, cookies, credenciais, certificados privados, logs de produção não sanitizados, dados pessoais, processos/documentos reais, informações de clientes e segredos comerciais.

Criar allowlist mínima, classificar antes de anexar, sanitizar cópia descartável, revisar contagens sem registrar valores, substituir pessoas por dados sintéticos e bloquear resultado inconclusivo. Registrar provedor, modelo, classe, arquivos e aprovação sem conteúdo sensível.

