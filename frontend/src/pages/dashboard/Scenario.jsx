import { useState, useEffect } from "react";
import { toast } from "react-toastify";
import {
    generateScenario,
    getScenarioHistory,
    getRoadClosure,
    getRainImpact,
    getEventTraffic,
    getVehicleLoad
} from "../../services/scenarioService";
import ScenarioCard from "../../components/ScenarioCard";
import "/src/styles/scenario.css";

const Scenario = () => {

const [history, setHistory] = useState([]);

const [roadClosure, setRoadClosure] = useState([]);

const [rainImpact, setRainImpact] = useState([]);

const [eventTraffic, setEventTraffic] = useState([]);

const [vehicleLoad, setVehicleLoad] = useState([]);

const [loading, setLoading] = useState(false);

useEffect(() => {

    loadScenarios();

}, []);

const loadScenarios = async () => {

    try{

        const [

            historyRes,

            roadClosureRes,

            rainImpactRes,

            eventTrafficRes,

            vehicleLoadRes

        ] = await Promise.all([

            getScenarioHistory(),

            getRoadClosure(),

            getRainImpact(),

            getEventTraffic(),

            getVehicleLoad()

        ]);

        setHistory(
            historyRes.data.items || []
        );

        setRoadClosure(
            roadClosureRes.data.simulation || []
        );

        setRainImpact(
            rainImpactRes.data.simulation || []
        );

        setEventTraffic(
            eventTrafficRes.data.simulation || []
        );

        setVehicleLoad(
            vehicleLoadRes.data.simulation || []
        );

    }

    catch(error){

        console.log(error);

        toast.error("Failed to load simulations.");

    }

};

const handleGenerate = async () => {

    try{

        setLoading(true);

        await generateScenario();

        toast.success("Scenario simulation completed.");

        loadScenarios();

    }

    catch(error){

        toast.error("Simulation failed.");

    }

    finally{

        setLoading(false);

    }

};

return(

<div className="scenario-page">

    {/* Header */}

    <div className="scenario-header">

        <h2>Scenario Simulation</h2>

        <p>

            Simulate various traffic scenarios and analyze their estimated impact.

        </p>

    </div>


    {/* Button */}

    <div className="scenario-actions">

        <button
            className="btn btn-primary"
            onClick={handleGenerate}
            disabled={loading}
        >

            {
                loading
                ?
                "Running..."
                :
                "Run Simulation"
            }

        </button>

    </div>


    {/* KPI */}

    <div className="scenario-summary">

        <div className="scenario-summary-card">

            <h3>{history.length}</h3>

            <p>Total Simulations</p>

        </div>

        <div className="scenario-summary-card">

            <h3>{roadClosure.length}</h3>

            <p>Road Closures</p>

        </div>

        <div className="scenario-summary-card">

            <h3>{rainImpact.length}</h3>

            <p>Rain Impact</p>

        </div>

        <div className="scenario-summary-card">

            <h3>{vehicleLoad.length}</h3>

            <p>Vehicle Load</p>

        </div>

    </div>


    {/* Scenario Cards */}

    <ScenarioCard
        title="Road Closure"
        data={roadClosure}
    />

    <ScenarioCard
        title="Rain Impact"
        data={rainImpact}
    />

    <ScenarioCard
        title="Festival / Event Traffic"
        data={eventTraffic}
    />

    <ScenarioCard
        title="Vehicle Load Increase"
        data={vehicleLoad}
    />


    {/* History */}

    <div className="scenario-card">

        <h4>Simulation History</h4>

        <table className="table table-striped">

            <thead>

                <tr>

                    <th>Scenario</th>

                    <th>Route</th>

                    <th>Congestion</th>

                    <th>Delay</th>

                    <th>Travel Time</th>

                </tr>

            </thead>

            <tbody>

                {

                    history.map((item,index)=>(

                        <tr key={index}>

                            <td>{item.scenario_type}</td>

                            <td>{item.affected_route}</td>

                            <td>{item.estimated_congestion}%</td>

                            <td>{item.estimated_delay}</td>

                            <td>{item.estimated_travel_time}</td>

                        </tr>

                    ))

                }

            </tbody>

        </table>

    </div>

</div>

);

}

export default Scenario;