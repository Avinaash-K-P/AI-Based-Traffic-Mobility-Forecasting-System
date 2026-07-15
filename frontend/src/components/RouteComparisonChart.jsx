import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend
} from "chart.js";

import { Bar } from "react-chartjs-2";

import "/src/styles/charts.css";

ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend
);

const RouteComparisonChart = ({ data = [] }) => {

    const chartData = {

        labels: data.map(item => item.route_id),

        datasets: [

            {
                label: "Average Speed (km/h)",

                data: data.map(item => item.average_speed),

                backgroundColor: "#3b82f6",

                borderRadius: 8
            },

            {
                label: "Vehicle Count",

                data: data.map(item => item.vehicle_count),

                backgroundColor: "#10b981",

                borderRadius: 8
            }

        ]

    };

    const options = {

        responsive: true,

        maintainAspectRatio: false,

        plugins: {

            title: {

                display: true,

                text: "Route Comparison Metrics"

            },

            legend: {

                position: "top"

            }

        },

        scales: {

            y: {

                beginAtZero: true

            }

        }

    };

    return (

        <div className="chart-card">

            <Bar
                data={chartData}
                options={options}
            />

        </div>

    );

};

export default RouteComparisonChart;