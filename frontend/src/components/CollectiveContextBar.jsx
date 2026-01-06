import React, { useEffect, useState } from 'react';
import { fetchCollectiveContext } from '../services/api';

export default function CollectiveContextBar() {
  const [context, setContext] = useState({teamGoal: '', updates: []});
  useEffect(() => { fetchCollectiveContext().then(setContext); }, []);
  return (
    <div style={{
      width: '100%', background: '#222', color: '#fff', padding: 12,
      display: 'flex', alignItems: 'center', justifyContent: 'space-between'
    }}>
      <div>
        <b>Current Goal:</b> {context.teamGoal || '—'}
      </div>
      <div style={{fontSize: 13}}>
        <b>Recent Team Updates:</b> {context.updates?.slice(0, 6).map((u, i) =>
          <span key={i} style={{marginLeft: 12}}>{u}</span>)}
      </div>
    </div>
  );
}
