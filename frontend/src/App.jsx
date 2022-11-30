import { Detail } from "./pages/Detail";
import { Home } from "./pages/Home";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

export function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/detail/:id" element={<Detail />} />
      </Routes>
    </Router>
  );
}
