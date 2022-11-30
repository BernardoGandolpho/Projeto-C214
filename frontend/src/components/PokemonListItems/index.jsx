import "./styles.css";

export function PokemonListItem(props) {
  return (
    <div className="pokemon-list-item">
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
