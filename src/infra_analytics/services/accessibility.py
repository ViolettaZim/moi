"""Accessibility analysis services for green infrastructure."""

import geopandas as gpd

from ..utils.validators import (
    ensure_metric_crs,
    validate_crs,
    validate_not_empty,
    validate_radius,
)


def count_within_radius(
    trees_gdf: gpd.GeoDataFrame,
    infrastructure_gdf: gpd.GeoDataFrame,
    radius: float,
) -> gpd.GeoDataFrame:
    """
    Count infrastructure objects (irrigation, benches, lighting) within radius of each tree.

    Parameters
    ----------
    trees_gdf : gpd.GeoDataFrame
        GeoDataFrame with tree locations (points).
    infrastructure_gdf : gpd.GeoDataFrame
        GeoDataFrame with infrastructure objects (points).
    radius : float
        Buffer radius in meters.

    Returns
    -------
    gpd.GeoDataFrame
        Trees GeoDataFrame with 'infrastructure_count' column added.
    """
    validate_not_empty(trees_gdf, "Trees GeoDataFrame")
    validate_not_empty(infrastructure_gdf, "Infrastructure GeoDataFrame")
    validate_crs(trees_gdf, "Trees")
    validate_crs(infrastructure_gdf, "Infrastructure")
    validate_radius(radius)

    trees_metric = ensure_metric_crs(trees_gdf.copy())
    infrastructure_metric = ensure_metric_crs(infrastructure_gdf.copy())

    trees_metric["geometry"] = trees_metric.buffer(radius)

    joined = gpd.sjoin(
        infrastructure_metric, trees_metric, how="inner", predicate="within"
    )

    counts = joined.groupby(joined.index).size()
    trees_metric["infrastructure_count"] = counts

    trees_metric["geometry"] = trees_gdf.geometry.values
    trees_metric["infrastructure_count"] = (
        trees_metric["infrastructure_count"].fillna(0).astype(int)
    )

    return trees_metric


def unserved_trees(
    trees_gdf: gpd.GeoDataFrame,
    infrastructure_gdf: gpd.GeoDataFrame,
    radius: float,
) -> gpd.GeoDataFrame:
    """
    Identify trees with no infrastructure objects within radius.

    Parameters
    ----------
    trees_gdf : gpd.GeoDataFrame
        GeoDataFrame with tree locations (points).
    infrastructure_gdf : gpd.GeoDataFrame
        GeoDataFrame with infrastructure objects (points).
    radius : float
        Buffer radius in meters.

    Returns
    -------
    gpd.GeoDataFrame
        GeoDataFrame of trees with zero infrastructure objects within radius.
    """
    trees_with_counts = count_within_radius(trees_gdf, infrastructure_gdf, radius)
    unserved = trees_with_counts[trees_with_counts["infrastructure_count"] == 0].copy()
    return unserved


def accessibility_ratio(
    trees_gdf: gpd.GeoDataFrame,
    infrastructure_gdf: gpd.GeoDataFrame,
    radius: float,
) -> float:
    """
    Calculate ratio of trees that have at least one infrastructure object within radius.

    Parameters
    ----------
    trees_gdf : gpd.GeoDataFrame
        GeoDataFrame with tree locations (points).
    infrastructure_gdf : gpd.GeoDataFrame
        GeoDataFrame with infrastructure objects (points).
    radius : float
        Buffer radius in meters.

    Returns
    -------
    float
        Ratio of served trees (0 to 1).
    """
    trees_with_counts = count_within_radius(trees_gdf, infrastructure_gdf, radius)
    total_trees = len(trees_with_counts)
    served_trees = (trees_with_counts["infrastructure_count"] > 0).sum()

    if total_trees == 0:
        return 0.0

    return served_trees / total_trees
