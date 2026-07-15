from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.core.security import get_current_user
from app.services.mobility_service import (
    generate_mobility_recommendations,
    get_mobility_recommendations,
    get_best_travel_times,
    get_alternatice_routes,
    get_congestion_reduction,
    get_route_load_balancing
    )

router = APIRouter(prefix="/mobility",tags=["Mobility Optimization"])

@router.post("/recommendation")
def add_recommendations(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    return generate_mobility_recommendations(db=db)

@router.get("/recommendation")
def view_recommendations(
    page:int=1,
    page_size:int=20,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    return get_mobility_recommendations(
        db=db,
        page=page,
        page_size=page_size
    )
    
@router.get("/best-travel-time")
def view_best_travel_time(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    return get_best_travel_times(db=db)
    
@router.get("/alternative-route")
def view_alternative_route(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    return get_alternatice_routes(db=db)


@router.get("/congestion-reduction")
def view_congestion_reduction(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    return get_congestion_reduction(db=db)

@router.get("/load-balancing")
def view_load_balancing(
    db:Session= Depends(get_db),
    user = Depends(get_current_user)  
):
    return get_route_load_balancing(db=db)

