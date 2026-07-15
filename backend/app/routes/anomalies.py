from fastapi import APIRouter, Depends
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.services.anomaly_service import(
    generate_traffic_anomalies,
    get_traffic_anomalies, 
    get_traffic_spikes,
    get_low_traffic,
    get_sensor_anomalies,
    get_event_surges,
    get_z_score_anomalies,
    get_isolation_forest_anomalies
)


router = APIRouter(prefix="/anomaly", tags=["Traffic Anomalies"])

@router.post("/generate")
def add_anomalies(
    db:Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return generate_traffic_anomalies(db=db)

@router.get("/history")
def view_anomaly_history(
    page:int=1,
    page_size:int=20,
    db:Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return get_traffic_anomalies(
        db=db,
        page=page,
        page_size=page_size
    )

@router.get("/traffic-spikes")
def view_traffic_spikes(
    db:Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return get_traffic_spikes(db=db)

@router.get("/low-traffic")
def view_low_traffic(
    db:Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return get_low_traffic(db=db)

@router.get("/sensor")
def view_sensor(
    db:Session = Depends(get_db),
    user = Depends(get_current_user)            
):
    return get_sensor_anomalies(db=db)

@router.get("/event-surges")
def view_event_surges(
    db:Session = Depends(get_db),
    user = Depends(get_current_user)    
):
    return get_event_surges(db=db)

@router.get("/z-score")
def view_z_score(
    db:Session=Depends(get_db),
    user = Depends(get_current_user)    
):
    return get_z_score_anomalies(db=db)
    
@router.get("/isolation-forest")
def view_isolation_forest_anomalies(
    db:Session=Depends(get_db),
    user = Depends(get_current_user)    
):
    return get_isolation_forest_anomalies(db=db)

