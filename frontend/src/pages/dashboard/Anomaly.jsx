import { useState, useEffect } from "react";
import { toast } from "react-toastify";
import {
    generateAnomalies,
    getAnomalyHistory,
    getZScoreAnomalies,
    getLowTraffic,
    getTrafficSpikes,
    getSensorAnomalies,
    getEventSurges,
    getIsolationForest
} from "../../services/anomalyService";
import AnomalyTable from "../../components/AnomalyTable";
import "/src/styles/anomaly.css";

const Anomaly = () => {

const [history, setHistory] = useState([]);

const [trafficSpikes, setTrafficSpikes] = useState([]);

const [lowTraffic, setLowTraffic] = useState([]);

const [sensorAnomalies, setSensorAnomalies] = useState([]);

const [eventSurges, setEventSurges] = useState([]);

const [isolationForest, setIsolationForest] = useState([]);

const [zScore, setZScore] = useState([]);

const [loading, setLoading] = useState(false);

const loadAnomalies = async () => {

    try{

        const [

            historyRes,

            trafficSpikeRes,

            lowTrafficRes,

            sensorRes,

            eventRes,

            isolationRes,

            zScoreRes

        ] = await Promise.all([

            getAnomalyHistory(),

            getTrafficSpikes(),

            getLowTraffic(),

            getSensorAnomalies(),

            getEventSurges(),

            getIsolationForest(),

            getZScoreAnomalies()

        ]);

        setHistory(
            historyRes.data.anomalies || []
        );

        setTrafficSpikes(
            trafficSpikeRes.data.anomalies || []
        );

        setLowTraffic(
            lowTrafficRes.data.anomalies || []
        );

        setSensorAnomalies(
            sensorRes.data.anomalies || []
        );

        setEventSurges(
            eventRes.data.anomalies || []
        );

        setIsolationForest(
            isolationRes.data.anomalies || []
        );

        setZScore(
            zScoreRes.data.anomalies || []
        );

    }

    catch(error){

        console.error(error);

        toast.error("Failed to load anomaly data.");

    }

};

const handleGenerate = async () => {

    try{

        setLoading(true);

        await generateAnomalies();

        toast.success("Traffic anomalies detected.");

        loadAnomalies();

    }

    catch{

        toast.error("Detection failed.");

    }

    finally{

        setLoading(false);

    }

};

return(

<div className="anomaly-page">

    <div className="anomaly-header">

        <h2>Traffic Anomaly Detection</h2>

        <p>
            Detect unusual traffic patterns using multiple anomaly detection techniques.
        </p>

    </div>

    <div className="anomaly-actions">

        <button
            className="btn btn-warning"
            onClick={handleGenerate}
            disabled={loading}
        >

            {
                loading
                ?
                "Detecting..."
                :
                "Detect Anomalies"
            }

        </button>

    </div>

    <div className="anomaly-summary">

        <div className="anomaly-summary-card">

            <h3>{history.length}</h3>

            <p>Total Anomalies</p>

        </div>

        <div className="anomaly-summary-card">

            <h3>{trafficSpikes.length}</h3>

            <p>Traffic Spikes</p>

        </div>

        <div className="anomaly-summary-card">

            <h3>{sensorAnomalies.length}</h3>

            <p>Sensor Anomalies</p>

        </div>

        <div className="anomaly-summary-card">

            <h3>{zScore.length}</h3>

            <p>Z-Score</p>

        </div>

    </div>

    <AnomalyTable
        title="Traffic Spikes"
        data={trafficSpikes}
    />

    <AnomalyTable
        title="Unexpected Low Traffic"
        data={lowTraffic}
    />

    <AnomalyTable
        title="Sensor Anomalies"
        data={sensorAnomalies}
    />

    <AnomalyTable
        title="Event Traffic Surges"
        data={eventSurges}
    />

    <AnomalyTable
        title="Isolation Forest"
        data={isolationForest}
        
    />

    <AnomalyTable
        title="Z-Score Detection"
        data={zScore}
    />

</div>

);


}

export default Anomaly;

