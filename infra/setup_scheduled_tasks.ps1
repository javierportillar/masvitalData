# MasVital — Configurar Scheduled Tasks
#
# Crea (o actualiza) las dos tareas programadas en la PC MasVital:
#   1. MasVital Auto-Pull:   cada 5 min  — git fetch + pull automático
#   2. MasVital Refresh:     cada 30 min — pipeline + upload + API refresh
#
# Ejecutar COMO ADMINISTRADOR en la PC MasVital:
#   powershell -ExecutionPolicy Bypass -File infra\setup_scheduled_tasks.ps1
#
# Para SOLO ver el estado actual (sin modificar):
#   powershell -ExecutionPolicy Bypass -File infra\setup_scheduled_tasks.ps1 -DryRun

param(
    [switch]$DryRun = $false
)

$ErrorActionPreference = "Stop"

# ─── Config ──────────────────────────────────────────────────────────────────
$RepoDir = "C:\Users\MasVital\Documents\masvitalData"
$PythonExe = Join-Path $RepoDir ".venv\Scripts\python.exe"

# ─── Helper ───────────────────────────────────────────────────────────────────
function Write-Info  { Write-Host "[INFO]  $($args -join ' ')" }
function Write-Ok    { Write-Host "[OK]    $($args -join ' ')" -ForegroundColor Green }
function Write-Warn  { Write-Host "[WARN]  $($args -join ' ')" -ForegroundColor Yellow }
function Write-Error { Write-Host "[ERROR] $($args -join ' ')" -ForegroundColor Red }

function Ensure-Task {
    param(
        [string]$TaskName,
        [string]$Description,
        [string]$ScriptPath,
        [string]$RepetitionInterval,
        [string]$StartTime = "06:00"
    )

    $fullPath = Join-Path $RepoDir $ScriptPath
    $actionArgs = "-ExecutionPolicy Bypass -File `"$fullPath`""
    $workingDir = $RepoDir

    if ($DryRun) {
        Write-Info "[DryRun] Crearía/actualizaría tarea: $TaskName"
        Write-Info "  Script: powershell.exe $actionArgs"
        Write-Info "  Cada: $RepetitionInterval"
        Write-Info "  Desde: $RepoDir"
        return
    }

    # Verificar que el script existe
    if (-not (Test-Path $fullPath)) {
        Write-Warn "Script no encontrado: $fullPath — saltando tarea $TaskName"
        return
    }

    # Construir XML de trigger para repetición infinita
    $triggerXml = @"
<Triggers>
    <CalendarTrigger>
        <StartBoundary>$(Get-Date $StartTime -Format "yyyy-MM-dd'T'HH:mm:ss")</StartBoundary>
        <Repetition>
            <Interval>$RepetitionInterval</Interval>
            <Duration>P1D</Duration>
            <StopAtDurationEnd>false</StopAtDurationEnd>
        </Repetition>
        <Enabled>true</Enabled>
    </CalendarTrigger>
</Triggers>
"@

    try {
        # Intentar crear/actualizar
        $params = @(
            "/Create", "/TN", "`"$TaskName`"",
            "/TR", "`"powershell.exe $actionArgs`"",
            "/SC", "MINUTE",
            "/MO", "1",
            "/DU", "P1D",
            "/F",  # force: overwrite if exists
            "/IT", # run only when user is logged on
            "/RL", "HIGHEST",
            "/NP"  # no preserve (no password prompt)
        )

        # No podemos pasar el XML de trigger fácilmente via schtasks.
        # Mejor: crear una tarea simple y luego actualizar el trigger via XML.
        # Pero el enfoque más portable es directamente vía COM.
        $sch = New-Object -ComObject "Schedule.Service"
        $sch.Connect()
        $root = $sch.GetFolder("\")

        # Eliminar si existe (para recrear limpia)
        try {
            $existing = $root.GetTask($TaskName)
            if ($existing) {
                Write-Info "Tarea '$TaskName' ya existe — se va a reemplazar"
                $root.DeleteTask($TaskName, 0)
            }
        } catch {
            # No existe, sigue
        }

        # Crear tarea
        $task = $sch.NewTask(0)
        $task.RegistrationInfo.Description = $Description

        # Settings
        $task.Settings.DisallowStartIfOnBatteries = $false
        $task.Settings.StopIfGoingOnBatteries = $false
        $task.Settings.ExecutionTimeLimit = "PT1H"  # 1 hora máximo
        $task.Settings.Priority = 5  # normal
        $task.Settings.Enabled = $true
        $task.Settings.AllowDemandStart = $true
        $task.Settings.StartWhenAvailable = $true
        $task.Settings.RestartCount = 3
        $task.Settings.RestartInterval = "PT5M"

        # Trigger: repetición
        $trigger = $task.Triggers.Create(1)  # TASK_TRIGGER_DAILY
        $trigger.StartBoundary = "$(Get-Date $StartTime -Format "yyyy-MM-dd'T'HH:mm:ss")"
        $trigger.DaysInterval = 1
        $trigger.Repetition.Interval = $RepetitionInterval
        $trigger.Repetition.Duration = "P1D"
        $trigger.Repetition.StopAtDurationEnd = $false
        $trigger.Enabled = $true

        # Action
        $action = $task.Actions.Create(0)  # TASK_ACTION_EXEC
        $action.Path = "powershell.exe"
        $action.Arguments = $actionArgs
        $action.WorkingDirectory = $workingDir

        # Registrar
        $root.RegisterTaskDefinition(
            $TaskName,
            $task,
            1,   # TASK_CREATE_OR_UPDATE
            $null,  # user
            $null,  # password
            4       # TASK_LOGON_NONE (run whether logged on or not)
        )

        Write-Ok "Tarea '$TaskName' creada/actualizada (cada $RepetitionInterval)"
    } catch {
        Write-Error "Falló al crear tarea '$TaskName': $_"
        Write-Info "Podés crearla manualmente siguiendo infra/AUTO_PULL_SETUP.md"
    }
}

# ─── Main ────────────────────────────────────────────────────────────────────

Write-Info "=== MasVital — Setup Scheduled Tasks ==="
Write-Info "Repositorio: $RepoDir"
Write-Info ""

# Verificar que el directorio del repo existe
if (-not (Test-Path $RepoDir)) {
    Write-Warn "Repo dir no encontrado en $RepoDir"
    Write-Info "Editá `$RepoDir` al inicio de este script con la ruta correcta"
    if (-not $DryRun) { exit 1 }
}

# ─── Tarea 1: Auto-Pull (cada 5 min) ─────────────────────────────────────────
Ensure-Task -TaskName "MasVital Auto-Pull" `
    -Description "Auto-pull de masvitalData cada 5 minutos. Corre infra\auto_pull_and_apply.ps1" `
    -ScriptPath "infra\auto_pull_and_apply.ps1" `
    -RepetitionInterval "PT5M" `
    -StartTime "06:00"

# ─── Tarea 2: Pipeline Refresh (cada 30 min) ─────────────────────────────────
Ensure-Task -TaskName "MasVital Refresh" `
    -Description "Pipeline ETL + upload R2 + refresh API cada 30 minutos. Corre infra\refresh.ps1" `
    -ScriptPath "infra\refresh.ps1" `
    -RepetitionInterval "PT30M" `
    -StartTime "06:00"

Write-Info ""
Write-Info "=== Hecho ==="
Write-Info "Verificá las tareas en Task Scheduler > Task Scheduler Library > MasVital*"
