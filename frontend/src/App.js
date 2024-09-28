import ReactDOM from "react-dom/client";
import { BrowserRouter as Router, Routes, Route, BrowserRouter } from 'react-router-dom';
import Home from './Home';
import Modules from './Modules';
import FighterStance from './FighterStance';
import Video from './Video';
import Learn from './Learn';
import LearnPunch from "./LearnPunch";
import Punch from './Punch';
import VideoPunch from './VideoPunch';

function App() {
  return (
    <BrowserRouter>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/modules" element={<Modules />} />
          <Route path="/fighter-stance" element={<FighterStance />} />
          <Route path="/video" element={<Video />} />
          <Route path="/learn" element={<Learn />} />
          <Route path="/learn-punch" element={<LearnPunch />} />
          <Route path="/punch" element={<Punch />} />
          <Route path="/video-punch" element={<VideoPunch />} />
        </Routes>
      </Router>
    </BrowserRouter>

  );
}

export default App;