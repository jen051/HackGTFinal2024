import './Home.css';
import { useNavigate } from 'react-router-dom';

function Punch() {
  const navigate = useNavigate();

  return (
    <div className="App">
      <header>
        <h1>Punch</h1>
        <button className="btn-back" onClick={() => navigate('/modules')}>Back</button>
      </header>
      
      <section className="module-details">
        <p>Difficulty: Medium</p>
        <div className="description">
          <p>Description:</p>
          <ul>
            <li>Pivot your foot, rotating your hips and extending your core muscles.</li>
            <li>Extend the shoulder and arm to strike powerfully.</li>
          </ul>
        </div>

        <div className="progress">
          <h3>My Progress:</h3>
          <span className="star">{"\u2605"}</span><span className="star">{"\u2605"}</span><span className="star">{"\u2605"}</span>
        </div>

        <button className="btn" onClick={() => navigate('/video-punch')}>Continue</button>
      </section>
    </div>
  );
}

export default Punch;