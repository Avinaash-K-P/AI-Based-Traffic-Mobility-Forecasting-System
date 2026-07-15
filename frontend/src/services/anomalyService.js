import api from "./api";

// Generate Traffic Anomalies
export const generateAnomalies = () => {
    return api.post("/anomaly/generate");
};

// Anomaly History
export const getAnomalyHistory = () => {
    return api.get("/anomaly/history");
};

// Z-Score Anomalies
export const getZScoreAnomalies = () => {
    return api.get("/anomaly/z-score");
};

// Traffic Spikes
export const getTrafficSpikes = () => {
    return api.get("/anomaly/traffic-spikes");
};

// Unexpected Low Traffic
export const getLowTraffic = () => {
    return api.get("/anomaly/low-traffic");
};

// Sensor Anomalies
export const getSensorAnomalies = () => {
    return api.get("/anomaly/sensor");
};

// Event Surges
export const getEventSurges = () => {
    return api.get("/anomaly/event-surges");
};

// Isolation Forest
export const getIsolationForest = () => {
    return api.get("/anomaly/isolation-forest");
};
