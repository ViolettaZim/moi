from datetime import datetime
from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, CheckConstraint, UniqueConstraint
from sqlalchemy.sql import func
from geoalchemy2 import Geometry
from sqlalchemy.orm import relationship

from ...common.db import Base


class GreenZone(Base):
    __tablename__ = "green_zones"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    zone_type = Column(String(100), nullable=False)
    level = Column(Integer, nullable=False)
    description = Column(String(500), nullable=True)
    geom = Column(
        Geometry(
            geometry_type="MULTIPOLYGON",
            srid=4326,
            spatial_index=False,
        ),
        nullable=False,
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    __table_args__ = (
        CheckConstraint("level >= 0", name="ck_green_zones_level_non_negative"),
    )

    metrics = relationship("GreenZoneMetric", back_populates="zone", cascade="all, delete-orphan")


class GreenZoneMetric(Base):
    __tablename__ = "green_zone_metrics"

    id = Column(Integer, primary_key=True)
    zone_id = Column(Integer, ForeignKey("green_zones.id", ondelete="CASCADE"), nullable=False)
    year = Column(Integer, nullable=False)
    tree_count = Column(Integer, nullable=True)
    avg_height = Column(Numeric(precision=6, scale=2), nullable=True)
    avg_diameter = Column(Numeric(precision=6, scale=2), nullable=True)
    health_score = Column(Numeric(precision=3, scale=2), nullable=True)
    source = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    __table_args__ = (
        UniqueConstraint("zone_id", "year", name="uq_green_zone_metrics_zone_year"),
    )

    zone = relationship("GreenZone", back_populates="metrics")
    