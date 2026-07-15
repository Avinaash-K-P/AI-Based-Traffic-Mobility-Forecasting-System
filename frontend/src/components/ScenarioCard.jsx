const ScenarioCard = ({ title, data }) => {

    return (

        <div className="scenario-card">

            <h4>{title}</h4>

            {

                data.length > 0 ? (

                    <div className="scenario-grid">

                        {

                            data.map((item, index) => (

                                <div
                                    key={index}
                                    className="scenario-item"
                                >

                                    <h5>{item.affected_route}</h5>

                                    <p>

                                        <strong>Scenario :</strong>

                                        {" "}

                                        {item.scenario_type}

                                    </p>

                                    <p>

                                        <strong>Estimated Congestion :</strong>

                                        {" "}

                                        {item.estimated_congestion} %

                                    </p>

                                    <p>

                                        <strong>Estimated Delay :</strong>

                                        {" "}

                                        {item.estimated_delay}

                                    </p>

                                    <p>

                                        <strong>Estimated Travel Time :</strong>

                                        {" "}

                                        {item.estimated_travel_time}

                                    </p>

                                </div>

                            ))

                        }

                    </div>

                ) : (

                    <div className="text-center py-4">

                        No simulation data available.

                    </div>

                )

            }

        </div>

    );

};

export default ScenarioCard;