import React, { useState } from 'react';
import axios from 'axios';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('/api/login/', { username, password })
      .then(response => {
        window.location.href = '/files';
      })
      .catch(err => {
        setError('Неверный логин или пароль');
      });
  };

  return (
    <div>
      <h2>Вход</h2>
      {error && <p style={{color: 'red'}}>{error}</p>}
      <form onSubmit={handleSubmit}>
        <div>
          <label>Логин: </label>
          <input type="text" value={username} onChange={e => setUsername(e.target.value)} required/>
        </div>
        <div>
          <label>Пароль: </label>
          <input type="password" value={password} onChange={e => setPassword(e.target.value)} required/>
        </div>
        <button type="submit">Войти</button>
      </form>
    </div>
  );
}

export default Login;