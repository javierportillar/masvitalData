# masvitalData · Operación PC Windows MasVital

> **Qué es este repo.** El "checkout operativo" del PC Windows de MasVital. Contiene únicamente lo que ese PC necesita para correr el pipeline ETL local, subir el DuckDB a R2 y mantenerse actualizado vía auto-pull.
>
> **Qué NO es.** El código del backend FastAPI y del frontend Next.js NO viven acá — viven en el repo de la plataforma: [`motoshopData`](https://github.com/javierportillar/motoshopData). Este repo es chico a propósito.

---

## 1 · Por qué existe este repo separado

| Razón | Detalle |
|---|---|
| Aislamiento operativo | El PC de MasVital es independiente del PC de MotoShop. Cada PC tiene su `.env`, su Task Scheduler, su Auto-Pull. |
| Mínimo riesgo de leak | El PC MasVital NUNCA debe ver el código backend completo ni credenciales de MotoShop. Solo lo necesario para su tenant. |
| Independencia de despliegue | Bug en pipeline MasVital no bloquea deploys de MotoShop ni viceversa. |
| Audit trail | Cada commit acá es operación de MasVital. Mezclar repos diluye trazabilidad. |

La plataforma compartida (backend multi-tenant, frontend con tenant picker, R2) vive en `motoshopData`. Acá solo lo del PC MasVital.

---

## 2 · Plan canónico

El plan multi-tenant aprobado vive en motoshopData:
**[`motoshopData/docs/plan-multi-tenant.md`](https://github.com/javierportillar/motoshopData/blob/main/docs/plan-multi-tenant.md)**

Este repo materializa el **Sprint M3 — Onboarding MasVital**.

Detalle local del sprint: [`docs/sprint-m3-onboarding.md`](docs/sprint-m3-onboarding.md).

---

## 3 · Quién hace qué — punto de entrada por rol

| Rol | Punto de entrada | Qué hace acá |
|---|---|---|
| 🔵 **Dev Back** | [`INICIAR_DEV_BACK.md`](INICIAR_DEV_BACK.md) | Copia el pipeline parametrizado desde motoshopData, deja scripts PS1, asegura que MasVital esté declarado en `tenants.yaml`. NO opera el PC MasVital. |
| 🟢 **Dev W (PC MasVital)** | [`INICIAR_DEV_W.md`](INICIAR_DEV_W.md) | Instala Python, clona este repo, configura `.env`, prueba pipeline, sube a R2, configura Task Scheduler + Auto-Pull. ÚNICAMENTE este rol toca el PC físico. |
| 🟣 **Reviewer / Arquitecto** | [`INICIAR_REVIEWER.md`](INICIAR_REVIEWER.md) | Valida que cross-tenant leak sea cero, que $0/mes se mantenga, que la trazabilidad esté íntegra antes de cada gate. |
| 👤 **PO (Javier)** | [`PENDIENTES.md`](PENDIENTES.md) | Lista de tareas humanas: dar acceso al PC, definir credenciales MySQL MasVital, validar primer briefing. |

---

## 4 · Estructura del repo

```
masvitalData/
├── README.md                       (este archivo)
├── INICIAR_DEV_W.md                Punto de entrada Dev W
├── INICIAR_DEV_BACK.md             Punto de entrada Dev Back
├── INICIAR_REVIEWER.md             Punto de entrada Reviewer
├── PENDIENTES.md                   Tareas humanas pendientes
├── SEGUIMIENTO.md                  Bitácora viva por sesión
├── .env.example                    Plantilla de variables (sin secretos)
├── .gitignore
├── docs/
│   ├── sprint-m3-onboarding.md     Detalle del Sprint M3 (este repo)
│   └── ADRs/                       Decisiones específicas del PC MasVital
├── pipeline/                       (poblado en M3 por Dev Back)
│   └── README.md                   Qué scripts ETL van acá y de dónde vienen
├── infra/                          (poblado en M3 por Dev Back)
│   ├── README.md                   Qué scripts PS1 van acá
│   └── logs/                       (.gitkeep · logs gitignored)
└── scripts/                        (poblado en M3 por Dev Back)
    └── README.md                   Qué scripts auxiliares van acá
```

---

## 5 · Estado actual

| Sprint | Estado | Bloqueante |
|---|---|---|
| M3.1 — Init repo `masvitalData` | ✅ Hecho | — |
| M3.2 — Estructura inicial + docs por rol | ✅ Hecho (este commit) | — |
| M3.3 — Copia pipeline parametrizado | ⬜ Pendiente Dev Back | Sprint M1 backend multi-tenant en prod |
| M3.4 — Adaptación esquema MySQL MasVital | ⬜ Pendiente Dev Back | Esquema real MySQL MasVital documentado por Dev W |
| M3.5 — Scripts PS1 (refresh, auto-pull, backup) | ⬜ Pendiente Dev Back | M3.3 |
| M3.6 — Setup PC MasVital | ⬜ Pendiente Dev W | M3.3-M3.5 |
| M3.7 — Validación end-to-end (PWA muestra MasVital) | ⬜ Pendiente PO | M3.6 + Sprint M2 frontend en prod |

Actualizá `SEGUIMIENTO.md` después de cada sesión.

---

## 6 · Política de seguridad

- **NUNCA commitear `.env`** — solo `.env.example` con placeholders
- **NUNCA commitear `.duckdb` ni `*.sql` dumps** — gitignored
- **NUNCA modificar el MySQL productivo de MasVital** — el usuario `api_read` es SELECT-only por diseño
- **El backup MySQL es responsabilidad del PC** — vive local, no entra al repo

---

## 7 · Plataforma de referencia

| Componente | Vive en | URL |
|---|---|---|
| Backend FastAPI | `motoshopData` | `api.fragloesja.uk` |
| Frontend PWA | `motoshopData` | `app.fragloesja.uk` |
| R2 bucket | Cloudflare | `motoshop-gold` (compartido, key `masvital_gold.duckdb`) |
| Briefing Telegram | GitHub Actions en `motoshopData` | activa cuando MasVital tenga ≥30 días de datos |
