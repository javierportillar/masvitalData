# MasVital - Dump to Cloud (alias para refresh.ps1)
#
# Script de compatibilidad. Ejecuta el pipeline completo + upload a R2.
# Disparado por Task Scheduler cada 30 min.
#
# Usage:
#   powershell -ExecutionPolicy Bypass -File infra\dump_to_cloud.ps1

& (Join-Path $PSScriptRoot "refresh.ps1") @args
