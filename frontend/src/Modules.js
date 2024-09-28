import './Home.css';
import { useNavigate } from 'react-router-dom';

function Modules() {
  const navigate = useNavigate();

  return (
    <div className="App">
      <header>
        <h1>Krav Maga Modules</h1>
        <button className="btn-back" onClick={() => navigate('/')}>Back</button>
      </header>
      
      <section className="module-list">
        <div className="module-item">
          <button className="module-btn" onClick={() => navigate("/fighter-stance")}>
            Fighter Stance
          </button>
          <p>Difficulty: Beginner</p>
          <div className="stars">
            <span className="star">{"\u2605"}</span><span className="star">{"\u2605"}</span><span className="star">{"\u2605"}</span>
          </div>
        </div>

        <div className="module-item">
          <button className="module-btn" onClick={() => navigate('/punch')}>
            Punch
          </button>
          <p>Difficulty: Intermediate</p>
          <div className="stars">
            <span className="star">{"\u2605"}</span><span className="star">{"\u2605"}</span><span className="star">{"\u2605"}</span>
          </div>
        </div>

        <div className="module-item">
          <button className="module-btn" onClick={() => navigate('/kick')}>
            Kick
          </button>
          <p>Difficulty: Challenging</p>
          <div className="stars">
            <span className="star">{"\u2606"}</span><span className="star">{"\u2606"}</span><span className="star">{"\u2606"}</span>
          </div>
        </div>
      </section>
    </div>
  );
}

export default Modules;