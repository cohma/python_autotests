import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2f9a78e019529c64a01d02e98bf65abc'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "Покемон",
    "photo_id": 978
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

data = response_create.json()
POKEMON_ID = data['id']

body_change = {
    "pokemon_id": POKEMON_ID,
    "name": "Новый покемон",
    "photo_id": 978
}

body_add_pokeball = {
    "pokemon_id": POKEMON_ID
}

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)

