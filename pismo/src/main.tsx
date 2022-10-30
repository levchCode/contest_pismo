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
import Works from './pages/Works'

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
            <Route exact path="/" element={<Home/>} />
            <Route exact path="/login" element={<Login/>} />
            <Route exact path="/profile" element={<Profile/>} />
            <Route exact path="/rules" element={<Rules/>} />
            <Route exact path="/submit" element={<Submit/>} />
            <Route exact path="/work" element={<Work/>} />
            <Route exact path="/works" element={<Works/>} />
          </Routes>
    </BrowserRouter>
  </React.StrictMode>
)
