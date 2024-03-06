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

	def test_pokemon_info_structure(self):
		_test_pokemon_info_structure(self)

class TestAbilitiesEndpoint(unittest.TestCase):
	def setUp(self):
		return True

	def tearDown(self):
		return True

	def test_pokemon_abilities(self):
		_test_pokemon_abilities(self)

class TestGenerationEndpoint(unittest.TestCase):
	def setUp(self):
		return True

	def tearDown(self):
		return True

	def test_generation_list(self):
		_test_generation_list(self)

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

pokemon_info_dict = {
    'id': int,
    'name': str,
	'base_experience': int,
	'height': int,
	'is_default': bool,
	'order': int,
	'order': int,
	'weight': int,
    'abilities': list,
	'forms': list,
	'game_indices': list,
	'held_items': list,
	'location_area_encounters': str,
	'moves': list,
	'past_types': list,
	'past_abilities': list,
	'sprites': dict,
	'cries': dict,
	'species': dict,
	'stats': list,
	'types': list
}

def _test_pokemon_info_structure(u):
# {
	url = "https://pokeapi.co/api/v2/pokemon/"
	r = requests.get(url)
	r_status_code = r.status_code
	u.assertEqual(r_status_code, 200)

	r_json = r.json()
	pokemon_results = r_json['results']

	pokemon_info_dict_keys = pokemon_info_dict.keys()
	expected_keys_set = set(pokemon_info_dict_keys)
	for p in pokemon_results:
		pokemon_url_info = p['url']
		r = requests.get(pokemon_url_info)
		u.assertEqual(r_status_code, 200)

		pokemon_info = r.json()
		pokemon_info_keys = pokemon_info.keys()
		pokemon_info_keys_set = set(pokemon_info_keys)
		u.assertEqual(pokemon_info_keys_set, expected_keys_set)

		for k in pokemon_info_keys:
			u.assertEqual(type(pokemon_info[k]), pokemon_info_dict[k])
# }

def _test_pokemon_abilities(u):
# {
	url = "https://pokeapi.co/api/v2/ability/1"
	r = requests.get(url)
	r_status_code = r.status_code
	u.assertEqual(r_status_code, 200)
# }

def _test_generation_list(u):
# {
	url = "https://pokeapi.co/api/v2/generation/"
	r = requests.get(url)
	r_status_code = r.status_code
	u.assertEqual(r_status_code, 200)

	response = r.json()
	u.assertEqual(type(response), dict)

	generations = response['results']
	u.assertEqual(type(generations), list)
# }

testcaselist_pokeapi = [
	TestPokemonEndpoint,
	TestAbilitiesEndpoint,
	TestGenerationEndpoint
]