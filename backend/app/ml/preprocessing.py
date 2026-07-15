import pandas as pd 

REQUIRED_COLUMNS = [
    "timestamp",
    "route_id",
    "vehicle_count",
    "average_speed",
    "congestion_level",
    "weather"
]

def load_dataset(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)

def validate_columns(df: pd.DataFrame):

    missing = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )
    
def handle_missing_values(
    df: pd.DataFrame
) -> pd.DataFrame:

    df = df.copy()

    df["weather"] = df["weather"].fillna("Unknown")

    df = df.dropna(
        subset=[
            "timestamp",
            "route_id",
            "vehicle_count",
            "average_speed",
            "congestion_level"
        ]
    )

    return df    

def remove_duplicates(
    df: pd.DataFrame
) -> pd.DataFrame:

    return df.drop_duplicates()

def convert_timestamp(
    df: pd.DataFrame
) -> pd.DataFrame:

    df = df.copy()

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    return df

def sort_dataset(
    df: pd.DataFrame
) -> pd.DataFrame:

    return df.sort_values(
        by="timestamp"
    ).reset_index(drop=True)

def feature_engineering(
    df: pd.DataFrame
) -> pd.DataFrame:

    df = df.copy()

    df["hour"] = df["timestamp"].dt.hour

    df["day"] = df["timestamp"].dt.day

    df["weekday"] = df["timestamp"].dt.weekday

    df["month"] = df["timestamp"].dt.month

    df["year"] = df["timestamp"].dt.year

    df["is_weekend"] = (
        df["weekday"] >= 5
    ).astype(int)

    return df

def preprocess_dataset(
    df: pd.DataFrame
) -> pd.DataFrame:

    validate_columns(df)

    df = handle_missing_values(df)

    df = remove_duplicates(df)

    df = convert_timestamp(df)

    df = sort_dataset(df)

    df = feature_engineering(df)

    return df
