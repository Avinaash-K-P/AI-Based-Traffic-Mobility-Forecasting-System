# AI Traffic and Mobility Forecasting System

## Dataset Explanation

The project uses a traffic mobility dataset containing route-wise traffic observations collected at regular time intervals. Each record represents the traffic conditions for a specific route and includes information required for forecasting, congestion analysis, anomaly detection, and scenario simulation.

**Dataset Fields**

* Timestamp
* Route ID
* Vehicle Count
* Average Speed (km/h)
* Congestion Level (%)
* Weather Condition

The uploaded dataset is validated, preprocessed, and stored in the SQLite database before being used for machine learning and analytics.

---

## Forecasting Methodology

The forecasting module predicts future traffic conditions using Machine Learning models.

### Prophet Model

* Time-series forecasting for traffic volume.
* Generates 24-hour and 7-day traffic predictions.
* Captures daily and seasonal traffic patterns.

### Random Forest Regression

* Learns relationships between traffic features.
* Predicts vehicle count and traffic trends.
* Complements time-series forecasting with feature-based predictions.

Forecast results are stored in the database and exposed through REST APIs for dashboard visualization.

---

## Optimization Logic

The mobility optimization module analyzes traffic conditions and provides decision-support recommendations.

Key optimization features include:

* Best travel time identification.
* Route comparison using traffic volume and average speed.
* Congestion-aware mobility recommendations.
* Identification of routes with improved travel efficiency.
* Support for traffic management and route planning.

The optimization logic helps users choose safer and faster travel routes based on current traffic conditions.

---

## Anomaly Detection Approach

The anomaly detection module identifies unusual traffic patterns using both rule-based and AI-driven techniques.

Implemented approaches include:

* Traffic Spike Detection
* Unexpected Low Traffic Detection
* Sensor Anomaly Detection
* Event-Based Traffic Surge Detection
* Isolation Forest Anomaly Detection
* Z-Score Statistical Anomaly Detection

Detected anomalies are categorized by severity and stored for visualization through the dashboard.

---

## System Architecture Overview

The application follows a modular full-stack architecture.

### Frontend

* React (Vite)
* Bootstrap
* React Router
* Axios
* Chart.js

### Backend

* FastAPI
* SQLAlchemy ORM
* JWT Authentication
* Pydantic Validation

### Machine Learning

* Prophet
* Random Forest Regression
* Isolation Forest
* SciPy (Z-Score Analysis)
* Pandas
* NumPy
* Scikit-learn

### Database

* SQLite

### Application Workflow

1. User Authentication
2. Dataset Upload
3. Data Preprocessing
4. Machine Learning Forecasting
5. Congestion Analysis
6. Mobility Optimization
7. Anomaly Detection
8. Scenario Simulation
9. Interactive Dashboard Visualization

---

## API Documentation

The backend exposes RESTful APIs organized into the following modules:

### Authentication

* User Registration
* User Login
* User Profile

### Dataset Management

* Upload Dataset
* Dataset History

### Forecasting

* Train Prophet Model
* Train Random Forest Model
* Generate 24-Hour Forecast
* Generate 7-Day Forecast
* Forecast History

### Congestion Analysis

* Congestion History
* Peak Hour Analytics
* High-Risk Route Detection

### Mobility Optimization

* Best Travel Time
* Route Comparison
* Travel Recommendations

### Anomaly Detection

* Generate Traffic Anomalies
* Traffic Spike Detection
* Low Traffic Detection
* Sensor Anomaly Detection
* Event Traffic Surge Detection
* Isolation Forest Detection
* Z-Score Detection
* Anomaly History

### Scenario Simulation

* Generate Scenario Simulations
* Road Closure Simulation
* Rain Impact Simulation
* Event Traffic Simulation
* Vehicle Load Simulation
* Simulation History

All APIs are documented using FastAPI's built-in OpenAPI/Swagger interface, enabling easy testing and integration with the frontend dashboard.
