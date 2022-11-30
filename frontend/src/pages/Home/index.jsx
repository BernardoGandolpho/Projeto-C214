import { useEffect, useState } from "react";
import "./styles.css";
import { PokemonListItem } from "../../components/PokemonListItems";
import { NavigationBar } from "../../components/NavigationBar";


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
      <NavigationBar />
      <main className="pokemon-list">
        {pokemons.map((p) => (
          <PokemonListItem key={p.pokedex_id} pokemon={p} />
        ))}
      </main>
    </>
  );
}
