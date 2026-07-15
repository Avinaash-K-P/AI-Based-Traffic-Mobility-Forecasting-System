from sqlalchemy.orm import Session
from app.models.traffic_data import TrafficData
from app.models.congestion_alert import CongestionAlert
import pandas as pd
from app.ml.congestion_prediction import (
    generate_alerts, 
    calculate_peak_hours, 
    detect_accident_prone_routes,
    detect_traffic_spikes
)
from app.utils.paginator import paginate

def analyze_congestion(
    db:Session,
):    
    traffic_data = db.query(TrafficData).all()

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

    alerts = generate_alerts(df)

    saved_alerts =[]

    for alert in alerts: 

        new_alerts = CongestionAlert(
        route_id = alert["route_id"],
        alert_type = alert["alert_type"],
        severity = alert["severity"],
        message = alert["message"],
        prediction_time = alert["prediction_time"],
        estimated_vehicle_count = alert["estimated_vehicle_count"],
        estimated_congestion = alert["estimated_congestion"]
    )

    db.add(new_alerts)
    saved_alerts.append(new_alerts)
    db.commit()
    for alert in saved_alerts:
        db.refresh(alert)

    return {
        "message": "Congestion analysis completed successfully.",
        "alerts": saved_alerts
    }

def get_peak_hours(db:Session):

    traffic_data = db.query(TrafficData).all()

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

    peak_hours = calculate_peak_hours(df)

    return {
        "message": "Congestion analysis completed successfully.",
        "peak_hours": peak_hours.to_dict(orient="records")
    }

def get_congestion_alerts(
    db:Session,
    page: int = 1,
    page_size: int = 20
):

    query = (
    db.query(CongestionAlert)
      .order_by(CongestionAlert.created_at.desc())
)

    return paginate(
        query=query,
        page=page,
        page_size=page_size
        )
    
def get_high_risk_routes(db:Session):

    traffic_data = db.query(TrafficData).all()

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

    high_risk_routes = detect_accident_prone_routes(df)

    return {
       "message": "High-risk routes fetched successfully.",
       "high_risk_routes": high_risk_routes.to_dict(orient="records")
    }
    
def get_traffic_spikes(db:Session):

    traffic_data = db.query(TrafficData).all()

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

    traffic_spikes = detect_traffic_spikes(df)

    return {
       "message": "High-risk routes fetched successfully.",
       "traffic_spikes": traffic_spikes.to_dict(orient="records")
    }