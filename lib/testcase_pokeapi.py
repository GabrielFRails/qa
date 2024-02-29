# 
# Copyright (c) Gabriel Freitas: gabriel.estudy.reis@gmail.com
#

import unittest
import requests

class TestPokemonEndpoint(unittest.TestCase):
	def setUp(self):
		return True

	def tearDown(self):
		return True

	def test_pokemon_list(self):
		_test_pokemon_list(self)

def _test_pokemon_list(u):
# {
	url = "https://pokeapi.co/api/v2/pokemon/"
	r = requests.get(url)
	r_status_code = r.status_code
	u.assertEqual(r_status_code, 200)

	r_json = r.json()
	pokemon_count = r_json['count']
	u.assertEqual(type(pokemon_count), int)

	pokemon_results = r_json['results']
	pokemon_results_lenght = len(pokemon_results)
	u.assertEqual(pokemon_results_lenght, 20)

	first_pokemon = pokemon_results[0]
	u.assertEqual(first_pokemon['name'], 'bulbasaur')
# }

testcaselist_pokeapi = [
	TestPokemonEndpoint,
]