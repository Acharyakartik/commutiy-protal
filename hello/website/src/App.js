import Navbar from "./components/Navbar";
import Home from "./components/Home";
import News from "./components/News";
import "./App.css";

function App() {
  return (
    <>
      <Navbar />
      <div className="container">
        <Home />
        <News />
      </div>
    </>
  );
}

export default App;
