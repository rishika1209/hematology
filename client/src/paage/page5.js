// App.js
import React, { useState } from 'react';
import axios from 'axios';
import '../styles/mix.css';
const Page5 = () => {
  const [gender, setGender] = useState('');
  const [hemoglobin, setHemoglobin] = useState('');
  const [mcv, setMCV] = useState('');
  const [result, setResult] = useState('');

  const submitForm = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/api5', {
        gender,
        hemoglobin,
        mcv,
      });

      setResult(response.data.result);
    } 
    catch (error) {
      console.error('Error submitting form:', error);
      setResult('An error occurred while processing the request.');
    }
  };

  const resultTextStyles = {
    fontSize: '18px',
    fontWeight: 'bold',
    color: result === 'Anemia' ? 'red' : 'green',
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.heading}>Anemia Prediction App</h1>
      <div style={styles.formContainer}>
        <label style={{ ...styles.label, ...styles.textLabel }}>
          Gender:
          <input
            type="text"
            value={gender}
            onChange={(e) => setGender(e.target.value)}
            style={{ ...styles.input, ...styles.textInput }}
          />
        </label>
        <br />
        <label style={{ ...styles.label, ...styles.hemoglobinLabel }}>
          Hemoglobin:
          <input
            type="text"
            value={hemoglobin}
            onChange={(e) => setHemoglobin(e.target.value)}
            style={{ ...styles.input, ...styles.textInput }}
          />
        </label>
        <br />
        <label style={{ ...styles.label, ...styles.mcvLabel }}>
          MCV:
          <input
            type="text"
            value={mcv}
            onChange={(e) => setMCV(e.target.value)}
            style={{ ...styles.input, ...styles.textInput }}
          />
        </label>
        <br />
        <button onClick={submitForm} style={styles.submitButton}>
          Submit
        </button>
      </div>
      {result !== null && (
        <div style={styles.resultContainer}>
          <h2 style={styles.resultHeading}>Result:</h2>
          <p style={resultTextStyles}>{result}</p>
        </div>
      )}
    </div>
  );
};

const styles = {
  container: {
    textAlign: 'center',
    margin: '20px',
  },
  heading: {
    marginBottom: '20px',
    color: '#333',
  },
  formContainer: {
    maxWidth: '400px',
    margin: 'auto',
    padding: '20px',
    background: '#f4f4f4',
    border: '1px solid #ddd',
    borderRadius: '5px',
  },
  label: {
    display: 'block',
    marginBottom: '10px',
    color: '#555',
  },
  input: {
    width: '100%',
    padding: '8px',
    boxSizing: 'border-box',
    borderRadius: '3px',
    border: '1px solid #ccc',
  },
  submitButton: {
    backgroundColor: '#4CAF50',
    color: 'white',
    padding: '10px',
    borderRadius: '5px',
    cursor: 'pointer',
    border: 'none',
  },
  resultContainer: {
    marginTop: '20px',
    padding: '20px',
    background: '#EFEFEF',
    border: '1px solid #ddd',
    borderRadius: '5px',
  },
  resultHeading: {
    color: '#333',
    marginBottom: '10px',
  },
  textInput: {
    fontWeight: 'bold',
    color: '#333',
  },
  textLabel: {
    fontfamily: "serif",
    color: '#333',
  },
  hemoglobinLabel: {
    color: '#333',// Custom color for Hemoglobin label
    textTransform: 'uppercase',
    fontfamily: "Helvetica Neue",
  },
  mcvLabel: {
    textTransform: 'uppercase',
    color: '#333', // Custom color for MCV label
  },
};

export default Page5;