import pandas as pd
from datetime import timedelta

def calculate_peak_hours(df: pd.DataFrame):
    
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df["hour"] = df["timestamp"].dt.hour

    peak_hours = (
    df.groupby("hour")["vehicle_count"]
      .mean()
      .reset_index()
)
    
    peak_hours.rename(
    columns={
        "vehicle_count": "average_vehicle_count"
    },
    inplace=True
)
    
    peak_hours = peak_hours.sort_values(
    by="average_vehicle_count",
    ascending=False
)
    
    return peak_hours

def detect_high_congestion(df:pd.DataFrame):
    
    HIGH_TRAFFIC_THRESHOLD = 500
    LOW_SPEED_THRESHOLD = 25
    HIGH_CONGESTION_THRESHOLD = 70
    
    high_congestion = df[
    (
        df["vehicle_count"] > HIGH_TRAFFIC_THRESHOLD
    )
    &
    (
        df["average_speed"] < LOW_SPEED_THRESHOLD
    )
    &
    (
        df["congestion_level"] > HIGH_CONGESTION_THRESHOLD
    )
].copy()

    high_congestion["severity"] = "High"
    high_congestion["alert_type"] = "High Congestion"
    high_congestion["end_time"] = (high_congestion["timestamp"] + timedelta(hours=2))

    high_congestion["message"] = (
    "High congestion expected on Route "
    + high_congestion["route_id"]
    + " between "
    + high_congestion["timestamp"].dt.strftime("%I:%M %p")
    + " and "
    + high_congestion["end_time"].dt.strftime("%I:%M %p")
)

    return high_congestion

def detect_traffic_spikes(df: pd.DataFrame):

    df = df.sort_values(
    by=["route_id", "timestamp"]
).copy()
    
    df["previous_vehicle_count"] = (
    df.groupby("route_id")["vehicle_count"]
      .shift(1)
)
    df["increase_percent"] = (
    (
        df["vehicle_count"] -
        df["previous_vehicle_count"]
    )
    /
    df["previous_vehicle_count"]
) * 100
    
    df["increase_percent"] = (
    df["increase_percent"]
      .fillna(0)
)
    SPIKE_THRESHOLD = 35

    traffic_spikes = df[
    df["increase_percent"] >= SPIKE_THRESHOLD
].copy()
    
    traffic_spikes["alert_type"] = "Traffic Spike"

    traffic_spikes["severity"] = "Medium"

    traffic_spikes["message"] = (
    "Traffic volume expected to increase by "
    + traffic_spikes["increase_percent"].round(0).astype(int).astype(str)
    + "% on Route "
    + traffic_spikes["route_id"]
    + " during the next hour."
)

    return traffic_spikes

def detect_accident_prone_routes(df:pd.DataFrame):
    
    accident_risk = df[
    (
        df["vehicle_count"] > 600
    )
    &
    (
        df["average_speed"] < 20
    )
    &
    (
        df["congestion_level"] > 80
    )
].copy()
    
    accident_risk["alert_type"] = "Accident Risk"

    accident_risk["severity"] = "High"

    accident_risk["message"] = (
    "High accident risk expected on Route "
    + accident_risk["route_id"]
    + " due to heavy congestion and low average speed."
    )

    return accident_risk

def generate_alerts(df:pd.DataFrame):

    high_congestion = detect_high_congestion(df)

    traffic_spikes = detect_traffic_spikes(df)

    accident_risk = detect_accident_prone_routes(df)

    alerts=[]

    for _, row in high_congestion.iterrows():
        
        alerts.append ({

        "route_id": row["route_id"],
        "alert_type": row["alert_type"],
        "severity": row["severity"],
        "message": row["message"],
        "prediction_time": row["timestamp"],
        "estimated_vehicle_count": row["vehicle_count"],
        "estimated_congestion": row["congestion_level"]
        
        })

    for _, row in traffic_spikes.iterrows():
        
        alerts.append ({

        "route_id": row["route_id"],
        "alert_type": row["alert_type"],
        "severity": row["severity"],
        "message": row["message"],
        "prediction_time": row["timestamp"],
        "estimated_vehicle_count": row["vehicle_count"],
        "estimated_congestion": row["congestion_level"]
        
        })   

    for _, row in accident_risk.iterrows():
        
        alerts.append ({

        "route_id": row["route_id"],
        "alert_type": row["alert_type"],
        "severity": row["severity"],
        "message": row["message"],
        "prediction_time": row["timestamp"],
        "estimated_vehicle_count": row["vehicle_count"],
        "estimated_congestion": row["congestion_level"]
        
        })    

    return alerts    
