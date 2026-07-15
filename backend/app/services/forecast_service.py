from sqlalchemy.orm import Session
from app.models.traffic_data import TrafficData
from app.models.forecast_result import ForecastResult
from app.ml.preprocessing import preprocess_dataset
from app.ml.train_test_split import split_dataset
from app.ml.prophet_model import (
    prepare_prophet_dataset, train_prophet_model, predict_prophet,
    forecast_next_24_hours, forecast_next_7_days
)
from app.ml.random_forest_model import (
    prepare_random_forest_dataset ,train_random_forest_model, predict_random_forest
)
from app.ml.evaluation import evaluate_model
from app.ml.model_manager import (
    save_model,load_model
)
import pandas as pd
from sklearn.model_selection import train_test_split
from app.utils.paginator import paginate

def train_prophet(db:Session):

    traffic_data = db.query(TrafficData).all()    

    if not traffic_data:
        
        return {
        "message": "No traffic data available for training."
        }

    df = pd.DataFrame([
    {
        "timestamp": row.timestamp,
        "route_id": row.route_id,
        "vehicle_count": row.vehicle_count,
        "average_speed": row.average_speed,
        "congestion_level": row.congestion_level,
        "weather": row.weather
    }

    for row in traffic_data
    ])

    preprocessed_df = preprocess_dataset(df) 

    prophet_df = prepare_prophet_dataset(preprocessed_df)

    train_df, test_df = split_dataset(prophet_df)

    model = train_prophet_model(train_df)

    forecast = predict_prophet(model, test_df)

    y_pred = forecast["yhat"]

    metrics = evaluate_model(test_df["y"], y_pred)

    save_model(model,"PROPHET_MODEL")

    return {
    "message": "Prophet model trained successfully.",
    "model_name": "Prophet",
    "evaluation": metrics
    }

def train_random_forest(db:Session):

    traffic_data = db.query(TrafficData).all()    
    
    if not traffic_data:
        
        return {
        "message": "No traffic data available for training."
        }
    
    df = pd.DataFrame([
        {
        "timestamp": row.timestamp,
        "route_id": row.route_id,
        "vehicle_count": row.vehicle_count,
        "average_speed": row.average_speed,
        "congestion_level": row.congestion_level,
        "weather": row.weather
        }
        for row in traffic_data
    ])

    preprocessed_df = preprocess_dataset(df) 

    X,y = prepare_random_forest_dataset(preprocessed_df)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False, random_state=42)

    model = train_random_forest_model(X_train, y_train)

    y_pred = predict_random_forest(model, X_test)

    metrics = evaluate_model(y_test, y_pred)

    save_model(model,"RANDOM_FOREST_MODEL")

    return {
    "message": "Random Forest model trained successfully.",
    "model_name": "Random Forest",
    "evaluation": metrics
    }

def get_forecast_next_24_hours(db:Session):
    
    model = load_model("PROPHET_MODEL")

    forecast = forecast_next_24_hours(model)

    # Delete old 7-day forecasts
    db.query(ForecastResult).filter(
        ForecastResult.forecast_type == "24_hours"
    ).delete()



    # Save new forecasts
    for _, row in forecast.iterrows():

        forecast_result = ForecastResult(
            route_id="ALL_ROUTES",
            prediction_time=row["ds"],
            predicted_vehicle_count=int(row["yhat"]),
            predicted_congestion=0.0,
            model_name="Prophet",
            forecast_type="24_hours"
        )

        db.add(forecast_result)

    db.commit()

    saved_forecasts = (
    db.query(ForecastResult)
    .filter(ForecastResult.forecast_type == "24_hours")
    .order_by(ForecastResult.prediction_time)
    .all()
)

    return {
        "message": "24-hour forecast generated successfully.",
        "forecast": saved_forecasts
    }

def get_forecast_next_7_days(db:Session):
    
    model = load_model("PROPHET_MODEL")

    forecast = forecast_next_7_days(model)

    # Delete old 7-day forecasts
    db.query(ForecastResult).filter(
        ForecastResult.forecast_type == "7_days"
    ).delete()

    for _, row in forecast.iterrows():

        forecast_result = ForecastResult(
            route_id="ALL_ROUTES",
            prediction_time=row["ds"],
            predicted_vehicle_count=int(row["yhat"]),
            predicted_congestion=0.0,
            model_name="Prophet",
            forecast_type="7_days"
        )

        db.add(forecast_result)

    db.commit()

    saved_forecasts = (
    db.query(ForecastResult)
    .filter(ForecastResult.forecast_type == "7_days")
    .order_by(ForecastResult.prediction_time)
    .all()
)

    return {
        "message": "7-Days forecast generated successfully.",
        "forecast": saved_forecasts
    }


def forecast_history(
    db: Session,
    page: int = 1,
    page_size: int = 20
):

    query = db.query(ForecastResult).order_by(
        ForecastResult.prediction_time.desc()
    )

    return paginate(
        query=query,
        page=page,
        page_size=page_size
    )