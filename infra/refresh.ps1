# MasVital - Pipeline Refresh (v15-style)
#
# Corre el pipeline + sube a R2 + loguea cada step a pipeline_runs.duckdb.
# Disparado por Task Scheduler cada 30 min (07:00-19:30 hora local).
#
# Usage:
#   powershell -ExecutionPolicy Bypass -File infra\refresh.ps1
#   powershell -ExecutionPolicy Bypass -File infra\refresh.ps1 -DryRun

param(
    [switch]$DryRun = $false
)

$ErrorActionPreference = "Stop"
$logFile = Join-Path $PSScriptRoot "logs\refresh.log"
$rootDir = Resolve-Path (Join-Path $PSScriptRoot "..")
$venvPython = Join-Path $rootDir ".venv\Scripts\python.exe"
$python = if (Test-Path $venvPython) { $venvPython } else { "python" }
$dbHelper = Join-Path $rootDir "scripts\pipeline_runs_db.py"
$uploadScript = Join-Path $rootDir "scripts\upload_duckdb_to_r2.py"

# ── Helpers de logging a archivo ──────────────────────────────────────────────
function Write-Log {
    param($Message, $Level = "INFO")
    $ts = (Get-Date -Format "yyyy-MM-dd HH:mm:ss")
    $line = "[$ts] [$Level] $Message"
    Write-Host $line
    Add-Content -Path $logFile -Value $line
}

# ── Helpers de logging a DuckDB (pipeline_runs.duckdb) ───────────────────────
$global:RunId = $null

function Invoke-DB {
    param([string]$Arguments)
    $argList = @($dbHelper) + ($Arguments -split ' ')
    $result = & $python $argList 2>&1
    $exitCode = $LASTEXITCODE
    $lastLine = ($result | Select-Object -Last 1) -join "`n"
    if ($exitCode -ne 0) {
        Write-Log "pipeline_runs_db.py failed: $($lastLine -replace '\s+', ' ')" "WARN"
        return $null
    }
    return $lastLine.Trim()
}

function Start-PipelineRun {
    param($PipelineName, $TriggeredBy)
    $id = Invoke-DB "start-run --pipeline $PipelineName --triggered-by $TriggeredBy"
    if ($id -match '^\d+$') {
        $global:RunId = [int]$id
        Write-Log "Pipeline run #$global:RunId creado en pipeline_runs.duckdb"
        return $global:RunId
    }
    Write-Log "No se pudo crear pipeline run en DuckDB" "WARN"
    return $null
}

function Start-PipelineStep {
    param($StepOrder, $StepName)
    if (-not $global:RunId) { return $null }
    $id = Invoke-DB "start-step --run-id $global:RunId --step-order $StepOrder --step-name $StepName"
    if ($id -match '^\d+$') { return [int]$id }
    return $null
}

function Complete-PipelineStep {
    param($StepId, $DurationSeconds, $LogExcerpt, $Status = "success", $ErrorMessage = $null)
    if (-not $StepId) { return }
    $env:PIPELINE_DB_LOG_EXCERPT = if ($LogExcerpt) { ($LogExcerpt -replace '[^\x20-\x7E\r\n\t]', ' ').Substring(0, [math]::Min($LogExcerpt.Length, 8000)) } else { '' }
    $env:PIPELINE_DB_ERROR_MSG = if ($ErrorMessage) { ($ErrorMessage -replace '[^\x20-\x7E\r\n\t]', ' ') } else { '' }
    Invoke-DB "complete-step --step-id $StepId --duration $DurationSeconds --status $Status"
    Remove-Item "env:PIPELINE_DB_LOG_EXCERPT" -ErrorAction SilentlyContinue
    Remove-Item "env:PIPELINE_DB_ERROR_MSG" -ErrorAction SilentlyContinue
}

function Complete-PipelineRun {
    param($DurationSeconds, $Status = "success", $ErrorMessage = $null)
    if (-not $global:RunId) { return }
    $env:PIPELINE_DB_ERROR_MSG = if ($ErrorMessage) { ($ErrorMessage -replace '[^\x20-\x7E\r\n\t]', ' ') } else { '' }
    Invoke-DB "complete-run --run-id $global:RunId --duration $DurationSeconds --status $Status"
    Remove-Item "env:PIPELINE_DB_ERROR_MSG" -ErrorAction SilentlyContinue
}

# ── Helper: ejecutar step con medicion + captura de output ───────────────────
function Invoke-Step {
    param(
        [scriptblock]$ScriptBlock,
        [string]$StepName,
        [int]$StepOrder
    )
    $stepId = Start-PipelineStep -StepOrder $StepOrder -StepName $StepName
    $stepStart = Get-Date
    $logDir = Split-Path $logFile -Parent
    $stepLog = Join-Path $logDir "step_${StepName}.tmp"
    $savedEA = $ErrorActionPreference

    try {
        $ErrorActionPreference = "Continue"
        & $ScriptBlock *> $stepLog
        $exitCode = $LASTEXITCODE
        $ErrorActionPreference = $savedEA
        $dur = [math]::Max(0, [math]::Round(((Get-Date) - $stepStart).TotalSeconds, 1))
        $excerptLines = Get-Content $stepLog -Tail 50 -ErrorAction SilentlyContinue
        $excerpt = $excerptLines -join "`n"

        if ($exitCode -ne 0) {
            Complete-PipelineStep -StepId $stepId -DurationSeconds $dur -LogExcerpt $excerpt -Status "failed" -ErrorMessage "Exit code $exitCode"
            throw "$StepName failed with exit code $exitCode"
        }

        Complete-PipelineStep -StepId $stepId -DurationSeconds $dur -LogExcerpt $excerpt -Status "success"
        Write-Log "$StepName completed (${dur}s)" "OK"
    } catch {
        $ErrorActionPreference = $savedEA
        if ($stepId) {
            $dur = [math]::Max(0, [math]::Round(((Get-Date) - $stepStart).TotalSeconds, 1))
            $excerptLines = if (Test-Path $stepLog) { Get-Content $stepLog -Tail 50 -ErrorAction SilentlyContinue } else { @() }
            $excerpt = $excerptLines -join "`n"
            Complete-PipelineStep -StepId $stepId -DurationSeconds $dur -LogExcerpt $excerpt -Status "failed" -ErrorMessage $_.Exception.Message
        }
        throw
    } finally {
        $ErrorActionPreference = $savedEA
        if (Test-Path $stepLog) { Remove-Item $stepLog -Force -ErrorAction SilentlyContinue }
    }
}

# ── Main ─────────────────────────────────────────────────────────────────────
$logDir = Split-Path $logFile -Parent
if (-not (Test-Path $logDir)) {
    New-Item -ItemType Directory -Path $logDir -Force | Out-Null
}

# Cargar .env
$envFile = Join-Path $PSScriptRoot "..\.env"
if (Test-Path $envFile) {
    . (Join-Path $PSScriptRoot "load_env.ps1") -EnvFile $envFile
}

$env:PYTHONPATH = $rootDir
$globalStart = Get-Date

# Inicializar run en DuckDB
if (-not $DryRun) {
    Start-PipelineRun -PipelineName "run_all" -TriggeredBy "scheduled"
} else {
    Write-Log "DryRun: pipeline run logging skipped" "INFO"
}

try {
    $stepOrder = 0

    # ── Step 1: Pipeline (run_all.py) ─────────────────────────────────────
    $stepOrder++
    if ($DryRun) {
        Write-Log "DryRun: python -m pipeline.run_all" "INFO"
    } else {
        Invoke-Step -StepOrder $stepOrder -StepName "run_all" -ScriptBlock {
            & $python -m pipeline.run_all
        }
    }

    if (-not $DryRun) {
        # ── Cerrar run (local) ANTES de publicar a R2 ─────────────────────
        $totalDur = [math]::Round(((Get-Date) - $globalStart).TotalSeconds, 1)
        Complete-PipelineRun -DurationSeconds $totalDur -Status "success"
        Write-Log "Pipeline completado (${totalDur}s)" "OK"
    }

    # ── Publicar AMBOS DuckDB a R2 ────────────────────────────────────────
    if ($DryRun) {
        Write-Log "DryRun: python scripts/upload_duckdb_to_r2.py" "INFO"
    } else {
        Write-Log "Subiendo DuckDBs a R2..." "INFO"
        $result = & $python $uploadScript 2>&1
        if ($LASTEXITCODE -ne 0) {
            throw "Upload a R2 falló: $($result[-1])"
        }
        Write-Log "Upload a R2 completado" "OK"
    }

    # ── Refrescar API ─────────────────────────────────────────────────────
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
                    $null = Invoke-RestMethod -Uri "$apiUrl/api/admin/pipeline/refresh" `
                        -Method Post -Headers $headers -ErrorAction SilentlyContinue
                    Write-Log "API cache y pipeline refresh completados" "INFO"
                }
            }
        } catch {
            Write-Log "API refresh opcional falló: $_" "WARN"
        }
    }

    if (-not $DryRun) {
        Write-Log "Refresh completado exitosamente" "OK"
    }

} catch {
    $err = $_.Exception.Message
    Write-Log "Refresh failed: $err" "ERROR"
    if (-not $DryRun) {
        $totalDur = [math]::Round(((Get-Date) - $globalStart).TotalSeconds, 1)
        Complete-PipelineRun -DurationSeconds $totalDur -Status "failed" -ErrorMessage $err

        # Publicar incluso en falla para que el estado sea visible en API
        & $python $uploadScript 2>$null
        try {
            $apiUrl = $env:PLATFORM_API_URL
            $adminUser = $env:PLATFORM_ADMIN_USER
            $adminPass = $env:PLATFORM_ADMIN_PASSWORD
            if ($apiUrl -and $adminUser -and $adminPass) {
                $loginResp = Invoke-RestMethod -Uri "$apiUrl/api/auth/login" -Method Post `
                    -ContentType "application/json" `
                    -Body "{`"username`":`"$adminUser`",`"password`":`"$adminPass`"}"
                if ($loginResp.access_token) {
                    $headers = @{
                        "Authorization" = "Bearer $($loginResp.access_token)"
                        "X-Tenant"      = $env:TENANT
                    }
                    $null = Invoke-RestMethod -Uri "$apiUrl/api/admin/data/refresh" -Method Post -Headers $headers -ErrorAction SilentlyContinue
                    $null = Invoke-RestMethod -Uri "$apiUrl/api/admin/pipeline/refresh" -Method Post -Headers $headers -ErrorAction SilentlyContinue
                }
            }
        } catch { }
    }
    exit 1
}
