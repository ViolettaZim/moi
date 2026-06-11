from sqlalchemy.orm import Session
from sqlalchemy import func, select
from geoalchemy2.shape import from_shape
from geoalchemy2.functions import ST_AsText, ST_Intersects
from shapely import wkt as shapely_wkt

from .models import GreenZone, GreenZoneMetric
from .schemas import GreenZoneCreate, GreenZoneUpdate, GreenZoneMetricCreate, GreenZoneMetricUpdate


def _zone_to_dict(zone: GreenZone) -> dict:
    result = {
        "id": zone.id,
        "name": zone.name,
        "zone_type": zone.zone_type,
        "level": zone.level,
        "description": zone.description,
        "geom_wkt": None,
        "created_at": zone.created_at,
    }
    if zone.geom:
        result["geom_wkt"] = zone.geom
    return result


def get_zone(db: Session, zone_id: int):
    stmt = select(
        GreenZone.id,
        GreenZone.name,
        GreenZone.zone_type,
        GreenZone.level,
        GreenZone.description,
        ST_AsText(GreenZone.geom).label("geom_wkt"),
        GreenZone.created_at,
    ).where(GreenZone.id == zone_id)
    result = db.execute(stmt).first()
    return result._asdict() if result else None


def list_zones(db: Session, limit: int = 100, offset: int = 0):
    stmt = select(
        GreenZone.id,
        GreenZone.name,
        GreenZone.zone_type,
        GreenZone.level,
        GreenZone.description,
        ST_AsText(GreenZone.geom).label("geom_wkt"),
        GreenZone.created_at,
    ).order_by(GreenZone.id).limit(limit).offset(offset)
    results = db.execute(stmt).all()
    return [r._asdict() for r in results]


def create_zone(db: Session, data: GreenZoneCreate):
    geom = from_shape(shapely_wkt.loads(data.geom_wkt), srid=4326)
    zone = GreenZone(
        name=data.name,
        zone_type=data.zone_type,
        level=data.level,
        description=data.description,
        geom=geom,
    )
    db.add(zone)
    db.commit()
    db.refresh(zone)
    return get_zone(db, zone.id)


def update_zone(db: Session, zone_id: int, data: GreenZoneUpdate):
    zone = db.query(GreenZone).filter(GreenZone.id == zone_id).first()
    if not zone:
        return None

    update_data = data.model_dump(exclude_unset=True)
    if "geom_wkt" in update_data and update_data["geom_wkt"]:
        zone.geom = from_shape(shapely_wkt.loads(update_data["geom_wkt"]), srid=4326)
        del update_data["geom_wkt"]

    for field, value in update_data.items():
        if value is not None:
            setattr(zone, field, value)

    db.commit()
    db.refresh(zone)
    return get_zone(db, zone.id)


def delete_zone(db: Session, zone_id: int) -> bool:
    zone = db.query(GreenZone).filter(GreenZone.id == zone_id).first()
    if not zone:
        return False
    db.delete(zone)
    db.commit()
    return True


def list_intersecting_zones(db: Session, wkt: str, limit: int = 100, offset: int = 0):
    search_geom = from_shape(shapely_wkt.loads(wkt), srid=4326)
    stmt = select(
        GreenZone.id,
        GreenZone.name,
        GreenZone.zone_type,
        GreenZone.level,
        GreenZone.description,
        ST_AsText(GreenZone.geom).label("geom_wkt"),
        GreenZone.created_at,
    ).where(ST_Intersects(GreenZone.geom, search_geom)).limit(limit).offset(offset)
    results = db.execute(stmt).all()
    return [r._asdict() for r in results]


def create_metric(db: Session, zone_id: int, data: GreenZoneMetricCreate):
    metric = GreenZoneMetric(
        zone_id=zone_id,
        year=data.year,
        tree_count=data.tree_count,
        avg_height=data.avg_height,
        avg_diameter=data.avg_diameter,
        health_score=data.health_score,
        source=data.source,
    )
    db.add(metric)
    db.commit()
    db.refresh(metric)
    return metric


def list_metrics_by_zone(db: Session, zone_id: int):
    metrics = db.query(GreenZoneMetric).filter(GreenZoneMetric.zone_id == zone_id).order_by(GreenZoneMetric.year).all()
    return metrics


def get_metric(db: Session, metric_id: int):
    return db.query(GreenZoneMetric).filter(GreenZoneMetric.id == metric_id).first()


def update_metric(db: Session, metric_id: int, data: GreenZoneMetricUpdate):
    metric = db.query(GreenZoneMetric).filter(GreenZoneMetric.id == metric_id).first()
    if not metric:
        return None

    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        if value is not None:
            setattr(metric, field, value)

    db.commit()
    db.refresh(metric)
    return metric


def delete_metric(db: Session, metric_id: int) -> bool:
    metric = db.query(GreenZoneMetric).filter(GreenZoneMetric.id == metric_id).first()
    if not metric:
        return False
    db.delete(metric)
    db.commit()
    return True
