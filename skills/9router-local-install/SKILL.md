---
name: 9router-local-install
description: Instalar, endurecer, validar e operar o 9Router localmente via Docker como proxy de IA compatível com OpenAI. Use quando for necessário preparar 9Router no Windows, manter painel/API apenas em loopback, adicionar provedores de forma controlada ou integrar posteriormente MetaGPT, Codex e OpenCode.
---

# 9Router Local Seguro

Instalar o 9Router como proxy local, sem cadastrar chaves de provedores durante o bootstrap. Tratar chaves de IA como dados sensíveis: a implementação observada persiste conexões de provedores no SQLite sem criptografia em repouso.

## Como usar

```text
Use $9router-local-install para instalar o 9Router em D:\9router.
Use $9router-local-install para auditar e endurecer minha instalação existente do 9Router.
Use $9router-local-install para preparar uma integração de teste entre 9Router e MetaGPT.
```

## Fluxo obrigatório

1. Confirmar Docker Desktop funcional e escolher um diretório local, por exemplo `D:\9router`.
2. Clonar ou atualizar `https://github.com/decolua/9router.git`; registrar commit e digest da imagem usada.
3. Copiar os arquivos de `assets/` para o diretório da instalação e executar `scripts/initialize-local-9router.ps1`.
4. Manter a API publicada somente em `127.0.0.1:20128`; nunca expor a porta em `0.0.0.0` sem revisão explícita de segurança.
5. Validar dashboard HTTP 200, `docker compose ps`, bind loopback, persistência SQLite e resposta 401 de `/v1/models` sem chave local.
6. Informar o caminho do arquivo de credenciais gerado, sem mostrar senha, tokens, `.env.docker` ou conteúdo do banco.

## Regras de segurança

- Manter `REQUIRE_API_KEY=true`, `ENABLE_REQUEST_LOGS=false`, `OBSERVABILITY_ENABLED=false`, Cloud Sync desativado e `NEXT_TELEMETRY_DISABLED=1`.
- Gerar `JWT_SECRET`, `INITIAL_PASSWORD`, `API_KEY_SECRET` e `MACHINE_ID_SALT` localmente. Nunca versionar `.env.docker`, SQLite ou credenciais.
- Não inserir automaticamente a chave principal de MetaGPT, OpenRouter, Codex ou produção. Orientar o usuário a usar primeiro uma chave de teste dedicada, limitada e revogável.
- Diferenciar chave do provedor da chave local de cliente do 9Router. A segunda é necessária quando `REQUIRE_API_KEY=true`.
- Não ativar logs de requisição, observabilidade de conteúdo ou Cloud Sync para "depurar" sem autorização explícita e avaliação do dado que poderá ser retido.
- Não configurar rotação de múltiplas chaves para contornar cotas, RPM ou políticas de provedores.

## Operação e integração

Usar `references/operations-and-integration.md` para comandos operacionais, investigação de falhas e URLs de integração. Antes de editar configurações de Codex, OpenCode ou MetaGPT, criar backups, cadastrar um único provedor de teste no dashboard e executar uma chamada curta controlada.

Para MetaGPT em Docker, usar `http://host.docker.internal:20128/v1`; para clientes no host, usar `http://127.0.0.1:20128/v1`. Isso confirma compatibilidade de protocolo, não equivalência completa de recursos: validar cada cliente após configurar.

## Encerramento

Reportar: diretório, commit do repositório, estado/ID da imagem, URL local, validações aprovadas, riscos residuais e próximo passo manual. Se o container não estiver saudável, coletar logs e parar antes de adicionar qualquer chave de provedor.
