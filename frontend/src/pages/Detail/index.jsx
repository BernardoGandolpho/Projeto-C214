import { useEffect, useState } from "react";
import "./styles.css";

export function Detail() {
  const [pokemon, setPokemon] = useState(null);
  const [isShiny, setIsShiny] = useState(false);
  const [search, setSearch] = useState("");

  function fetchPokemon(pokedex_id) {
    fetch(`http://localhost:8088/pokemons/${pokedex_id}`)
      .then((res) => res.json())
      .then((res) => {
        setPokemon(res.pokemon);
      });
  }

  const handleSearch = (event) => {
    setSearch(event.target.value);
  };

  const handleKeyDown = (event) => {
    if (event.key === "Enter") {
      fetchPokemon(search);
    }
  };

  useEffect(() => {
    fetchPokemon(1);
  }, []);

  return (
    <>
      <div className="nav-bar">
        <div>
          <span>API Pokemon</span>
          <div>
            <input
              onKeyDown={handleKeyDown}
              onChange={handleSearch}
              placeholder="Type pokemon's name or ID"
            />
            <button onClick={() => fetchPokemon(search)}>Search</button>
          </div>
        </div>
      </div>
      <main>
        {pokemon && (
          <div className="pokemon">
            <div>
              <h2>
                {pokemon.name}
                <span> #{pokemon.pokedex_id}</span>
              </h2>
              <div>
                <img
                  src={isShiny ? pokemon.images.shiny : pokemon.images.default}
                />
              </div>
              <span>{pokemon.types.join(", ")}</span>
              <div className="shiny-check">
                <input
                  type="checkbox"
                  id="is-shiny"
                  checked={isShiny}
                  onChange={() => setIsShiny(!isShiny)}
                />
                <label htmlFor="is-shiny">Shiny</label>
              </div>
            </div>
            <table>
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Type</th>
                  <th>Power</th>
                  <th>Accuracy</th>
                </tr>
              </thead>
              <tbody>
                {pokemon.moveset.map((m) => (
                  <tr>
                    <td>{m.name}</td>
                    <td>{m.type}</td>
                    <td>{m.power ?? "--"}</td>
                    <td>{m.accuracy ? m.accuracy * 100 + " %" : "--"}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </main>
    </>
  );
}
