import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_data(name):
    response = requests.get(f"{BASE_URL}{name}")
    
    if response.status_code != 200:
        print(f"Erro ao buscar {name}")
        return None
    
    return response.json()