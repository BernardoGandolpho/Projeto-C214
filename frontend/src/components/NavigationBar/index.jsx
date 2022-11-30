import { useState } from "react";
import { useNavigate } from 'react-router-dom'
import "./styles.css";

export function NavigationBar(props) {
  const [search, setSearch] = useState("");
  const navigate = useNavigate();

  const handleSearch = (event) => {
    setSearch(event.target.value);
  };

  const handleKeyDown = (event) => {
    if (event.key === "Enter") {
      navigate(`/detail/${search}`);
    }
  };

  return (
    <div className="nav-bar">
      <div>
        <img src={"/logo-api.png"} onClick={() => navigate('/')}></img>
        <div>
          <input
            onKeyDown={handleKeyDown}
            onChange={handleSearch}
            placeholder="Type pokemon's name or ID"
          />
          <button
            onClick={() => {
              navigate(`/detail/${search}`);
            }}
          >
            Search
          </button>
        </div>{" "}
      </div>
    </div>
  );
}
