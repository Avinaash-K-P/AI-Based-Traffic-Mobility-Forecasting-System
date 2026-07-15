from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from app.db.database import Base

class TrafficAnomaly(Base):

    __tablename__ = "traffic_anomalies"

    id = Column(Integer, primary_key=True, index=True)

    route_id = Column(String(20),nullable=False)

    anomaly_type = Column(String(20), nullable=False)

    severity = Column(String(20), nullable=False)

    message = Column(String(255), nullable=False)

    vehicle_count = Column(Integer, nullable=False)

    timestamp = Column(DateTime, nullable=False)

    created_at = Column(DateTime, default= datetime.utcnow())