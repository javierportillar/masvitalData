"""Qué tablas necesita el backend del gold de MasVital (para publicar un artefacto chico).

El gold tiene ~175 tablas de analítica; el backend sólo lee estas 16. Publicar un
``{tenant}_metrics.duckdb`` con únicamente estas tablas baja la descarga a unos pocos MB,
con la misma frescura: es lo que permite refrescar seguido sin saturar la memoria de Render.
"""

from __future__ import annotations

VENTANA_POR_TABLA: dict[str, int] = {
    "silver_fact_inventario": 7,
}

TABLAS_ARTEFACTO: tuple[str, ...] = (
    "silver_fact_ventas",
    "silver_fact_ventas_detalle",
    "silver_fact_compras",
    "silver_fact_compras_detalle",
    "silver_dim_producto",
    "silver_dim_bodega",
    "silver_fact_inventario",
    "gold_mart_ventas_diarias_sku",
    "gold_mart_inventario_actual",
    "gold_mart_productos_dormidos",
    "gold_mart_rotacion_abc",
    "gold_mart_abc_xyz",
    "gold_mart_cohortes_clientes",
    "gold_alertas_quiebre",
    "gold_alertas_drift",
    "gold_forecast_categoria",
)
