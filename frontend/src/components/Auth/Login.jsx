import React, { useState } from 'react';
import { login } from '../../services/api';

export default function Login({ onLogin }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const handleSubmit = async e => {
    e.preventDefault();
    try {
      await login(username, password);
      onLogin();
    } catch (err) {
      setError('Login failed.');
    }
  };
  return (
    <form onSubmit={handleSubmit} style={{maxWidth: 340, margin: '40px auto'}}>
      <h2>Login</h2>
      {error && <div style={{color: 'red'}}>{error}</div>}
      <label>Username <input value={username} onChange={e => setUsername(e.target.value)} required /></label><br/>
      <label>Password <input type="password" value={password} onChange={e => setPassword(e.target.value)} required /></label><br/>
      <button type="submit" style={{marginTop: 12}}>Login</button>
    </form>
  );
}
