from sqlalchemy.orm import Session
from app.models.traffic_data import TrafficData
from app.schemas.traffic import TrafficDataCreate
from app.utils.paginator import paginate

def create_traffic_data(
        db:Session,
        payload:TrafficDataCreate
):
    
    new_traffic_data = TrafficData(
        timestamp = payload.timestamp,
        route_id = payload.route_id,
        vehicle_count = payload.vehicle_count,
        average_speed  = payload.average_speed,
        congestion_level = payload.congestion_level,
        weather = payload.weather
    )

    db.add(new_traffic_data)
    db.commit()
    db.refresh(new_traffic_data)

    return {
        "message":"New traffic data Added",
        "data": new_traffic_data
    }

def get_traffic_data(
        db:Session,
        page:int=1,
        page_size:int=20
):

    query = db.query(TrafficData)

    result =  paginate(query=query,page=page,page_size=page_size)

    return {
        "message":"Traffic list fetched",
        "data": result
    }

def get_traffic_data_by_id(
        db:Session,
        traffic_id:int
):

    traffic_data = db.query(TrafficData).filter(
        TrafficData.id == traffic_id
    ).first()

    if not traffic_data:
        return {
            "message": "Traffic data not found",
            "data": None
    }

    return {
        "message":"Traffic data fetched by id",
        "data": traffic_data
    }

def update_traffic_data(
    db: Session,
    traffic_id: int,
    payload: TrafficDataCreate
):
    traffic_data = (
        db.query(TrafficData)
        .filter(TrafficData.id == traffic_id)
        .first()
    )

    if not traffic_data:
        return {
            "message": "Traffic data not found",
            "data": None
        }

    traffic_data.timestamp = payload.timestamp # type: ignore
    traffic_data.route_id = payload.route_id# type: ignore
    traffic_data.vehicle_count = payload.vehicle_count# type: ignore
    traffic_data.average_speed = payload.average_speed# type: ignore
    traffic_data.congestion_level = payload.congestion_level# type: ignore
    traffic_data.weather = payload.weather# type: ignore

    db.commit()
    db.refresh(traffic_data)

    return {
        "message": "Traffic data updated successfully",
        "data": traffic_data
    }

def delete_traffic_data(
    db: Session,
    traffic_id: int
):
    traffic_data = (
        db.query(TrafficData)
        .filter(TrafficData.id == traffic_id)
        .first()
    )

    if not traffic_data:
        return {
            "message": "Traffic data not found",
            "data": None
        }

    db.delete(traffic_data)
    db.commit()

    return {
        "message": "Traffic data deleted successfully"
    }