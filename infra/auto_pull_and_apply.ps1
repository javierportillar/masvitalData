# MasVital - Auto-Pull and Apply (Windows)
#
# Espejo del de motoshopData pero adaptado al repo masvitalData.
#
# Logica:
#   1. git fetch origin main
#   2. Compara HEAD local vs origin/main
#   3. Si difieren, hace git pull + detecta que cambio
#   4. Si cambio pipeline/** -> log "codigo nuevo, proximo run lo usa"
#   5. Si cambio infra/** -> log + considerar reiniciar Task si toco scripts
#   6. Si cambio .env.example -> log WARN ("revisar .env local manualmente")
#   7. Log resultado a infra\logs\auto_pull.log
#
# Disparado por Scheduled Task cada 5 min.
#
# Manual run:
#   powershell -ExecutionPolicy Bypass -File infra\auto_pull_and_apply.ps1
#
# Para deshabilitar (mantenimiento):
#   Crear archivo infra\AUTO_PULL_DISABLED

param(
    [switch]$DryRun = $false
)

$ErrorActionPreference = "Continue"
$RepoRoot = "C:\Users\MasVital\Documents\masvitalData"
$LogFile = "$RepoRoot\infra\logs\auto_pull.log"
$DisableFlag = "$RepoRoot\infra\AUTO_PULL_DISABLED"
$LockFile = "$RepoRoot\infra\auto_pull.lock"

function Log {
    param([string]$Level, [string]$Message)
    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $line = "[$ts] [$Level] $Message"
    Add-Content -Path $LogFile -Value $line -Encoding UTF8
}

# ─── Pre-flight ─────────────────────────────────────────────

if (!(Test-Path $RepoRoot)) {
    Log "ERROR" "Repo root no existe: $RepoRoot"
    exit 1
}

New-Item -ItemType Directory -Path "$RepoRoot\infra\logs" -Force | Out-Null

if (Test-Path $DisableFlag) {
    Log "INFO" "AUTO_PULL_DISABLED flag presente. Aborting."
    exit 0
}

if (Test-Path $LockFile) {
    $lockAge = (Get-Date) - (Get-Item $LockFile).LastWriteTime
    if ($lockAge.TotalMinutes -lt 10) {
        Log "WARN" "Lock file presente (otra instancia corriendo o stale). Aborting."
        exit 0
    } else {
        Log "WARN" "Lock file stale (>10min). Removing."
        Remove-Item $LockFile -Force
    }
}
New-Item -ItemType File -Path $LockFile | Out-Null

try {
    Set-Location $RepoRoot

    # ─── Fetch origin ────────────────────────────────────────
    Log "INFO" "Fetching origin..."
    $fetchOutput = git fetch origin main 2>&1
    if ($LASTEXITCODE -ne 0) {
        Log "ERROR" "git fetch fallo: $fetchOutput"
        exit 1
    }

    $localHead = git rev-parse HEAD
    $remoteHead = git rev-parse origin/main

    if ($localHead -eq $remoteHead) {
        Log "INFO" "Up-to-date (HEAD=$($localHead.Substring(0,7))). Nothing to do."
        exit 0
    }

    Log "INFO" "Updates detected: local=$($localHead.Substring(0,7)) -> remote=$($remoteHead.Substring(0,7))"

    # ─── Detectar que cambio ─────────────────────────────────
    $changedFiles = git diff --name-only $localHead $remoteHead 2>&1
    if ($LASTEXITCODE -ne 0) {
        Log "ERROR" "git diff fallo: $changedFiles"
        exit 1
    }

    $pipelineChanged = $changedFiles | Where-Object { $_ -match "^pipeline/" }
    $infraScriptsChanged = $changedFiles | Where-Object { $_ -match "^infra/.*\.ps1$" }
    $envExampleChanged = $changedFiles | Where-Object { $_ -match "^\.env\.example$" }

    Log "INFO" "Changed files: $($changedFiles.Count). Pipeline=$($pipelineChanged.Count), infra-scripts=$($infraScriptsChanged.Count), env-example=$($envExampleChanged.Count)"

    if ($DryRun) {
        Log "INFO" "DryRun mode. No changes applied."
        $changedFiles | ForEach-Object { Log "INFO" "  Would pull: $_" }
        exit 0
    }

    # ─── Pull ────────────────────────────────────────────────
    Log "INFO" "Pulling..."
    $pullOutput = git pull --ff-only origin main 2>&1
    if ($LASTEXITCODE -ne 0) {
        Log "ERROR" "git pull fallo (no es fast-forward?): $pullOutput"
        exit 1
    }
    Log "INFO" "Pull OK"

    # ─── Notificar cambios relevantes ─────────────────────────
    if ($pipelineChanged.Count -gt 0) {
        Log "INFO" "Pipeline code changed ($($pipelineChanged.Count) files). Next pipeline run will use new code."
    }

    if ($infraScriptsChanged.Count -gt 0) {
        Log "WARN" "Infra scripts changed ($($infraScriptsChanged.Count) files). Consider restarting Task Scheduler tasks."
        $infraScriptsChanged | ForEach-Object { Log "WARN" "  $_" }
    }

    if ($envExampleChanged.Count -gt 0) {
        Log "WARN" ".env.example changed. Check your local .env for new required variables."
    }

    Log "INFO" "Auto-apply COMPLETE. New HEAD=$($remoteHead.Substring(0,7))"

} catch {
    Log "ERROR" "Excepcion no manejada: $_"
    Log "ERROR" $_.ScriptStackTrace
    exit 1
} finally {
    if (Test-Path $LockFile) {
        Remove-Item $LockFile -Force -ErrorAction SilentlyContinue
    }
}
