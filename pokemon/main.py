
# def pokemon_json_maker(pokemon):
#     pokemon_json = {}
#     keys_to_extract = ["abilities", "moves", "types"]
#     for key, value in pokemon.items():
#         if key in keys_to_extract:
#                 pokemon_json[key] = value
#                 return pokemon_json

# print(pokemon_json_maker(pikachu))

# with open("pikachu_poke.json", "w") as jsonfile:
#     json.dump(pikachu_poke, jsonfile) # writes json data to file

# with open("gen_1.json") as jsonfile:
#     gen_1_file = json.load(gen_1) # turns JSON encoded data into a python dictionary
# pikachu_req = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
#
# abilities = pikachu_req.json()["abilities"][0]["ability"]["name"]
# # print(abilities)
# moves = pikachu_req.json()["moves"][0]["move"]["name"]
# # print(moves)
# types = pikachu_req.json()["types"][0]["type"]["name"]
# # print(type(types))

# squirtle_req = requests.get("https://pokeapi.co/api/v2/pokemon/squirtle")
# bulbasaur_req = requests.get("https://pokeapi.co/api/v2/pokemon/bulbasaur")
# charmander_req = requests.get("https://pokeapi.co/api/v2/pokemon/charmander")
#
# squirtle = squirtle_req.json()
# bulbasaur = bulbasaur_req.json()
# charmander = charmander_req.json()

import json
import requests

def json_file_maker(pokemon, file_name): # funtion to create a json file of pokemon using .dump
    with open(f"{file_name}", "w") as jsonfile:
        json.dump(pokemon, jsonfile)

# json_file_maker(charmander, "charmander.json") # calling upon the function to create JSON file of pokemon

def pokemon_get(pokemon_name: str) -> dict:
    pokemon_req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    pokemon_dict = pokemon_req.json()
    json_file_maker(pokemon_dict, f"{pokemon_name}.json")

# Function that takes a pokemons name and searches the PokeAPI and returns a dictionary of all JSON data

# pokemon_get("zapdos")

def poke_info(pokemon_json_file: dict) -> dict:
    with open(f"{pokemon_json_file}", "r") as read_file:
        data = json.load(read_file)
        poke_info = {
        "ability" : data["abilities"][0]["ability"]["name"],
        "moves" : data["moves"][0]["move"]["name"],
        "types" : data["types"][0]["type"]["name"]
        }
        print(poke_info)

# function that returns a dictionary of a pokemons first ability, move and type

squirtle_info = poke_info("squirtle.json")
charmander_info = poke_info("charmander.json")
bulbasaur_info = poke_info("bulbasaur.json")
pikachu_info = poke_info("pikachu.json")
zapdos_info = poke_info("zapdos.json")