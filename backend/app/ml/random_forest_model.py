import pandas as pd
from sklearn.ensemble import RandomForestRegressor

def prepare_random_forest_dataset(df: pd.DataFrame):

    feature_columns = [
        "hour",
        "day",
        "weekday",
        "month",
        "year",
        "is_weekend",
        "average_speed",
        "congestion_level"
    ]

    X = df[feature_columns]

    y = df["vehicle_count"]

    return X, y


def train_random_forest_model(X_train, y_train):

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    return model

def predict_random_forest(model, X):

    predictions = model.predict(X)

    return predictions
