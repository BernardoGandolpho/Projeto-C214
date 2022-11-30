import { useNavigate } from "react-router-dom";
import "./styles.css";

export function PokemonListItem(props) {
  const navigate = useNavigate();

  return (
    <div
      className="pokemon-list-item"
      onClick={() => {
        navigate(`/detail/${props.pokemon.pokedex_id}`);
      }}
    >
      <h2>
        {props.pokemon.name}
        <span> #{props.pokemon.pokedex_id}</span>
      </h2>
      <div>
        <img src={props.pokemon.images.default} />
      </div>
      <span>{props.pokemon.types.join(", ")}</span>
    </div>
  );
}
