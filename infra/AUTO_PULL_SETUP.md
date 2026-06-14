# MasVital - Auto-Pull Setup (Task Scheduler)

Configurar la Scheduled Task de Windows para que `auto_pull_and_apply.ps1` corra cada 5 minutos.

## Pasos

1. Abrir **Task Scheduler** como Administrador.
2. Crear nueva tarea:
   - **Nombre:** `MasVital Auto-Pull`
   - **Ejecutar con:** `NT AUTHORITY\SYSTEM` (o el usuario que ejecuta el pipeline)
   - **Configurar para:** Windows 10/11
3. **Trigger:**
   - **Iniciar tarea:** `En un programacion`
   - **Repetir cada:** `5 minutos`
   - **Duración:** `Indefinidamente`
   - **Habilitado:** ✅
4. **Action:**
   - **Programa/script:** `powershell.exe`
   - **Argumentos:**
     ```
     -ExecutionPolicy Bypass -File "C:\Users\MasVital\Documents\masvitalData\infra\auto_pull_and_apply.ps1"
     ```
   - **Iniciar en:** `C:\Users\MasVital\Documents\masvitalData`
5. **Conditions:**
   - Desmarcar "Detener si el equipo cambia a bateria"
   - Marcar "Ejecutar incluso si no hay conexion de red" (se necesita red para git pull, pero que no falle si no hay)
6. **Settings:**
   - Marcar "Permitir ejecucion bajo demanda"
   - Marcar "Ejecutar la tarea lo antes posible si no se inicia programada"
   - Marcar "Si la tarea falla, reiniciar cada 5 minutos"

## Deshabilitar temporalmente

Crear archivo `infra\AUTO_PULL_DISABLED` en el repo. Mientras exista, el script aborta sin hacer nada.

Para re-habilitar, eliminar el archivo.

## Verificar logs

Los logs se escriben en `infra\logs\auto_pull.log`. Verificar contenido para confirmar que corre:
```
[2026-06-14 07:00:01] [INFO] Fetching origin...
[2026-06-14 07:00:02] [INFO] Up-to-date (HEAD=abc1234). Nothing to do.
```
