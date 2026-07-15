import api from "./api";

export const getForecastHistory = () => {
    return api.get("/forecast/history");
};

export const getCongestionHistory = () => {
    return api.get("/congestion/alerts");
};

export const getMobilityHistory = () => {
    return api.get("/mobility/recommendation");
};

export const getAnomalyHistory = () => {
    return api.get("/anomaly/history");
};

export const getScenarioHistory = () => {
    return api.get("/scenario/history");
};