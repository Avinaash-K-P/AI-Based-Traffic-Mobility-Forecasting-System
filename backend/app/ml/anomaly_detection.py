from app.ml.congestion_prediction import detect_traffic_spikes
import pandas as pd
from sklearn.ensemble import IsolationForest
from scipy.stats import zscore

def detect_low_traffic(df: pd.DataFrame):
    
    low_traffic = df[
    (df["vehicle_count"] < 100)
    &
    (df["congestion_level"] < 20)
    ].copy()

    if low_traffic.empty:
        return []   
    
    anomalies = []

    for _, row in low_traffic.iterrows():

        anomalies.append(
        {
            "route_id": row["route_id"],

            "anomaly_type": "Low Traffic",

            "severity": "Medium",

            "message":
            f"Unexpected low traffic detected on Route {row['route_id']}.",

            "vehicle_count": int(row["vehicle_count"]),

            "timestamp": row["timestamp"]
        }
    )

    return anomalies

def detect_sensor_anomalies(df: pd.DataFrame):
    
    sensor_anomalies = df[
    (df["vehicle_count"] < 0)
    |
    (df["vehicle_count"] > 2000)
    |
    (df["average_speed"] < 0)
    |
    (df["congestion_level"] > 100)
    ].copy()

    if sensor_anomalies.empty:
        return []
    
    anomalies = []

    for _, row in sensor_anomalies.iterrows():

        anomalies.append(
        {
            "route_id": row["route_id"],

            "anomaly_type": "Sensor Anomaly",

            "severity": "High",

            "message":
            f"Possible sensor anomaly detected on Route {row['route_id']}.",

            "vehicle_count": int(row["vehicle_count"]),

            "timestamp": row["timestamp"]
        }
    )

    return anomalies

def detect_event_surges(df:pd.DataFrame):
    event_surges = df[
    (df["vehicle_count"] > 700)
    &
    (df["congestion_level"] > 85)
    ].copy()    

    if event_surges.empty:
        return []
    
    anomalies = []

    for _, row in event_surges.iterrows():

        anomalies.append(
        {
            "route_id": row["route_id"],

            "anomaly_type": "Event Surge",

            "severity": "High",

            "message":
            f"Possible event-based traffic surge detected on Route {row['route_id']}.",

            "vehicle_count": int(row["vehicle_count"]),

            "timestamp": row["timestamp"]
        }
    )

    return anomalies

def detect_isolation_forest_anomalies(df:pd.DataFrame):
    features = df[
    [
        "vehicle_count",
        "average_speed",
        "congestion_level"
    ]
    ]
    
    model = IsolationForest(
    contamination=0.05,
    random_state=42
    )

    df["anomaly"] = model.fit_predict(features)

    anomaly_df = df[df["anomaly"] == -1].copy()

    if anomaly_df.empty:
        return []
       
    anomalies = []

    for _, row in anomaly_df.iterrows():

       anomalies.append(
           {
               "route_id": row["route_id"],

               "anomaly_type": "Isolation Forest",

               "severity": "High",

               "message":
               f"Isolation Forest detected an unusual traffic pattern on Route {row['route_id']}.",

               "vehicle_count": int(row["vehicle_count"]),

               "timestamp": row["timestamp"]
           }
       )

    return anomalies    

def detect_z_score_anomalies(df:pd.DataFrame):

    df["z_score"] = zscore(df["vehicle_count"]) # type: ignore

    df["z_score"] = df["z_score"].fillna(0)

    z_score_df = df[df["z_score"].abs() > 3].copy()

    if z_score_df.empty:
        return []
    
    anomalies = []

    for _, row in z_score_df.iterrows():

        anomalies.append(
        {
            "route_id": row["route_id"],

            "anomaly_type": "Z-Score",

            "severity": "High",

            "message":
            f"Statistical anomaly detected on Route {row['route_id']} "
            f"(Z-score = {row['z_score']:.2f}).",

            "vehicle_count": int(row["vehicle_count"]),

            "timestamp": row["timestamp"]
        }
    )

    return anomalies

def generate_anomalies(df:pd.DataFrame):

    traffic_spikes_df = detect_traffic_spikes(df)

    traffic_spikes = []

    for _, row in traffic_spikes_df.iterrows():

        traffic_spikes.append(
        {
            "route_id": row["route_id"],
            "anomaly_type": "Traffic Spike",
            "severity": row["severity"],
            "message": row["message"],
            "vehicle_count": int(row["vehicle_count"]),
            "timestamp": row["timestamp"]
        }
    )

    low_traffic = detect_low_traffic(df)

    sensor_anomalies = detect_sensor_anomalies(df)

    event_surges = detect_event_surges(df)

    isolation_forest = detect_isolation_forest_anomalies(df)

    anomalies = []

    anomalies.extend(traffic_spikes)

    anomalies.extend(low_traffic)

    anomalies.extend(sensor_anomalies)

    anomalies.extend(event_surges)

    anomalies.extend(isolation_forest)

    return anomalies