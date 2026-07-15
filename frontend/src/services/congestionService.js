import api from "./api";

// Generate Congestion Analysis
export const analyzeCongestion = () => {
    return api.post("/congestion/analyze");
};

// Congestion History
export const getCongestionHistory = () => {
    return api.get("/congestion/alerts");
};

// Peak Hours
export const getPeakHours = () => {
    return api.get("/congestion/peak-hours");
};

// High Risk Routes
export const getHighRiskRoutes = () => {
    return api.get("/congestion/high-risk-routes");
};