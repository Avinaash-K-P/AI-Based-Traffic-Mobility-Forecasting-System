from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.core.security import get_current_user
from app.services.forecast_service import (
    train_prophet,
    train_random_forest,
    get_forecast_next_24_hours,
    get_forecast_next_7_days,
    forecast_history
)


router = APIRouter(prefix="/forecast", tags=["Forecast"])

@router.post("/train/prophet")
def train_prophet_model(
    db:Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    return train_prophet(db=db)

@router.post("/train/random-forest")
def train_random_forest_model(
    db:Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    return train_random_forest(db=db)

@router.get("/24-hours")
def forecast_24_hours(
    db:Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    return get_forecast_next_24_hours(db=db)

@router.get("/7-days")
def forecast_7_days(
    db:Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    return get_forecast_next_7_days(db=db)

@router.get("/history")
def get_forecast_history(
    page: int = 1,
    page_size: int = 20,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    return forecast_history(
        db=db,
        page=page,
        page_size=page_size
    )