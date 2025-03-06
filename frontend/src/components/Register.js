import React, { useState } from 'react';
import axios from 'axios';

function Register() {
  const [formData, setFormData] = useState({
    username: '',
    full_name: '',
    email: '',
    password: ''
  });
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  const handleChange = (e) => {
    setFormData({...formData, [e.target.name]: e.target.value});
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Здесь можно добавить клиентскую валидацию полей
    axios.post('/api/register/', formData)
      .then(response => {
        setSuccess("Регистрация прошла успешно!");
        setError('');
      })
      .catch(err => {
        setError("Ошибка регистрации");
        setSuccess('');
      });
  };