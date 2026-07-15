import { Link, NavLink, Outlet, useNavigate } from "react-router-dom";
import {  jwtDecode } from "jwt-decode";
import "/src/styles/dashboardLayout.css"
import {
    FaTrafficLight,
    FaChartLine,
    FaUpload,
    FaCar,
    FaExclamationTriangle,
    FaRoute,
    FaProjectDiagram,
    FaUser,
    FaUserCircle,
    FaSignOutAlt,
    FaBars,
    FaHome
} from "react-icons/fa";

    const DashboardLayout = () => {
    const navigate = useNavigate();
  
    //Retrieving username from JWT Decode
    const token = localStorage.getItem("token");

    let user = null;

    try {
        if (token) {
            user = jwtDecode(token);
        }
    } catch (error) {
        localStorage.removeItem("token");
        navigate("/");
    }

    const username = user?.username;   //To get role
  
    //Logout
    const handleLogout = () => {
        localStorage.removeItem("token");  
        navigate("/");
    };

  return(


<div className="dashboard-layout">

    {/* Header */}
    <header className="dashboard-header"     href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&display=swap"
    rel="stylesheet">

    <h3 className="dashboard-title">
        <FaTrafficLight className="title-icon" />
        AI Traffic & Mobility Forecasting
    </h3>

        <div className="dashboard-user">

            <span>
                Welcome, <strong>{username}</strong>
            </span>

            {/* Dropdown */}

               <div className="dropdown">

                <button
                    className="user-dropdown-btn"
                    data-bs-toggle="dropdown"
                >
                    <FaUserCircle className="user-icon" />
                </button>

                <ul className="dropdown-menu dropdown-menu-end">

                    <li>

                        <Link
                            className="dropdown-item"
                            to="/dashboard/profile"
                        >
                        
                            <FaUserCircle />

                            <span>Profile</span>

                        </Link>

                    </li>

                    <li>

<button
    type="button"
    className="dropdown-item logout-btn"
    onClick={handleLogout}
>
    <FaSignOutAlt />
    <span>Logout</span>
</button>

                    </li>

                </ul>

            </div>

        </div>

    </header>


    {/* Body */}

    <div className="dashboard-body">

        {/* Sidebar */}

        <aside className="dashboard-sidebar">

            <NavLink to="/dashboard"> 
                <FaHome /> 
                Dashboard
            </NavLink>

            <NavLink to="/dashboard/upload">
                <FaUpload/> 
                Dataset Upload
            </NavLink>

            <NavLink to="/dashboard/forecast">
                <FaChartLine/> 
                Forecast
            </NavLink>

            <NavLink to="/dashboard/congestion">
                <FaTrafficLight/>
                Congestion
            </NavLink>

            <NavLink to="/dashboard/mobility">
                <FaRoute/>
                Mobility
            </NavLink>

            <NavLink to="/dashboard/anomaly">
                <FaExclamationTriangle/>
                Anomaly
            </NavLink>

            <NavLink to="/dashboard/scenario">
            <FaProjectDiagram/>
                Scenario
            </NavLink>

        </aside>


        {/* Main Content */}

        <main className="dashboard-content">

            <Outlet />

        </main>

    </div>


    {/* Footer */}

    <footer className="dashboard-footer">

        © 2026 AI Traffic & Mobility Forecasting System

    </footer>

</div>
  
);

}

export default DashboardLayout;