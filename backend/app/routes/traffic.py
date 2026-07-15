from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.traffic import TrafficDataCreate, TrafficDataResponse
from app.core.security import get_current_user
from app.services.traffic_service import (
    create_traffic_data,
    get_traffic_data,
    get_traffic_data_by_id,
    update_traffic_data,
    delete_traffic_data
)

router = APIRouter(prefix="/traffic", tags=["Traffic Data"])

@router.post("/")
def add_traffic_data(
    payload: TrafficDataCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    
    return create_traffic_data(
        db=db,
        payload=payload
    ) 

@router.get("/list")
def list_traffic_data(
    page:int=1,
    page_size:int=20,
    db:Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    
    return get_traffic_data(db=db, page=page, page_size=page_size)

@router.get("/{traffic_id}")
def view_traffic_data(
    traffic_id:int,
    db:Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    return get_traffic_data_by_id(
        db=db, 
        traffic_id=traffic_id
    )

@router.put("/{traffic_id}")
def edit_traffic_data(
    payload: TrafficDataCreate,
    traffic_id:int,
    db:Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    return update_traffic_data(
        db=db, 
        traffic_id=traffic_id,
        payload=payload
    )


@router.delete("/{traffic_id}")
def remove_traffic_data(
    traffic_id:int,
    db:Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    return delete_traffic_data(
        db=db, 
        traffic_id=traffic_id
    )
