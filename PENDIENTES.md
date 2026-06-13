# PENDIENTES · masvitalData

> Tareas humanas (PO + Dev W) que NO se pueden hacer por código. Si una de estas no está resuelta, los devs IA se traban.

---

## 🟥 Bloqueantes para empezar el Sprint M3

### Del PO

- [ ] **Confirmar línea de negocio de MasVital.** ¿Qué vende? Repuestos, suministros médicos, otra cosa. Define el modelo de productos esperado.
- [ ] **Definir nombre de la BD MySQL real** del POS de MasVital (ej: `masvital2026`, `masvitalpos`, etc.). Se completa en `.env.example` placeholder `MYSQL_DATABASE`.
- [ ] **Indicar cuál es el POS** de MasVital. ¿Es sgHermes igual que MotoShop? ¿O es otro POS? Esto define si el pipeline genérico funciona tal cual o si Dev Back necesita adaptar mapeo en M3.4.
- [ ] **Aprobar acceso del Dev W al PC físico** (Anydesk/RDP/presencial). Confirmar canal y credenciales.
- [ ] **Definir ruta del repo en el PC.** Default sugerido: `C:\Users\MasVital\Documents\masvitalData`. Confirmar o cambiar.
- [ ] **Validar usuario admin con tenants_allowed.** El password `FG28` ya es válido, pero el PO confirma que el usuario `admin` global puede ver ambos tenants (`tenants_allowed: [motoshop, masvital]`).
- [ ] **Decidir si MasVital tendrá chat de Telegram propio para briefing.** Si sí, dar `TELEGRAM_GERENTE_CHAT_ID` específico. Si no, briefing diario MasVital queda apagado hasta M4+.

### Del Dev W (cuando reciba acceso al PC)

- [ ] **Ejecutar `pipeline/explore_mysql_schema.py`** y commitear el snapshot a `docs/mysql-schema-snapshot.md`. Esto es insumo crítico para Dev Back en M3.4.
- [ ] **Crear usuario MySQL `api_read` SELECT-only** y validar que NO puede hacer INSERT/UPDATE/DELETE.
- [ ] **Asegurar que el PC tiene fecha y zona horaria correctas** (America/Bogota). Si está mal, el `business_date` derivado en silver queda mal.
- [ ] **Confirmar que MySQL del POS arranca con el PC** (servicio Windows) y no requiere login interactivo.

---

## 🟧 Bloqueantes para cerrar Sprint M3

- [ ] Sprint M1 (backend multi-tenant) en prod
- [ ] Sprint M2 (frontend tenant picker) en prod
- [ ] Dev Back terminó M3.3-M3.5 (pipeline + scripts PS1 en este repo)
- [ ] Dev W terminó setup PC + 24h estables
- [ ] Reviewer aprobó gate M3

---

## 🟨 Próximas tareas (post Sprint M3)

- [ ] **Cuando MasVital tenga 30 días de datos:** habilitar `briefing.activo: true` en `tenants.yaml`. Sprint M4 ya soporta briefing dual.
- [ ] **Cuando MasVital tenga 90 días de datos:** habilitar `dormidos`, `cohortes` en `enabled_features`.
- [ ] **Cuando MasVital tenga 6+ meses:** habilitar `forecast`, `drift`, `plan-compras`.
- [ ] **Si llega un 3er negocio:** refactorizar pipeline a paquete instalable (`pip install -e ./pipeline`) en lugar de duplicar. Refactor mediano, vale la pena con N≥3.

---

## 📌 Decisiones pendientes (escalan al Reviewer)

- [ ] ¿Bucket R2 único o separado por tenant? (hoy: único. Si llega segregación de permisos por dueño, separar.)
- [ ] ¿GitHub repo `masvitalData` público o privado? (hoy: privado por defecto. Si vamos a abrir el código de la plataforma, partir backend a su propio repo público.)
- [ ] ¿Mantener Dev W como agente IA o que sea un humano operativo? (hoy: agente IA, mismo patrón que MotoShop.)

---

Actualizá esta lista marcando ✅ a medida que se cierran tareas. NO borres entries cerradas — quedan como historial.
