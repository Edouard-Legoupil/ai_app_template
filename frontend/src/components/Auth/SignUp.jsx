import React, { useState } from 'react';
import { signup } from '../../services/api';

export default function SignUp({ onSignUp }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const handleSubmit = async e => {
    e.preventDefault();
    try {
      await signup(username, password);
      onSignUp();
    } catch (err) {
      setError('Failed to create account.');
    }
  };
  return (
    <form onSubmit={handleSubmit} style={{maxWidth: 340, margin: '40px auto'}}>
      <h2>Create Account</h2>
      {error && <div style={{color: 'red'}}>{error}</div>}
      <label>Username <input value={username} onChange={e => setUsername(e.target.value)} required /></label><br/>
      <label>Password <input type="password" value={password} onChange={e => setPassword(e.target.value)} required /></label><br/>
      <button type="submit" style={{marginTop: 12}}>Sign Up</button>
    </form>
  );
}
