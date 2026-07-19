from __future__ import annotations

import duckdb

from pipeline import gold


def _sales_connection() -> duckdb.DuckDBPyConnection:
    con = duckdb.connect(":memory:")
    con.execute(
        """
        CREATE TABLE silver_fact_ventas (
            num_documento VARCHAR,
            cod_clase VARCHAR,
            business_date DATE,
            nit_cliente VARCHAR,
            total_factura DOUBLE,
            estado_documento VARCHAR
        )
        """
    )
    con.execute(
        """
        CREATE TABLE silver_fact_ventas_detalle (
            num_documento VARCHAR,
            cod_clase VARCHAR,
            business_date DATE,
            cod_producto VARCHAR,
            cod_bodega VARCHAR,
            cantidad DOUBLE,
            valor_unitario DOUBLE,
            descuento_valor DOUBLE
        )
        """
    )
    con.execute(
        "CREATE TABLE silver_dim_producto (cod_producto VARCHAR, nombre_producto VARCHAR)"
    )
    con.execute(
        "CREATE TABLE silver_dim_bodega (cod_bodega VARCHAR, nombre_bodega VARCHAR)"
    )
    con.execute("INSERT INTO silver_dim_producto VALUES ('SKU-1', 'Producto')")
    con.execute("INSERT INTO silver_dim_bodega VALUES ('B-1', 'Principal')")
    return con


def test_daily_sales_mart_excludes_cancelled_invoices() -> None:
    con = _sales_connection()
    try:
        con.execute(
            """
            INSERT INTO silver_fact_ventas VALUES
                ('VALIDA', 'FV', DATE '2026-07-01', 'CLIENTE', 100.0, 'B'),
                ('ANULADA', 'FV', DATE '2026-07-01', 'CLIENTE', 900.0, 'A')
            """
        )
        con.execute(
            """
            INSERT INTO silver_fact_ventas_detalle VALUES
                ('VALIDA', 'FV', DATE '2026-07-01', 'SKU-1', 'B-1', 1, 100, 0),
                ('ANULADA', 'FV', DATE '2026-07-01', 'SKU-1', 'B-1', 1, 900, 0)
            """
        )

        gold.mart_ventas_diarias_sku(con)

        row = con.execute(
            "SELECT cantidad_total, valor_total, num_facturas "
            "FROM gold_mart_ventas_diarias_sku"
        ).fetchone()
        assert row == (1.0, 100.0, 1)
    finally:
        con.close()


def test_customer_cohorts_ignore_cancelled_invoices() -> None:
    con = _sales_connection()
    try:
        con.execute(
            """
            INSERT INTO silver_fact_ventas VALUES
                ('ANULADA', 'FV', DATE '2026-01-10', 'CLIENTE', 900.0, 'A'),
                ('VALIDA', 'FV', DATE '2026-02-10', 'CLIENTE', 100.0, 'B')
            """
        )

        gold.mart_cohortes_clientes(con)

        rows = con.execute(
            "SELECT mes_cohorte, business_month, ticket_promedio "
            "FROM gold_mart_cohortes_clientes ORDER BY business_month"
        ).fetchall()
        assert rows == [("2026-02-01", "2026-02-01", 100.0)]
    finally:
        con.close()


def test_dormant_products_ignore_recent_cancelled_sales() -> None:
    con = _sales_connection()
    try:
        con.execute(
            """
            CREATE TABLE gold_mart_inventario_actual (
                cod_producto VARCHAR,
                cantidad_actual DOUBLE
            )
            """
        )
        con.execute("INSERT INTO gold_mart_inventario_actual VALUES ('SKU-1', 5)")
        con.execute(
            """
            INSERT INTO silver_fact_ventas VALUES
                ('VALIDA', 'FV', CURRENT_DATE - INTERVAL '100' DAY,
                 'CLIENTE', 100.0, 'B'),
                ('ANULADA', 'FV', CURRENT_DATE, 'CLIENTE', 900.0, 'A')
            """
        )
        con.execute(
            """
            INSERT INTO silver_fact_ventas_detalle VALUES
                ('VALIDA', 'FV', CURRENT_DATE - INTERVAL '100' DAY,
                 'SKU-1', 'B-1', 1, 100, 0),
                ('ANULADA', 'FV', CURRENT_DATE,
                 'SKU-1', 'B-1', 1, 900, 0)
            """
        )

        gold.mart_productos_dormidos(con)

        row = con.execute(
            "SELECT ultima_fecha_venta = CURRENT_DATE - INTERVAL '100' DAY, "
            "dias_sin_venta FROM gold_mart_productos_dormidos "
            "WHERE cod_producto = 'SKU-1'"
        ).fetchone()
        assert row == (True, 100)
    finally:
        con.close()


def test_stockout_alerts_ignore_cancelled_sales_demand() -> None:
    con = _sales_connection()
    try:
        con.execute("ALTER TABLE silver_dim_producto ADD COLUMN existencia DOUBLE")
        con.execute("UPDATE silver_dim_producto SET existencia = 5 WHERE cod_producto = 'SKU-1'")
        con.execute(
            """
            INSERT INTO silver_fact_ventas VALUES
                ('VALIDA', 'FV', CURRENT_DATE, 'CLIENTE', 100.0, 'B'),
                ('ANULADA', 'FV', CURRENT_DATE, 'CLIENTE', 900.0, 'A')
            """
        )
        con.execute(
            """
            INSERT INTO silver_fact_ventas_detalle VALUES
                ('VALIDA', 'FV', CURRENT_DATE, 'SKU-1', 'B-1', 7, 100, 0),
                ('ANULADA', 'FV', CURRENT_DATE, 'SKU-1', 'B-1', 70, 900, 0)
            """
        )

        gold.alertas_quiebre(con)

        row = con.execute(
            "SELECT demanda_predicha, dias_hasta_quiebre, urgencia "
            "FROM gold_alertas_quiebre WHERE sku = 'SKU-1'"
        ).fetchone()
        assert row == (1.0, 5, "media")
    finally:
        con.close()
