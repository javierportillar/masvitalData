# MasVital - Backup MySQL
#
# Ejecuta mysqldump y comprime con gzip.
# Output a C:\Backups\MasVital\backup_YYYYMMDD.sql.gz.
# Retencion: 14 dias (borra backups anteriores).
#
# Usage:
#   powershell -ExecutionPolicy Bypass -File infra\backup_mysql.ps1

param(
    [string]$BackupDir = "C:\Backups\MasVital",
    [string]$MySQLHost = "localhost",
    [int]$Port = 3306,
    [string]$User = "api_read",
    [string]$Password = "",
    [string]$Database = "",
    [int]$RetentionDays = 14,
    [switch]$Simular
)

# Modo simulacion: no hace dump ni borra nada, solo dice que archivos quedarian
# fuera por antiguedad. Se usa para que el operador autorice la limpieza.
function Get-BackupsVencidos {
    param([string]$Dir, [int]$Dias, [string]$Excepto)

    if (-not (Test-Path $Dir)) { return @() }
    $limite = (Get-Date).AddDays(-$Dias)
    # El fallback .NET comprime con GZipStream pero guarda con extension .zip:
    # si la retencion mira solo *.sql.gz, esos archivos no se purgan nunca.
    Get-ChildItem -Path $Dir -File |
        Where-Object {
            ($_.Extension -eq ".gz" -or $_.Extension -eq ".zip") -and
            $_.LastWriteTime -lt $limite -and
            $_.Name -ne $Excepto
        } |
        Sort-Object LastWriteTime
}

if ($Simular) {
    $vencidos = @(Get-BackupsVencidos -Dir $BackupDir -Dias $RetentionDays -Excepto "")
    Write-Host "MODO SIMULACION - no se borra nada."
    Write-Host "Directorio: $BackupDir"
    Write-Host "Retencion: $RetentionDays dias (corte: $((Get-Date).AddDays(-$RetentionDays).ToString('yyyy-MM-dd HH:mm')))"
    if ($vencidos.Count -eq 0) {
        Write-Host "  (ningun backup vencido: no borraria nada)"
    } else {
        foreach ($f in $vencidos) {
            Write-Host ("  borraria: {0} | {1:N2} MB | {2}" -f $f.Name, ($f.Length / 1MB), $f.LastWriteTime.ToString("yyyy-MM-dd HH:mm"))
        }
        $mb = [math]::Round((($vencidos | Measure-Object Length -Sum).Sum) / 1MB, 2)
        Write-Host ("  total: {0} archivo(s), {1} MB" -f $vencidos.Count, $mb)
    }
    exit 0
}

if (-not (Get-Command mysqldump -ErrorAction SilentlyContinue)) {
    Write-Error "mysqldump no encontrado. Verifica que MySQL este en el PATH."
    exit 1
}

# Intentar leer .env si no se pasaron parametros
$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$envFile = Join-Path $repoRoot ".env"
if (Test-Path $envFile) {
    Get-Content $envFile | ForEach-Object {
        if ($_ -match "^\s*MYSQL_(HOST|PORT|USER|PASSWORD|DATABASE)=(.*)$") {
            $key = "MYSQL_$($matches[1])"
            $val = $matches[2].Trim('"', "'")
            Set-Item -Path "env:$key" -Value $val -ErrorAction SilentlyContinue
        }
    }
    if (-not $Password) { $Password = $env:MYSQL_PASSWORD }
    if (-not $Database) { $Database = $env:MYSQL_DATABASE }
}

if (-not $Database) {
    Write-Error "MYSQL_DATABASE no definida. Pasa -Database o configura .env"
    exit 1
}

# Crear directorio si no existe
if (-not (Test-Path $BackupDir)) {
    New-Item -ItemType Directory -Path $BackupDir -Force | Out-Null
}

$Timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$OutFile = Join-Path $BackupDir "${Database}_${Timestamp}.sql.gz"

Write-Host "Origen:  $User@$MySQLHost`:$Port/$Database"
Write-Host "Destino: $OutFile"

$mysqldumpArgs = @(
    "--host=$MySQLHost"
    "--port=$Port"
    "--user=$User"
    "--lock-tables"
    "--routines"
    "--triggers"
    "--default-character-set=utf8"
    $Database
)

if ($Password) {
    $mysqldumpArgs += "--password=$Password"
}

$Start = Get-Date
Write-Host "Iniciando mysqldump..."

$tempFile = Join-Path $env:TEMP "masvital_dump_$([System.Guid]::NewGuid().ToString('N')).sql"
$result = & mysqldump @mysqldumpArgs 2>&1
$exitCode = $LASTEXITCODE

if ($exitCode -ne 0) {
    Write-Host "ERROR de mysqldump ($exitCode):"
    $result | ForEach-Object { Write-Host "  $_" }
    exit 2
}

$result | Where-Object { $_ -is [string] } | Out-File -FilePath $tempFile -Encoding utf8
if (-not (Test-Path $tempFile) -or ((Get-Item $tempFile).Length -eq 0)) {
    Write-Error "No se creo el archivo de dump o esta vacio"
    exit 3
}

Write-Host "Dump completado ($((Get-Item $tempFile).Length) bytes). Comprimiendo..."

# Comprimir con gzip o fallback .NET
$compressOk = $false
if (Get-Command gzip -ErrorAction SilentlyContinue) {
    $gzOut = & gzip -9 -c $tempFile 2>&1
    $gzExit = $LASTEXITCODE
    if ($gzExit -eq 0) {
        [System.IO.File]::WriteAllBytes($OutFile, [System.Text.Encoding]::UTF8.GetBytes($gzOut))
        $compressOk = $true
    } else {
        Write-Host "gzip fallo (codigo $gzExit), usando fallback .NET..."
    }
}
if (-not $compressOk) {
    Write-Host "Usando compresion nativa .NET (GZipStream)..."
    $zipFile = [System.IO.Path]::ChangeExtension($OutFile, ".zip")
    $fsIn = [System.IO.File]::OpenRead($tempFile)
    $fsOut = [System.IO.File]::Create($zipFile)
    $gzs = New-Object System.IO.Compression.GZipStream $fsOut, ([System.IO.Compression.CompressionMode]::Compress)
    $fsIn.CopyTo($gzs)
    $gzs.Close(); $fsOut.Close(); $fsIn.Close()
    $OutFile = $zipFile
}
Remove-Item $tempFile

$End = Get-Date
$Duration = [math]::Round(($End - $Start).TotalSeconds, 0)
$Size = [math]::Round((Get-Item $OutFile).Length / 1MB, 2)

Write-Host "Tamano:   ${Size}MB"
Write-Host "Duracion: ${Duration}s"

# Verificar integridad
if ($OutFile -like "*.gz" -and (Get-Command gzip -ErrorAction SilentlyContinue)) {
    Write-Host "Verificando integridad..."
    $null = & gzip -t $OutFile 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "OK - integridad verificada"
    } else {
        Write-Host "Advertencia: fallo verificacion de integridad"
    }
}

# Limpiar backups antiguos (incluye los .zip del fallback .NET)
Write-Host "Limpiando backups anteriores a $RetentionDays dias..."
$vencidos = @(Get-BackupsVencidos -Dir $BackupDir -Dias $RetentionDays -Excepto (Split-Path $OutFile -Leaf))
foreach ($f in $vencidos) {
    Remove-Item $f.FullName -Force
    Write-Host "  Eliminado: $($f.Name)"
}

Write-Host ""
Write-Host "Backup completado:"
Write-Host "  archivo:  $OutFile"
Write-Host "  tamano:   ${Size}MB"
Write-Host "  duracion: ${Duration}s"
