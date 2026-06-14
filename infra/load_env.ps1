# Helper: carga .env como variables de sesion PowerShell
# Uso: . .\infra\load_env.ps1
#
# Busca .env en el repo root o en la ruta especificada.
# NO exporta secretos a procesos hijos (solo sesion actual).

param(
    [string]$EnvFile = (Join-Path (Split-Path $PSScriptRoot -Parent) ".env")
)

if (-not (Test-Path $EnvFile)) {
    Write-Warning "load_env: .env no encontrado en $EnvFile"
    return
}

Get-Content $EnvFile | ForEach-Object {
    if ($_ -match "^\s*([^#=]+)=(.*)$") {
        $key = $matches[1].Trim()
        $val = $matches[2].Trim('"', "'")
        Set-Item -Path "env:$key" -Value $val -ErrorAction SilentlyContinue
    }
}

Write-Host "[load_env] Variables cargadas desde $EnvFile"
