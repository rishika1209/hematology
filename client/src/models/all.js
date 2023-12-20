import React, { useState } from 'react';
import axios from 'axios';
import '../styles/mix.css';
import '../styles/All.css'; // Import your CSS file for styling

const All = () => {
  const [selectedModel, setSelectedModel] = useState('model1');
  const [responses, setResponses] = useState([]);
  const [gender, setGender] = useState('');
  const [hemoglobin, setHemoglobin] = useState('');
  const [mcv, setMCV] = useState('');
  const [mchc, setMCHC] = useState('');
  const [mch, setMCH] = useState('');
  

  const handleChange = (event) => {
    setSelectedModel(event.target.value);
  };

  const models = [
    {
      "id": "model1",
      "label": "Model 1",
      "data": {
        "gender": 1,
        "hemoglobin": 14.7,
        "mch": 22,
        "mchc": 28.2,
        "mcv": 99.5,
        "result": "non-anemic",
      },
    },
    {
      "id": "model2",
      "label": "Model 2",
      "data": {
        "gender": 1,
        "hemoglobin": 12.7,
        "mch": 19.5,
        "mchc": 28.9,
        "mcv": 89.9,
        "result": "anemic",
      },
    },
    {
      "id": "model3",
      "label": "Model 3",
      "data": {
        "gender": 0,
        "hemoglobin": 14.1,
        "mch": 29.7,
        "mchc": 30.5,
        "mcv": 75.2,
        "result": "non-anemic",
      },
    },
  ];

  const submitRequest = async () => {
    try {
      const selectedModelData = models.find((model) => model.id === selectedModel)?.data;

      if (selectedModelData) {
        const response = await axios.post('http://127.0.0.1:5000/api13', {
          gender: selectedModelData.gender,
          hemoglobin: selectedModelData.hemoglobin,
          mch: selectedModelData.mch,
          mchc: selectedModelData.mchc,
          mcv: selectedModelData.mcv,
        });

        setResponses(response.data); // Assuming the response.data is an array of results
      }
    } catch (error) {
      console.error('Error submitting request:', error);
      setResponses([{ error: 'An error occurred while processing the request.' }]);
    }
  };

  const submitForm = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/api13', {
        gender,
        hemoglobin,
        mcv,
        mchc,
        mch,
      });

      setResponses(response.data);
    } catch (error) {
      console.error('Error submitting form:', error);
      setResponses('An error occurred while processing the request.');
    }
  };



  return (
    <div>
      <div className="container">
        <div className="centered-container">
          <select value={selectedModel} onChange={handleChange}>
            {models.map((model) => (
              <option key={model.id} value={model.id}>
                {model.label}
              </option>
            ))}
          </select>
        </div>

        <div className="centered-container">
          <button className="purple-button" onClick={submitRequest}>
            Submit
          </button>
        </div>
      </div>
      {/* Form Section */}
<div className="container">
  <div className="centered-container">
    <label>
      Gender:
      <input
        type="text"
        value={gender}
        onChange={(e) => setGender(e.target.value)}
        className="input-field"
      />
    </label>
    <br />
    <label>
      Hemoglobin:
      <input
        type="text"
        value={hemoglobin}
        onChange={(e) => setHemoglobin(e.target.value)}
        className="input-field"
      />
    </label>
    <br />
    <label className="input-label">
  MCV:
  <input
    type="text"
    value={mcv}
    onChange={(e) => setMCV(e.target.value)}
    className="input-field"
  />
</label>

    <br />
    <label>
      MCHC:
      <input
        type="text"
        value={mchc}
        onChange={(e) => setMCHC(e.target.value)}
        className="input-field"
      />
    </label>
    <br />
    <label>
      MCH:
      <input
        type="text"
        value={mch}
        onChange={(e) => setMCH(e.target.value)}
        className="input-field"
      />
    </label>
    <br />
    <button className="purple-button" onClick={submitForm}>
      Submit Form
    </button>
  </div>


        {responses.length > 0 && (
          <div className="responses-container">
            <table className="styled-table">
              <thead>
                <tr>
                  <th>Model Name</th>
                  <th>Optimized</th>
                  <th>All Features</th>
                </tr>
              </thead>
              <tbody>
              <tr>
            <td>Decision Tree</td>
            <td>{responses[0].result}</td>
            <td>{responses[0].result}</td>
          </tr>
          <tr>
            <td>Random Tree</td>
            <td>{responses[1].result}</td>
            <td>{responses[1].result}</td>
          </tr>
          <tr>
            <td>Logistic Regression</td>
            <td>{responses[2].result}</td>
            <td>{responses[2].result}</td>
          </tr>
          <tr>
            <td>KNN</td>
            <td>{responses[3].result}</td>
            <td>{responses[3].result}</td>
          </tr>
          <tr>
            <td>Support Vector machine</td>
            <td>{responses[4].result}</td>
            <td>{responses[4].result}</td>
          </tr>
          <tr>
            <td>Gaussian NB</td>
            <td>{responses[5].result}</td>
            <td>{responses[5].result}</td>
          </tr>
              </tbody>
            </table>
          </div>
        )}
        <div style={{ margin: '20px' }}></div>
      </div>
    </div>
  );
  
};

export default All;
