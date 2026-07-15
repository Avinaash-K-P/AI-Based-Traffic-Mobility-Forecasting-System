import { useState, useEffect } from "react";
import { toast } from "react-toastify";

import {
    analyzeCongestion,
    getCongestionHistory,
    getPeakHours,
    getHighRiskRoutes

} from "../../services/congestionService";
import "/src/styles/congestion.css";
import "/src/styles/charts.css";
import CongestionChart from "../../components/CongestionChart";
import PeakHourChart from "../../components/PeakHourChart";
import RouteComparisonChart from "../../components/RouteComparisonChart";

const Congestion = () => {

const [history, setHistory] = useState([]);

const [peakHours, setPeakHours] = useState([]);

const [highRiskRoutes, setHighRiskRoutes] = useState([]);

const [loading, setLoading] = useState(false);

useEffect(() => {

    loadCongestionData();

}, []);

const loadCongestionData = async () => {

    try{

        const [
            historyRes,
            peakHourRes,
            highRiskRes
        ] = await Promise.all([

            getCongestionHistory(),

            getPeakHours(),

            getHighRiskRoutes()

        ]);

        setHistory(historyRes.data.items || []);

        setPeakHours(peakHourRes.data.peak_hours || []);

        setHighRiskRoutes(highRiskRes.data.high_risk_routes || []);

    }

    catch(error){

        console.log(error);

    }

};

const handleAnalyze = async () => {

    try{

        setLoading(true);

        await analyzeCongestion();

        toast.success("Congestion analysis completed.");

        loadCongestionData();

    }

    catch(error){

        toast.error("Analysis failed.");

    }

    finally{

        setLoading(false);

    }

};

    return(

<div className="congestion-page">

    <div className="congestion-header">

        <h2>Congestion Analytics</h2>

        <p>
            Analyze congestion patterns and identify peak traffic periods.
        </p>

    </div>


    <div className="congestion-actions">

        <button
            className="btn btn-danger"
            onClick={handleAnalyze}
            disabled={loading}
        >

            {
                loading
                ?
                "Analyzing..."
                :
                "Analyze Congestion"
            }

        </button>

    </div>

<CongestionChart
    data={highRiskRoutes}
/>

<PeakHourChart
    data={peakHours}
/>

<RouteComparisonChart
    data={highRiskRoutes}
/>


    <div className="congestion-summary">

        <div className="summary-card">

            <h3>{history.length}</h3>

            <p>Total Alerts</p>

        </div>

        <div className="summary-card">

            <h3>{peakHours.length}</h3>

            <p>Peak Hours</p>

        </div>

        <div className="summary-card">

            <h3>{highRiskRoutes.length}</h3>

            <p>High Risk Routes</p>

        </div>

    </div>


    {/* Peak Hours */}

    <div className="congestion-card">

        <h4>Peak Hour Analytics</h4>

        <table className="table table-hover">

            <thead>

                <tr>

                    <th>Hour</th>

                    <th>Average Vehicle Count</th>

                </tr>

            </thead>

            <tbody>

            {
                peakHours.map((hour,index)=>(

                    <tr key={index}>

                        <td>{hour.hours}:00</td>

                        <td>{hour.average_vehicle_count}</td>

                    </tr>

                ))
            }

            </tbody>

        </table>

    </div>


    {/* High Risk Routes */}

    <div className="congestion-card">

        <h4>High Risk Routes</h4>

        <table className="table table-hover">

            <thead>

                <tr>

                    <th>Route</th>

                    <th>Vehicle Count</th>

                </tr>

            </thead>

            <tbody>

            {
                highRiskRoutes.map((route,index)=>(

                    <tr key={index}>

                        <td>{route.route_id}</td>

                        <td>{route.vehicle_count}</td>

                    </tr>

                ))
            }

            </tbody>

        </table>

    </div>


    {/* History */}

    <div className="congestion-card">

        <h4>Congestion History</h4>

        <table className="table table-striped">

            <thead>

                <tr>

                    <th>Route</th>

                    <th>Alert Type</th>

                    <th>Severity</th>

                    <th>Message</th>

                </tr>

            </thead>

            <tbody>

            {
                history.map((alert,index)=>(

                    <tr key={index}>

                        <td>{alert.route_id}</td>

                        <td>{alert.alert_type}</td>

                        <td>{alert.severity}</td>

                        <td>{alert.message}</td>

                    </tr>

                ))
            }

            </tbody>

        </table>

    </div>

</div>

);

}

export default Congestion;

