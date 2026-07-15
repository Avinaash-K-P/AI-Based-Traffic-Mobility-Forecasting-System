import { useEffect, useState } from "react";
import {
    FaDatabase,
    FaChartLine,
    FaTrafficLight,
    FaRoute,
    FaExclamationTriangle,
    FaMapMarkedAlt
} from "react-icons/fa";

import {
    getForecastHistory,
    getCongestionHistory,
    getMobilityHistory,
    getAnomalyHistory,
    getScenarioHistory
} from "../../services/dashboardService";
import "../../styles/dashboard.css";

const Dashboard = () => {

    
    const [forecasts, setForecasts] = useState([]);

    const [congestionAlerts, setCongestionAlerts] = useState([]);

    const [mobilityRecommendations, setMobilityRecommendations] = useState([]);

    const [anomalies, setAnomalies] = useState([]);

    const [scenarios, setScenarios] = useState([]);

    useEffect(() => {
        loadDashboard();
    }, []);

        const loadDashboard = async () => {

        try {

            const [
                forecastRes,
                congestionRes,
                mobilityRes,
                anomalyRes,
                scenarioRes
            ] = await Promise.all([
                getForecastHistory(),
                getCongestionHistory(),
                getMobilityHistory(),
                getAnomalyHistory(),
                getScenarioHistory()
            ]);

            setForecasts(forecastRes.data.items || []);

            setCongestionAlerts(congestionRes.data.items || []);

            setMobilityRecommendations(mobilityRes.data.items || []);

            setAnomalies(anomalyRes.data.items || []);

            setScenarios(scenarioRes.data.items || []);

        }

        catch(error){

            console.log(error);

        }

    };

    return (

<div className="dashboard-page">

    {/* Welcome */}

    <div className="welcome-card">

        <h2>
            Welcome 
        </h2>

        <p>
            AI Traffic & Mobility Forecasting Dashboard
        </p>

    </div>


    {/* KPI Cards */}

    <div className="stats-grid">

        <div className="stat-card">

            <FaChartLine />

            <h3>{forecasts.length}</h3>

            <p>Forecast Results</p>

        </div>

        <div className="stat-card">

            <FaTrafficLight />

            <h3>{congestionAlerts.length}</h3>

            <p>Congestion Alerts</p>

        </div>

        <div className="stat-card">

            <FaRoute />

            <h3>{mobilityRecommendations.length}</h3>

            <p>Mobility Recommendations</p>

        </div>

        <div className="stat-card">

            <FaExclamationTriangle />

            <h3>{anomalies.length}</h3>

            <p>Traffic Anomalies</p>

        </div>

        <div className="stat-card">

            <FaMapMarkedAlt />

            <h3>{scenarios.length}</h3>

            <p>Scenario Simulations</p>

        </div>

    </div>


    {/* Recent Activity */}

    <div className="dashboard-grid">

        <div className="dashboard-card">

            <h4>Recent Forecasts</h4>

            <table className="table table-striped">

                <thead>

                    <tr>

                        <th>Route</th>

                        <th>Vehicle Count</th>

                    </tr>

                </thead>

                <tbody>

                {
                    forecasts.slice(0,5).map((forecast,index)=>(

                        <tr key={index}>

                            <td>{forecast.route_id}</td>

                            <td>{forecast.predicted_vehicle_count}</td>

                        </tr>

                    ))
                }

                </tbody>

            </table>

        </div>


        <div className="dashboard-card">

            <h4>Recent Alerts</h4>

            <table className="table table-striped">

                <thead>

                    <tr>

                        <th>Route</th>

                        <th>Severity</th>

                    </tr>

                </thead>

                <tbody>

                {
                    congestionAlerts.slice(0,5).map((alert,index)=>(

                        <tr key={index}>

                            <td>{alert.route_id}</td>

                            <td>{alert.severity}</td>

                        </tr>

                    ))
                }

                </tbody>

            </table>

        </div>

    </div>

</div>

);

}

export default Dashboard;