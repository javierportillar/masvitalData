"""Explorador del esquema MySQL de MasVital.

UTILIDAD para Dev W: lista tablas, columnas, tipos y samples de cada tabla
en la BD MySQL de MasVital. Output en Markdown para commitear como
docs/mysql-schema-snapshot.md (insumo crítico para Dev Back en M3.4).

Usage:
    python -m pipeline.explore_mysql_schema

Requiere env vars:
    MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE
"""

from __future__ import annotations

import json
import os
from datetime import datetime


def _get_connection():
    import pymysql
    return pymysql.connect(
        host=os.environ.get("MYSQL_HOST", "localhost"),
        port=int(os.environ.get("MYSQL_PORT", "3306")),
        user=os.environ.get("MYSQL_USER", ""),
        password=os.environ.get("MYSQL_PASSWORD", ""),
        database=os.environ.get("MYSQL_DATABASE", ""),
        charset=os.environ.get("MYSQL_CHARSET", "latin1"),
        connect_timeout=10,
    )


def _get_all_tables(cur) -> list[str]:
    cur.execute("SHOW TABLES")
    return [r[0] for r in cur.fetchall()]


def _describe_table(cur, table: str) -> list[dict]:
    cur.execute(f"DESCRIBE `{table}`")
    columns = []
    for r in cur.fetchall():
        columns.append({
            "field": r[0],
            "type": r[1],
            "null": r[2],
            "key": r[3],
            "default": r[4],
            "extra": r[5],
        })
    return columns


def _sample_rows(cur, table: str, limit: int = 5) -> list[dict]:
    cur.execute(f"SELECT * FROM `{table}` LIMIT {limit}")
    col_names = [desc[0] for desc in cur.description]
    rows = []
    for r in cur.fetchall():
        rows.append(dict(zip(col_names, [str(v) if v is not None else None for v in r])))
    return rows


def _row_count(cur, table: str) -> int:
    cur.execute(f"SELECT COUNT(*) FROM `{table}`")
    return cur.fetchone()[0]


def explore() -> str:
    conn = _get_connection()
    cur = conn.cursor()

    db_name = os.environ.get("MYSQL_DATABASE", "")
    tables = _get_all_tables(cur)

    lines = [
        f"# MySQL Schema Snapshot -- {db_name}",
        "",
        f"Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Host: {os.environ.get('MYSQL_HOST', 'localhost')}",
        f"Tablas encontradas: {len(tables)}",
        "",
        "---",
        "",
    ]

    for table in sorted(tables):
        count = _row_count(cur, table)
        columns = _describe_table(cur, table)
        samples = _sample_rows(cur, table, limit=3)

        lines.append(f"## `{table}` ({count} filas)")
        lines.append("")
        lines.append("| Campo | Tipo | Nulo | Key | Default | Extra |")
        lines.append("|-------|------|------|-----|---------|-------|")
        for col in columns:
            null_str = "SI" if col["null"] == "YES" else "NO"
            default_str = str(col["default"]) if col["default"] is not None else ""
            lines.append(
                f"| {col['field']} | {col['type']} | {null_str} | "
                f"{col['key']} | {default_str} | {col['extra']} |"
            )

        lines.append("")
        lines.append("**Muestras (3 filas):**")
        lines.append("")
        lines.append("```json")
        lines.append(json.dumps(samples, indent=2, ensure_ascii=False))
        lines.append("```")
        lines.append("")
        lines.append("---")
        lines.append("")

    cur.close()
    conn.close()

    return "\n".join(lines)


if __name__ == "__main__":
    print(explore())
