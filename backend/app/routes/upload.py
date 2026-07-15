from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.upload_service import upload_dataset
from app.core.security import get_current_user

router = APIRouter(
    prefix="/upload",
    tags=["Dataset Upload"]
)


@router.post("/dataset")
def upload_traffic_dataset(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    return upload_dataset(
        db=db,
        file=file
    )