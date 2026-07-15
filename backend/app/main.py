from fastapi import FastAPI
from app.routes import (
    auth,
    profile,
    traffic, 
    upload, 
    forecast, 
    congestion, 
    mobility,
    anomalies,
    scenario
)
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Traffic and Mobility Forecasting",
    description="""
    Features added:
     - Secure user authentication and authorization using JWT.
     - Traffic dataset upload with preprocessing support.
     - 24-hour and 7-day traffic forecasting using Machine Learning models.
     - Congestion prediction and high-risk route analysis.
     - Mobility analytics with optimal travel time recommendations.
     - Traffic anomaly detection using statistical and AI-based techniques.
     - Scenario simulation for road closures, weather impacts, and traffic events.
     - Standard API's for seamless frontend dashboard integration.
     - Interactive analytics for traffic monitoring and decision support.

    """,
    version= "1.0.0"
    )

#CORS Confurigation
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)    

app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(traffic.router)
app.include_router(upload.router)
app.include_router(forecast.router)
app.include_router(congestion.router)
app.include_router(mobility.router)
app.include_router(anomalies.router)
app.include_router(scenario.router)

@app.get("/")
def root():
    return {"message":"API connected successfully!"}