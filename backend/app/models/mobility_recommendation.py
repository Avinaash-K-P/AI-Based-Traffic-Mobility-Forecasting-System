from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from app.db.database import Base


class MobilityRecommendation(Base):

    __tablename__ = "mobility_recommendations"
    
    id=Column(Integer, primary_key=True, index=True)
    
    route_id=Column(String(20),nullable=False)
   
    recommendation_type=Column(String(100), nullable=False)	
  
    recommendation=Column(String(255), nullable=False)	
  
    expected_improvement=Column(Float, nullable=False)	
 
    created_at=Column(DateTime, default=datetime.utcnow())	
