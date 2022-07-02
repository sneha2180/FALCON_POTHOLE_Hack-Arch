import "./App.css";
import Logo from "./assets/images/logo.png"

function App() {
  
  return (
    <div className="App">
      <nav>
        <img className="logo" src={Logo} alt="Logo" />
        <button className="button">Get Started</button>
      </nav>

      <div className="content">
        <h1>The ultimate <br/>pothole detector</h1>
        <p>We target a future of roads with no potholes. Our team resonate presents<br/>
        the ultimate pothole detector. Reduce Potholes, reduce accidents.</p>
        <button className="button">Try now</button>
      </div>
    </div>
  );
}

export default App;
