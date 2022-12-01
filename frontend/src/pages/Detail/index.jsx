import { useEffect, useState } from "react";
import { NavigationBar } from "../../components/NavigationBar";
import { useParams } from "react-router-dom";
import "./styles.css";

export function Detail() {
  const [pokemon, setPokemon] = useState(null);
  const [isShiny, setIsShiny] = useState(false);
  const { id } = useParams();

  function fetchPokemon(pokemon_id) {
    fetch(`http://localhost:8088/pokemons/${pokemon_id}`)
      .then((res) => res.json())
      .then((res) => {
        setPokemon(res.pokemon);
      });
  }

  useEffect(() => {
    fetchPokemon(id);
  }, [id]);

  return (
    <>
      <NavigationBar />
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
                  <tr key={m.name}>
                    <td>{m.name}</td>
                    <td>{m.type}</td>
                    <td>{m.power ?? "--"}</td>
                    <td>{m.accuracy ? (m.accuracy * 100).toFixed() + " %" : "--"}</td>
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
