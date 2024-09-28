import './Home.css';
import { useNavigate } from 'react-router-dom';

function VideoPunch() {
  const navigate = useNavigate();

  return (
    <div className="App video-page-container"> {/* Added a container class */}
      <header>
        <button className="btn-back" onClick={() => navigate('/modules')}>Back</button>
      </header>

      <section className="video-page">
        <h2>Watch the Video</h2>
        <div className="video-player">
            <video width="750" height="500" controls>
                <source src={`${process.env.PUBLIC_URL}/PunchVideo.mov`} type="video/mp4" />
                Your browser does not support the video tag.
            </video>
        </div>

        {/* The Continue button is still here, but we'll use CSS to position it at the bottom */}
        <button className="btn btn-bottom" onClick={() => navigate('/learn-punch')}>Continue</button>
      </section>
    </div>
  );
}

export default VideoPunch;