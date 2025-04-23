import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2f9a78e019529c64a01d02e98bf65abc'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '27918'

def test_status_code():
	response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
	assert response.status_code == 200

def test_trainer_name():
	response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
	assert response_get.json()["data"][0]['trainer_name'] == 'Dannie'