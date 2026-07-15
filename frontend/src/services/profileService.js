import api from "./api";

// View Profile
export const getProfile = () => {
    return api.get("/profile/view");
};

export const updateProfile = (data) => {
    return api.put("/profile/update", data);
};