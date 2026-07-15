from fastapi import APIRouter, Depends
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.services.congestion_service import (
    analyze_congestion,
    get_peak_hours,
    get_congestion_alerts,
    get_high_risk_routes,
    get_traffic_spikes
)


router = APIRouter(prefix="/congestion", tags=["Congestion Alerts"])

@router.post("/analyze")
def add_congestion_alerts(
    db:Session = Depends(get_db),
    user = Depends(get_current_user)    
):
    return analyze_congestion(db=db)

@router.get("/peak-hours")
def view_peak_hours(
    db:Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    return get_peak_hours(db=db)

@router.get("/alerts")
def view_alerts(
    page: int = 1,
    page_size: int = 20,
    db:Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    return get_congestion_alerts(
        db=db,
        page=page,
        page_size=0  
        )

@router.get("/high-risk-routes")
def view_high_risk_routes(
    db:Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    return get_high_risk_routes(db=db)

@router.get("/traffic-spikes")
def view_traffic_spikes(
    db:Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    return get_traffic_spikes(db=db)