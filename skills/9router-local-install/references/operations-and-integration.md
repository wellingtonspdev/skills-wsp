# Operacao e Integracao

## Instalar no Windows

```powershell
git clone https://github.com/decolua/9router.git D:\9router
& C:\Users\Wellington\.codex\skills\9router-local-install\scripts\initialize-local-9router.ps1 -InstallDirectory D:\9router -Start
```

Nao sobrescrever `.env.docker` existente. Para uma instalacao existente, primeiro verificar a origem e o estado do container.

## Validar

```powershell
Set-Location D:\9router
docker compose -f .\docker-compose.local-secure.yml ps
docker compose -f .\docker-compose.local-secure.yml logs --tail 100
Invoke-WebRequest http://127.0.0.1:20128 -UseBasicParsing
Invoke-WebRequest http://127.0.0.1:20128/v1/models -UseBasicParsing
```

Esperar HTTP 200 no dashboard e HTTP 401 sem chave no endpoint `/v1/models`. Confirmar que o bind do Docker e `127.0.0.1:20128`, nao `0.0.0.0:20128`.

## Operar

```powershell
Set-Location D:\9router
docker compose -f .\docker-compose.local-secure.yml logs -f
docker compose -f .\docker-compose.local-secure.yml down
docker compose -f .\docker-compose.local-secure.yml up -d
```

Dashboard: `http://127.0.0.1:20128`. Ler a senha em `D:\9router-runtime\DASHBOARD_CREDENTIALS.txt`; nunca imprimi-la no chat ou em log.

## Adicionar um provedor depois do bootstrap

1. Alterar a senha do dashboard.
2. Manter Cloud Sync, Request Logs e Observability desativados.
3. Cadastrar apenas uma chave de teste restrita, com teto de gasto.
4. Selecionar um modelo e fazer uma chamada curta no dashboard.
5. Criar uma chave local de cliente do 9Router para os clientes, pois a API local exige autenticação.

Chave de provedor e chave local de cliente são diferentes. Não alterar configurações de clientes antes de o teste controlado passar.

## Integrações posteriores

| Cliente | Base URL | Procedimento |
| --- | --- | --- |
| MetaGPT em Docker | `http://host.docker.internal:20128/v1` | Usar cliente OpenAI compatível e chave local 9Router; validar uma chamada simples. |
| Codex no host | `http://127.0.0.1:20128/v1` | Fazer backup de `~/.codex/config.toml` e `~/.codex/auth.json` antes de aplicar. |
| OpenCode no host | `http://127.0.0.1:20128/v1` | Fazer backup de `~/.config/opencode/opencode.json` antes de aplicar. |

O 9Router possui endpoints OpenAI compatíveis, mas cada integração precisa de validação funcional independente.

## Falhas comuns

- Docker daemon inacessível: iniciar Docker Desktop e repetir apenas o bootstrap.
- Dashboard não abre: verificar `docker compose ps`, logs e bind loopback.
- `401` em `/v1/models`: comportamento esperado sem chave local.
- Falha ao usar provedor: não ativar logs de conteúdo automaticamente; verificar cadastro, modelo e limites no próprio provedor.
- Build local Windows com `EPERM`: preferir imagem Docker publicada; não inferir que o container está inválido por esse erro de varredura de junctions.
