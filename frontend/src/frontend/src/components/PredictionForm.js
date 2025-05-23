import React, { useState } from 'react';

function PredictionForm({ onResult }) {
  const [form, setForm] = useState({
    Pregnancies: '',
    Glucose: '',
    BloodPressure: '',
    SkinThickness: '',
    Insulin: '',
    BMI: '',
    DiabetesPedigreeFunction: '',
    Age: ''
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await fetch('http://localhost:8000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form)
      });

      if (!res.ok) {
        throw new Error('Failed to fetch prediction');
      }

      const data = await res.json();
      onResult(data);
    } catch (error) {
      console.error('Error:', error);
      alert('Prediction failed. Please try again.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {Object.entries(form).map(([key, value]) => (
        <div key={key} style={{ marginBottom: 10 }}>
          <label>{key}:</label>
          <input
            type="number"
            name={key}
            value={value}
            onChange={handleChange}
            step="any"
            required
          />
        </div>
      ))}
      <button type="submit">Predict</button>
    </form>
  );
}

export default PredictionForm;
