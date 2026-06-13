# Sprint M3 · Onboarding MasVital

> **Plan canónico:** [`motoshopData/docs/plan-multi-tenant.md`](https://github.com/javierportillar/motoshopData/blob/main/docs/plan-multi-tenant.md) §5 Sprint M3
>
> **Este documento es la vista del Sprint M3 desde el repo `masvitalData`.** Refleja la tabla M3.* del plan canónico, pero con detalle operativo para Dev Back, Dev W y Reviewer en este repo.

---

## 1 · Objetivo

Llevar el PC Windows de MasVital de cero a corriendo el pipeline ETL cada 30 minutos, subiendo el DuckDB a R2, y que la PWA muestre datos reales del negocio MasVital cuando el usuario escoge ese tenant en `/select-tenant`.

---

## 2 · Pre-requisito (NO empezar sin esto)

**Sprint M1 (backend multi-tenant) debe estar en `motoshopData/main` y en prod en `api.fragloesja.uk`.**

Validación rápida:

```bash
curl -X POST https://api.fragloesja.uk/api/auth/login \
  -H 'Content-Type: application/json' \
  -d '{"username":"admin","password":"FG28"}' | jq '.tenants_allowed'
# Esperado: ["motoshop","masvital"]
```

Si no responde con eso → M1 no está listo → no empezamos M3.

---

## 3 · Sub-tareas M3 con asignación

### M3.1 — Init repo `masvitalData` [✅ Hecho]

- [x] GitHub repo creado: `github.com/javierportillar/masvitalData`
- [x] Primer commit local
- [x] Branch `main` activa

### M3.2 — Estructura inicial + docs por rol [✅ Hecho]

- [x] `README.md`, `INICIAR_*.md`, `PENDIENTES.md`, `SEGUIMIENTO.md`
- [x] `.env.example` con todos los campos
- [x] `.gitignore`
- [x] Placeholders `pipeline/`, `infra/`, `scripts/`
- [x] `docs/sprint-m3-onboarding.md` (este archivo)

### M3.3 — Copia pipeline parametrizado [⬜ Dev Back]

**Responsable:** Dev Back
**Bloqueante:** M1 en prod
**Esfuerzo:** ~2 h
**Files acá:**

- `pipeline/__init__.py`
- `pipeline/mysql_source.py` (parametrizado por env vars `MYSQL_*`)
- `pipeline/silver.py` (tablas sin prefijo `motoshop_` — refactor que vino con M1.8)
- `pipeline/gold.py` (igual)
- `pipeline/embeddings_skus.py`
- `pipeline/run_all.py` (lee `TENANT`, `OUTPUT_PATH`)
- `pipeline/explore_mysql_schema.py` (utilidad NUEVA para Dev W)
- `pipeline/requirements.txt` (pin exacto de deps)
- `scripts/upload_duckdb_to_r2.py` (parametrizado por `R2_OBJECT_KEY`, `LOCAL_DB_PATH`)

**DoD:**
- `python pipeline/run_all.py` corre localmente en macOS o WSL contra un MySQL dummy
- Subida a R2 funciona con bucket de test
- Tabla DuckDB resultante: tablas se llaman `bronze_*`, `silver_*`, `gold_*` (SIN prefijo `motoshop_`)

### M3.4 — Adaptación esquema MySQL MasVital [⬜ Dev Back]

**Responsable:** Dev Back
**Bloqueante:** Dev W ya generó `docs/mysql-schema-snapshot.md`
**Esfuerzo:** depende del esquema (1 h si es idéntico a sgHermes, hasta 6 h si es POS distinto)

**Input:** snapshot del esquema MySQL MasVital generado por Dev W.

**Output:**
- `pipeline/mysql_source.py` actualizado con mapeo correcto de tablas/columnas MasVital → bronze genérico
- Si MasVital usa POS distinto a sgHermes: documentar en `docs/ADRs/ADR-001-mapeo-pos-masvital.md` qué se mapeó y cómo

**DoD:**
- Pipeline corre localmente contra dump de MySQL MasVital y genera `bronze_*` poblados
- Silver → Gold no rompe con los datos MasVital

### M3.5 — Scripts PS1 (refresh, auto-pull, backup) [⬜ Dev Back]

**Responsable:** Dev Back
**Bloqueante:** M3.3-M3.4
**Esfuerzo:** ~3 h
**Files acá:**

- `infra/refresh.ps1` (orquestador: pipeline + upload R2)
- `infra/auto_pull_and_apply.ps1` (git fetch + pull si hay cambios)
- `infra/backup_mysql.ps1` (mysqldump nightly, retención 14 días)
- `infra/load_env.ps1` (helper que parsea `.env`)
- `infra/AUTO_PULL_SETUP.md` (instructivo Task Scheduler)
- `infra/logs/.gitkeep`

**Patrón:** copiar y adaptar desde `motoshopData/infra/auto_pull_and_apply.ps1` y `motoshopData/infra/refresh_v15.ps1`.

**DoD:**
- Scripts probados en una VM Windows o WSL antes de mandar a Dev W
- `refresh.ps1 -DryRun` muestra lo que haría sin ejecutar
- Logs estructurados en `infra/logs/refresh_YYYYMMDD.log`

### M3.W — Setup PC MasVital [⬜ Dev W]

**Responsable:** Dev W
**Bloqueante:** M3.3-M3.5 + acceso al PC
**Esfuerzo:** ~3-5 h efectivas
**Detalle:** ver [`INICIAR_DEV_W.md`](../INICIAR_DEV_W.md) — son 14 pasos en orden.

### M3.PO — Validación end-to-end [⬜ PO]

**Responsable:** PO (Javier)
**Bloqueante:** M3.W + Sprint M2 frontend en prod
**Esfuerzo:** ~15 min
**Pasos:**

1. Abrir `app.fragloesja.uk` desde el celular
2. Login `admin` / `FG28`
3. Escoger MasVital en `/select-tenant`
4. Recorrer cada dashboard habilitado y verificar que muestra datos
5. Probar chat IA preguntando "¿cuántos productos hay en MasVital?"
6. Cambiar a MotoShop y verificar que TODO sigue igual que antes

Si todo ok → ✅ marcar Sprint M3 cerrado en `SEGUIMIENTO.md` y en `motoshopData/MASTER.md`.

---

## 4 · Cuándo NO cerrar M3

No cerrar M3 si:

- ❌ Cross-tenant leak detectado (admin con MasVital ve SKUs de MotoShop)
- ❌ Pipeline corre pero los datos en DuckDB están vacíos (esquema mal mapeado)
- ❌ Task Scheduler no dispara o falla intermitente sin retry
- ❌ Briefing diario MotoShop dejó de llegar (M3 rompió algo en M4-preparado)
- ❌ Costo R2 dispara por algún motivo (revisar uploads duplicados)

En cualquiera de esos casos: rollback (apagar Task Scheduler, eliminar `masvital_gold.duckdb` de R2, quitar entry de `tenants.yaml`) + issue + retomar.

---

## 5 · Trazabilidad de M3

Cada sesión que toque este sprint debe agregar entry en `SEGUIMIENTO.md` con:
- Qué se hizo
- Qué quedó pendiente
- Próxima sesión esperada y rol

El Reviewer audita ambos `SEGUIMIENTO.md` (este + motoshopData) antes de aprobar el gate M3.
