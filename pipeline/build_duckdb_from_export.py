"""Construye el DuckDB desde JSON exportados.

No requiere Databricks — es para casos donde se tenga un dump JSON.
El nombre del archivo DuckDB se define por env var TENANT.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

import duckdb

INPUT_DIR = Path("_staging/parquet")
TENANT = os.environ.get("TENANT", "masvital")
OUTPUT_PATH = Path(f"out/{TENANT}_gold.duckdb")

TABLES = [
    ("gold.mart_ventas_diarias_sku", "gold_mart_ventas_diarias_sku"),
    ("gold.mart_inventario_actual", "gold_mart_inventario_actual"),
    ("gold.mart_rotacion_abc", "gold_mart_rotacion_abc"),
    ("gold.mart_cohortes_clientes", "gold_mart_cohortes_clientes"),
    ("gold.mart_productos_dormidos", "gold_mart_productos_dormidos"),
    ("gold.alertas_quiebre", "gold_alertas_quiebre"),
    ("gold.alertas_drift", "gold_alertas_drift"),
    ("gold.forecast_categoria", "gold_forecast_categoria"),
    ("gold.mart_abc_xyz", "gold_mart_abc_xyz"),
    ("silver.fact_ventas", "silver_fact_ventas"),
    ("silver.fact_ventas_detalle", "silver_fact_ventas_detalle"),
    ("silver.fact_compras", "silver_fact_compras"),
    ("silver.fact_compras_detalle", "silver_fact_compras_detalle"),
    ("silver.dim_bodega", "silver_dim_bodega"),
    ("silver.dim_producto", "silver_dim_producto"),
]


def build_from_json(duckdb_path: str | Path) -> str:
    con = duckdb.connect(str(duckdb_path))
    total_rows = 0

    for _, alias in TABLES:
        short_name = alias.replace("gold_", "").replace("silver_", "")
        json_path = INPUT_DIR / f"{short_name}.json"

        if not json_path.exists():
            print(f"  SKIP {alias}: JSON no encontrado")
            continue

        rows = json.loads(json_path.read_text(encoding="utf-8"))
        count = len(rows)
        if count == 0:
            print(f"  SKIP {alias}: 0 filas")
            continue

        sample = rows[0]
        cols = []
        for k, v in sample.items():
            if isinstance(v, bool):
                t = "BOOLEAN"
            elif isinstance(v, int):
                t = "BIGINT"
            elif isinstance(v, float):
                t = "DOUBLE"
            else:
                t = "VARCHAR"
            cols.append(f'"{k}" {t}')

        con.execute(f"DROP TABLE IF EXISTS {alias}")
        schema_sql = ", ".join(cols)
        con.execute(f"CREATE TABLE {alias} ({schema_sql})")

        col_names = ", ".join([f'"{c}"' for c in sample.keys()])
        placeholders = ", ".join(["?"] * len(sample))
        stmt = f"INSERT INTO {alias} ({col_names}) VALUES ({placeholders})"

        batch = []
        for r in rows:
            row_vals = []
            for c in sample.keys():
                v = r.get(c)
                if isinstance(v, str) and v.strip() == "":
                    v = None
                row_vals.append(v)
            batch.append(row_vals)
            if len(batch) >= 1000:
                con.executemany(stmt, batch)
                batch = []
        if batch:
            con.executemany(stmt, batch)

        total_rows += count
        print(f"  {alias}: {count} filas")

    con.close()
    print(f"\nDuckDB listo: {duckdb_path} ({total_rows} filas totales)")
    return str(duckdb_path)


if __name__ == "__main__":
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    build_from_json(OUTPUT_PATH)
