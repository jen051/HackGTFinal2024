import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Home from './Home';
import Modules from './Modules';
import FighterStance from './FighterStance';
import Video from './Video';
import Learn from './Learn';
import LearnPunch from './LearnPunch';
import Punch from './Punch';
import VideoPunch from './VideoPunch';
import reportWebVitals from './reportWebVitals';
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home></Home>,
  },
  {
    path: "/Modules",
    element: <Modules></Modules>,
    
  },
  {
    path: "/fighter-stance",
    element: <FighterStance></FighterStance>
  },
  {
    path: "/video",
    element: <Video></Video>
  },
  {
    path: "/learn",
    element: <Learn></Learn>
  },
  {
    path: "/punch",
    element: <Punch></Punch>
  },
  {
    path: "/learn-punch",
    element: <LearnPunch></LearnPunch>
  },
  {
    path: "/video-punch",
    element: <VideoPunch></VideoPunch>
  }
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
