"""Pipeline orquestador parametrizado por tenant.

Ejecuta en orden: carga bronze (MySQL) -> silver -> gold -> embeddings.

El DuckDB final se llama {TENANT}_gold.duckdb y contiene tablas bronze,
silver y gold sin prefijo de tenant (el tenancy lo da el archivo).

Usage:
    python -m pipeline.run_all

Requiere env vars:
    TENANT=masvital
    MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE
"""

from __future__ import annotations

import logging
import os
import sys
import urllib.request
import urllib.error
import json
from datetime import datetime, timezone
from pathlib import Path

import duckdb

from pipeline import gold, silver
from pipeline.mysql_source import get_mysql_connection, logger as mysql_logger
from scripts.pipeline_runs_db import capture_layer_stats, start_stats_run, complete_stats_run

logger = logging.getLogger(__name__)

TENANT = os.environ.get("TENANT", "masvital")
OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "out"))
OUTPUT_PATH = OUTPUT_DIR / f"{TENANT}_gold.duckdb"

# Map MySQL tables -> bronze table names and their column aliases
# Formato: (mysql_table, bronze_table, [(mysql_col, bronze_col), ...])
# Este mapeo se ajusta en M3.4 segun el esquema real de MasVital.
_MYSQL_BRONZE_MAP = [
    ("productos", "bronze_productos", [
        ("codprod", "codprod"), ("nomprod", "nomprod"), ("codbar", "codbar"),
        ("codmed", "codmed"), ("valmed", "valmed"), ("presen", "presen"),
        ("stockmin", "stockmin"), ("stockmax", "stockmax"), ("exiprod", "exiprod"),
        ("cosprod", "cosprod"), ("cosulc", "cosulc"), ("pvsini", "pvsini"),
        ("pvconi", "pvconi"), ("actprod", "actprod"), ("codpor", "codpor"),
        ("codlin1", "codlin1"), ("desprod", "desprod"), ("nitter", "nitter"),
        ("codbod", "codbod"), ("fecapa", "fecapa"),
    ]),
    ("bodegas", "bronze_bodegas", [
        ("codbod", "codbod"), ("nombod", "nombod"), ("telbod", "telbod"),
        ("ubibod", "ubibod"), ("resbod", "resbod"),
    ]),
    ("facventas", "bronze_facventas", [
        ("numfven", "numfven"), ("codclas", "codclas"), ("prefven", "prefven"),
        ("fecfven", "fecfven"), ("nitter", "nitter"), ("clifven", "clifven"),
        ("nitvend", "nitvend"), ("venfven", "venfven"), ("codpag", "codpag"),
        ("diasfven", "diasfven"), ("subfven", "subfven"),
        ("totdct", "dctofven"), ("totiva", "ivafven"), ("totipo", "totimp"),
        ("retfte", "retefte"), ("retiva", "reteiva"), ("retica", "reteica"),
        ("totfven", "totfven"), ("obsfven", "obsfven"), ("estfven", "estfven"),
        ("codsuc", "codsuc"), ("codemp", "codemp"),
        (None, "codempal"),
        ("codres", "codres"),
    ]),
    ("detfventas", "bronze_detfventas", [
        ("numfven", "numfven"), ("codclas", "codclas"), ("codprod", "codprod"),
        ("nomdet", "nomdet"), ("candet", "candet"), ("valuni", "valuni"),
        ("dctpor", "dctpor"), ("dctpes", "dctpes"), ("ivapor", "ivapor"),
        ("ivapes", "ivapes"), ("ipopor", "ipopor"), ("ipopes", "ipopes"),
        ("totdet", "totdet"), ("cosprod", "cosprod"), ("numite", "numite"),
        ("codbod", "codbod"), ("codcos", "codcos"),
    ]),
    ("compras", "bronze_faccompras", [
        ("numcom", "numfcom"), ("codclas", "codclas"),
        ("feccom", "fecfcom"), ("nitter", "nitpro"),
        ("procom", "profcom"), ("codpag", "codpag"),
        ("totcom", "totfcom"), ("estcom", "estfcom"),
    ]),
    ("detcompras", "bronze_detfcompras", [
        ("numcom", "numfcom"), ("codclas", "codclas"), ("codprod", "codprod"),
        ("nomdet", "nomdet"), ("candet", "candet"), ("valuni", "valuni"),
        ("totdet", "totdet"), ("cosprod", "cosprod"),
    ]),
    ("auxinventario", "bronze_auxinventario", [
        ("codlis", "codlis"), ("nomlis", "nomlis"), ("codlin1", "codlin1"),
        ("nomlin", "nomlin"), ("codlin2", "codlin2"), ("nomlin2", "nomlin2"),
        ("codbod", "codbod"), ("nombod", "nombod"), ("nitter", "nitter"),
        ("nomter", "nomter"), ("numdoc", "numdoc"), ("nomdoc", "nomdoc"),
        ("codprod", "codprod"), ("sernum", "sernum"), ("nomprod", "nomprod"),
        ("unimed", "unimed"), ("valor1", "valor1"), ("valor2", "valor2"),
        ("valor3", "valor3"), ("valor4", "valor4"), ("valor5", "valor5"),
        ("docfec", "docfec"), ("docnum", "docnum"), ("nomsub", "nomsub"),
        ("multiplo", "multiplo"), ("codcos", "codcos"), ("nomcos", "nomcos"),
    ]),
]


def _build_bronze_from_mysql(con: duckdb.DuckDBPyConnection) -> bool:
    """Lee MySQL y reconstruye tablas bronze en DuckDB.

    Returns True si pudo conectar y cargar al menos productos.
    """
    mysql_conn = get_mysql_connection()
    if mysql_conn is None:
        logger.info("MySQL no disponible -- usando bronze existente o seed")
        return False

    try:
        cur = mysql_conn.cursor()
        total_rows = 0

        for mysql_table, bronze_table, columns in _MYSQL_BRONZE_MAP:
            select_parts = []
            for mysql_col, bronze_col in columns:
                if mysql_col is None:
                    select_parts.append(f"NULL AS `{bronze_col}`")
                else:
                    select_parts.append(f"`{mysql_col}` AS `{bronze_col}`")

            select_sql = ", ".join(select_parts)

            cur.execute(f'SELECT {select_sql} FROM `{mysql_table}`')
            rows = cur.fetchall()
            col_names = [bronze_col for _, bronze_col in columns]

            if not rows:
                logger.info("  MySQL %s: 0 rows, skipping", mysql_table)
                continue

            con.execute(f"DROP TABLE IF EXISTS {bronze_table}")

            col_defs = ", ".join([f'"{c}" VARCHAR' for c in col_names])
            con.execute(f"CREATE TABLE {bronze_table} ({col_defs})")

            placeholders = ", ".join(["?"] * len(col_names))
            col_names_q = ", ".join([f'"{c}"' for c in col_names])
            stmt = f"INSERT INTO {bronze_table} ({col_names_q}) VALUES ({placeholders})"

            batch = []
            for row in rows:
                processed = [str(v) if v is not None else None for v in row]
                batch.append(processed)
                if len(batch) >= 1000:
                    con.executemany(stmt, batch)
                    batch = []
            if batch:
                con.executemany(stmt, batch)

            total_rows += len(rows)
            logger.info("  MySQL %s -> %s: %d rows", mysql_table, bronze_table, len(rows))

        try:
            max_date = con.execute("SELECT MAX(fecfven) FROM bronze_facventas").fetchone()[0]
        except Exception:
            max_date = "N/A"

        logger.info(
            "Bronze refreshed from MySQL -- %d filas totales, hasta %s",
            total_rows,
            max_date,
        )
        return True

    except Exception as e:
        logger.warning("MySQL bronze refresh failed: %s -- usando bronze existente", e)
        return False
    finally:
        mysql_conn.close()


def _build_bronze_from_silver(con: duckdb.DuckDBPyConnection) -> None:
    """Crea tablas bronze desde silver existente (modo offline)."""

    con.execute("""
        CREATE TABLE bronze_productos AS
        SELECT
            cod_producto           AS codprod,
            nombre_producto        AS nomprod,
            codigo_barras          AS codbar,
            cod_medida             AS codmed,
            valor_medida           AS valmed,
            presentacion           AS presen,
            stock_minimo           AS stockmin,
            stock_maximo           AS stockmax,
            existencia             AS exiprod,
            costo_producto         AS cosprod,
            costo_ultima_compra    AS cosulc,
            precio_venta_sin_iva   AS pvsini,
            precio_venta_con_iva   AS pvconi,
            estado_producto        AS actprod,
            cod_grupo              AS codpor,
            cod_linea1             AS codlin1,
            descripcion            AS desprod,
            nit_proveedor          AS nitter,
            cod_bodega_default     AS codbod,
            fecha_actualizacion    AS fecapa
        FROM silver_dim_producto
    """)

    con.execute("""
        CREATE TABLE bronze_bodegas AS
        SELECT
            cod_bodega    AS codbod,
            nombre_bodega AS nombod,
            telefono      AS telbod,
            ubicacion     AS ubibod,
            responsable   AS resbod
        FROM silver_dim_bodega
    """)

    con.execute("""
        CREATE TABLE bronze_facventas AS
        SELECT
            num_documento       AS numfven,
            cod_clase           AS codclas,
            prefijo             AS prefven,
            CAST(fecha_documento_ts AS TIMESTAMP) AS fecfven,
            nit_cliente         AS nitter,
            nombre_cliente      AS clifven,
            nit_vendedor        AS nitvend,
            nombre_vendedor     AS venfven,
            cod_formapago       AS codpag,
            dias_formapago      AS diasfven,
            subtotal            AS subfven,
            total_descuentos    AS dctofven,
            total_iva           AS ivafven,
            total_impuesto      AS totimp,
            retencion_fuente    AS retefte,
            retencion_iva       AS reteiva,
            retencion_ica       AS reteica,
            total_factura       AS totfven,
            observaciones       AS obsfven,
            estado_documento    AS estfven,
            cod_sucursal        AS codsuc,
            cod_empresa         AS codemp,
            cod_empresa_alt     AS codempal,
            cod_resolucion      AS codres
        FROM silver_fact_ventas
    """)

    con.execute("""
        CREATE TABLE bronze_detfventas AS
        SELECT
            num_documento        AS numfven,
            cod_clase            AS codclas,
            cod_producto         AS codprod,
            nombre_detalle       AS nomdet,
            cantidad             AS candet,
            valor_unitario       AS valuni,
            descuento_porcentaje AS dctpor,
            descuento_valor      AS dctpes,
            iva_porcentaje       AS ivapor,
            iva_valor            AS ivapes,
            ipo_porcentaje       AS ipopor,
            ipo_valor            AS ipopes,
            total_detalle        AS totdet,
            costo_producto       AS cosprod,
            num_item             AS numite,
            cod_bodega           AS codbod,
            cod_centro_costo     AS codcos
        FROM silver_fact_ventas_detalle
    """)

    con.execute("""
        CREATE TABLE bronze_faccompras AS
        SELECT
            num_documento    AS numfcom,
            cod_clase        AS codclas,
            business_date    AS fecfcom,
            nit_proveedor    AS nitpro,
            nombre_proveedor AS profcom,
            cod_formapago    AS codpag,
            total_factura    AS totfcom,
            estado_documento AS estfcom
        FROM silver_fact_compras
    """)

    con.execute("""
        CREATE TABLE bronze_detfcompras AS
        SELECT
            num_documento  AS numfcom,
            cod_clase      AS codclas,
            cod_producto   AS codprod,
            nombre_detalle AS nomdet,
            cantidad       AS candet,
            valor_unitario AS valuni,
            total_detalle  AS totdet,
            costo_producto AS cosprod
        FROM silver_fact_compras_detalle
    """)

    logger.info(
        "Bronze built from silver -- productos=%d bodegas=%d ventas=%d detalle=%d compras=%d",
        con.execute("SELECT COUNT(*) FROM bronze_productos").fetchone()[0],
        con.execute("SELECT COUNT(*) FROM bronze_bodegas").fetchone()[0],
        con.execute("SELECT COUNT(*) FROM bronze_facventas").fetchone()[0],
        con.execute("SELECT COUNT(*) FROM bronze_detfventas").fetchone()[0],
        con.execute("SELECT COUNT(*) FROM bronze_faccompras").fetchone()[0],
    )


# ── Threshold de frescura de datos ──────────────────────────────────────────
# Si la última venta en MySQL es más vieja que esto, se logea WARNING + Telegram.
_MAX_DATA_AGE_HOURS = 18  # tolera cierre nocturno (~19:00 → ~13:00 del día siguiente)


def _send_telegram_alert(message: str) -> None:
    """Envía una alerta a Telegram si el token y chat_id están configurados."""
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.environ.get("TELEGRAM_GERENTE_CHAT_ID", "").strip()
    if not token or not chat_id or "<COMPLETAR" in token or "<COMPLETAR" in chat_id:
        return  # silently skip — no configurado
    try:
        payload = json.dumps({
            "chat_id": chat_id,
            "text": f"🚨 MasVital — {message}",
            "parse_mode": "HTML",
        }).encode("utf-8")
        req = urllib.request.Request(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        urllib.request.urlopen(req, timeout=10)
    except Exception as exc:
        logger.warning("Telegram alert falló: %s", exc)


def _check_data_freshness(con: duckdb.DuckDBPyConnection) -> None:
    """Verifica que las ventas en MySQL sean recientes y alerta si están viejas.

    Debe llamarse DESPUÉS de que bronze_facventas exista.
    """
    try:
        row = con.execute("SELECT MAX(fecfven) FROM bronze_facventas").fetchone()
        max_date_raw = row[0] if row and row[0] else None
    except Exception as exc:
        logger.warning("DATA FRESHNESS: no se pudo leer bronze_facventas — %s", exc)
        return

    if max_date_raw is None:
        logger.warning("DATA FRESHNESS: bronze_facventas está VACÍA — sin ventas en MySQL")
        _send_telegram_alert("⚠️ No hay ventas registradas en MySQL de MasVital")
        return

    # Normalizar a datetime
    if isinstance(max_date_raw, str):
        max_dt = datetime.fromisoformat(max_date_raw.replace("Z", "+00:00"))
    else:
        max_dt = max_date_raw

    # Si el datetime no tiene timezone, asumir UTC
    if max_dt.tzinfo is None:
        # La PC MasVital está en America/Bogota (UTC-5)
        from datetime import timedelta, timezone as tz
        bogota = tz(timedelta(hours=-5))
        max_dt = max_dt.replace(tzinfo=bogota)

    now = datetime.now(tz=timezone.utc)
    delta_hours = (now - max_dt).total_seconds() / 3600

    if delta_hours > _MAX_DATA_AGE_HOURS:
        # Si pasa de 24h, es CRÍTICO
        level = "CRÍTICO" if delta_hours > 24 else "ADVERTENCIA"
        msg = (
            f"DATA FRESHNESS [{level}]: Última venta en MySQL fue "
            f"{max_date_raw} (hace {delta_hours:.1f}h) — "
            f"el POS NO está escribiendo nuevas ventas a MySQL."
        )
        logger.warning(msg)

        telegram_msg = (
            f"🔴 Datos desactualizados ({delta_hours:.0f}h sin ventas nuevas). "
            f"Última venta: {max_date_raw}. "
            f"Revisar importación POS→MySQL en PC MasVital."
        )
        _send_telegram_alert(telegram_msg)
    else:
        logger.info(
            "DATA FRESHNESS OK: última venta %s (hace %.1fh)",
            max_date_raw, delta_hours,
        )


def _load_dotenv() -> None:
    """Carga .env desde la raiz del repo si no están ya en el environment."""
    # Si MYSQL_HOST ya está en env, respetar (lo cargó el PS1)
    if os.environ.get("MYSQL_HOST", ""):
        return

    env_path = Path(__file__).resolve().parent.parent / ".env"
    if not env_path.exists():
        logger.warning(".env no encontrado en %s — usar env vars manualmente", env_path)
        return

    loaded = 0
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key = key.strip()
        val = val.strip().strip("\"'").strip()
        # No sobrescribir vars ya definidas
        if key and key not in os.environ:
            os.environ[key] = val
            loaded += 1

    logger.info(".env cargado: %d variables (desde %s)", loaded, env_path)


def run_all(enable_stats: bool = True) -> str:
    """Pipeline completo: bronze -> silver -> gold."""
    # ── Cargar .env ANTES de cualquier conexion ──────────────────────────
    _load_dotenv()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    stats_run_id = None
    if enable_stats:
        try:
            stats_run_id = start_stats_run("run_all")
            logger.info("Stats capture run #%d started in pipeline_runs.duckdb", stats_run_id)
        except Exception as exc:
            logger.warning("Stats capture init failed: %s — continuando sin stats", exc)
            stats_run_id = None

    logger.info("Pipeline iniciado para tenant=%s output=%s", TENANT, OUTPUT_PATH)

    con = duckdb.connect(str(OUTPUT_PATH))

    # Paso 1: Bronze desde MySQL
    mysql_ok = _build_bronze_from_mysql(con)

    if not mysql_ok:
        bronze_exists = False
        try:
            count = con.execute("SELECT COUNT(*) FROM bronze_productos").fetchone()[0]
            bronze_exists = count > 0
        except Exception:
            pass

        if not bronze_exists:
            silver_exists = False
            try:
                con.execute("SELECT COUNT(*) FROM silver_dim_producto").fetchone()
                silver_exists = True
            except Exception:
                pass

            if silver_exists:
                logger.info("Silver tables found -- building bronze via reverse-mapping")
                _build_bronze_from_silver(con)
            else:
                raise RuntimeError(
                    "Ni MySQL, ni bronze_productos, ni silver_dim_producto existen -- "
                    "conecta MySQL o provee un DuckDB base"
                )
        else:
            logger.info("Bronze tables already exist, skipping build")

    # Stats: Bronze
    if stats_run_id is not None:
        con.close()
        try:
            logger.info("Capturing bronze stats...")
            capture_layer_stats(stats_run_id, "bronze", str(OUTPUT_PATH))
        except Exception as exc:
            logger.warning("Bronze stats capture failed: %s", exc)
        con = duckdb.connect(str(OUTPUT_PATH))

    # ── Data Freshness Check ────────────────────────────────────────────────
    # Verifica que MySQL haya recibido ventas recientes.
    # Si la última venta es muy vieja, logea WARNING y envía alerta Telegram.
    try:
        _check_data_freshness(con)
    except Exception as exc:
        logger.warning("Data freshness check error: %s", exc)

    # Paso 2: Silver
    logger.info("Running silver transformations...")
    silver.dim_producto(con)
    silver.dim_bodega(con)
    silver.fact_ventas(con)
    silver.fact_ventas_detalle(con)
    silver.fact_compras(con)
    silver.fact_compras_detalle(con)
    silver.fact_inventario(con)
    logger.info("Silver: 7/7 transformations complete")

    # Stats: Silver
    if stats_run_id is not None:
        con.close()
        try:
            logger.info("Capturing silver stats...")
            capture_layer_stats(stats_run_id, "silver", str(OUTPUT_PATH))
        except Exception as exc:
            logger.warning("Silver stats capture failed: %s", exc)
        con = duckdb.connect(str(OUTPUT_PATH))

    # Paso 3: Gold
    logger.info("Running gold transformations...")
    gold.mart_ventas_diarias_sku(con)
    gold.mart_inventario_actual(con)
    gold.mart_cohortes_clientes(con)
    gold.mart_productos_dormidos(con)
    gold.mart_rotacion_abc(con)
    gold.forecast_categoria(con)
    gold.alertas_drift(con)
    gold.mart_abc_xyz(con)
    gold.mart_rotacion_promedio(con)
    gold.alertas_quiebre(con)
    logger.info("Gold: 10/10 transformations complete")

    # Paso 4: Embeddings (solo si hay productos sin embedding)
    try:
        from pipeline.embeddings_skus import generate_embeddings
        embed_count = generate_embeddings(str(OUTPUT_PATH), mode="delta")
        if embed_count > 0:
            logger.info("Embeddings: %d SKUs processed", embed_count)
    except ImportError:
        logger.info("Embeddings skipped: sentence-transformers no instalado")
    except Exception as exc:
        logger.warning("Embeddings skipped: %s", exc)

    # Stats: Gold
    if stats_run_id is not None:
        con.close()
        try:
            logger.info("Capturing gold stats...")
            capture_layer_stats(stats_run_id, "gold", str(OUTPUT_PATH))
            complete_stats_run(stats_run_id, "success")
            logger.info("Stats capture run #%d complete", stats_run_id)
        except Exception as exc:
            logger.warning("Gold stats capture failed: %s", exc)
            try:
                complete_stats_run(stats_run_id, "failed")
            except Exception:
                pass

    con.close()
    logger.info("Pipeline completo -> %s", OUTPUT_PATH)
    return str(OUTPUT_PATH)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    path = run_all()
    print(f"\nPipeline exitoso -> {path}")
