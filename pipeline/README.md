# pipeline/ · ETL bronze → silver → gold (placeholder)

> **Estado:** Vacío. Se puebla en Sprint M3.3 por **Dev Back**.

---

## Qué va a vivir acá (después de M3.3)

| Archivo | Función | Fuente |
|---|---|---|
| `__init__.py` | módulo | nuevo |
| `mysql_source.py` | Lee MySQL local con pymysql, parametrizado por env vars `MYSQL_*`. Mapea tablas POS → bronze genérico. | copia de `motoshopData/pipeline/mysql_source.py` + adaptado por M3.4 |
| `silver.py` | Bronze → silver: dim_producto, dim_bodega, fact_ventas, fact_compras, fact_inventario. Embeddings preservados. | copia de `motoshopData/pipeline/silver.py` (sin prefijo `motoshop_` post-M1) |
| `gold.py` | Silver → 10 marts gold. Algunos requieren histórico (skip si MasVital no tiene aún). | copia de `motoshopData/pipeline/gold.py` |
| `embeddings_skus.py` | Llama HuggingFace Inference API para embeddings de productos nuevos. | copia de `motoshopData/pipeline/embeddings_skus.py` |
| `run_all.py` | Orquestador. Lee `TENANT`, `OUTPUT_PATH`. Loguea con structlog. | copia adaptada |
| `explore_mysql_schema.py` | **Nuevo.** Ejecuta Dev W una sola vez para generar `docs/mysql-schema-snapshot.md`. Lista tablas + columnas + 3 samples por tabla. | NUEVO en M3.3 |
| `requirements.txt` | Pin exacto de dependencias Python para el PC MasVital. | NUEVO |

---

## Reglas críticas (recordatorio para Dev Back)

1. **NO importar nada de `motoshopData`.** Self-contained.
2. **Tablas DuckDB sin prefijo de tenant.** Solo `bronze_*`, `silver_*`, `gold_*`. El tenancy lo da el archivo `masvital_gold.duckdb`.
3. **Pin exacto en `requirements.txt`.** Reproducibilidad en el PC.
4. **Logs estructurados.** structlog JSON al stdout + file.
5. **Idempotente.** Si el pipeline corre 2 veces seguidas con los mismos datos, el output es idéntico.

---

## Cómo Dev W lo prueba (después de M3.3)

```powershell
cd C:\Users\MasVital\Documents\masvitalData
.\.venv\Scripts\Activate.ps1
python pipeline\run_all.py
```

Tiempo esperado primer run: 2-4 min para ~5.000 SKUs.
