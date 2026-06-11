from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from ...common.db import get_db
from . import crud
from .schemas import (
    GreenZoneCreate,
    GreenZoneUpdate,
    GreenZoneRead,
    GreenZoneMetricCreate,
    GreenZoneMetricUpdate,
    GreenZoneMetricRead,
)

router = APIRouter(prefix="/green-zones", tags=["Green Zones"])


@router.post("/", response_model=GreenZoneRead, status_code=201)
def create_zone(data: GreenZoneCreate, db: Session = Depends(get_db)):
    return crud.create_zone(db, data)


@router.get("/", response_model=list[GreenZoneRead])
def list_zones(limit: int = 100, offset: int = 0, db: Session = Depends(get_db)):
    return crud.list_zones(db, limit, offset)


@router.get("/intersects", response_model=list[GreenZoneRead])
def list_intersecting_zones(
    wkt: str = Query(..., description="WKT geometry to intersect with"),
    limit: int = 100,
    offset: int = 0,
    db: Session = Depends(get_db)
):
    return crud.list_intersecting_zones(db, wkt, limit, offset)


@router.get("/{zone_id}", response_model=GreenZoneRead)
def get_zone(zone_id: int, db: Session = Depends(get_db)):
    zone = crud.get_zone(db, zone_id)
    if not zone:
        raise HTTPException(status_code=404, detail="Green zone not found")
    return zone


@router.put("/{zone_id}", response_model=GreenZoneRead)
def update_zone(zone_id: int, data: GreenZoneUpdate, db: Session = Depends(get_db)):
    zone = crud.update_zone(db, zone_id, data)
    if not zone:
        raise HTTPException(status_code=404, detail="Green zone not found")
    return zone


@router.delete("/{zone_id}", status_code=204)
def delete_zone(zone_id: int, db: Session = Depends(get_db)):
    if not crud.delete_zone(db, zone_id):
        raise HTTPException(status_code=404, detail="Green zone not found")
    return None


@router.post("/{zone_id}/metrics", response_model=GreenZoneMetricRead, status_code=201)
def create_metric(zone_id: int, data: GreenZoneMetricCreate, db: Session = Depends(get_db)):
    zone = crud.get_zone(db, zone_id)
    if not zone:
        raise HTTPException(status_code=404, detail="Green zone not found")
    return crud.create_metric(db, zone_id, data)


@router.get("/{zone_id}/metrics", response_model=list[GreenZoneMetricRead])
def list_metrics(zone_id: int, db: Session = Depends(get_db)):
    zone = crud.get_zone(db, zone_id)
    if not zone:
        raise HTTPException(status_code=404, detail="Green zone not found")
    return crud.list_metrics_by_zone(db, zone_id)


@router.put("/{zone_id}/metrics/{metric_id}", response_model=GreenZoneMetricRead)
def update_metric(
    zone_id: int,
    metric_id: int,
    data: GreenZoneMetricUpdate,
    db: Session = Depends(get_db)
):
    zone = crud.get_zone(db, zone_id)
    if not zone:
        raise HTTPException(status_code=404, detail="Green zone not found")
    metric = crud.update_metric(db, metric_id, data)
    if not metric:
        raise HTTPException(status_code=404, detail="Metric not found")
    return metric


@router.delete("/{zone_id}/metrics/{metric_id}", status_code=204)
def delete_metric(zone_id: int, metric_id: int, db: Session = Depends(get_db)):
    zone = crud.get_zone(db, zone_id)
    if not zone:
        raise HTTPException(status_code=404, detail="Green zone not found")
    if not crud.delete_metric(db, metric_id):
        raise HTTPException(status_code=404, detail="Metric not found")
    return None
