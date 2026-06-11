from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional


class GreenZoneBase(BaseModel):
    name: str = Field(..., description="Name of the green zone")
    zone_type: str = Field(..., description="Type of zone (park, forest_park, etc.)")
    level: int = Field(..., ge=0, description="Administrative level")
    description: Optional[str] = Field(None, description="Description")
    geom_wkt: str = Field(..., description="Geometry in WKT format")


class GreenZoneCreate(GreenZoneBase):
    pass


class GreenZoneUpdate(BaseModel):
    name: Optional[str] = None
    zone_type: Optional[str] = None
    level: Optional[int] = Field(None, ge=0)
    description: Optional[str] = None
    geom_wkt: Optional[str] = None


class GreenZoneRead(BaseModel):
    id: int
    name: str
    zone_type: str
    level: int
    description: Optional[str] = None
    geom_wkt: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class GreenZoneMetricBase(BaseModel):
    year: int = Field(..., description="Year of measurement")
    tree_count: Optional[int] = Field(None, description="Number of trees")
    avg_height: Optional[float] = Field(None, description="Average tree height in meters")
    avg_diameter: Optional[float] = Field(None, description="Average tree diameter in cm")
    health_score: Optional[float] = Field(None, ge=0, le=1, description="Health score (0-1)")
    source: Optional[str] = Field(None, description="Data source")


class GreenZoneMetricCreate(GreenZoneMetricBase):
    pass


class GreenZoneMetricUpdate(BaseModel):
    year: Optional[int] = None
    tree_count: Optional[int] = None
    avg_height: Optional[float] = None
    avg_diameter: Optional[float] = None
    health_score: Optional[float] = Field(None, ge=0, le=1)
    source: Optional[str] = None


class GreenZoneMetricRead(BaseModel):
    id: int
    zone_id: int
    year: int
    tree_count: Optional[int] = None
    avg_height: Optional[float] = None
    avg_diameter: Optional[float] = None
    health_score: Optional[float] = None
    source: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
    