from sqlalchemy import Column, Integer, String, Float, DateTime
from app.db.database import Base
from datetime import datetime

class Scenario(Base):

    __tablename__ = "scenario_simulations"

    id = Column(Integer, primary_key=True, index=True)	

    scenario_type = Column(String(30), nullable=False)
    
    affected_route = Column(String(30), nullable=False) 

    estimated_congestion = Column(Float, nullable=False) 	

    estimated_delay = Column(Float, nullable=False) 

    estimated_travel_time = Column(Float, nullable=False) 	

    created_at = Column(DateTime, default= datetime.utcnow())
