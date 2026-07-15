from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CongestionAlertBase(BaseModel):

    route_id: str
    alert_type: str
    severity: str
    message: str
    prediction_time: datetime
    estimated_vehicle_count: int
    estimated_congestion: float


class CongestionAlertResponse(CongestionAlertBase):

    id: int
    created_at: datetime
    model_config = ConfigDict(
        from_attributes=True
    )