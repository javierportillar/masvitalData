# PENDIENTES · masvitalData

> Tareas humanas (PO + Dev W) que NO se pueden hacer por código. Si una de estas no está resuelta, los devs IA se traban.
>
> **Estado al 2026-06-16:** MasVital está VIVO en producción. Sprints M1+M2+M3.3 completados. Datos reales en `app.fragloesja.uk` con paleta y logo propios. Lo que queda son tareas operativas chicas y el sprint M4 de trazabilidad cross-tenant (no bloqueante).

---

## ✅ Resuelto en esta etapa (Sprint M3 cerrado)

### Del PO

- [x] **Línea de negocio MasVital confirmada:** distribuidora de víveres y abarrotes. Top SKUs vistos: GRANOLA KETO, AGUA DE COCO, BROWNIES DE CACAO, CHORIZO PARRILLERO. POS = sgHermes igual que MotoShop, pipeline genérico funciona tal cual sin adaptación M3.4.
- [x] **BD MySQL real:** `masvital`. Confirmado por Dev W en sesión 2.
- [x] **Acceso al PC del Dev W:** ejecutado vía RDP. PC operativo.
- [x] **Ruta del repo:** `C:\Users\ProDesk\Documents\javdevmasv\masvitalData`. Cambió respecto al sugerido pero quedó documentado.
- [x] **Usuario admin con tenants_allowed:** `admin` global ve ambos tenants (`tenants_allowed: [motoshop, masvital]`). Verificado contra producción.

### Del Dev W

- [x] **`pipeline/explore_mysql_schema.py` ejecutado** y `docs/mysql-schema-snapshot.md` commiteado con 179 tablas. Sirvió como insumo para confirmar que sgHermes MasVital es idéntico estructuralmente al de MotoShop.
- [x] **Usuario MySQL `api_read` SELECT-only** creado y verificado contra `masvital.*`.
- [x] **Fecha + zona horaria del PC** OK (America/Bogota).
- [x] **MySQL arranca automático** con el PC.
- [x] **Pipeline corriendo cada 30min** vía Task Scheduler `MasVitalRefresh` (07:00–19:30 COL). Logs sin errores en 24h+.
- [x] **Auto-pull cada 5min** vía `MasVitalAutoPull` (06:00–20:00). Refleja cambios del repo al PC sin intervención.
- [x] **Backup diario MySQL** vía `MasVitalBackupMySQL` a las 02:00. Carpeta `C:\Backups\MasVital\` recibiendo dumps.

### Bloqueantes de plataforma

- [x] **Sprint M1** backend multi-tenant en prod (`api.fragloesja.uk`).
- [x] **Sprint M2** frontend tenant picker en prod (`app.fragloesja.uk` con `/select-tenant`).
- [x] **Sprint M3.3** pipeline parametrizado entregado por Dev Back, mergeado en `main` de este repo.
- [x] **Setup PC Windows MasVital** terminado por Dev W (sesión 2 del 2026-06-15).

---

## 🟨 Próximas tareas (post Sprint M3, no bloqueantes)

### Datos / crecimiento del negocio

- [ ] **Cuando MasVital tenga 30 días de datos:** habilitar `briefing.activo: true` en `tenants.yaml`. Sprint M4 ya soporta briefing dual.
- [ ] **Cuando MasVital tenga 90 días de datos:** habilitar `dormidos`, `cohortes` en `enabled_features`.
- [ ] **Cuando MasVital tenga 6+ meses:** habilitar `forecast`, `drift`, `plan-compras`.

### Operación

- [ ] **Definir si MasVital tendrá chat de Telegram propio para briefing.** Hoy compartido con MotoShop. Si el PO quiere segregar, dar `TELEGRAM_GERENTE_CHAT_ID` específico para MasVital.
- [ ] **Calidad de captura en la POS** — observación de la primera semana de datos: el ~40% de las facturas tiene `cod_formapago` como "SIN_COD" (ej. factura LORENA MORA $149K). Y el `nombre_vendedor` viene siempre vacío. Vale la pena que el operador del POS de MasVital marque siempre forma de pago y vendedor antes de cerrar la venta. Mejora directa del cierre de Caja y del card "Top vendedores".
- [ ] **Pagos partidos en la POS** — sgHermes registra UN solo código de pago por factura. Si MasVital recibe muchas ventas mitad efectivo + mitad tarjeta, el cierre de Caja va a tener delta vs caja física. Confirmar con el operador del POS de MasVital si esto pasa seguido. Si sí, escalar al Dev Back para ver si sgHermes tiene tabla `recibos_caja` o `cobrosdetalle` que podamos traer a bronze.

### Escalabilidad

- [ ] **Si llega un 3er negocio:** refactorizar pipeline a paquete instalable (`pip install -e ./pipeline`) en lugar de duplicar. Refactor mediano, vale la pena con N≥3.

---

## 📌 Decisiones pendientes (escalan al Reviewer)

- [ ] **¿Bucket R2 único o separado por tenant?** Hoy ambos tenants conviven en `motoshop-gold`. Si llega segregación de permisos por dueño del negocio, separar.
- [ ] **¿Mantener Dev W como agente IA o que sea un humano operativo?** Hoy: agente IA, mismo patrón que MotoShop. La sesión 2 demostró que funciona — diagnóstico autónomo de problemas (ExecutionPolicy, venv path, stderr capture, password placeholder) y resolución vía PR.

---

## 🟦 Sprint M4 (siguiente, no bloqueante)

**Estado:** ⬜ pendiente del Dev Back en `motoshopData`. No bloquea MasVital — el negocio ya está operando.

Resumen de lo que cubre M4:
- Trazabilidad cross-tenant en logs (structlog `bind(tenant=...)`)
- Endpoints admin con filtro por tenant: `/admin/pipeline?tenant=`, `/admin/llm-cost`, `/admin/audit`
- Briefing diario doble: uno por tenant con prefijo `[MotoShop]` o `[MasVital]`
- Audit log de switches de tenant del usuario admin

Cuando arranque M4, el Reviewer abre Gate M4 en `INICIAR_REVIEWER.md` §M4.

---

Actualizá esta lista marcando ✅ a medida que se cierran tareas. NO borres entries cerradas — quedan como historial.
