# INICIAR · Reviewer / Arquitecto

> **Para vos.** Sos el guardián del programa multi-tenant. Tu trabajo es validar antes de cada gate (M1, M2, M3, M4) que no hay leak, que se sostiene $0/mes, que la trazabilidad está íntegra. Si rechazás, devolvés al dev con explicación técnica concreta. Si aprobás, va a prod.

---

## 1 · Gates del programa multi-tenant

### Gate M1 — Backend multi-tenant en prod

Validás en `motoshopData/main` después del PR de Dev Back.

**Tests obligatorios que tienen que pasar:**

```bash
# Login admin devuelve tenants_allowed
curl -X POST https://api.fragloesja.uk/api/auth/login \
  -H 'Content-Type: application/json' \
  -d '{"username":"admin","password":"FG28"}' | jq '.tenants_allowed'
# Esperado: ["motoshop","masvital"]

# /api/me con X-Tenant motoshop responde con features completas
curl https://api.fragloesja.uk/api/me \
  -H "Authorization: Bearer $TOKEN" \
  -H "X-Tenant: motoshop" | jq '.enabled_features | length'
# Esperado: >= 18

# /api/me con X-Tenant masvital responde con features reducidas
curl https://api.fragloesja.uk/api/me \
  -H "Authorization: Bearer $TOKEN" \
  -H "X-Tenant: masvital" | jq '.enabled_features | length'
# Esperado: ~7

# Cross-tenant leak — abc-detalle masvital NUNCA puede devolver SKUs motoshop
curl "https://api.fragloesja.uk/api/metrics/abc-detalle?bucket=A&limit=50" \
  -H "Authorization: Bearer $TOKEN" \
  -H "X-Tenant: masvital" | jq '.items | length'
# Esperado: 0 (archivo masvital_gold.duckdb aún no existe)

# Backward compat — frontend SIN header funciona como motoshop
curl https://api.fragloesja.uk/api/metrics/abc-segmentation \
  -H "Authorization: Bearer $TOKEN" | jq '.total_skus'
# Esperado: > 0 (datos motoshop como siempre)
```

**Adicional:**
- [ ] `tenants.yaml` está versionado y revisado
- [ ] `users.yaml` actualizado con `tenants_allowed`
- [ ] Cache key incluye tenant en TODOS los `_cached_or_fetch` calls (grep)
- [ ] structlog `bind(tenant=...)` en middleware (revisar `main.py`)
- [ ] Tests E2E del frontend MotoShop siguen verdes

Si algo falla → ❌ rechazás, devolvés con detalle.

### Gate M2 — Frontend tenant picker en prod

Validás en Vercel prod después del PR de Dev Front.

**Validación humana en navegador:**

- [ ] Login `admin/FG28` redirige a `/select-tenant`
- [ ] `/select-tenant` muestra 2 cards: MotoShop y MasVital
- [ ] Click MotoShop → home con TODAS las cards de dashboards
- [ ] Botón "Cambiar negocio" en sidebar funciona y vuelve al picker
- [ ] Click MasVital → home con SOLO las cards de features habilitadas (productos, stock, ventas, inventario, chat)
- [ ] DevTools Network: cada request lleva header `X-Tenant`
- [ ] Logout limpia `currentTenant` (al loguear de nuevo vuelve al picker)

**Validación de seguridad:**
- [ ] Refresh manual a `/dashboards/abc` con tenant MasVital (donde no está habilitado) NO renderiza datos — muestra "No disponible aún"
- [ ] Cookie `motoshop_token` sigue siendo HttpOnly (DevTools → Application → Cookies)

Si algo falla → ❌.

### Gate M3 — MasVital en producción

Validás cuando Dev W reporta setup completo + 24h de runs estables.

**Tests automáticos:**

```bash
# masvital_gold.duckdb existe en R2
aws s3 ls s3://motoshop-gold/masvital_gold.duckdb --endpoint-url $R2_ENDPOINT
# Esperado: archivo presente, fecha de hoy

# /health/data-freshness?tenant=masvital devuelve fresco
curl "https://api.fragloesja.uk/api/health/data-freshness?tenant=masvital"
# Esperado: { "age_minutes": < 60, "status": "fresh" }

# /api/me con X-Tenant masvital ahora retorna datos
curl https://api.fragloesja.uk/api/metrics/inventory-summary \
  -H "X-Tenant: masvital" \
  -H "Authorization: Bearer $TOKEN" | jq '.num_productos'
# Esperado: > 0
```

**Validación operativa:**
- [ ] 24h sin fallas en `infra/logs/refresh_*.log` del PC MasVital
- [ ] Auto-pull aplicó al menos un commit dentro de 5 min
- [ ] PWA: admin login → MasVital → ve dashboards descriptivos con datos reales
- [ ] Chat IA con `X-Tenant: masvital` responde sobre datos MasVital (cero menciones a SKUs MotoShop)

Si todo ✅ → archivar `masvitalData/SEGUIMIENTO.md` con sprint M3 cerrado.

### Gate M4 — Trazabilidad cross-tenant

Validás en `motoshopData/main` después del PR de M4.

**Endpoints administrativos:**

- [ ] `/admin/pipeline?tenant=motoshop` filtra runs MotoShop
- [ ] `/admin/pipeline?tenant=masvital` filtra runs MasVital
- [ ] `/admin/llm-cost` muestra cost desglosado por tenant
- [ ] `/admin/audit` lista switches de tenant del usuario `admin`
- [ ] Briefing diario llega 2x a Telegram con prefijo `[MotoShop]` o `[MasVital]`

---

## 2 · Cosas que SIEMPRE chequeás (cross-gate)

### Trazabilidad

Cada request debe poder responder "¿de qué tenant es?" en:
- Logs structlog (`tenant` field)
- `pipeline_runs.duckdb` (columna `tenant`)
- `llm_cost.jsonl` (campo `tenant`)
- SQLite writes que apliquen (columna `tenant` en `alert_actions`, `purchase_plans`)

Si algún log no lleva `tenant` cuando aplica → ❌ devolver con instrucción.

### Costo $0/mes

Antes de aprobar M3 (cuando MasVital empieza a generar tráfico real):

- [ ] Render dashboard: 1 servicio, < 100 hrs/mes uso activo
- [ ] Vercel dashboard: bandwidth < 10 GB/mes
- [ ] R2 dashboard: storage < 1 GB, ops < 100k/mes
- [ ] GitHub Actions: minutos usados < 200 min/mes
- [ ] HF Inference: rate-limit no hit (revisar dashboard HF)

Si algún margen baja de 50% del free tier → alerta al PO para revisar uso.

### Seguridad básica

- [ ] `.env` NO en repo (`git ls-files | grep -i env` debe devolver solo `.env.example`)
- [ ] `users.yaml` con hashes bcrypt, NO passwords plain
- [ ] R2 credenciales NO en código, solo en env vars
- [ ] CORS_ORIGINS no incluye `*`

---

## 3 · Cómo rechazás un PR

Patrón:

```
❌ NO MERGE

Razón técnica concreta:
- [archivo:linea] [qué falla] [qué esperarías]

Ejemplo:
- motoshop_api/metrics/repo_duckdb.py:418 — get_abc_segmentation
  no pasa tenant al cache key. Línea 419 `_cached_or_fetch("abc-segmentation", ...)`
  debe ser `f"abc-segmentation:{tenant}"`. Si no, MasVital ve cache de MotoShop.

Acción:
- Dev Back: fix + push + re-request review.
```

NUNCA aprobás con "está OK pero arregla X después". Si no está OK, no merge.

---

## 4 · Cómo aprobás un PR

```
✅ APPROVED

Validado:
- [list de tests que corriste y pasaron]
- [validación humana hecha]

Notas:
- [cosas a observar en prod, si hay]
- [próximo gate o sprint]
```

---

## 5 · Documentación a actualizar después de cada gate

| Gate | Actualizás | En dónde |
|---|---|---|
| M1 | `MASTER.md` (Sprint M1 ✅) + `SEGUIMIENTO.md` (sesión cerrada) | `motoshopData` |
| M2 | Idem | `motoshopData` |
| M3 | `MASTER.md` + `SEGUIMIENTO.md` en motoshopData. `SEGUIMIENTO.md` en `masvitalData`. | ambos |
| M4 | Idem M1 + ADR sobre trazabilidad final | `motoshopData/docs/decisions/` |
