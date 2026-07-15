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

const PeakHourChart = ({ data = [] }) => {

    const chartData = {

        labels: data.map(item => `${item.hour}:00`),

        datasets: [

            {

                label: "Traffic Volume",

                data: data.map(item => item.average_vehicle_count),

                backgroundColor: "#2563eb",

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

                text: "Peak Hour Traffic"

            }

        },

        scales: {

            y: {

                beginAtZero: true,

                title: {

                    display: true,

                    text: "Vehicle Count"

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

export default PeakHourChart;