from api import get_pokemon_data
from analysis import analyze_pokemons, top_3_pokemons

pokemons = ["pikachu", "charizard", "bulbasaur", "squirtle", "gengar"]

dados = []

for name in pokemons:
    data = get_pokemon_data(name)
    if data:
        dados.append(data)

analyze_pokemons(dados)
top_3_pokemons(dados)