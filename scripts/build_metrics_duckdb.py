"""Construye el artefacto chico del gold de MasVital: sólo las tablas que el backend lee.

Uso:
    python scripts/build_metrics_duckdb.py <gold_completo.duckdb> <salida.duckdb>

Se corre antes de publicar a R2. Abre el origen en sólo lectura, copia las tablas
del manifiesto y verifica que ninguna falte.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Permitir ejecucion directa como script agregando repo root al sys.path
_repo_root = Path(__file__).resolve().parent.parent
if str(_repo_root) not in sys.path:
    sys.path.insert(0, str(_repo_root))

import duckdb
from pipeline.artefacto import TABLAS_ARTEFACTO, VENTANA_POR_TABLA


def construir(origen: Path, destino: Path) -> dict[str, int]:
    if not origen.is_file():
        raise SystemExit(f"no existe el gold de origen: {origen}")
    if destino.exists():
        destino.unlink()

    con = duckdb.connect(str(destino))
    try:
        con.execute(f"ATTACH '{origen.as_posix()}' AS origen (READ_ONLY)")
        existentes = {
            fila[0].lower()
            for fila in con.execute(
                "SELECT table_name FROM information_schema.tables WHERE table_catalog = 'origen'"
            ).fetchall()
        }
        faltantes = [t for t in TABLAS_ARTEFACTO if t not in existentes]
        if faltantes:
            raise SystemExit(
                "el gold no tiene estas tablas del manifiesto: " + ", ".join(faltantes)
            )
        tamanos: dict[str, int] = {}
        for tabla in TABLAS_ARTEFACTO:
            fechas = VENTANA_POR_TABLA.get(tabla)
            if fechas:
                con.execute(
                    f"""
                    CREATE TABLE {tabla} AS
                    WITH ult AS (
                        SELECT DISTINCT business_date FROM origen.{tabla}
                        ORDER BY business_date DESC LIMIT {fechas}
                    )
                    SELECT s.* FROM origen.{tabla} s
                    JOIN ult USING (business_date)
                    """
                )
            else:
                con.execute(f"CREATE TABLE {tabla} AS SELECT * FROM origen.{tabla}")
            tamanos[tabla] = con.execute(f"SELECT COUNT(*) FROM {tabla}").fetchone()[0]
        con.execute("CHECKPOINT")
    finally:
        con.close()
    return tamanos


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    origen, destino = Path(sys.argv[1]), Path(sys.argv[2])
    tamanos = construir(origen, destino)
    total = destino.stat().st_size
    print(f"artefacto: {destino} ({total / 1_048_576:.1f} MB)")
    for tabla, filas in tamanos.items():
        print(f"  {tabla}: {filas} filas")
    print(f"gold origen: {origen.stat().st_size / 1_048_576:.1f} MB")


if __name__ == "__main__":
    main()
