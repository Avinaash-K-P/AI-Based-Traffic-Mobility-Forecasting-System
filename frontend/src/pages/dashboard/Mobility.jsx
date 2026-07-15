import { useState, useEffect } from "react";
import { toast } from "react-toastify";
import {
    generateMobilityRecommendations,
    getMobilityHistory,
    getAlternativeRoutes,
    getBestTravelTimes,
    getCongestionReduction,
    getRouteLoadBalancing
} from "../../services/mobilityService";
import "/src/styles/mobility.css";

const Mobility= () => {

const [history, setHistory] = useState([]);

const [alternativeRoutes, setAlternativeRoutes] = useState([]);

const [bestTravelTimes, setBestTravelTimes] = useState([]);

const [congestionReduction, setCongestionReduction] = useState([]);

const [loadBalancing, setLoadBalancing] = useState([]);

const [loading, setLoading] = useState(false);

const loadMobilityData = async () => {

    try{

        const [
            historyRes,
            alternativeRes,
            travelRes,
            congestionRes,
            loadRes
        ] = await Promise.all([

            getMobilityHistory(),

            getAlternativeRoutes(),

            getBestTravelTimes(),

            getCongestionReduction(),

            getRouteLoadBalancing()

        ]);

        setHistory(historyRes.data.items || []);

        setAlternativeRoutes(alternativeRes.data.recommendations || []);

        setBestTravelTimes(travelRes.data.recommendations || []);

        setCongestionReduction(congestionRes.data.recommendations || []);

        setLoadBalancing(loadRes.data.recommendations || []);

    }

    catch(error){

        console.log(error);

    }

};

const handleGenerate = async () => {

    try{

        setLoading(true);

        await generateMobilityRecommendations();

        toast.success("Mobility recommendations generated.");

        loadMobilityData();

    }

    catch{

        toast.error("Generation failed.");

    }

    finally{

        setLoading(false);

    }

};


return(

<div className="mobility-page">

    {/* Header */}

    <div className="mobility-header">

        <h2>Mobility Optimization</h2>

        <p>

            Generate AI-powered traffic optimization recommendations.

        </p>

    </div>


    {/* Button */}

    <div className="mobility-actions">

        <button
            className="btn btn-success"
            onClick={handleGenerate}
            disabled={loading}
        >

            {

                loading

                ?

                "Generating..."

                :

                "Generate Recommendations"

            }

        </button>

    </div>


    {/* Summary */}

    <div className="mobility-summary">

        <div className="summary-card">

            <h3>{history.length}</h3>

            <p>Total Recommendations</p>

        </div>

        <div className="summary-card">

            <h3>{alternativeRoutes.length}</h3>

            <p>Alternative Routes</p>

        </div>

        <div className="summary-card">

            <h3>{bestTravelTimes.length}</h3>

            <p>Best Travel Times</p>

        </div>

        <div className="summary-card">

            <h3>{loadBalancing.length}</h3>

            <p>Load Balancing</p>

        </div>

    </div>


    {/* Alternative Routes */}

    <div className="mobility-card">

        <h4>Alternative Routes</h4>

        {

            alternativeRoutes.map((item,index)=>(

                <div
                    key={index}
                    className="recommendation-box"
                >

                    <h5>{item.route_id}</h5>

                    <p>{item.recommendation}</p>

                    <strong>

                        Expected Improvement :

                        {item.expected_improvement} %

                    </strong>

                </div>

            ))

        }

    </div>


    {/* Best Travel Times */}

    <div className="mobility-card">

        <h4>Best Travel Times</h4>

        {

            bestTravelTimes.map((item,index)=>(

                <div
                    key={index}
                    className="recommendation-box"
                >

                    <h5>{item.route_id}</h5>

                    <p>{item.recommendation}</p>

                    <strong>

                        Expected Improvement :

                        {item.expected_improvement} %

                    </strong>

                </div>

            ))

        }

    </div>


    {/* Congestion Reduction */}

    <div className="mobility-card">

        <h4>Congestion Reduction</h4>

        {

            congestionReduction.map((item,index)=>(

                <div
                    key={index}
                    className="recommendation-box"
                >

                    <h5>{item.route_id}</h5>

                    <p>{item.recommendation}</p>

                    <strong>

                        Expected Improvement :

                        {item.expected_improvement} %

                    </strong>

                </div>

            ))

        }

    </div>


    {/* Load Balancing */}

    <div className="mobility-card">

        <h4>Route Load Balancing</h4>

        {

            loadBalancing.map((item,index)=>(

                <div
                    key={index}
                    className="recommendation-box"
                >

                    <h5>{item.route_id}</h5>

                    <p>{item.recommendation}</p>

                    <strong>

                        Expected Improvement :

                        {item.expected_improvement} %

                    </strong>

                </div>

            ))

        }

    </div>


    {/* History */}

    <div className="mobility-card">

        <h4>Recommendation History</h4>

        <table className="table table-striped">

            <thead>

                <tr>

                    <th>Route</th>

                    <th>Recommendation Type</th>

                    <th>Improvement</th>

                </tr>

            </thead>

            <tbody>

                {

                    history.map((item,index)=>(

                        <tr key={index}>

                            <td>{item.route_id}</td>

                            <td>{item.recommendation_type}</td>

                            <td>{item.expected_improvement}%</td>

                        </tr>

                    ))

                }

            </tbody>

        </table>

    </div>

</div>

);

}

export default Mobility;