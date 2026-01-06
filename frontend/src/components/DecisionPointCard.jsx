import React, { useState } from 'react';
import RippleForecastPanel from './RippleForecastPanel';
import { submitDecision } from '../services/api';

export default function DecisionPointCard({ decision }) {
  const [choice, setChoice] = useState('');
  const [rationale, setRationale] = useState('');
  const [showRipple, setShowRipple] = useState(false);
  const [submitted, setSubmitted] = useState(false);

  async function handleSubmit() {
    await submitDecision(decision.id, choice, rationale);
    setSubmitted(true);
  }

  if (submitted) return (
    <div style={{
      border: '1px solid #d0ffe6', background: '#f6fff7',
      borderRadius: 6, padding: 18, color: '#27a07d'
    }}><b>Decision submitted!</b></div>
  );

  return (
    <div style={{
      border: '1px solid #eee', padding: 16, borderRadius: 6,
      background: '#fff', boxShadow: '0 1px 4px #eee'
    }}>
      <h3>{decision.question}</h3>
      <div style={{marginBottom: 8}}>
        <b>Context:</b> {decision.context}
      </div>
      <div>
        <b>Document Story:</b>
        <ul>
          {decision.supporting_docs?.map(doc => 
            <li key={doc.doc_id}>{doc.title} ({doc.type})</li>
          )}
        </ul>
      </div>
      <div>
        <b>Options:</b>
        <ul>
          {decision.options.map(option =>
            <li key={option.option}>
              <input type="radio" name={`dp-${decision.id}`} value={option.option}
                checked={choice === option.option}
                onChange={e => setChoice(e.target.value)} />
              {option.option}: <i>{option.pros}</i> / <i>{option.cons}</i> [{option.risks}]
            </li>
          )}
        </ul>
      </div>
      <button onClick={() => setShowRipple(!showRipple)} style={{marginBottom: 8}}>
        Ripple Forecast {showRipple ? '▲' : '▼'}
      </button>
      {showRipple && <RippleForecastPanel decisionId={decision.id} />}
      <div>
        <label>
          Rationale (optional):<br/>
          <textarea value={rationale} onChange={e => setRationale(e.target.value)} rows={2} style={{width: '100%'}} />
        </label>
      </div>
      <button
        onClick={handleSubmit}
        disabled={!choice}
        style={{marginTop: 8}}
      >Submit Decision</button>
    </div>
  );
}
