# MasVital - Start Pipeline (ejecucion unica)
#
# Corre una sola vez el pipeline ETL sin upload a R2.
# Util para pruebas manuales o debugging.
#
# Usage:
#   powershell -ExecutionPolicy Bypass -File infra\start_pipeline.ps1

$ErrorActionPreference = "Stop"
$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")

# Cargar .env
. (Join-Path $PSScriptRoot "load_env.ps1")

$env:PYTHONPATH = $repoRoot

Push-Location $repoRoot
try {
    Write-Host "Iniciando pipeline ETL para tenant: $env:TENANT"
    python -m pipeline.run_all
    $exitCode = $LASTEXITCODE
    if ($exitCode -eq 0) {
        Write-Host "Pipeline completado exitosamente"
    } else {
        Write-Host "Pipeline fallo con exit code $exitCode"
        exit $exitCode
    }
} finally {
    Pop-Location
}
