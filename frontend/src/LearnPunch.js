import React from 'react';
import './Home.css';

function LearnPunch() {

  const goToModulesPage = () => {
    window.location.href = '/modules';  // Adjust URL path based on your routing
  };

  return (
    <div className="App">
      <header>
        <h1>Webcam Pose Detection</h1>
        <button className="btn-back" onClick={() => window.history.back()}>Back</button>
      </header>

      <section className="learn-page">
        {/* Punching Practice title */}
        <div style={{ marginTop: '10px', textAlign: 'center' }}>
          <h2 style={{ fontSize: '2rem', paddingBottom: '10px' }}>Punching Practice</h2>
        </div>

        {/* Live video and Modules button wrapped in the same div */}
        <div style={{ position: 'relative', width: '100%', marginTop: '20px', textAlign: 'center' }}>
          {/* Streamlit iframe with portrait mode and adjusted height */}
          <iframe
            src="http://localhost:9000"
            title="Webcam feed"
            style={{
              width: 'auto',
              height: '50vh', // Extend the height to make the video larger
              aspectRatio: '9/16', // Enforce portrait mode aspect ratio
              border: 'none',
              display: 'block',
              margin: '0 auto' // Center the iframe
            }}
          />

          {/* Modules Button below the video */}
          <div style={{ textAlign: 'center', marginTop: '20px' }}>
            <button
              className="btn-modules"
              onClick={goToModulesPage}
              style={{
                padding: '10px 20px',
                fontSize: '1.2rem',
                cursor: 'pointer'
              }}
            >
              Go to Modules
            </button>
          </div>
        </div>
      </section>
    </div>
  );
}

export default LearnPunch;
