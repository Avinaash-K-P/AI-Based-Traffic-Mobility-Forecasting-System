import pandas as pd
from prophet import Prophet

def prepare_prophet_dataset(
    df: pd.DataFrame
):
    prophet_df = df[
        [
            "timestamp",
            "vehicle_count"
        ]
    ].copy()

    prophet_df.rename(
        columns={
            "timestamp": "ds",
            "vehicle_count": "y"
        },
        inplace=True
    )

    return prophet_df


def train_prophet_model(train_df:pd.DataFrame):

    model = Prophet(
        yearly_seasonality=True, # type: ignore
        weekly_seasonality=True, # type: ignore
        daily_seasonality=True # type: ignore
    )

    model.fit(train_df)

    return model

def future_dataframe(
        model,
        period:int,
        freq:str='h'
):
    future = model.make_future_dataframe(
        period=period,
        freq=freq
    )

    return future

def predict_prophet(
    model,
    future_df
):
    forecast = model.predict(future_df)

    return forecast


def forecast_next_24_hours(model):
    
    future = model.make_future_dataframe(
        periods=24,
        freq='h'
    )

    forecast = predict_prophet(model=model, future_df=future)

    return forecast.tail(24)

def forecast_next_7_days(model):
    
    future = model.make_future_dataframe(
        periods=7,
        freq='d'
    )

    forecast = predict_prophet(model=model, future_df=future)

    return forecast.tail(24)
