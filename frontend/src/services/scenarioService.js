import api from "./api";

// Generate Scenario Simulation
export const generateScenario = () => {
    return api.post("/scenario/generate");
};

// Simulation History
export const getScenarioHistory = () => {
    return api.get("/scenario/history");
};

// Road Closure Simulation
export const getRoadClosure = () => {
    return api.get("/scenario/road-closure");
};

// Rain Impact Simulation
export const getRainImpact = () => {
    return api.get("/scenario/rain-impact");
};

// Event Traffic Simulation
export const getEventTraffic = () => {
    return api.get("/scenario/event-traffic");
};

// Vehicle Load Simulation
export const getVehicleLoad = () => {
    return api.get("/scenario/vehicle-load");
};