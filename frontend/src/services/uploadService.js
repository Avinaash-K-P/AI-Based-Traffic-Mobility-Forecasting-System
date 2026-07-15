import api from "./api";

export const uploadDataset = (file) => {

    const formData = new FormData();

    formData.append("file", file);

    return api.post(
        "/upload/dataset",
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data"
            }
        }
    );
};