# SEGUIMIENTO · masvitalData

> Bitácora viva por sesión. Cada vez que un rol (Dev W, Dev Back, Reviewer, PO) trabaja acá, agrega una entry abajo con: fecha, rol, qué hizo, qué quedó pendiente.
>
> Formato: una sección por sesión, orden cronológico ascendente. NO borrar entries — son trazabilidad.

---

## Sesión 1 · 2026-06-13 · Reviewer

**Rol:** Reviewer / Arquitecto
**Duración:** ~30 min
**Output:**

- Estructura inicial del repo creada:
  - `README.md` — rol del repo y links
  - `INICIAR_DEV_W.md` — paso a paso operativo (14 pasos) para configurar el PC desde 0
  - `INICIAR_DEV_BACK.md` — qué hace Dev Back acá vs en motoshopData
  - `INICIAR_REVIEWER.md` — gates M1-M4 con tests cURL concretos
  - `PENDIENTES.md` — tareas humanas bloqueantes
  - `.env.example` — plantilla con todas las variables comentadas
  - `.gitignore` — secrets, .duckdb, logs, etc
  - `docs/sprint-m3-onboarding.md` — detalle del Sprint M3
  - Placeholders en `pipeline/`, `infra/`, `scripts/` con README explicando qué va

**Estado tras la sesión:**

- ✅ Estructura lista para que Dev Back arranque M3 (cuando M1 esté en prod)
- ⬜ Dev Back: bloqueado hasta M1 en prod
- ⬜ Dev W: bloqueado hasta M3.3-M3.5 (Dev Back pueble el repo)
- ⬜ PO: pendiente confirmar línea de negocio MasVital + esquema MySQL real (ver `PENDIENTES.md`)

**Próxima sesión esperada:** Dev Back arrancando Sprint M1 en `motoshopData/`.

---

## Sesión 2 · 2026-06-15 · Dev W

**Rol:** Dev W (PC Windows — runtime/setup)
**Duración:** ~45 min
**Output:**

- Relevamiento completo del estado del PC MasVital:
  - Git 2.54.0 ✅ | Python 3.12.10 ✅ | MySQL Server 5.0.45 corriendo ✅
  - ExecutionPolicy RemoteSigned ✅ | .venv con dependencias ✅
  - Repo clonado en `C:\Users\ProDesk\Documents\javdevmasv\masvitalData` (actualizado, origin/main)
  - `.env` poblado con credenciales reales (R2, HF, MySQL, OpenCode, API) y verificado no-trackeado
  - Usuario `api_read@localhost` existe con SELECT-only en `masvital.*` ✅
  - `docs/mysql-schema-snapshot.md` (8554 lines, 179 tablas) generado ✅
- Pipeline verificado: corridas exitosas (logs de 2026-06-14 y 2026-06-15)
  - Bronze: 1912 filas (productos 510, facventas 102, detfventas 276, etc.)
  - Silver: 7/7 ✅, Gold: 10/10 ✅
  - DuckDB: 14 MB, subido a R2 como `masvital_gold.duckdb` en `motoshop-gold` bucket
- Task Scheduler:
  - `MasVitalRefresh`: Ready, cada 30 min 07:00-19:30 ⏰
  - `MasVitalAutoPull`: Ready, cada 5 min 06:00-20:00 ⏰
  - `MasVitalBackupMySQL`: Ready, daily 02:00 ⏰
  - `C:\Backups\MasVital\` dir existe ✅
- Ajustes aplicados:
  - MySQL bin (`C:\Program Files (x86)\MySQL\MySQL Server 5.0\bin`) agregado a PATH de usuario
  - `PLATFORM_ADMIN_PASSWORD` corregido en `.env` (estaba como placeholder, causaba 401 en cache refresh)
- API validada:
  - Login admin/FG28 funciona — tenants: motoshop, masvital
  - `/api/auth/me` con X-Tenant: masvital ok
  - `/api/admin/data/refresh` ok (carga DuckDB desde R2)
  - `/api/metrics/drift-summary` funciona (0 alertas, negocio nuevo)
  - `/api/metrics/sales-*` retorna 500 — probablemente el backend necesita ajuste para schema MasVital

**Estado tras la sesión:**

- ✅ PC MasVital configurado y operativo
- ✅ Pipeline corre cada 30 min y sube a R2
- ✅ Auto-pull y backups configurados
- ✅ Auth funciona, tenant MasVital accesible
- ⬜ `/api/metrics/sales-*` da 500 — reportar a Dev Back para revisión de queries contra schema MasVital
- ⬜ Validación visual PWA con navegador (el humano debe loguearse en app.fragloesja.uk como admin/FG28, elegir MasVital en /select-tenant y verificar KPIs)
- ⬜ 24h estables de runs sin error (observación)

**Próxima sesión esperada:** Reviewer — Gate M3: validación cross-tenant en navegador después de 24h estables. O Dev Back si necesita fix de queries.

---
