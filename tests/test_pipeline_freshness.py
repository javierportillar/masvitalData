from __future__ import annotations

import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from types import SimpleNamespace

import duckdb
import pytest

from pipeline import run_all
from scripts import pipeline_runs_db


def _stub_pipeline_stages(monkeypatch) -> None:
    no_op_names = {
        "dim_producto",
        "dim_bodega",
        "fact_ventas",
        "fact_ventas_detalle",
        "fact_compras",
        "fact_compras_detalle",
        "fact_inventario",
    }
    monkeypatch.setattr(
        run_all,
        "silver",
        SimpleNamespace(**{name: (lambda _con: None) for name in no_op_names}),
    )
    gold_names = {
        "mart_ventas_diarias_sku",
        "mart_inventario_actual",
        "mart_cohortes_clientes",
        "mart_productos_dormidos",
        "mart_rotacion_abc",
        "forecast_categoria",
        "alertas_drift",
        "mart_abc_xyz",
        "mart_rotacion_promedio",
        "alertas_quiebre",
    }
    monkeypatch.setattr(
        run_all,
        "gold",
        SimpleNamespace(**{name: (lambda _con: None) for name in gold_names}),
    )
    monkeypatch.setitem(
        sys.modules,
        "pipeline.embeddings_skus",
        SimpleNamespace(generate_embeddings=lambda *_args, **_kwargs: 0),
    )


class _FakeMySqlCursor:
    def __init__(self) -> None:
        self.table = ""
        self.is_probe = False

    def execute(self, sql: str) -> None:
        self.is_probe = sql.startswith("SELECT 1 FROM")
        self.table = sql.rsplit("`", 2)[1]

    def fetchone(self) -> tuple[int] | None:
        return None if self.table == "facventas" else (1,)

    def fetchall(self) -> list[tuple[object, ...]]:
        if self.is_probe:
            row = self.fetchone()
            return [row] if row else []
        if self.table != "productos":
            return []
        column_count = next(
            len(columns)
            for mysql_table, _bronze_table, columns in run_all._MYSQL_BRONZE_MAP
            if mysql_table == "productos"
        )
        return [tuple(["NEW-SKU", *([None] * (column_count - 1))])]


class _FakeMySqlConnection:
    def __init__(self) -> None:
        self.was_closed = False
        self._cursor = _FakeMySqlCursor()

    def cursor(self) -> _FakeMySqlCursor:
        return self._cursor

    def close(self) -> None:
        self.was_closed = True


def test_mysql_builder_preserves_bronze_when_critical_table_is_empty(
    monkeypatch,
) -> None:
    mysql_connection = _FakeMySqlConnection()
    monkeypatch.setattr(run_all, "get_mysql_connection", lambda: mysql_connection)
    con = duckdb.connect(":memory:")
    con.execute("CREATE TABLE bronze_productos (codprod VARCHAR)")
    con.execute("INSERT INTO bronze_productos VALUES ('OLD-SKU')")
    con.execute("CREATE TABLE bronze_facventas (fecfven TIMESTAMP)")
    con.execute("INSERT INTO bronze_facventas VALUES (TIMESTAMP '2026-07-01')")
    try:
        result = run_all._build_bronze_from_mysql(con)

        assert result.refreshed is False
        assert "facventas" in str(result.warning)
        assert con.execute("SELECT codprod FROM bronze_productos").fetchall() == [
            ("OLD-SKU",)
        ]
        assert con.execute("SELECT COUNT(*) FROM bronze_facventas").fetchone() == (1,)
        assert mysql_connection.was_closed is True
    finally:
        con.close()


def test_reused_bronze_is_recorded_as_not_fresh(
    tmp_path: Path,
    monkeypatch,
) -> None:
    output_path = tmp_path / "masvital_gold.duckdb"
    con = duckdb.connect(str(output_path))
    con.execute("CREATE TABLE bronze_productos (codprod VARCHAR)")
    con.execute("INSERT INTO bronze_productos VALUES ('SKU-1')")
    con.execute("CREATE TABLE bronze_facventas (fecfven TIMESTAMP)")
    con.execute("INSERT INTO bronze_facventas VALUES (?)", [datetime.now(timezone.utc)])
    con.close()

    completed: dict[str, object] = {}

    monkeypatch.setattr(run_all, "OUTPUT_DIR", tmp_path)
    monkeypatch.setattr(run_all, "OUTPUT_PATH", output_path)
    monkeypatch.setattr(run_all, "_load_dotenv", lambda: None)
    monkeypatch.setattr(
        run_all,
        "_build_bronze_from_mysql",
        lambda _con: run_all.BronzeBuildResult(
            refreshed=False,
            warning="Critical MySQL table facventas returned zero rows",
        ),
    )
    monkeypatch.setattr(run_all, "start_stats_run", lambda _name: 17)
    monkeypatch.setattr(run_all, "capture_layer_stats", lambda *_args: None)
    monkeypatch.setattr(
        run_all,
        "complete_stats_run",
        lambda run_id, status, **kwargs: completed.update(
            {"run_id": run_id, "status": status, **kwargs}
        ),
    )

    _stub_pipeline_stages(monkeypatch)

    assert run_all.run_all(enable_stats=True) == str(output_path)
    assert completed["status"] == "success"
    assert completed["data_freshness_status"] == "reused_bronze"
    assert "not refreshed from MySQL" in str(completed["data_freshness_warning"])
    assert "facventas returned zero rows" in str(completed["data_freshness_warning"])


def test_reused_silver_is_recorded_as_not_fresh(
    tmp_path: Path,
    monkeypatch,
) -> None:
    output_path = tmp_path / "masvital_gold.duckdb"
    con = duckdb.connect(str(output_path))
    con.execute("CREATE TABLE silver_dim_producto (cod_producto VARCHAR)")
    con.execute("INSERT INTO silver_dim_producto VALUES ('SKU-1')")
    con.close()

    completed: dict[str, object] = {}

    def build_bronze_from_silver(con: duckdb.DuckDBPyConnection) -> None:
        con.execute("CREATE TABLE bronze_productos (codprod VARCHAR)")
        con.execute("INSERT INTO bronze_productos VALUES ('SKU-1')")
        con.execute("CREATE TABLE bronze_facventas (fecfven TIMESTAMPTZ)")
        con.execute("INSERT INTO bronze_facventas VALUES (?)", [datetime.now(timezone.utc)])

    monkeypatch.setattr(run_all, "OUTPUT_DIR", tmp_path)
    monkeypatch.setattr(run_all, "OUTPUT_PATH", output_path)
    monkeypatch.setattr(run_all, "_load_dotenv", lambda: None)
    monkeypatch.setattr(
        run_all,
        "_build_bronze_from_mysql",
        lambda _con: run_all.BronzeBuildResult(
            refreshed=False,
            warning="Critical MySQL table facventas returned zero rows",
        ),
    )
    monkeypatch.setattr(run_all, "_build_bronze_from_silver", build_bronze_from_silver)
    monkeypatch.setattr(run_all, "start_stats_run", lambda _name: 18)
    monkeypatch.setattr(run_all, "capture_layer_stats", lambda *_args: None)
    monkeypatch.setattr(
        run_all,
        "complete_stats_run",
        lambda run_id, status, **kwargs: completed.update(
            {"run_id": run_id, "status": status, **kwargs}
        ),
    )
    _stub_pipeline_stages(monkeypatch)

    assert run_all.run_all(enable_stats=True) == str(output_path)
    assert completed["status"] == "success"
    assert completed["data_freshness_status"] == "reused_silver"
    assert "facventas returned zero rows" in str(completed["data_freshness_warning"])


@pytest.mark.parametrize(
    ("latest_sale", "expected_status"),
    [
        (datetime.now(timezone.utc), "fresh"),
        (datetime.now(timezone.utc) - timedelta(days=2), "stale"),
        (None, "empty"),
    ],
)
def test_data_freshness_status_branches(
    latest_sale: datetime | None,
    expected_status: str,
    monkeypatch,
) -> None:
    monkeypatch.setattr(run_all, "_send_telegram_alert", lambda _message: None)
    con = duckdb.connect(":memory:")
    con.execute("CREATE TABLE bronze_facventas (fecfven TIMESTAMPTZ)")
    if latest_sale is not None:
        con.execute("INSERT INTO bronze_facventas VALUES (?)", [latest_sale])
    try:
        result = run_all._check_data_freshness(con)
        assert result.status == expected_status
        assert (result.warning is None) is (expected_status == "fresh")
    finally:
        con.close()


def test_data_freshness_is_unknown_when_sales_table_cannot_be_read() -> None:
    con = duckdb.connect(":memory:")
    try:
        result = run_all._check_data_freshness(con)
        assert result.status == "unknown"
        assert "No se pudo leer bronze_facventas" in str(result.warning)
    finally:
        con.close()


def test_stats_run_persists_structured_freshness_metadata(
    tmp_path: Path,
    monkeypatch,
) -> None:
    db_path = tmp_path / "pipeline_runs.duckdb"
    monkeypatch.setattr(pipeline_runs_db, "DB_PATH", db_path)
    legacy = duckdb.connect(str(db_path))
    legacy.execute(
        """
        CREATE TABLE app_pipeline_runs (
            id INTEGER PRIMARY KEY,
            pipeline_name VARCHAR NOT NULL,
            started_at TIMESTAMP NOT NULL,
            finished_at TIMESTAMP,
            status VARCHAR NOT NULL,
            duration_seconds INTEGER,
            rows_processed INTEGER,
            triggered_by VARCHAR NOT NULL,
            error_message TEXT
        )
        """
    )
    legacy.close()

    run_id = pipeline_runs_db.start_stats_run("run_all")
    pipeline_runs_db.complete_stats_run(
        run_id,
        "success",
        rows_processed=42,
        data_freshness_status="reused_bronze",
        data_freshness_warning="Bronze was not refreshed from MySQL",
    )

    con = duckdb.connect(str(db_path), read_only=True)
    try:
        row = con.execute(
            "SELECT status, rows_processed, data_freshness_status, "
            "data_freshness_warning FROM app_pipeline_runs WHERE id = ?",
            [run_id],
        ).fetchone()
        assert row == (
            "success",
            42,
            "reused_bronze",
            "Bronze was not refreshed from MySQL",
        )
    finally:
        con.close()
