from datetime import datetime

from pydantic import BaseModel, ConfigDict


class MobilityRecommendationBase(BaseModel):

    route_id: str

    recommendation_type: str

    recommendation: str

    expected_improvement: float


class MobilityRecommendationResponse(MobilityRecommendationBase):

    id: int

    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )