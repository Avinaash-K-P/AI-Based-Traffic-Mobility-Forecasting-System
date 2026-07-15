import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
} from "chart.js";

import { Line } from "react-chartjs-2";

import "/src/styles/charts.css";

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
);

const HistoricalForecastChart = ({
    historical = [],
    forecast = []
}) => {

    // Historical Dataset
    const historicalLabels = historical.map(item =>
        item.timestamp ??
        item.prediction_time ??
        ""
    );

    const historicalValues = historical.map(item =>
        item.vehicle_count ??
        item.traffic_volume ??
        item.predicted_vehicle_count ??
        0
    );

    // Forecast Dataset
    const forecastLabels = forecast.map(item =>
        item.prediction_time ??
        item.timestamp ??
        ""
    );

    const forecastValues = forecast.map(item =>
        item.predicted_vehicle_count ??
        item.vehicle_count ??
        0
    );

    // Combine Labels
    const labels = [
        ...historicalLabels,
        ...forecastLabels
    ];

    const data = {

        labels,

        datasets: [

            {
                label: "Historical Traffic",

                data: [
                    ...historicalValues,
                    ...new Array(forecastValues.length).fill(null)
                ],

                borderColor: "#2563eb",

                backgroundColor: "#2563eb",

                tension: 0.35,

                borderWidth: 3
            },

            {
                label: "Predicted Traffic",

                data: [
                    ...new Array(historicalValues.length).fill(null),
                    ...forecastValues
                ],

                borderColor: "#f59e0b",

                backgroundColor: "#f59e0b",

                borderDash: [8,5],

                tension: 0.35,

                borderWidth: 3
            }

        ]

    };

    const options = {

        responsive: true,

        maintainAspectRatio: false,

        plugins: {

            legend: {

                position: "top"

            },

            title: {

                display: true,

                text: "Historical vs Predicted Traffic"

            }

        }

    };

    return (

        <div className="chart-card">

            <Line
                data={data}
                options={options}
            />

        </div>

    );

};

export default HistoricalForecastChart;