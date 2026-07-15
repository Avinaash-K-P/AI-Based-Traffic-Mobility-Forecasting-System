from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from app.db.database import Base


class ForecastResult(Base):
    __tablename__ = "forecast_results"

    id = Column(Integer, primary_key=True, index=True)

    route_id = Column(String(100), nullable=False, index=True)

    prediction_time = Column(DateTime, nullable=False)

    predicted_vehicle_count = Column(Float, nullable=False)

    predicted_congestion = Column(Float, nullable=False)

    model_name = Column(String(100), nullable=False)

    forecast_type = Column(String(50), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)