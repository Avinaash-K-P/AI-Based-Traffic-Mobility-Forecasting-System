from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite database path
DATABASE_URL = "sqlite:///traffic_forecast.db"

# Create engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for models
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Model for database

from app.models.user import User
from app.models.traffic_data import TrafficData
from app.models.forecast_result import ForecastResult
from app.models.congestion_alert import CongestionAlert
from app.models.mobility_recommendation import MobilityRecommendation
from app.models.traffic_anomaly import TrafficAnomaly
from app.models.scenario_simullation import Scenario

Base.metadata.create_all(bind=engine)
