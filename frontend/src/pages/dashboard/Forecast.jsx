import { useState, useEffect } from "react";
import { toast } from "react-toastify";

import { 
    trainProphet, 
    trainRandomForest, 
    get24HourForecast, 
    get7DayForecast, 
    getForecastHistory 
} from "../../services/forecastService";
import HistoricalForecastChart from "../../components/HistoricalForecastChart";
import "/src/styles/forecast.css";
import "/src/styles/charts.css";

const Forecast = () => {

    const [forecast24, setForecast24] = useState([]);

    const [forecast7, setForecast7] = useState([]);

    const [history, setHistory] = useState([]);

    const [loading, setLoading] = useState(false);

    useEffect(() => {

    loadForecastData();

    }, []);

    const loadForecastData = async () => {

    try{

        const [
            forecast24Res,
            forecast7Res,
            historyRes
        ] = await Promise.all([
            get24HourForecast(),
            get7DayForecast(),
            getForecastHistory()
        ]);

        setForecast24(forecast24Res.data.forecast);

        setForecast7(forecast7Res.data.forecast);

        setHistory(historyRes.data.items || []);

    }

    catch(error){

        console.log(error);

    }

    };

    const handleProphetTraining = async () => {

    setLoading(true);

    try{

        await trainProphet();

        toast.success("Prophet model trained successfully.");

        loadForecastData();

    }

    catch{

        toast.error("Training failed.");

    }

    finally{

        setLoading(false);

    }

};

const handleRandomForestTraining = async () => {

    setLoading(true);

    try{

        await trainRandomForest();

        toast.success("Random Forest model trained successfully.");

        loadForecastData();

    }

    catch{

        toast.error("Training failed.");

    }

    finally{

        setLoading(false);

    }

};


return(

<div className="forecast-page">

    {/* Header */}

    <div className="forecast-header">

        <h2>Forecast Analytics</h2>

        <p>
            Train forecasting models and view traffic predictions.
        </p>

    </div>


    {/* Model Training */}

    <div className="forecast-actions">

        <button
            className="btn btn-primary"
            onClick={handleProphetTraining}
            disabled={loading}
        >
            Train Prophet
        </button>

        <button
            className="btn btn-success"
            onClick={handleRandomForestTraining}
            disabled={loading}
        >
            Train Random Forest
        </button>

    </div>

{/*Chart*/}
<HistoricalForecastChart

    historical={history}

    forecast={forecast24}

/>

    {/* Summary Cards */}

    <div className="forecast-summary">

        <div className="summary-card">

            <h3>{history.length}</h3>

            <p>Total Forecasts</p>

        </div>

        <div className="summary-card">

            <h3>{forecast24.length}</h3>

            <p>24 Hour Forecast</p>

        </div>

        <div className="summary-card">

            <h3>{forecast7.length}</h3>

            <p>7 Day Forecast</p>

        </div>

    </div>


    {/* 24 Hour Forecast */}

    <div className="forecast-card">

        <h4>24 Hour Forecast</h4>

        <table className="table table-hover">

            <thead>

                <tr>

                    <th>Route</th>

                    <th>Prediction Time</th>

                    <th>Vehicle Count</th>

                    <th>Congestion</th>

                </tr>

            </thead>

            <tbody>

                {
                    forecast24.map((forecast,index)=>(

                        <tr key={index}>

                            <td>{forecast.route_id}</td>

                            <td>{forecast.prediction_time}</td>

                            <td>{forecast.predicted_vehicle_count}</td>

                            <td>{forecast.predicted_congestion}</td>

                        </tr>

                    ))
                }

            </tbody>

        </table>

    </div>


    {/* 7 Day Forecast */}

    <div className="forecast-card">

        <h4>7 Day Forecast</h4>

        <table className="table table-hover">

            <thead>

                <tr>

                    <th>Route</th>

                    <th>Prediction Time</th>

                    <th>Vehicle Count</th>

                    <th>Congestion</th>

                </tr>

            </thead>

            <tbody>

                {
                    forecast7.map((forecast,index)=>(

                        <tr key={index}>

                            <td>{forecast.route_id}</td>

                            <td>{forecast.prediction_time}</td>

                            <td>{forecast.predicted_vehicle_count}</td>

                            <td>{forecast.predicted_congestion}</td>

                        </tr>

                    ))
                }

            </tbody>

        </table>

    </div>


    {/* Forecast History */}

    <div className="forecast-card">

        <h4>Forecast History</h4>

        <table className="table table-striped">

            <thead>

                <tr>

                    <th>Route</th>

                    <th>Forecast Type</th>

                    <th>Model</th>

                    <th>Vehicle Count</th>

                </tr>

            </thead>

            <tbody>

                {
                    history.map((forecast,index)=>(

                        <tr key={index}>

                            <td>{forecast.route_id}</td>

                            <td>{forecast.forecast_type}</td>

                            <td>{forecast.model_name}</td>

                            <td>{forecast.predicted_vehicle_count}</td>

                        </tr>

                    ))
                }

            </tbody>

        </table>

    </div>

</div>

);

}

export default Forecast;

