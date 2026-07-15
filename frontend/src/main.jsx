import { StrictMode} from 'react'
import { createRoot } from 'react-dom/client'
// import './index.css'
import App from './App.jsx'

// CSS Bootstrap 
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";

// React Toast Notification
import { ToastContainer } from 'react-toastify';
import "react-toastify/dist/ReactToastify.css";

createRoot(document.getElementById('root')).render(

 <StrictMode>

        <App />
 
        <ToastContainer
            position="top-right"
            autoClose={3000}
            hideProgressBar={false}
            closeOnClick
            pauseOnHover
            theme="colored"
        />
 
    </StrictMode>

)