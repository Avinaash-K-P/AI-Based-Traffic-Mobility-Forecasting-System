import api from "./api";

// Train Prophet Model
export const trainProphet = () => {
    return api.post("/forecast/train/prophet");
};

// Train Random Forest Model
export const trainRandomForest = () => {
    return api.post("/forecast/train/random-forest");
};

// Next 24 Hours Forecast
export const get24HourForecast = () => {
    return api.get("/forecast/24-hours");
};

// Next 7 Days Forecast
export const get7DayForecast = () => {
    return api.get("/forecast/7-days");
};

// Forecast History
export const getForecastHistory = () => {
    return api.get("/forecast/history");
};