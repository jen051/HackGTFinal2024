import './Home.css';
import { useNavigate } from 'react-router-dom';

function Home() {
  const navigate = useNavigate();

  
  return (
    <div className="App">
          <header>
        <div class="container">
            <img src="file.png" alt="Website Logo" class="logo"/> 
        </div>
    </header>

    <section className="kravmaga">
        <div className="container">
          <h1>Mastering Krav Maga</h1>
          <img src="fightingpanda.png" alt="Fighting Panda" className="panda-image" width="200px"/>
        </div>
        <button className="btn" onClick={() => navigate('/modules')}>
            START
          </button>
      </section>
    </div>
    
  );

  
}

export default Home;
