from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime
)

from app.db.database import Base


class CongestionAlert(Base):

    __tablename__ = "congestion_alerts"

    id = Column(Integer,primary_key=True,index=True)

    route_id = Column(String, nullable=False)

    alert_type = Column(String,nullable=False)

    severity = Column(String, nullable=False)

    message = Column(String,nullable=False)

    prediction_time = Column(DateTime, nullable=False)

    estimated_vehicle_count = Column(Integer, nullable=False)

    estimated_congestion = Column(Float, nullable=False)

    created_at = Column(DateTime,default=datetime.utcnow)