import { useEffect, useState } from "react";
import "./styles.css";
import { PokemonListItem } from "../../components/PokemonListItems";

export function Home() {
  const [pokemons, setPokemons] = useState([]);

  function fetchPokemons() {
    fetch("http://localhost:8088/pokemons?limit=1000")
      .then((res) => res.json())
      .then((res) => {
        setPokemons(res.pokemons);
      });
  }

  useEffect(() => {
    fetchPokemons();
  }, []);

  return (
    <>
      <div className="nav-bar">
        <div>
          <span>API Pokemon</span>
          <div>
            <input placeholder="Type pokemon's name or ID" />
            <button>Search</button>
          </div>
        </div>
      </div>
      <main className="pokemon-list">
        {pokemons.map((p) => (
          <PokemonListItem pokemon={p} />
        ))}
      </main>
    </>
  );
}
