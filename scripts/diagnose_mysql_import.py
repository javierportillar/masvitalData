#!/usr/bin/env python3
"""Diagnóstico de importación POS→MySQL para MasVital.

Uso (en PC MasVital):
    python scripts/diagnose_mysql_import.py

Requiere .env configurado con credenciales MySQL de MasVital.
Lee MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE.

Este script NO modifica nada — solo diagnóstico.
"""

from __future__ import annotations

import logging
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger("diagnose")

# ── Colores para la salida ──────────────────────────────────────────────────
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

REPO_ROOT = Path(__file__).resolve().parent.parent


def ok(msg: str) -> None:
    print(f"  {GREEN}✅ {msg}{RESET}")


def warn(msg: str) -> None:
    print(f"  {YELLOW}⚠️  {msg}{RESET}")


def fail(msg: str) -> None:
    print(f"  {RED}❌ {msg}{RESET}")


def info(msg: str) -> None:
    print(f"  {CYAN}ℹ️  {msg}{RESET}")


def header(title: str) -> None:
    print(f"\n{BOLD}═══ {title} ═══{RESET}")


def load_env() -> dict:
    """Carga .env manualmente (sin depender de load_env.ps1)."""
    env_file = REPO_ROOT / ".env"
    if not env_file.exists():
        fail(f"No se encuentra .env en {env_file}")
        return {}

    env_vars = {}
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key = key.strip()
        val = val.strip().strip("\"'").strip()
        # Solo cargar las que nos interesan
        if key.startswith("MYSQL_") or key in (
            "TENANT", "TELEGRAM_BOT_TOKEN", "TELEGRAM_GERENTE_CHAT_ID",
            "LOG_DIR", "LOCAL_DB_PATH", "R2_OBJECT_KEY",
        ):
            env_vars[key] = val
    return env_vars


# ── Checks ──────────────────────────────────────────────────────────────────


def check_mysql_connection(env: dict) -> bool:
    header("Conexión MySQL")
    required = ["MYSQL_HOST", "MYSQL_PORT", "MYSQL_USER", "MYSQL_PASSWORD", "MYSQL_DATABASE"]
    missing = [k for k in required if k not in env or not env[k]]
    if missing:
        fail(f"Faltan variables en .env: {', '.join(missing)}")
        return False

    info(f"Host: {env['MYSQL_HOST']}:{env['MYSQL_PORT']}, DB: {env['MYSQL_DATABASE']}, User: {env['MYSQL_USER']}")

    try:
        import pymysql
        conn = pymysql.connect(
            host=env["MYSQL_HOST"],
            port=int(env["MYSQL_PORT"]),
            user=env["MYSQL_USER"],
            password=env["MYSQL_PASSWORD"],
            database=env["MYSQL_DATABASE"],
            charset="latin1",
            connect_timeout=5,
        )
        ok(f"Conexión exitosa — MySQL {conn.get_server_info()}")
        conn.close()
        return True
    except ImportError:
        fail("pymysql no instalado — correr: pip install pymysql")
        return False
    except Exception as e:
        fail(f"No se pudo conectar a MySQL: {e}")
        return False


def check_mysql_tables_and_data(env: dict) -> None:
    header("Datos en MySQL (facventas)")

    try:
        import pymysql
        conn = pymysql.connect(
            host=env["MYSQL_HOST"],
            port=int(env["MYSQL_PORT"]),
            user=env["MYSQL_USER"],
            password=env["MYSQL_PASSWORD"],
            database=env["MYSQL_DATABASE"],
            charset="latin1",
            connect_timeout=5,
        )
        cur = conn.cursor()

        # ── 1. Últimas ventas ──────────────────────────────────────────────
        cur.execute("""
            SELECT fecfven, numfven, clifven, totfven, estfven
            FROM facventas
            ORDER BY fecfven DESC
            LIMIT 10
        """)
        rows = cur.fetchall()
        if not rows:
            fail("facventas está VACÍA — no hay ventas registradas en MySQL")
        else:
            ok(f"facventas tiene datos. Últimas 10 ventas:")
            for r in rows:
                fecha, num, cliente, total, est = r
                fecha_str = str(fecha) if fecha else "NULL"
                print(f"     📄 {fecha_str} | #{num} | {cliente or '?'} | ${total or 0} | [{est}]")

        # ── 2. Fecha máxima ────────────────────────────────────────────────
        cur.execute("SELECT MAX(fecfven) FROM facventas")
        max_fecha = cur.fetchone()[0]
        cur.execute("SELECT MIN(fecfven) FROM facventas WHERE fecfven IS NOT NULL")
        min_fecha = cur.fetchone()[0]

        if max_fecha:
            # Comparar con ahora
            try:
                if isinstance(max_fecha, str):
                    max_dt = datetime.fromisoformat(max_fecha.replace("Z", "+00:00"))
                else:
                    max_dt = max_fecha
                if max_dt.tzinfo is None:
                    from datetime import timedelta, timezone as tz
                    max_dt = max_dt.replace(tzinfo=tz(timedelta(hours=-5)))
                now = datetime.now(tz=timezone.utc)
                delta_h = (now - max_dt).total_seconds() / 3600

                if delta_h > 24:
                    fail(f"Última venta: {max_fecha} — HACE {delta_h:.0f} HORAS (datos CRÍTICAMENTE viejos)")
                elif delta_h > 12:
                    warn(f"Última venta: {max_fecha} — hace {delta_h:.0f}h (datos viejos)")
                else:
                    ok(f"Última venta: {max_fecha} — hace {delta_h:.0f}h (datos frescos)")
            except Exception:
                info(f"Última venta: {max_fecha}")
            info(f"Primera venta: {min_fecha}")
        else:
            fail("No se pudo determinar la fecha máxima de ventas")

        # ── 3. Ventas de HOY ─────────────────────────────────────────────
        cur.execute("""
            SELECT COUNT(*), COALESCE(SUM(totfven), 0)
            FROM facventas
            WHERE DATE(fecfven) = CURDATE()
        """)
        count_hoy, total_hoy = cur.fetchone()
        if count_hoy and count_hoy > 0:
            ok(f"Ventas de HOY: {count_hoy} facturas, total ${total_hoy:.0f}")
        else:
            # Fallback: tratar de comparar por fecha sin hora
            cur.execute("""
                SELECT COUNT(*), COALESCE(SUM(totfven), 0)
                FROM facventas
                WHERE DATE(fecfven) = DATE(NOW())
            """)
            count_hoy, total_hoy = cur.fetchone()
            if count_hoy and count_hoy > 0:
                ok(f"Ventas de HOY: {count_hoy} facturas, total ${total_hoy:.0f}")
            else:
                warn("NO hay ventas hoy en MySQL")

        # ── 4. Conteo de registros ────────────────────────────────────────
        for table in ("productos", "facventas", "detfventas", "compras", "detcompras", "auxinventario"):
            try:
                cur.execute(f"SELECT COUNT(*) FROM {table}")
                count = cur.fetchone()[0]
                print(f"     📊 {table}: {count} registros")
            except Exception as e:
                warn(f"No se pudo leer {table}: {e}")

        cur.close()
        conn.close()

    except Exception as e:
        fail(f"Error consultando MySQL: {e}")


def check_recent_pipeline_runs() -> None:
    header("Pipeline Runs Recientes")

    duckdb_path = REPO_ROOT / "out" / "pipeline_runs.duckdb"
    if not duckdb_path.exists():
        warn("No existe pipeline_runs.duckdb — el pipeline nunca corrió o se borró")
        return

    try:
        import duckdb
        con = duckdb.connect(str(duckdb_path))
        rows = con.execute("""
            SELECT started_at, finished_at, status, duration_seconds, triggered_by
            FROM app_pipeline_runs
            ORDER BY started_at DESC
            LIMIT 10
        """).fetchall()
        if not rows:
            warn("app_pipeline_runs está vacía")
        else:
            ok(f"Últimas {len(rows)} ejecuciones:")
            for r in rows:
                start, finish, status, dur, triggered = r
                status_icon = f"{GREEN}✅{RESET}" if status == "success" else f"{RED}❌{RESET}"
                dur_str = f"{dur}s" if dur else "?"
                print(f"     {status_icon} {str(start)[:19]} → {status} ({dur_str}) [{triggered}]")

        # Última corrida hoy?
        row = con.execute("""
            SELECT COUNT(*) FROM app_pipeline_runs
            WHERE DATE(started_at) = CURRENT_DATE
        """).fetchone()
        if row and row[0] > 0:
            ok(f"Pipeline corrió {row[0]} veces hoy")
        else:
            warn("Pipeline NO ha corrido hoy")

        con.close()
    except ImportError:
        warn("duckdb no instalado en este entorno")
    except Exception as e:
        warn(f"Error leyendo pipeline_runs.duckdb: {e}")


def check_mysql_service() -> None:
    header("Servicio MySQL (Windows)")

    # En Windows, verificar si el servicio MySQL está corriendo
    if sys.platform != "win32":
        warn("No estamos en Windows — saltando chequeo de servicio")
        return

    try:
        result = subprocess.run(
            ["sc", "query", "MySQL"],
            capture_output=True, text=True, timeout=10,
        )
        output = result.stdout + result.stderr
        if "RUNNING" in output:
            ok("Servicio MySQL (sc query MySQL): RUNNING")
        elif "STOPPED" in output:
            fail("Servicio MySQL (sc query MySQL): DETENIDO")
            info("Para iniciar: net start MySQL o Services.msc → MySQL → Start")
        else:
            # Probar con otros nombres de servicio
            for svc in ["MySQL80", "MySQL57", "MySQL55", "Mysql", "MariaDB"]:
                result = subprocess.run(
                    ["sc", "query", svc],
                    capture_output=True, text=True, timeout=5,
                )
                if "RUNNING" in result.stdout + result.stderr:
                    ok(f"Servicio {svc}: RUNNING")
                    break
            else:
                warn("No se pudo detectar servicio MySQL — puede ser MySQL 5.0 sin service wrapper")
                info("Verificar manualmente: Services.msc o `net start | findstr MySQL`")
    except Exception as e:
        warn(f"No se pudo verificar servicio MySQL: {e}")


def check_tcp_port(host: str = "localhost", port: int = 3306) -> None:
    header(f"Puerto TCP {host}:{port}")
    try:
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        result = s.connect_ex((host, port))
        s.close()
        if result == 0:
            ok(f"Puerto {port} — ACCESIBLE")
        else:
            fail(f"Puerto {port} — NO accesible (código {result})")
    except Exception as e:
        fail(f"Error chequeando puerto: {e}")


def check_disk_space() -> None:
    header("Espacio en disco")
    try:
        import shutil
        usage = shutil.disk_usage(REPO_ROOT)
        free_gb = usage.free / (1024**3)
        total_gb = usage.total / (1024**3)
        pct = usage.free / usage.total * 100
        if free_gb < 1:
            fail(f"Espacio libre: {free_gb:.1f} GB / {total_gb:.0f} GB ({pct:.0f}% libre) — CRÍTICO")
        elif free_gb < 5:
            warn(f"Espacio libre: {free_gb:.1f} GB / {total_gb:.0f} GB ({pct:.0f}% libre)")
        else:
            ok(f"Espacio libre: {free_gb:.1f} GB / {total_gb:.0f} GB ({pct:.0f}% libre)")
    except Exception as e:
        warn(f"No se pudo verificar espacio en disco: {e}")


def check_duckdb_integrity() -> None:
    header("Integridad DuckDB local")
    duckdb_path = REPO_ROOT / "out" / "masvital_gold.duckdb"
    if not duckdb_path.exists():
        warn("No existe masvital_gold.duckdb local")
        return

    size_mb = duckdb_path.stat().st_size / (1024**2)
    last_write = datetime.fromtimestamp(duckdb_path.stat().st_mtime)

    info(f"Tamaño: {size_mb:.1f} MB")
    info(f"Última modificación: {last_write}")

    try:
        import duckdb
        con = duckdb.connect(str(duckdb_path))

        # Verificar que las tablas principales existen y tienen datos
        checks = [
            ("bronze_productos", "productos"),
            ("bronze_facventas", "últimas ventas"),
            ("silver_fact_ventas", "ventas silver"),
            ("silver_dim_producto", "productos silver"),
        ]
        for table, desc in checks:
            try:
                count = con.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
                ok(f"{table} ({desc}): {count} registros")
            except Exception:
                warn(f"{table} ({desc}): no existe o error")

        # Mostrar fecha máxima
        try:
            row = con.execute("SELECT MAX(fecfven) FROM bronze_facventas").fetchone()
            info(f"Última venta en DuckDB: {row[0]}")
        except Exception:
            pass

        con.close()
    except Exception as e:
        warn(f"Error verificando DuckDB: {e}")


def check_repo_state() -> None:
    header("Estado del repositorio")
    try:
        import subprocess
        result = subprocess.run(
            ["git", "status", "--short"],
            capture_output=True, text=True, timeout=10,
            cwd=REPO_ROOT,
        )
        if result.returncode == 0:
            if result.stdout.strip():
                warn(f"Cambios sin commitear:\n{result.stdout}")
            else:
                ok("Working tree limpio")

        result = subprocess.run(
            ["git", "log", "--oneline", "-3"],
            capture_output=True, text=True, timeout=10,
            cwd=REPO_ROOT,
        )
        if result.returncode == 0:
            print(f"     Últimos commits:\n{result.stdout}")
    except Exception as e:
        warn(f"No se pudo verificar git: {e}")


# ── E-P-I-C (External POS Import Check) ─────────────────────────────────────

def check_pos_import_processes() -> None:
    """Intenta detectar si hay procesos de importación POS→MySQL activos."""
    header("Importación POS → MySQL")

    if sys.platform != "win32":
        warn("No estamos en Windows — saltando chequeo de procesos")
        return

    # Nombres de procesos que podrían ser el importador del POS
    candidates = [
        ("sgHermes", "sgHermes.exe (POS)"),
        ("HermesAdmin", "HermesAdmin.exe (Admin POS)"),
        ("mysqld", "mysqld.exe (MySQL server)"),
        ("MySQL", "MySQL.exe (MySQL)"),
    ]

    found_any = False
    for proc_name, display in candidates:
        try:
            result = subprocess.run(
                ["tasklist", "/FI", f"IMAGENAME eq {proc_name}", "/NH"],
                capture_output=True, text=True, timeout=10,
            )
            if proc_name.lower() in result.stdout.lower():
                ok(f"{display} — EN EJECUCIÓN")
                found_any = True
            else:
                info(f"{display} — NO detectado")
        except Exception as e:
            warn(f"Error chequeando {proc_name}: {e}")

    if not found_any:
        warn("No se detectaron procesos POS o MySQL — verificar si el POS está encendido")

    # Buscar posibles scripts de importación
    import_scripts = list(REPO_ROOT.rglob("*.bat")) + list(REPO_ROOT.rglob("*.ps1"))
    import_related = [f for f in import_scripts if "import" in f.stem.lower() or "capture" in f.stem.lower()]
    if import_related:
        info(f"Scripts relacionados encontrados en repo:")
        for f in import_related:
            print(f"     📜 {f.relative_to(REPO_ROOT)}")

    # Revisar logs del sistema por errores de MySQL
    try:
        result = subprocess.run(
            ["wevtutil", "qe", "System", "/q:*[System[Level=2]]", "/c:5", "/f:text"],
            capture_output=True, text=True, timeout=10,
        )
        mysql_errors = [l for l in result.stdout.splitlines() if "mysql" in l.lower()]
        if mysql_errors:
            warn(f"Errores recientes del sistema relacionados con MySQL ({len(mysql_errors)} líneas)")
            for err in mysql_errors[:3]:
                print(f"     {err.strip()}")
    except Exception:
        pass


# ── Resumen ─────────────────────────────────────────────────────────────────

def print_summary(env: dict) -> None:
    header("RESUMEN DE DIAGNÓSTICO")
    print(f"""
  Tenant:         {env.get('TENANT', '?')}
  MySQL Host:     {env.get('MYSQL_HOST', '?')}:{env.get('MYSQL_PORT', '?')}
  MySQL DB:       {env.get('MYSQL_DATABASE', '?')}
  R2 Object Key:  {env.get('R2_OBJECT_KEY', '?')}
  Log Dir:        {env.get('LOG_DIR', '?')}
  Telegram:       {'✅ configurado' if env.get('TELEGRAM_BOT_TOKEN') and '<COMPLETAR' not in env.get('TELEGRAM_BOT_TOKEN', '') else '⚠️  no configurado'}

  CORRECCIÓN RÁPIDA (si no hay datos en MySQL):
  1. Verificar que el POS sgHermes esté abierto y en uso
  2. Verificar que el servicio MySQL esté corriendo
  3. Buscar el proceso de importación POS→MySQL (preguntar al operador del POS)
  4. Si el importador es un .bat, revisar si está en el Startup de Windows
  5. Si nada funciona, reiniciar MySQL y el POS

  Si MySQL TIENE datos pero DuckDB no:
  1. El pipeline debería cargarlos automáticamente cada 30 min
  2. Forzar corrida: powershell -ExecutionPolicy Bypass -File infra\\refresh.ps1
  3. La última corrida fue hoy? Revisar refresh.log
""")


# ── Main ────────────────────────────────────────────────────────────────────

def main() -> None:
    print(f"\n{BOLD}{'='*60}{RESET}")
    print(f"{BOLD}  🔍 DIAGNÓSTICO MASVITAL — IMPORTACIÓN POS→MySQL{RESET}")
    print(f"{BOLD}{'='*60}{RESET}")
    print(f"  Repo: {REPO_ROOT}")
    print(f"  Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")

    env = load_env()

    if not env:
        fail("No se pudo cargar .env — el diagnóstico no puede continuar")
        sys.exit(1)

    ok(".env cargado correctamente")
    info(f"Tenant: {env.get('TENANT', '?')}")
    info(f"MySQL: {env.get('MYSQL_HOST', '?')}:{env.get('MYSQL_PORT', '?')}/{env.get('MYSQL_DATABASE', '?')}")

    # Ejecutar todos los checks
    mysql_ok = check_mysql_connection(env)
    if mysql_ok:
        check_mysql_tables_and_data(env)

    check_tcp_port(
        env.get("MYSQL_HOST", "localhost"),
        int(env.get("MYSQL_PORT", "3306")),
    )

    if sys.platform == "win32":
        check_mysql_service()

    check_recent_pipeline_runs()
    check_duckdb_integrity()
    check_disk_space()
    check_repo_state()
    check_pos_import_processes()
    print_summary(env)

    print(f"\n{BOLD}✅ Diagnóstico completado.{RESET}")
    print(f"   Revisar las marcas {RED}❌{RESET} y {YELLOW}⚠️{RESET} arriba para acciones prioritarias.\n")


if __name__ == "__main__":
    main()
