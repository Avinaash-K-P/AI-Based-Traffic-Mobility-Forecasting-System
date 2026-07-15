from sqlalchemy.orm import Session
from app.models.traffic_data import TrafficData
from app.models.traffic_anomaly import TrafficAnomaly
import pandas as pd
from app.ml.anomaly_detection import (
    detect_event_surges,
    detect_isolation_forest_anomalies,
    detect_low_traffic,
    detect_sensor_anomalies,
    detect_z_score_anomalies,
    generate_anomalies
)
from app.utils.paginator import paginate

def generate_traffic_anomalies(db:Session):
    
    traffic_data = db.query(TrafficData).all()
    
    if not traffic_data:
        return {
        "message": "No traffic data available."
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
    anomalies = generate_anomalies(df)

    if not anomalies:
        return {
        "message": "No anomalies detected."
    }

    db.query(TrafficAnomaly).delete()

    saved_anomalies=[]

    for anomaly in anomalies:

        new_anomaly = TrafficAnomaly(
        route_id=anomaly["route_id"],
        anomaly_type=anomaly["anomaly_type"],
        severity=anomaly["severity"],
        message=anomaly["message"],
        vehicle_count=anomaly["vehicle_count"],
        timestamp=anomaly["timestamp"]
    )

        db.add(new_anomaly)

        saved_anomalies.append(new_anomaly)

    db.commit()

    for anomaly in saved_anomalies:
        db.refresh(anomaly)

    return {
        "message": "Traffic anomalies generated successfully.",
        "anomalies": saved_anomalies
    }    

def get_traffic_anomalies(
    db:Session,
    page:int=1,
    page_size:int =20
):

    query = (
    db.query(TrafficAnomaly)
      .order_by(TrafficAnomaly.created_at.desc())
    )

    return paginate(
        query=query,
        page=page,
        page_size=page_size
    )
    
def get_traffic_spikes(db: Session):

    traffic_spikes = (
        db.query(TrafficAnomaly)
        .filter(
            TrafficAnomaly.anomaly_type == "Traffic Spike"
        )
        .all()
    )

    return {
        "message": "Traffic spikes fetched successfully.",
        "anomalies": traffic_spikes
    }

def get_low_traffic(db:Session):

    traffic_data = db.query(TrafficData).all()
    
    if not traffic_data:
        return {
        "message": "No traffic data available."
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

    low_traffic = detect_low_traffic(df)

    return {
        "message": "Low traffic anomalies detected successfully.",
        "anomalies": low_traffic
    }

def get_sensor_anomalies(db:Session):
    
    traffic_data = db.query(TrafficData).all()
    
    if not traffic_data:
        return {
        "message": "No traffic data available."
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

    sensor_anomalies = detect_sensor_anomalies(df)

    return {
        "message": "Sensor anomalies detected successfully.",
        "anomalies": sensor_anomalies
    }

def get_event_surges(db:Session):

    traffic_data = db.query(TrafficData).all()
    
    if not traffic_data:
        return {
        "message": "No traffic data available."
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

    event_surges = detect_event_surges(df)

    return {
        "message": "Event-based traffic surges detected successfully.",
        "anomalies": event_surges
    }

def get_z_score_anomalies(db:Session):

    traffic_data = db.query(TrafficData).all()
    
    if not traffic_data:
        return {
        "message": "No traffic data available."
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

    z_score = detect_z_score_anomalies(df)

    return{
        "message":"Z-Score detected successfully",
        "anomalies": z_score
    }



def get_isolation_forest_anomalies(db:Session):

    traffic_data = db.query(TrafficData).all()
    
    if not traffic_data:
        return {
        "message": "No traffic data available."
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

    isolation_anomalies = detect_isolation_forest_anomalies(df)

    return {
        "message": "Isolation Forest anomalies detected successfully.",
        "anomalies": isolation_anomalies
    }
