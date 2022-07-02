import "./App.css";
import Logo from "./assets/images/logo.png";
import Blur from './assets/images/sphere.gif'

function App() {
  return (
    <div className="App">
      <nav>
        <img className="logo" src={Logo} alt="Logo" />
        <button className="button">Get Started</button>
      </nav>

      <div className="whole">
        <div className="content">
          <h1>
            The ultimate <br />
            pothole detector
          </h1>
          <p>
            We target a future of roads with no potholes. Our team resonate
            presents
            <br />
            the ultimate pothole detector. Reduce Potholes, reduce accidents.
          </p>
          <button className="button">Try now</button>
        </div>

        <div className="image">
          <img src={Blur} className="blur" alt="blur" />
        </div>

      </div>
    </div>
  );
}

export default App;
