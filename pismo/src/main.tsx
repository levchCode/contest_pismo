import React from 'react'
import ReactDOM from 'react-dom/client'
import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import Home from './pages/Home'
import Login from './pages/Login'
import Profile from './pages/Profile'
import Rules from './pages/Rules'
import Submit from './pages/Submit'
import Work from './pages/Work'
import Review from './pages/Review'
import Works from './pages/Works'
import WorksReview from './pages/WorksReview';
import WorksUser from './pages/WorksUser';
import Register from './pages/Register';

import { gapi } from "gapi-script";

import {clientId} from './consts';

import './css/main.css';




gapi.load("client:auth2", () => {
  gapi.client.init({
    clientId:
      clientId,
      plugin_name: "pismo",
  });
});

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <BrowserRouter>
          <Routes>
            <Route path="/" element={<Home/>} />
            <Route path="/login" element={<Login/>} />
            <Route path="/reg" element={<Register/>} />
            <Route path="/profile" element={<Profile/>} />
            <Route path="/rules" element={<Rules/>} />
            <Route path="/submit" element={<Submit/>} />
            <Route path="/work/:id" element={<Work/>} />
            <Route path="/review/:id" element={<Review/>} />
            <Route path="/works/:contest" element={<Works/>} />
            <Route path="/review/:contest" element={<WorksReview/>} />
            <Route path="/user/works/:id" element={<WorksUser/>} />
          </Routes>
    </BrowserRouter>
  </React.StrictMode>
)
