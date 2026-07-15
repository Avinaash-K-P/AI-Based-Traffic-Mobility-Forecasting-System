const AnomalyTable = ({ title, data }) => {

    return (

        <div className="anomaly-card">

            <h4>{title}</h4>

            <table className="table table-striped table-hover">

                <thead>

                    <tr>

                        <th>Route</th>

                        <th>Severity</th>

                        <th>Message</th>

                        <th>Vehicle Count</th>

                        <th>Timestamp</th>

                    </tr>

                </thead>

                <tbody>

                    {
                        data.length > 0 ? (

                            data.map((item, index) => (

                                <tr key={index}>

                                    <td>{item.route_id}</td>

                                    <td>{item.severity}</td>

                                    <td>{item.message}</td>

                                    <td>{item.vehicle_count}</td>

                                    <td>{item.timestamp}</td>

                                </tr>

                            ))

                        ) : (

                            <tr>

                                <td
                                    colSpan="5"
                                    className="text-center"
                                >
                                    "No records found."
                                </td>

                            </tr>

                        )
                    }

                </tbody>

            </table>

        </div>

    );

};

export default AnomalyTable;