from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

import duckdb
import pytest

from pipeline import run_all
from scripts import pipeline_runs_db


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
