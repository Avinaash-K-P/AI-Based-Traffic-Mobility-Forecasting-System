from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.core.security import get_current_user
from app.services.simulation_service import (
    create_simulation,
    get_event_traffic,
    get_rain_impact,
    get_road_closure,
    get_scenario_history,
    get_vehicle_load
)

router = APIRouter(prefix="/scenario", tags=["Scenario Simulation"])

@router.post("/generate")
def add_simulation(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    return create_simulation(db=db)

@router.get("/road-closure")
def view_road_closure(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    return get_road_closure(db=db)

@router.get("/rain-impact")
def view_rain_impact(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    return get_rain_impact(db=db)

@router.get("/event-traffic")
def view_event_traffic(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    return get_event_traffic(db=db)

@router.get("/vehicle-load")
def view_vehicle_load(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    return get_vehicle_load(db=db)

@router.get("/history")
def view_history(
    page:int=1,
    page_size:int=20,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    return get_scenario_history(
        db=db,
        page=page,
        page_size=page_size
    )
