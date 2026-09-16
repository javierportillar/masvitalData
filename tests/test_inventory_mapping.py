from __future__ import annotations

import duckdb

from pipeline import silver


def test_inventory_maps_export_values_to_stock_cost_and_sale_price() -> None:
    con = duckdb.connect(":memory:")
    try:
        columns = ", ".join(
            f"{name} {type_name}"
            for name, type_name in [
                ("codlis", "VARCHAR"),
                ("nomlis", "VARCHAR"),
                ("codlin1", "VARCHAR"),
                ("nomlin", "VARCHAR"),
                ("codlin2", "VARCHAR"),
                ("nomlin2", "VARCHAR"),
                ("codbod", "VARCHAR"),
                ("nombod", "VARCHAR"),
                ("nitter", "VARCHAR"),
                ("nomter", "VARCHAR"),
                ("numdoc", "VARCHAR"),
                ("nomdoc", "VARCHAR"),
                ("codprod", "VARCHAR"),
                ("sernum", "VARCHAR"),
                ("nomprod", "VARCHAR"),
                ("unimed", "VARCHAR"),
                ("valor1", "DOUBLE"),
                ("valor2", "DOUBLE"),
                ("valor3", "DOUBLE"),
                ("valor4", "DOUBLE"),
                ("valor5", "DOUBLE"),
                ("docfec", "DATE"),
                ("docnum", "VARCHAR"),
                ("nomsub", "VARCHAR"),
                ("multiplo", "DOUBLE"),
                ("codcos", "VARCHAR"),
                ("nomcos", "VARCHAR"),
            ]
        )
        con.execute(f"CREATE TABLE bronze_auxinventario ({columns})")
        values = [None] * 27
        values[12:23] = [
            "SKU-1", None, "Product", "001", 7.0, 12000.0, 18500.0,
            None, None, "2026-09-15", "DOC-1",
        ]
        con.execute(
            "INSERT INTO bronze_auxinventario VALUES ("
            + ",".join(["?"] * 27)
            + ")",
            values,
        )

        silver.fact_inventario(con)

        assert con.execute(
            "SELECT valor_costo, valor_venta, cantidad FROM silver_fact_inventario"
        ).fetchone() == (12000.0, 18500.0, 7.0)
    finally:
        con.close()
