from fastapi import HTTPException
import pytest
from mock.mock import Mock

from backend.app import poke_app

def test_home():
    # EXERCISE
    result = poke_app.root()

    # ASSERTS
    assert result == {"message": "Salve"}

def test_list_pokemon__db_not_empty__expected_pokemon():
    # FIXTURE
    mock_repository = Mock()
    mock_pokemon = [
        {
            "name": "Bulbasaur",
            "pokedex_id": 1,
            "types": [
                "Grass",
                "Poison"
            ],
            "images": {
                "default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
                "shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/1.png"
            }
        },
        {
            "name": "Ivysaur",
            "pokedex_id": 2,
            "types": [
                "Grass",
                "Poison"
            ],
            "images": {
                "default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/2.png",
                "shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/2.png"
            }
        }
    ]

    mock_repository.list_all.return_value = mock_pokemon

    # EXERCISE
    result = poke_app.list_pokemon(
        repository=mock_repository
    )

    # ASSERTS
    assert result == {"pokemons": mock_pokemon}
    mock_repository.list_all.assert_called_once()

def test_list_pokemon__db_empty__expected_not_found():
    # FIXTURE
    mock_repository = Mock()
    mock_repository.list_all.return_value = None

    # EXERCISE
    with pytest.raises(Exception) as error:
        poke_app.list_pokemon(
            repository=mock_repository
        )

    # ASSERTS
    assert error.value.status_code == 404
    assert error.value.detail == "Pokemon not found"
    mock_repository.list_all.assert_called_once()

def test_find_pokemon__find_existing_pokemon__expected_pokemon():
    # FIXTURE
    mock_repository = Mock()
    mock_pokemon = {
        "name": "Bulbasaur",
        "pokedex_id": 1,
        "types": [
            "Grass",
            "Poison"
        ],
        "moveset": [
            {
                "name": "Razor-Wind",
                "power": 80,
                "accuracy": 1.0,
                "type": "Normal"
            },
            {
                "name": "Cut",
                "power": 50,
                "accuracy": 0.95,
                "type": "Normal"
            },
            {
                "name": "Vine-Whip",
                "power": 45,
                "accuracy": 1.0,
                "type": "Grass"
            }
        ],
        "images": {
            "default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
            "shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/1.png"
        }
    }

    mock_repository.list_one_pokemon.return_value = mock_pokemon

    # EXERCISE
    result = poke_app.find_pokemon(
        id=1,
        repository=mock_repository
    )

    # ASSERTS
    assert result == {"pokemon": mock_pokemon}
    mock_repository.list_one_pokemon.assert_called_once()

def test_find_pokemon__pokemon_not__expected_not_found():
    # FIXTURE
    mock_repository = Mock()
    mock_repository.list_one_pokemon.return_value = None

    # EXERCISE
    with pytest.raises(Exception) as error:
        poke_app.find_pokemon(
            id=3,
            repository=mock_repository
        )

    # ASSERTS
    assert error.value.status_code == 404
    assert error.value.detail == "Pokemon 3 not found"
    mock_repository.list_one_pokemon.assert_called_once()

def test_list_moveset__existing_pokemon_with_moves__expected_moveset():
    # FIXTURE
    mock_repository = Mock()
    mock_moveset = [
        {
            "name": "Razor-Wind",
            "power": 80,
            "accuracy": 1.0,
            "type": "Normal"
        },
        {
            "name": "Cut",
            "power": 50,
            "accuracy": 0.95,
            "type": "Normal"
        },
        {
            "name": "Vine-Whip",
            "power": 45,
            "accuracy": 1.0,
            "type": "Grass"
        }
    ]
    mock_pokemon = {
        "name": "Bulbasaur",
        "pokedex_id": 1,
        "types": [
            "Grass",
            "Poison"
        ],
        "moveset": mock_moveset,
        "images": {
            "default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
            "shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/1.png"
        }
    }

    mock_repository.list_one_pokemon.return_value = mock_pokemon

    # EXERCISE
    result = poke_app.list_moveset(
        id=1,
        skip=0,
        limit=10,
        repository=mock_repository
    )

    # ASSERTS
    assert result == {"moveset": mock_moveset}
    mock_repository.list_one_pokemon.assert_called_once()

def test_list_moveset__existing_pokemon_with_no_moves__expected_not_found():
    # FIXTURE
    mock_repository = Mock()
    mock_pokemon = {
        "name": "Bulbasaur",
        "pokedex_id": 1,
        "types": [
            "Grass",
            "Poison"
        ],
        "moveset": [],
        "images": {
            "default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
            "shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/1.png"
        }
    }

    mock_repository.list_one_pokemon.return_value = mock_pokemon

    # EXERCISE
    with pytest.raises(Exception) as error:
        poke_app.list_moveset(
            id=1,
            skip=0,
            limit=10,
            repository=mock_repository
        )

    # ASSERTS
    assert error.value.status_code == 404
    assert error.value.detail == "No moves found from pokemon 1"
    mock_repository.list_one_pokemon.assert_called_once()

def test_list_moveset__pokemon_not_found__expected_not_found():
    # FIXTURE
    mock_repository = Mock()
    mock_pokemon = None

    mock_repository.list_one_pokemon.return_value = mock_pokemon

    # EXERCISE
    with pytest.raises(Exception) as error:
        poke_app.list_moveset(
            id=1,
            skip=0,
            limit=10,
            repository=mock_repository
        )

    # ASSERTS
    assert error.value.status_code == 404
    assert error.value.detail == "Pokemon 1 not found"
    mock_repository.list_one_pokemon.assert_called_once()

def test_find_move__existing_pokemon_with_move__expected_move():
    # FIXTURE
    mock_repository = Mock()
    mock_moveset = [
        {
            "name": "Razor-Wind",
            "power": 80,
            "accuracy": 1.0,
            "type": "Normal"
        },
        {
            "name": "Cut",
            "power": 50,
            "accuracy": 0.95,
            "type": "Normal"
        },
        {
            "name": "Vine-Whip",
            "power": 45,
            "accuracy": 1.0,
            "type": "Grass"
        }
    ]
    mock_pokemon = {
        "name": "Bulbasaur",
        "pokedex_id": 1,
        "types": [
            "Grass",
            "Poison"
        ],
        "moveset": mock_moveset,
        "images": {
            "default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
            "shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/1.png"
        }
    }

    mock_repository.list_one_pokemon.return_value = mock_pokemon

    # EXERCISE
    result = poke_app.find_move(
        id=1,
        move_id=1,
        repository=mock_repository
    )

    # ASSERTS
    assert result == {"move": mock_moveset[1]}
    mock_repository.list_one_pokemon.assert_called_once()

def test_find_move__existing_pokemon_without_move__expected_not_found():
    # FIXTURE
    mock_repository = Mock()
    mock_moveset = []
    mock_pokemon = {
        "name": "Bulbasaur",
        "pokedex_id": 1,
        "types": [
            "Grass",
            "Poison"
        ],
        "moveset": mock_moveset,
        "images": {
            "default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
            "shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/1.png"
        }
    }

    mock_repository.list_one_pokemon.return_value = mock_pokemon

    # EXERCISE
    with pytest.raises(Exception) as error:
        poke_app.find_move(
            id=1,
            move_id=1,
            repository=mock_repository
        )

    # ASSERTS
    assert error.value.status_code == 404
    assert error.value.detail == "Move 1 from pokemon 1 was not found"
    mock_repository.list_one_pokemon.assert_called_once()

def test_find_move__pokemon_not_found__expected_not_found():
    # FIXTURE
    mock_repository = Mock()
    mock_pokemon = None

    mock_repository.list_one_pokemon.return_value = mock_pokemon

    # EXERCISE
    with pytest.raises(Exception) as error:
        poke_app.find_move(
            id=1,
            move_id=1,
            repository=mock_repository
        )

    # ASSERTS
    assert error.value.status_code == 404
    assert error.value.detail == "Pokemon 1 not found"
    mock_repository.list_one_pokemon.assert_called_once()