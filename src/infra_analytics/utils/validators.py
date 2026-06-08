<<<<<<< HEAD
"""Validation utilities for infra_analytics library."""

import geopandas as gpd

from ..exceptions import (
    EmptyDataError,
    InvalidCRSError,
    InvalidRadiusError,
    InvalidTreeDataError,
)
=======
import geopandas as gpd

from ..exceptions import EmptyDataError, InvalidCRSError, InvalidRadiusError
>>>>>>> master


def validate_not_empty(gdf: gpd.GeoDataFrame, name: str) -> None:
    """Validate that GeoDataFrame is not empty."""
    if gdf.empty:
        raise EmptyDataError(f"{name} is empty. Cannot perform operation.")


def validate_crs(gdf: gpd.GeoDataFrame, name: str) -> None:
    """Validate that GeoDataFrame has CRS."""
    if gdf.crs is None:
        raise InvalidCRSError(f"{name} has no CRS set. Please set CRS first.")


def validate_radius(radius: float) -> None:
    """Validate that radius is positive."""
    if radius <= 0:
        raise InvalidRadiusError(f"Radius must be positive. Got: {radius}")


<<<<<<< HEAD
def validate_tree_metrics(diameter: float, height: float) -> None:
    """Validate tree biometric parameters."""
    if diameter < 0:
        raise InvalidTreeDataError(f"Tree diameter cannot be negative: {diameter}")
    if height < 0:
        raise InvalidTreeDataError(f"Tree height cannot be negative: {height}")


=======
>>>>>>> master
def ensure_metric_crs(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """Convert GeoDataFrame to metric CRS if not already."""
    if gdf.crs and not gdf.crs.is_projected:
        gdf = gdf.to_crs("EPSG:32631")
    return gdf
<<<<<<< HEAD
=======

>>>>>>> master
