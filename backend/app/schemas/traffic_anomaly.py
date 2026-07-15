from datetime import datetime

from pydantic import BaseModel, ConfigDict

class TrafficAnomalyBase(BaseModel):

    route_id: str

    anomaly_type: str

    severity: str

    message: str

    vehicle_count: int

    timestamp: datetime

class TrafficAnomalyResponse(TrafficAnomalyBase):

    id: int

    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )    