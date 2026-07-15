import api from "./api";

// Generate Recommendations
export const generateMobilityRecommendations = () => {
    return api.post("/mobility/recommendation");
};

// Recommendation History
export const getMobilityHistory = () => {
    return api.get("/mobility/recommendation");
};

// Alternative Routes
export const getAlternativeRoutes = () => {
    return api.get("/mobility/alternative-route");
};

// Best Travel Times
export const getBestTravelTimes = () => {
    return api.get("/mobility/best-travel-time");
};

// Congestion Reduction
export const getCongestionReduction = () => {
    return api.get("/mobility/congestion-reduction");
};

// Route Load Balancing
export const getRouteLoadBalancing = () => {
    return api.get("/mobility/load-balancing");
};