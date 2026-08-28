[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [Parameter()]
    [string]$Source = (Split-Path -Parent $PSScriptRoot),

    [Parameter()]
    [ValidateSet('Codex', 'OpenCode', 'Antigravity', 'Universal')]
    [string[]]$Target = @('Codex', 'OpenCode', 'Antigravity', 'Universal'),

    [Parameter()]
    [switch]$Update
)

$ErrorActionPreference = 'Stop'
$skillName = 'ai-issue-router'
$sourcePath = (Resolve-Path -LiteralPath $Source).Path
$skillFile = Join-Path $sourcePath 'SKILL.md'

if (-not (Test-Path -LiteralPath $skillFile -PathType Leaf)) {
    throw "SKILL.md não encontrado em $sourcePath"
}

$targetRoots = @{
    Codex = Join-Path $env:USERPROFILE '.codex\skills'
    OpenCode = Join-Path $env:USERPROFILE '.config\opencode\skills'
    Antigravity = Join-Path $env:USERPROFILE '.gemini\skills'
    Universal = Join-Path $env:USERPROFILE '.agents\skills'
}

function Get-TreeManifest {
    param([Parameter(Mandatory)][string]$Path)

    $root = (Resolve-Path -LiteralPath $Path).Path
    $manifest = @{}
    Get-ChildItem -LiteralPath $root -Recurse -File | ForEach-Object {
        $relative = $_.FullName.Substring($root.Length).TrimStart('\')
        $manifest[$relative] = (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash
    }
    return $manifest
}

function Test-ManifestsEqual {
    param(
        [Parameter(Mandatory)][hashtable]$Left,
        [Parameter(Mandatory)][hashtable]$Right
    )

    if ($Left.Count -ne $Right.Count) { return $false }
    foreach ($key in $Left.Keys) {
        if (-not $Right.ContainsKey($key) -or $Left[$key] -ne $Right[$key]) {
            return $false
        }
    }
    return $true
}

$sourceManifest = Get-TreeManifest -Path $sourcePath
$results = @()

foreach ($targetName in $Target) {
    $destinationRoot = $targetRoots[$targetName]
    $destination = Join-Path $destinationRoot $skillName

    if (Test-Path -LiteralPath $destination) {
        $destinationManifest = Get-TreeManifest -Path $destination
        if (Test-ManifestsEqual -Left $sourceManifest -Right $destinationManifest) {
            $results += [pscustomobject]@{
                target = $targetName
                path = $destination
                status = 'already_synchronized'
                backup = $null
            }
            continue
        }
        if (-not $Update) {
            throw "Destino existente e diferente: $destination. Use -Update para criar backup e atualizar."
        }
    }

    if ($PSCmdlet.ShouldProcess($destination, "Instalar $skillName")) {
        New-Item -ItemType Directory -Path $destinationRoot -Force | Out-Null
        $backup = $null
        if (Test-Path -LiteralPath $destination) {
            $stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
            $backup = "$destination.backup-$stamp"
            Copy-Item -LiteralPath $destination -Destination $backup -Recurse
        } else {
            New-Item -ItemType Directory -Path $destination | Out-Null
        }

        Copy-Item -Path (Join-Path $sourcePath '*') -Destination $destination -Recurse -Force
        $installedManifest = Get-TreeManifest -Path $destination
        if (-not (Test-ManifestsEqual -Left $sourceManifest -Right $installedManifest)) {
            throw "Verificação de hashes falhou em $destination"
        }

        $results += [pscustomobject]@{
            target = $targetName
            path = $destination
            status = 'installed_and_verified'
            backup = $backup
        }
    }
}

$results | ConvertTo-Json -Depth 4
