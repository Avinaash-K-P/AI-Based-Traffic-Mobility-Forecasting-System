import { useState } from "react";
import { toast } from "react-toastify";

import { uploadDataset } from "../../services/uploadService";

import "/src/styles/upload.css";

const Upload = () => {

const [selectedFile, setSelectedFile] = useState(null);

const [loading, setLoading] = useState(false);

const handleFileChange = (event) => {

    const file = event.target.files[0];

    setSelectedFile(file);

};

const handleUpload = async () => {

    if (!selectedFile){

        toast.error("Please select a CSV file.");

        return;

    }

    try{

        setLoading(true);

        await uploadDataset(selectedFile);

        toast.success("Dataset uploaded successfully.");

        setSelectedFile(null);

    }

    catch(error){

        toast.error("Dataset upload failed.");

    }

    finally{

        setLoading(false);

    }

};

return(

<div className="upload-page">

    <div className="upload-card">

        <h2>Dataset Upload</h2>

        <p>
            Upload your traffic dataset (.csv)
        </p>

        <input
            type="file"
            accept=".csv"
            onChange={handleFileChange}
        />

        {
            selectedFile && (

                <div className="selected-file">

                    <h5>Selected File</h5>

                    <p>{selectedFile.name}</p>

                    <p>
                        {(selectedFile.size / 1024).toFixed(2)} KB
                    </p>

                </div>

            )
        }

        <button
            className="btn btn-primary mt-3"
            onClick={handleUpload}
            disabled={loading}
        >

            {
                loading
                ?
                "Uploading..."
                :
                "Upload Dataset"
            }

        </button>

    </div>

    <div className="upload-guidelines">

        <h4>Upload Guidelines</h4>

        <ul>

            <li>CSV files only</li>

            <li>Timestamp column required</li>

            <li>Route ID required</li>

            <li>Vehicle Count required</li>

            <li>Average Speed required</li>

            <li>Congestion Level required</li>

            <li>Weather required</li>

        </ul>

    </div>

</div>

);

}

export default Upload;
