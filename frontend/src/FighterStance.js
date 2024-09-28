import "./Home.css";
import { useNavigate } from "react-router-dom";

function FighterStance() {
  const navigate = useNavigate();
  // console.log("Fighter Stance Component Loaded");
  return (
    <div className="App">
      <header>
        <h1>Fighter Stance</h1>
        <button className="btn-back" onClick={() => navigate("/modules")}>
          Back
        </button>
      </header>

      <section className="module-details">
        <p>Difficulty: Easy</p>
        <div className="description">
          <p>Description:</p>
          <ul>
            <li>
              Shoulders should be high and your feet should be placed
              shoulder-width apart.
            </li>
            <li>Hands should be near eye level to protect your head.</li>
          </ul>
        </div>

        <div className="progress">
          <h3>My Progress:</h3>
          <span className="star">{"\u2605"}</span>
          <span className="star">{"\u2605"}</span>
          <span className="star">{"\u2605"}</span>
        </div>

        <button className="btn" onClick={() => navigate("/video")}>
          Continue
        </button>
      </section>
    </div>
  );
}

export default FighterStance;
