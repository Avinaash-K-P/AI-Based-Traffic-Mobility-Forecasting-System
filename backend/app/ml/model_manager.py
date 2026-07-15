from pathlib import Path

import joblib

MODEL_DIR = "trained_models"

BASE_DIR = Path(__file__).resolve().parent.parent.parent

MODEL_DIR = BASE_DIR / "trained_models"

MODEL_DIR.mkdir(exist_ok=True)

def get_model_path(
    model_name: str
):
    return MODEL_DIR / f"{model_name}.pkl" # type: ignore

def save_model(
    model,
    model_name: str
):

    model_path = get_model_path(model_name)

    joblib.dump(
        model,
        model_path
    )

    return model_path

def load_model(
    model_name: str
):

    model_path = get_model_path(model_name)

    return joblib.load(model_path)

def model_exists(
    model_name: str
):

    model_path = get_model_path(model_name)

    return model_path.exists()

def delete_model(
    model_name: str
):

    model_path = get_model_path(model_name)

    if model_path.exists():
        model_path.unlink()

        return True

    return False
