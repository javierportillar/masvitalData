# MasVital - Pipeline Refresh
#
# Wrapper que corre el pipeline + sube a R2.
# Disparado por Task Scheduler cada 30 min (07:00-19:30 hora local).
#
# Usage:
#   powershell -ExecutionPolicy Bypass -File infra\refresh.ps1

param(
    [switch]$DryRun = $false
)

$ErrorActionPreference = "Stop"
$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$logDir = Join-Path $repoRoot "infra\logs"
$logFile = Join-Path $logDir "refresh_$(Get-Date -Format yyyyMMdd).log"
$python = "python"

# Asegurar dir de logs
if (-not (Test-Path $logDir)) {
    New-Item -ItemType Directory -Path $logDir -Force | Out-Null
}

function Write-Log {
    param($Message, $Level = "INFO")
    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $line = "[$ts] [$Level] $Message"
    Write-Host $line
    Add-Content -Path $logFile -Value $line -Encoding UTF8
}

# Cargar .env
$envFile = Join-Path $repoRoot ".env"
if (Test-Path $envFile) {
    . (Join-Path $PSScriptRoot "load_env.ps1") -EnvFile $envFile
}

$env:PYTHONPATH = $repoRoot
$globalStart = Get-Date

try {
    # ── Step 1: Pipeline ────────────────────────────────────────────
    Write-Log "Iniciando pipeline (TENANT=$env:TENANT)..." "INFO"

    if ($DryRun) {
        Write-Log "DryRun: python -m pipeline.run_all" "INFO"
    } else {
        Push-Location $repoRoot
        & $python -m pipeline.run_all 2>&1 | Tee-Object -FilePath $logFile -Append
        $exitCode = $LASTEXITCODE
        Pop-Location

        if ($exitCode -ne 0) {
            throw "Pipeline fallo con exit code $exitCode"
        }
    }

    # ── Step 2: Upload a R2 ─────────────────────────────────────────
    Write-Log "Subiendo DuckDB a R2..." "INFO"

    if ($DryRun) {
        Write-Log "DryRun: python scripts/upload_duckdb_to_r2.py" "INFO"
    } else {
        Push-Location $repoRoot
        & $python scripts/upload_duckdb_to_r2.py 2>&1 | Tee-Object -FilePath $logFile -Append
        $exitCode = $LASTEXITCODE
        Pop-Location

        if ($exitCode -ne 0) {
            throw "Upload a R2 fallo con exit code $exitCode"
        }
    }

    # ── Step 3: Notificar a API (cache refresh) ─────────────────────
    if (-not $DryRun) {
        try {
            $apiUrl = $env:PLATFORM_API_URL
            $adminUser = $env:PLATFORM_ADMIN_USER
            $adminPass = $env:PLATFORM_ADMIN_PASSWORD
            if ($apiUrl -and $adminUser -and $adminPass) {
                Write-Log "Refrescando cache de API..." "INFO"
                $loginResp = Invoke-RestMethod -Uri "$apiUrl/api/auth/login" -Method Post `
                    -ContentType "application/json" `
                    -Body "{`"username`":`"$adminUser`",`"password`":`"$adminPass`"}" `
                    -ErrorAction SilentlyContinue
                if ($loginResp.access_token) {
                    $headers = @{
                        "Authorization" = "Bearer $($loginResp.access_token)"
                        "X-Tenant"      = $env:TENANT
                    }
                    $null = Invoke-RestMethod -Uri "$apiUrl/api/admin/data/refresh" `
                        -Method Post -Headers $headers -ErrorAction SilentlyContinue
                    Write-Log "API cache refrescado" "INFO"
                }
            }
        } catch {
            Write-Log "API refresh opcional fallo: $_" "WARN"
        }
    }

    $totalDur = [math]::Round(((Get-Date) - $globalStart).TotalSeconds, 1)
    Write-Log "Refresh completado exitosamente (${totalDur}s)" "OK"

} catch {
    Write-Log "Refresh failed: $_" "ERROR"
    exit 1
}
