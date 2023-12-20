import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const Dt = () => {
  const navigate = useNavigate();

  const goToModel1 = () => {
    navigate('/api');
  };

  const goToModel2 = () => {
    navigate('/api1');
  };

  const userValid = () => {
    let token = localStorage.getItem("userdbtoken");
    if (token) {
      console.log("user valid");
    } else {
      navigate("*");
    }
  };

  useEffect(() => {
    userValid();
  }, []);

  return (
    <div
      style={{
        textAlign: 'center',
        marginTop: '20vh',
      }}
    >
      <section>
        <h1></h1>
        <button
          className='btn'
          style={{
            padding: '10px 20px',
            fontSize: '25px',
            backgroundColor: 'rgba(220, 20, 60, 0.8)', // Crimson color with 0.8 alpha (slightly transparent)
            color: '#fff',
            border: 'none',
            borderRadius: '5px',
            cursor: 'pointer',
            boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
            transition: 'background-color 0.3s ease',
            margin: '0 auto',
            width: '300px',
            marginBottom: '20px',
          }}
          onClick={goToModel1}
        >
          Prediction with 3 features
        </button>
        <br />
        <button
          className='btn'
          style={{
            padding: '10px 20px',
            fontSize: '25px',
            backgroundColor: 'rgba(220, 20, 60, 0.8)', // Crimson color with 0.8 alpha (slightly transparent)
            color: '#fff',
            border: 'none',
            borderRadius: '5px',
            cursor: 'pointer',
            boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
            transition: 'background-color 0.3s ease',
            margin: '0 auto',
            width: '300px',
            marginBottom: '20px',
          }}
          onClick={goToModel2}
        >
          Prediction with 5 features
        </button>
      </section>
    </div>
  );
};

export default Dt;