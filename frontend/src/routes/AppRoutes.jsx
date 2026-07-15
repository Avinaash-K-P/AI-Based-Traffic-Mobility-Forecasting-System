import { BrowserRouter, Routes, Route } from "react-router-dom";

import AuthLayout from "../layouts/AuthLayout";
import DashboardLayout from "../layouts/DashboardLayout";

import Login from "../pages/auth/Login";
import Register from "../pages/auth/Register";

import Dashboard from "../pages/dashboard/Dashboard";
import Upload from "../pages/dashboard/Upload";
import Forecast from "../pages/dashboard/Forecast";
import Congestion from "../pages/dashboard/Congestion";
import Mobility from "../pages/dashboard/Mobility";
import Anomaly from "../pages/dashboard/Anomaly";
import Scenario from "../pages/dashboard/Scenario";
import Profile from "../pages/dashboard/Profile";

const AppRoutes = () => {
    return (
        <BrowserRouter>

            <Routes>

                {/* Authentication */}

                <Route element={<AuthLayout />}>

                    <Route path="/" element={<Login />}/>
                    <Route path="/register" element={<Register />}/>

                </Route>


                {/* Dashboard */}

                <Route path="/dashboard" element={<DashboardLayout />}>

                    <Route index element={<Dashboard />}/>
                    <Route path="upload" element={<Upload />}/>
                    <Route path="forecast" element={<Forecast />}/>
                    <Route path="congestion" element={<Congestion/>}/>
                    <Route path="mobility" element={<Mobility/>}/>
                    <Route path="anomaly" element ={<Anomaly/>} />
                    <Route path="scenario" element ={<Scenario/>} />
                    <Route path="profile" element = {<Profile/>}/>
                </Route>

            </Routes>

        </BrowserRouter>
    );
};

export default AppRoutes;