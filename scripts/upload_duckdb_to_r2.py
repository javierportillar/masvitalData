#!/usr/bin/env python3
"""Sube el DuckDB del tenant a Cloudflare R2.

Parametrizado por env vars -- NO hardcodea tenant ni object key.

Usage:
    python scripts/upload_duckdb_to_r2.py

Requiere en .env:
    R2_ENDPOINT, R2_ACCESS_KEY_ID, R2_SECRET_ACCESS_KEY, R2_BUCKET
    R2_OBJECT_KEY, LOCAL_DB_PATH
"""

from __future__ import annotations

import os
import sys
from pathlib import Path


def _load_dotenv() -> None:
    """Carga .env desde la raiz del repo si no están ya en el environment."""
    if os.environ.get("R2_ACCESS_KEY_ID", ""):
        return
    env_path = Path(__file__).resolve().parent.parent / ".env"
    if not env_path.exists():
        print(".env no encontrado en %s" % env_path)
        return
    loaded = 0
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key = key.strip()
        val = val.strip().strip("\"'").strip()
        if key and key not in os.environ:
            os.environ[key] = val
            loaded += 1
    print(".env cargado: %d variables (desde %s)" % (loaded, env_path))

TENANT = os.environ.get("TENANT", "masvital")
R2_ENDPOINT = os.environ.get(
    "R2_ENDPOINT",
    "https://4bd1502b7fa3f33d1d3c45ae2d252cfd.r2.cloudflarestorage.com",
)
R2_BUCKET = os.environ.get("R2_BUCKET", "motoshop-gold")
R2_OBJECT_KEY = os.environ.get("R2_OBJECT_KEY", "masvital_gold.duckdb")
LOCAL_DB_PATH = Path(os.environ.get("LOCAL_DB_PATH", "out/masvital_gold.duckdb"))
PIPELINE_DB_PATH = Path("out/pipeline_runs.duckdb")


def _upload_file(s3, local_path: Path, r2_key: str) -> None:
    if not local_path.exists():
        print(f"[SKIP] {local_path} no existe, saltando {r2_key}")
        return
    size_mb = local_path.stat().st_size / (1024 * 1024)
    print(f"Subiendo {local_path} ({size_mb:.0f} MB) -> s3://{R2_BUCKET}/{r2_key}")
    s3.upload_file(str(local_path), R2_BUCKET, r2_key)
    print(f"[OK] {r2_key}")


def main():
    _load_dotenv()

    r2_key = os.environ.get("R2_ACCESS_ID") or os.environ.get("R2_ACCESS_KEY_ID", "")
    r2_secret = os.environ.get("R2_SECRET_ACCESS_KEY", "")

    if not r2_key or not r2_secret:
        print("ERROR: R2_ACCESS_KEY_ID y R2_SECRET_ACCESS_KEY requeridas en entorno.")
        print("Set desde .env en el PC MasVital.")
        sys.exit(1)

    if not LOCAL_DB_PATH.exists():
        print(f"ERROR: DuckDB no encontrado en {LOCAL_DB_PATH}")
        print("Corre primero: python -m pipeline.run_all")
        sys.exit(1)

    import boto3
    s3 = boto3.client(
        "s3",
        endpoint_url=R2_ENDPOINT,
        aws_access_key_id=r2_key,
        aws_secret_access_key=r2_secret,
        region_name="auto",
    )

    _upload_file(s3, LOCAL_DB_PATH, R2_OBJECT_KEY)
    _upload_file(s3, PIPELINE_DB_PATH, f"{TENANT}_pipeline_runs.duckdb")


if __name__ == "__main__":
    main()
