import React, { useEffect, useState } from 'react';
import { fetchPendingDecisions } from '../services/api';
import DecisionPointCard from './DecisionPointCard';

export default function DecisionDashboard() {
  const [decisions, setDecisions] = useState([]);
  useEffect(() => { fetchPendingDecisions().then(setDecisions); }, []);
  return (
    <div>
      <h2>Decision Dashboard</h2>
      {decisions.length === 0 && <p>No pending decisions. All processes up-to-date!</p>}
      <div style={{display: 'grid', gap: 24, marginTop: 16}}>
        {decisions.map(decision => 
          <DecisionPointCard key={decision.id} decision={decision} />
        )}
      </div>
    </div>
  );
}
