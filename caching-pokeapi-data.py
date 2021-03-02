#from flask import Flask, render_template
import requests
import json
import ast
import os

#pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/'+str(151)).json()
#print(pokemon)

pokedex_dict = {}

## CACHING BY WRITING INTO A FILE
if os.path.exists("api-cache.txt"):
    f = open("api-cache.txt", "r")
    pokedex_dict = ast.literal_eval(f.read())

else:
    for i in range(1,808): #All pokemon in Kanto region = 1 (Bulbasaur) to 807 (Zeraora) ==> total of 807 Pokemon exist
        pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/'+str(i)).json()
        pokedex_dict[i] = {}
        name = pokemon['name']
        print("Fetching " + name)
        img_url = pokemon['sprites']['front_default']
        id = pokemon['id']
        type = []
        if len(pokemon['types'])>1:
            type.append(pokemon['types'][0]['type']['name'])
            type.append(pokemon['types'][1]['type']['name'])
        else:
            type.append(pokemon['types'][0]['type']['name'])
        pokedex_dict[i]['name'] = name
        pokedex_dict[i]['id'] = id
        pokedex_dict[i]['img_url'] = img_url
        pokedex_dict[i]['type'] = type

    f = open("api-cache.txt", "w")
    f.write(str(pokedex_dict))
    f.close()

print("PokeDex of length:")
print(len(pokedex_dict))

## TESTING
print("Testing for Zeraora:")

print(pokedex_dict[807]['name'])
print(pokedex_dict[807]['img_url'])
print(pokedex_dict[807]['id'])
if len(pokedex_dict[807]['type'])>1:
    print(pokedex_dict[807]['type'][0])
    print(pokedex_dict[807]['type'][1])
else:
    print(pokedex_dict[807]['type'][0])
