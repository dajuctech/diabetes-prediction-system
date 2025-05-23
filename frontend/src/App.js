import React, { useState } from 'react';
import PredictionForm from './components/PredictionForm';

function App() {
  const [result, setResult] = useState(null);

  return (
    <div style={{ padding: 20, maxWidth: 600, margin: 'auto' }}>
      <h2>Diabetes Prediction</h2>
      <PredictionForm onResult={setResult} />
      {result && (
        <div style={{ marginTop: 20 }}>
          <h3>Result</h3>
          <p><strong>Prediction:</strong> {result.prediction ? 'Positive' : 'Negative'}</p>
          <p><strong>Probability:</strong> {result.probability.toFixed(3)}</p>
        </div>
      )}
    </div>
  );
}

export default App;
