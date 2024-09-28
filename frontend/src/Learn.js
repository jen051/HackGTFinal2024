import React, { useRef, useState } from "react";
import "./Home.css";

function Learn() {
  const goToModulesPage = () => {
    window.location.href = "/modules"; // Adjust URL path based on your routing
  };

  return (
    <div className="App">
      <header>
        <h1>Webcam Pose Detection</h1>
        <button className="btn-back" onClick={() => window.history.back()}>
          Back
        </button>
      </header>

      <section className="learn-page">
        <h2> Fighting Stance Practice</h2>

        {/* Live video and Modules button wrapped in the same div */}
        <div
          style={{
            position: "relative",
            width: "100%",
            height: "50vh",
            marginTop: "20px",
          }}
        >
          <iframe
            style={{ height: "50vh" }}
            src="http://localhost:8501"
            title="Webcam feed"
          />

          {/* Modules Button below the video */}
          <div style={{ textAlign: "center", marginTop: "20px" }}>
            <button className="btn-modules" onClick={goToModulesPage}>
              Go to Modules
            </button>
          </div>
        </div>
      </section>
    </div>
  );
}

export default Learn;
