import requests


# This script populates the database with data from another api


def delete_all(max_pokedex_id, my_url):
    for i in range(1, max_pokedex_id+1):
        response = requests.delete(my_url + str(i))

        if response.status_code == 204:
            print(f"Pokemon {i} excluido com sucesso!")
        else:
            print(f"Ocorreu um erro ao tentar excluir o pokemon {i}: {response.status_code}")


def get_moves(max_move_id, source_url):
    moves = []

    for i in range(1, max_move_id+1):
        response = requests.get(f"{source_url}move/{str(i)}")

        if response.status_code != 200:
            print(f"Nao pegou o ataque {i}: {response.status_code}")
            continue

        response = response.json()

        data = {
            "name": response["name"].title(),
            "type": response["type"]["name"].title()
        }

        if type(response["power"]) is int:
            data["power"] = response["power"]

        if type(response["accuracy"]) is int:
            data["accuracy"] = response["accuracy"]/100

        moves.append(data)
        print(f"Ataque {i} armazenado com sucesso!")

    return moves


def post_all(max_pokedex_id, max_move_id, source_url, my_url):
    moves = get_moves(max_move_id, source_url)

    for i in range (1, max_pokedex_id+1):
        url_pokemon = f"{source_url}pokemon/{str(i)}"

        response = requests.get(url_pokemon)

        if response.status_code != 200:
            print(f"Não achou os dados do pokemon {i}: {response.status_code}")
            continue

        response = response.json()

        pokemon_moves = []
        for move in (response["moves"]):
            move_url = move["move"]["url"]
            move_id = int(move_url.split('/')[-2])-1

            if move_id in moves:
                pokemon_moves.append(moves[move_id])


        types = []
        for pokemon_type in (response["types"]):
            types.append(pokemon_type["type"]["name"].title())

        sprites = {
            "default": response['sprites']['front_default'],
            "shiny": response['sprites']['front_shiny']
        }

        pokemon = {
            "name": response["name"].title(),
            "pokedex_id": i,
            "types": types,
            "moveset": pokemon_moves,
            "images": sprites
        }
        
        response = requests.post(my_url, json=pokemon)

        if response.status_code == 201:
            print(f"Pokemon {i} postado com sucesso!")
        else:
            print(f"Puxou os dados de {i}, mas a minha api nao aceitou: {response.status_code}")


if __name__ == "__main__":
    source_url = "https://pokeapi.co/api/v2/"
    my_url = "http://0.0.0.0:8088/pokemons/"

    max_pokedex_id = 809
    max_move_id = 826

    delete_all(max_pokedex_id, my_url)
    post_all(max_pokedex_id, max_move_id, source_url, my_url)
