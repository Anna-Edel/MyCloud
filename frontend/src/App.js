import React from "react";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from "./components/LoginPage/LoginPage";
import UserPage from "./components/UserPage/UserPage";
import Registration from "./components/RegisterPage/RegisterPage";
import AdminPage from "./components/AdminPage/AdminPage";

export default function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Login />} />
                <Route path="/register" element={<Registration />} />
                <Route path="/user" element={<UserPage />} />
                <Route path="/admin" element={<AdminPage />} />
            </Routes>
        </Router>
    );
}