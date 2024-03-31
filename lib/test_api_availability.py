# 
# Copyright (c) Gabriel Freitas: gabriel.estudy.reis@gmail.com
#

from librequest import *

import unittest

class PokemonGroupAvailabilityTestCase(unittest.TestCase):
	def setUp(self):
		return True

	def tearDown(self):
		return True

	def test_pokemon_group_availability(self):
		pokemon_group_endpoint_list = [
			"ability", "characteristic", "egg-group",
			"gender", "growth-rate", "nature", "pokeathlon-stat",
			"pokemon", "pokemon-color", "pokemon-form", "pokemon-habitat",
			"pokemon-shape", "pokemon-species", "stat", "type"
     	]

		for endpoint in pokemon_group_endpoint_list:
			url = f"https://pokeapi.co/api/v2/{endpoint}"
			r = request_get(url)
			self.assertEqual(r.status_code, 200)

testcaselist_availability = [
	PokemonGroupAvailabilityTestCase,
]