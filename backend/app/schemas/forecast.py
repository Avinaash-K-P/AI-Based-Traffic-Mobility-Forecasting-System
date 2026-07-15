from datetime import datetime

from pydantic import BaseModel, ConfigDict

class ForecastResultBase(BaseModel):
    route_id:str
    prediction_time:datetime
    predicted_vehicle_count:int
    predicted_congestion:float
    model_name:str
    forecast_type :str

class ForecastResultResponse(ForecastResultBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TrainModelResponse(ForecastResultBase):
    message: str
    model_name: str
    evaluation: ModelEvaluationResponse

class Forecast24HoursResponse(ForecastResultBase):
    pass

class Forecast7DaysResponse(ForecastResultBase):
    pass

class ModelEvaluationResponse(ForecastResultBase):
    MAE: float
    RMSE: float
    R2: float
    MAPE: float