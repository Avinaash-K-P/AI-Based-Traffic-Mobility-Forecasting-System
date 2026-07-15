from sqlalchemy.orm import Session
from app.models.traffic_data import TrafficData
from app.models.scenario_simullation import Scenario
from app.utils.paginator import paginate
from app.ml.scenario_simulation import (
    generate_simulation,
    simulate_event_traffic,
    simulate_rain_impact,
    simulate_road_closure,
    simulate_vehicle_load
)
import pandas as pd

def create_simulation(db:Session):

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

    if not traffic_data:
        return {
        "message": "No traffic data available."
    }

    simulations = generate_simulation(df)

    saved_simulations = []

    db.query(Scenario).delete()

    for simulation in simulations:

        new_simulation = Scenario(
            scenario_type = simulation["scenario_type"],
            affected_route = simulation["affected_route"],
            estimated_congestion = simulation["estimated_congestion"],
            estimated_delay = simulation["estimated_delay"],
            estimated_travel_time = simulation["estimated_travel_time"]
        )  

        db.add(new_simulation)
        saved_simulations.append(new_simulation)

    db.commit()

    for simulation in saved_simulations:
        db.refresh(simulation)

    return {
        "message": "Scenario simulation generated successfully!",
        "simulation": saved_simulations
    }        

def get_scenario_history(
        db:Session,
        page:int=1,
        page_size:int =20
):
    query = db.query(Scenario).order_by(
        Scenario.created_at.desc()
    )

    return paginate(
        query=query,
        page=page,
        page_size=page_size
    )

def get_road_closure(db:Session):

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

    simulation =[]

    road_closure = simulate_road_closure(df)

    simulation.append(road_closure)

    return {
        "message": "Road closure simulation generated successfully!",
        "simulation": simulation
    }       

def get_rain_impact(db:Session):

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

    simulation =[]

    rain_impact = simulate_rain_impact(df)

    simulation.append(rain_impact)

    return {
        "message": "Rain impact simulation generated successfully!",
        "simulation": simulation
    }       

def get_event_traffic(db:Session):

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

    simulation =[]    

    event_traffic = simulate_event_traffic(df)

    simulation.append(event_traffic)

    return {
        "message": "Event traffic simulation generated successfully!",
        "simulation": simulation
    }       

def get_vehicle_load(db:Session):

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

    simulation =[]

    vehicel_load = simulate_vehicle_load(df)

    simulation.append(vehicel_load)

    return {
        "message": "Vehicle load simulation generated successfully!",
        "simulation": simulation
    }       

