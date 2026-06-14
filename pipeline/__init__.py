"""Pipeline ETL parametrizado para MasVital (y cualquier tenant futuro).

Ejecuta bronze (MySQL) → silver → gold → embeddings, produce un archivo
DuckDB cuyo nombre incluye el tenant slug.

No importa nada de motoshopData — es self-contained para el PC MasVital.
"""

from __future__ import annotations
