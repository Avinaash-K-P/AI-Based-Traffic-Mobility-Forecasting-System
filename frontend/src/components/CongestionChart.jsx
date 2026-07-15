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

const CongestionChart = ({ data = [] }) => {

    const chartData = {

        labels: data.map(item => item.route_id),

        datasets: [

            {

                label: "Congestion Level (%)",

                data: data.map(item => item.congestion_level),

                backgroundColor: "#f59e0b",

                borderRadius: 8

            }

        ]

    };

    const options = {

        responsive: true,

        maintainAspectRatio: false,

        plugins: {

            legend: {

                display: false

            },

            title: {

                display: true,

                text: "Route-wise Congestion"

            }

        },

        scales: {

            y: {

                beginAtZero: true,

                max: 100,

                title: {

                    display: true,

                    text: "Congestion (%)"

                }

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

export default CongestionChart;