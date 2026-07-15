from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from app.db.database import Base


class TrafficData(Base):
    
    __tablename__ = "traffic_data"

    id = Column(Integer, primary_key=True, index=True)

    timestamp = Column(DateTime, nullable=False, index=True)

    route_id = Column(String(100), nullable=False, index=True)

    vehicle_count = Column(Integer, nullable=False)

    average_speed = Column(Float, nullable=False)

    congestion_level = Column(Float, nullable=False)

    weather = Column(String(100), nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)