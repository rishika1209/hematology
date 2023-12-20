// Importing necessary libraries
import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

// Dashboard component
const Dashboard = () => {
  const navigate = useNavigate();

  // Function to handle model button clicks
  const redirectToModel = (modelName) => {
    // Navigating to separate routes for each model
    if (modelName === 'Decision Tree') {
      navigate('/dectree');
    } else if (modelName === 'Random Forest') {
      navigate('/randfor');
    } else if (modelName === 'Logistic Regression') {
      navigate('/logic');
    } else if (modelName === 'k-NN') {
      navigate('/knn');
    } else if (modelName === 'SVM') {
      navigate('/svm');
    } else if (modelName === 'Gaussian NB') {
      navigate('/nb');
    }else if (modelName === 'ALL') {
      navigate('/all'); 
    }else {
      // For other models, navigate to their respective pages
      navigate(`/models/${modelName.toLowerCase().replace(/\s+/g, '-')}`);
    }
  };

  // Function to check if user is valid (you can customize this)
  const userValid = () => {
    let token = localStorage.getItem('userdbtoken');
    if (!token) {
      navigate('/login'); // Redirect to the login page or an error page
    }
  };

  // useEffect to check user validity on component mount
  useEffect(() => {
    userValid();
  }, []);

  // Array of model buttons
  const modelButtons = [
    'Decision Tree',
    'Random Forest',
    'Logistic Regression',
    'k-NN',
    'SVM',
    'Gaussian NB',
    'ALL'
  ];

  // Rendering the Dashboard component
  return (
    <div
      style={{
        textAlign: 'center',
        marginTop: '20vh',
      }}
    >
      <section>
        <h1></h1>
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
          {modelButtons.map((modelName, index) => (
            <button
              key={index}
              className='btn'
              style={{
                padding: '15px 20px',
                fontSize: '18px',
                backgroundColor: 'rgba(138, 43, 226, 0.8)', // Violet color with 0.8 alpha (slightly transparent)
                color: '#fff',
                border: 'none',
                borderRadius: '5px',
                cursor: 'pointer',
                boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
                transition: 'background-color 0.3s ease',
                width: '300px', // Fixed width for uniformity
                marginBottom: '20px',
              }}
              onClick={() => redirectToModel(modelName)}
            >
              {`${ modelName }`}
            </button>
          ))}
        </div>
      </section>
    </div>
  );
};

// Exporting the Dashboard component
export default Dashboard;