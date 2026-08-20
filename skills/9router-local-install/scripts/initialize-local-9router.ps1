[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$InstallDirectory,

    [string]$RuntimeDirectory = "D:\9router-runtime",

    [switch]$Start
)

$ErrorActionPreference = "Stop"

function New-Secret {
    param([int]$ByteCount = 32)

    $bytes = New-Object byte[] $ByteCount
    $rng = [System.Security.Cryptography.RandomNumberGenerator]::Create()
    try {
        $rng.GetBytes($bytes)
    }
    finally {
        $rng.Dispose()
    }

    return [Convert]::ToBase64String($bytes).TrimEnd("=").Replace("+", "-").Replace("/", "_")
}

$installPath = (Resolve-Path -LiteralPath $InstallDirectory).Path
$runtimePath = [System.IO.Path]::GetFullPath($RuntimeDirectory)
$composeTemplate = Join-Path $PSScriptRoot "..\assets\docker-compose.local-secure.yml"
$envPath = Join-Path $installPath ".env.docker"

if (-not (Test-Path -LiteralPath (Join-Path $installPath ".git"))) {
    throw "O diretorio de instalacao deve conter um clone do repositorio 9Router: $installPath"
}

if (Test-Path -LiteralPath $envPath) {
    throw "O arquivo .env.docker ja existe. Recusei sobrescrever segredos locais existentes."
}

if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    throw "Docker nao foi encontrado no PATH. Instale/inicie o Docker Desktop e tente novamente."
}

& docker info *> $null
if ($LASTEXITCODE -ne 0) {
    throw "O Docker daemon nao esta acessivel. Inicie o Docker Desktop e tente novamente."
}

$dataPath = Join-Path $runtimePath "data"
New-Item -ItemType Directory -Force -Path $dataPath | Out-Null

$compose = Get-Content -LiteralPath $composeTemplate -Raw
$dockerDataPath = ($dataPath -replace "\\", "/")
$compose = $compose.Replace("__RUNTIME_DATA_PATH__", $dockerDataPath)
Set-Content -LiteralPath (Join-Path $installPath "docker-compose.local-secure.yml") -Value $compose -Encoding ascii

$password = New-Secret 24
@(
    "# Gerado localmente; nunca versionar ou compartilhar.",
    "JWT_SECRET=$(New-Secret)",
    "INITIAL_PASSWORD=$password",
    "API_KEY_SECRET=$(New-Secret)",
    "MACHINE_ID_SALT=$(New-Secret)"
) | Set-Content -LiteralPath $envPath -Encoding ascii

$credentialsPath = Join-Path $runtimePath "DASHBOARD_CREDENTIALS.txt"
@(
    "9Router dashboard local",
    "URL: http://127.0.0.1:20128",
    "Usuario: admin",
    "Senha inicial: $password",
    "Altere a senha no primeiro acesso."
) | Set-Content -LiteralPath $credentialsPath -Encoding ascii

$currentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
& icacls $runtimePath /inheritance:r /grant:r "${currentUser}:(OI)(CI)F" "SYSTEM:(OI)(CI)F" | Out-Null
if ($LASTEXITCODE -ne 0) {
    throw "Falha ao proteger o diretorio de runtime com ACLs locais."
}

& icacls $envPath /inheritance:r /grant:r "${currentUser}:F" "SYSTEM:F" | Out-Null
if ($LASTEXITCODE -ne 0) {
    throw "Falha ao proteger o arquivo .env.docker com ACLs locais."
}

Write-Host "Configuracao local criada. Credenciais: $credentialsPath"
Write-Host "Nenhuma chave de provedor foi adicionada."

if ($Start) {
    Push-Location $installPath
    try {
        & docker compose -f .\docker-compose.local-secure.yml up -d
        if ($LASTEXITCODE -ne 0) {
            throw "Falha ao iniciar o container 9Router."
        }
    }
    finally {
        Pop-Location
    }
}
