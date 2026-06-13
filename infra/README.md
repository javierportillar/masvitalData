# infra/ · Scripts PowerShell operativos (placeholder)

> **Estado:** Vacío. Se puebla en Sprint M3.5 por **Dev Back**.

---

## Qué va a vivir acá (después de M3.5)

| Archivo | Función | Cuándo se ejecuta |
|---|---|---|
| `load_env.ps1` | Parsea `.env` y carga variables a la sesión PowerShell actual. | Helper invocado por todos los demás scripts |
| `refresh.ps1` | Pipeline + upload R2 + log a `logs/refresh_YYYYMMDD.log`. | Task Scheduler cada 30 min entre 07:00-19:30 |
| `auto_pull_and_apply.ps1` | `git fetch + pull` si hay commits nuevos. Detecta cambios y notifica. | Task Scheduler cada 5 min entre 06:00-20:00 |
| `backup_mysql.ps1` | `mysqldump` con compresión gzip a `C:\Backups\MasVital\backup_YYYYMMDD.sql.gz`. Retención 14 días. | Task Scheduler 02:00 diario |
| `check_health.ps1` | Verifica que la API esté responsive + último ETL < 60 min. | Manual o Task opcional |
| `AUTO_PULL_SETUP.md` | Instructivo Task Scheduler paso a paso (mismo patrón que MotoShop) | Doc, no script |
| `logs/.gitkeep` | Garantiza que la carpeta existe en clone fresco | — |

---

## Reglas críticas (recordatorio para Dev Back)

1. **Todos los scripts asumen `.env` cargado** — invocar `load_env.ps1` al inicio.
2. **Idempotentes ante fallas parciales.** Si `refresh.ps1` falla en el upload, el próximo run lo retoma sin duplicar trabajo.
3. **Logs estructurados.** Cada línea: `[YYYY-MM-DD HH:MM:SS] [LEVEL] mensaje`.
4. **`-DryRun` flag obligatorio** en `refresh.ps1` y `auto_pull_and_apply.ps1` para que Dev W pruebe sin aplicar cambios reales.
5. **NO usar `Invoke-Expression`** sobre strings — vulnerabilidad de injection.

---

## Patrón de logging esperado

```
[2026-06-13 07:00:00] [INFO ] refresh start (TENANT=masvital)
[2026-06-13 07:00:00] [INFO ] env loaded from .env
[2026-06-13 07:00:01] [INFO ] activating venv
[2026-06-13 07:00:02] [INFO ] running pipeline/run_all.py
[2026-06-13 07:03:14] [INFO ] pipeline completed in 192s
[2026-06-13 07:03:14] [INFO ] uploading masvital_gold.duckdb to R2
[2026-06-13 07:03:21] [INFO ] upload completed (47.2 MB)
[2026-06-13 07:03:21] [INFO ] refresh end
```

---

## Cómo Dev W los configura

Ver [`../INICIAR_DEV_W.md`](../INICIAR_DEV_W.md) pasos 10-12 (Task Scheduler).
