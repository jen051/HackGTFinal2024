import './Home.css';
import { useNavigate } from 'react-router-dom';

function Video() {
  const navigate = useNavigate();
  console.log(process.env)

  return (
    <div className="App video-page-container">
      <header>
        <button className="btn-back" onClick={() => navigate('/fighter-stance')}>Back</button>
      </header>

      <section className="video-page">
        <h2>Watch the Video</h2>
        <div className="video-player">
          {/* Reference the video file from the public folder */}
          <video width="750" height="500" controls>
            <source src={`${process.env.PUBLIC_URL}/FighterStanceVideo.mov`} type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        </div>

        {/* Continue button at the bottom */}
        <button className="btn btn-bottom" onClick={() => navigate('/learn')}>Continue</button>
      </section>
    </div>
  );
}

export default Video;
