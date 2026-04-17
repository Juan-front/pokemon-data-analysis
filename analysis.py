import numpy as np

def extract_stat(pokemon, stat_name):
    for stat in pokemon["stats"]:
        if stat["stat"]["name"] == stat_name:
            return stat["base_stat"]
    return 0


def analyze_pokemons(pokemons_data):
    attacks = []
    hp = []

    for p in pokemons_data:
        attacks.append(extract_stat(p, "attack"))
        hp.append(extract_stat(p, "hp"))

    print("\n📊 RESULTADOS:")
    print(f"Média de ataque: {np.mean(attacks):.2f}")
    print(f"Maior ataque: {np.max(attacks)}")
    print(f"Média de HP: {np.mean(hp):.2f}")
    print(f"\n🔍 Total de Pokémon analisados: {len(pokemons_data)}")

def top_3_pokemons(pokemons_data):
    ranking = []

    for p in pokemons_data:
        attack = extract_stat(p, "attack")
        ranking.append((p["name"], attack))

    ranking.sort(key=lambda x: x[1], reverse=True)

    print("\n🏆 TOP 3 POKÉMON MAIS FORTES:")
    for i, (name, attack) in enumerate(ranking[:3], 1):
        print(f"{i}. {name} ({attack})")