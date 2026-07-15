from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class TrafficDataBase(BaseModel):
    timestamp: datetime
    route_id: str
    vehicle_count: int
    average_speed: float
    congestion_level: float
    weather: Optional[str] = None


class TrafficDataCreate(TrafficDataBase):
    pass


class TrafficDataResponse(TrafficDataBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)