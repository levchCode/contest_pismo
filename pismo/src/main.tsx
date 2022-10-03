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
import Signup from './pages/Signup'
import Submit from './pages/Submit'
import Work from './pages/Work'

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <BrowserRouter>
          <Routes>
            <Route exact path="/" element={<Home/>} />
            <Route exact path="/login" element={<Login/>} />
            <Route exact path="/signup" element={<Signup/>} />
            <Route exact path="/profile" element={<Profile/>} />
            <Route exact path="/rules" element={<Rules/>} />
            <Route exact path="/submit" element={<Submit/>} />
            <Route exact path="/work" element={<Work/>} />
          </Routes>
    </BrowserRouter>
  </React.StrictMode>
)
