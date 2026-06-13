# scripts/ · Auxiliares Python (placeholder)

> **Estado:** Vacío. Se puebla en Sprint M3.3 por **Dev Back**.

---

## Qué va a vivir acá (después de M3.3)

| Archivo | Función |
|---|---|
| `upload_duckdb_to_r2.py` | Sube el `masvital_gold.duckdb` a R2 con la key `R2_OBJECT_KEY`. Idempotente. Logging. |
| `download_duckdb_from_r2.py` | Útil para Dev Back: baja el último DuckDB para inspección local. |
| `capture_new_sales.py` (opcional) | Si replicamos el patrón incremental de MotoShop: solo trae ventas del día y hace upsert. |

---

## Reglas

1. **Self-contained** — no importar `pipeline/` ni `motoshopData`.
2. **Acepta env vars** — nunca hardcodear paths ni credenciales.
3. **Idempotente** — re-ejecutar es seguro.
4. **Logs claros** — print + structlog si aplica.

---

## Cuándo se invocan

| Script | Invocador |
|---|---|
| `upload_duckdb_to_r2.py` | `infra/refresh.ps1` al final de cada run |
| `download_duckdb_from_r2.py` | Manual por Dev Back o Reviewer |
| `capture_new_sales.py` | Task Scheduler dedicado (más frecuente que `refresh.ps1`) |
