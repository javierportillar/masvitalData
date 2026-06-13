# INICIAR · Dev Back (Backend + Pipeline parametrizado)

> **Para vos.** Sos el responsable de que (a) el backend en `motoshopData` sea multi-tenant y (b) este repo `masvitalData` tenga el pipeline parametrizado, los scripts PS1 y la doc operativa lista para que Dev W instale en el PC sin pensar.
>
> **No tocás el PC físico.** Esa es responsabilidad exclusiva de Dev W.

---

## 1 · Tu trabajo se divide en dos repos

### En `motoshopData` (la plataforma)

Esto es Sprint M1 y parte de M3. Detalle completo:
→ **[`motoshopData/docs/plan-multi-tenant.md`](https://github.com/javierportillar/motoshopData/blob/main/docs/plan-multi-tenant.md)** §5 (Sprints M1, M3)

Resumen:
- Sprint M1: backend acepta `X-Tenant` header, abre `/tmp/{tenant}_gold.duckdb`, cache keys con tenant, `tenants.yaml` declara MasVital con `enabled_features` reducidas, JWT lleva `tenants_allowed`.
- Tarea M3.10 (vive en `motoshopData/.github/workflows/`): briefing-daily.yml itera por tenants con `briefing.activo: true`.

### En `masvitalData` (este repo)

Esto es el grueso del Sprint M3 (tareas M3.1 → M3.5, M3.8, M3.9). Detalle: [`docs/sprint-m3-onboarding.md`](docs/sprint-m3-onboarding.md).

---

## 2 · Orden estricto

NO empezás `masvitalData` hasta que Sprint M1 esté en prod. Razón: necesitás validar que el backend acepta `X-Tenant: masvital` con un DuckDB vacío sin crashear. Eso son tus tests M1.11.

Cuando M1 esté ✅ en `api.fragloesja.uk`, entonces sí:

1. M3.3 — Copiar pipeline parametrizado a `masvitalData/pipeline/`
2. M3.4 — Adaptar mapeo MySQL → bronze según esquema MasVital (insumo: `masvitalData/docs/mysql-schema-snapshot.md` generado por Dev W)
3. M3.5 — Escribir scripts PS1 (`refresh.ps1`, `auto_pull_and_apply.ps1`, `backup_mysql.ps1`)
4. M3.8 — Pulir `INICIAR_DEV_W.md` con cualquier paso adicional que descubriste
5. M3.9 — Asegurar que `README.md` y `SEGUIMIENTO.md` reflejen el estado

---

## 3 · Cómo copiar el pipeline

El pipeline genérico vive en `motoshopData/pipeline/`. La copia NO es idéntica — hay que parametrizar:

### Archivos que copiás tal cual (no cambian)

- `pipeline/silver.py` (asume tablas `bronze_*`, las renombró M1.8 ya sin prefijo `motoshop_`)
- `pipeline/gold.py` (igual)
- `pipeline/embeddings_skus.py`
- `pipeline/build_duckdb_from_export.py`

### Archivos que parametrizás

- `pipeline/mysql_source.py` → acepta env vars `MYSQL_HOST`, `MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_DATABASE`
- `pipeline/run_all.py` → lee env var `OUTPUT_PATH = f"./{TENANT}_gold.duckdb"`
- `scripts/upload_duckdb_to_r2.py` → lee env var `R2_OBJECT_KEY` y `LOCAL_DB_PATH`

### Archivos nuevos que escribís

- `pipeline/explore_mysql_schema.py` — utilidad para Dev W (lista tablas + columnas + samples) que se ejecuta una sola vez para que vos sepas qué tiene MasVital
- `pipeline/requirements.txt` — pin exacto de dependencias (duckdb, pymysql, boto3, httpx, huggingface-hub, pydantic, structlog)

---

## 4 · Scripts PS1 que escribís

### `infra/refresh.ps1`

```powershell
# Wrapper que corre el pipeline + sube a R2
# Loguea a infra/logs/refresh_YYYYMMDD.log

# Cargar .env
. .\infra\load_env.ps1

# Activar venv
.\.venv\Scripts\Activate.ps1

# Pipeline
python pipeline\run_all.py 2>&1 | Tee-Object -FilePath "infra\logs\refresh_$(Get-Date -Format yyyyMMdd).log" -Append

# Upload a R2
python scripts\upload_duckdb_to_r2.py 2>&1 | Tee-Object -FilePath "infra\logs\refresh_$(Get-Date -Format yyyyMMdd).log" -Append

# Trigger Render rebuild (opcional, Render rehidrata al próximo cold-start)
# curl -X POST https://api.fragloesja.uk/api/admin/data/refresh -H "X-Tenant: masvital" ...
```

### `infra/auto_pull_and_apply.ps1`

Mismo patrón que `motoshopData/infra/auto_pull_and_apply.ps1` pero adaptado:
- Trabaja sobre repo `masvitalData`
- Si cambió `pipeline/**` → log "código nuevo, próximo run lo usa"
- Si cambió `infra/**` → log + considerar reiniciar Task si tocó scripts
- Si cambió `.env.example` → log WARN ("revisar .env local manualmente")

### `infra/backup_mysql.ps1`

Mismo patrón que MotoShop. Output a `C:\Backups\MasVital\backup_YYYYMMDD.sql.gz`.

### `infra/load_env.ps1`

Helper que parsea `.env` y lo carga como variables de sesión PowerShell. Mismo pattern que MotoShop.

---

## 5 · Checklist de finalización Sprint M3 (lo tuyo)

- [ ] Sprint M1 en prod (no tu responsabilidad terminar M1 acá, pero es bloqueante)
- [ ] `tenants.yaml` declara MasVital con `enabled_features` reducidas
- [ ] `users.yaml` `admin` tiene `tenants_allowed: [motoshop, masvital]`
- [ ] `masvitalData/pipeline/` poblado con scripts parametrizados
- [ ] `masvitalData/scripts/upload_duckdb_to_r2.py` parametrizado
- [ ] `masvitalData/infra/*.ps1` escritos y probados localmente
- [ ] `masvitalData/pipeline/requirements.txt` con pins exactos
- [ ] `masvitalData/.env.example` completo con TODOS los campos comentados
- [ ] `INICIAR_DEV_W.md` actualizado con cualquier paso adicional descubierto
- [ ] PR mergeado en `masvitalData/main`
- [ ] Notificás al PO + Dev W que el repo está listo para onboarding

---

## 6 · Reglas no-negociables

| Regla | Por qué |
|---|---|
| El pipeline en `masvitalData/` NO importa nada de `motoshopData/` — es self-contained | El PC MasVital solo clona este repo. Si tiene dependencias cruzadas, se rompe. |
| Los nombres de tablas DuckDB NO llevan prefijo `motoshop_` ni `masvital_` — solo `bronze_*`, `silver_*`, `gold_*` | El tenancy lo da el archivo (`masvital_gold.duckdb`), no el nombre de tabla |
| Cualquier query SQL que escribas tipea contra esos nombres genéricos | Para que MotoShop y MasVital usen las mismas queries en el backend |
| NO commitees nada con secretos en `.env.example` — solo placeholders `<COMPLETAR>` | Seguridad básica |
| NO toques el `.env` real ni pidas que te lo manden — Dev W lo configura en el PC | Aislamiento de secretos |
