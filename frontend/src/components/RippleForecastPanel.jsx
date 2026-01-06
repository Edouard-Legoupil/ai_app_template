import React, { useEffect, useState } from 'react';
import { fetchRippleForecast } from '../services/api';

export default function RippleForecastPanel({ decisionId }) {
  const [forecast, setForecast] = useState(null);
  useEffect(() => { fetchRippleForecast(decisionId).then(setForecast); }, [decisionId]);
  if (!forecast) return <div>Loading ripple effects...</div>;
  return (
    <div style={{borderLeft: '4px solid #59f', padding: '8px 16px', marginTop: 4}}>
      <h4>Ripple Outcomes</h4>
      <ul>
        {forecast.paths.map((path, i) => (
          <li key={i}>
            {path.outcome}: <i>{path.description}</i><br/>
            <b>Risks/Opportunities:</b> {path.risks || 'None'}<br/>
            <b>Next Steps:</b> {path.next_nodes?.join(', ') || 'End'}
          </li>
        ))}
      </ul>
    </div>
  );
}
