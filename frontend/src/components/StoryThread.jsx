import React, { useEffect, useState } from 'react';
import { fetchProcessStoryThread } from '../services/api';

export default function StoryThread() {
  const [events, setEvents] = useState([]);
  useEffect(() => { fetchProcessStoryThread().then(setEvents); }, []);
  return (
    <div>
      <h3>Story Thread (Process Narrative)</h3>
      <ul style={{paddingLeft: 20, fontSize: 13}}>
        {events.map(ev =>
          <li key={ev.id} style={{marginBottom: 8}}>
            <b>{ev.type}</b>: {ev.summary}<br/>
            <span style={{color: '#59f'}}>{ev.timestamp}</span>
            {ev.related_decision && (
              <span> | linked to decision <b>{ev.related_decision}</b></span>
            )}
            {ev.related_doc && (
              <span> | doc: <b>{ev.related_doc}</b></span>
            )}
          </li>
        )}
      </ul>
    </div>
  );
}
