import numpy as np

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

def calculate_mae(
    y_true,
    y_pred
):

    return mean_absolute_error(
        y_true,
        y_pred
    )

def calculate_rmse(
    y_true,
    y_pred
):

    mse = mean_squared_error(
        y_true,
        y_pred
    )

    return np.sqrt(mse)

def calculate_r2(
    y_true,
    y_pred
):

    return r2_score(
        y_true,
        y_pred
    )

def calculate_mape(
    y_true,
    y_pred
):

    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    mask = y_true != 0

    mape = np.mean(
        np.abs(
            (y_true[mask] - y_pred[mask])
            / y_true[mask]
        )
    )

    return mape * 100


def evaluate_model(y_true, y_pred):
    return {
        "mae": round(calculate_mae(y_true, y_pred),2),
        "rmse": round(calculate_rmse(y_true, y_pred),2),
        "r2": round(calculate_r2(y_true, y_pred),2),
        "mape": round(calculate_mape(y_true, y_pred),2) 
    }