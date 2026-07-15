import os
import shutil
import pandas as pd
from fastapi import HTTPException, UploadFile, status
from sqlalchemy.orm import Session
from app.models.traffic_data import TrafficData
from app.services.forecast_service import (
    train_prophet,
    train_random_forest,
)

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_uploaded_file(file: UploadFile) -> str:

    if not file.filename.endswith(".csv"): #type:ignore
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only CSV files are allowed."
        )

    file_path = os.path.join(UPLOAD_DIR, file.filename) # type: ignore

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path


def validate_dataset_columns(df: pd.DataFrame):

    required_columns = {
        "timestamp",
        "route_id",
        "vehicle_count",
        "average_speed",
        "congestion_level",
        "weather"
    }

    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Missing columns: {', '.join(missing_columns)}"
        )


def upload_dataset(
    db: Session,
    file: UploadFile
):
    

    file_path = save_uploaded_file(file)

    df = pd.read_csv(file_path)

    validate_dataset_columns(df)

    df["timestamp"] = pd.to_datetime(df["timestamp"], format="%d-%m-%Y %H:%M")

    records = []

    for _, row in df.iterrows():

        traffic = TrafficData(
            timestamp=row["timestamp"],
            route_id=row["route_id"],
            vehicle_count=row["vehicle_count"],
            average_speed=row["average_speed"],
            congestion_level=row["congestion_level"],
            weather=row["weather"]
        )

        records.append(traffic)

    db.bulk_save_objects(records)
    db.commit()

    return {
        "message": "Dataset uploaded successfully.",
        "records_inserted": len(records)
    }
