from sqlalchemy.orm import Session
from app.models.traffic_data import TrafficData
from app.models.mobility_recommendation import MobilityRecommendation
import pandas as pd
from app.utils.paginator import paginate

from app.ml.mobility import (
    recommend_alternative_routes,
    recommend_best_travel_times,
    recommend_congestion_reduction,
    recommend_route_load_balancing,
    generate_recommendations
)

def generate_mobility_recommendations(db:Session):

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

    recommendations = generate_recommendations(df)

    saved_recommendations = []

    db.query(MobilityRecommendation).delete()

    for recommendation in recommendations:
        new_recommendation = MobilityRecommendation(
            route_id=recommendation["route_id"],
            recommendation_type=recommendation["recommendation_type"],
            recommendation=recommendation["recommendation"],
            expected_improvement=recommendation["expected_improvement"]
        )

        db.add(new_recommendation)
        saved_recommendations.append(new_recommendation)

    db.commit()    
    
    for recommendation in saved_recommendations:
        db.refresh(recommendation)

    return {
        "message": "Mobility recommendations generated successfully.",
        "recommendations": saved_recommendations
    }    

def  get_mobility_recommendations(
        db:Session,
        page:int = 1,
        page_size:int = 20
        ):

    query = (
    db.query(MobilityRecommendation)
      .order_by(MobilityRecommendation.created_at.desc())
)

    return paginate(
        query=query,
        page=page,
        page_size=page_size
    )

def get_best_travel_times(db:Session):

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
    
    best_travel_times = recommend_best_travel_times(df)

    return {
    "message": "Best travel time recommendations fetched successfully.",
    "recommendations": best_travel_times
    }

def get_alternatice_routes(db:Session):
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

    alternative_routes = recommend_alternative_routes(df)

    return {
    "message": "Alternative route recommendations fetched successfully.",
    "recommendations": alternative_routes
}

def get_route_load_balancing(db:Session):
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

    load_balancing = recommend_route_load_balancing(df)

    return {
        "message": "Route load balancing recommendations fetched successfully.",
        "recommendations": load_balancing
    }

def get_congestion_reduction(db:Session):

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

    congestion_reduction = recommend_congestion_reduction(df)

    return {
        "message": "Congestion reduction recommendations fetched successfully.",
        "recommendations": congestion_reduction
    }

