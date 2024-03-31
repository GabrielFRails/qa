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

class BerriesGroupAvailabilityTestCase(unittest.TestCase):
	def setUp(self):
		return True

	def tearDown(self):
		return True

	def test_berries_group_availability(self):
		pokemon_group_endpoint_list = [
			"berry", "berry-firmness", "berry-flavor"
		]

		for endpoint in pokemon_group_endpoint_list:
			url = f"https://pokeapi.co/api/v2/{endpoint}"
			r = request_get(url)
			self.assertEqual(r.status_code, 200)

class ContestsGroupAvailabilityTestCase(unittest.TestCase):
	def setUp(self):
		return True

	def tearDown(self):
		return True

	def test_contests_group_availability(self):
		pokemon_group_endpoint_list = [
			"contest-type", "contest-effect", "super-contest-effect"
		]

		for endpoint in pokemon_group_endpoint_list:
			url = f"https://pokeapi.co/api/v2/{endpoint}"
			r = request_get(url)
			self.assertEqual(r.status_code, 200)

class EncountersGroupAvailabilityTestCase(unittest.TestCase):
	def setUp(self):
		return True

	def tearDown(self):
		return True

	def test_encounters_group_availability(self):
		pokemon_group_endpoint_list = [
			"encounter-method", "encounter-condition", "encounter-condition-value"
		]

		for endpoint in pokemon_group_endpoint_list:
			url = f"https://pokeapi.co/api/v2/{endpoint}"
			r = request_get(url)
			self.assertEqual(r.status_code, 200)

class EvolutionGroupAvailabilityTestCase(unittest.TestCase):
	def setUp(self):
		return True

	def tearDown(self):
		return True

	def test_evolution_group_availability(self):
		pokemon_group_endpoint_list = [
			"evolution-chain", "evolution-trigger"
		]

		for endpoint in pokemon_group_endpoint_list:
			url = f"https://pokeapi.co/api/v2/{endpoint}"
			r = request_get(url)
			self.assertEqual(r.status_code, 200)

class GamesGroupAvailabilityTestCase(unittest.TestCase):
	def setUp(self):
		return True

	def tearDown(self):
		return True

	def test_games_group_availability(self):
		pokemon_group_endpoint_list = [
			"generation", "pokedex", "version", "version-group"
		]

		for endpoint in pokemon_group_endpoint_list:
			url = f"https://pokeapi.co/api/v2/{endpoint}"
			r = request_get(url)
			self.assertEqual(r.status_code, 200)

class ItemsGroupAvailabilityTestCase(unittest.TestCase):
	def setUp(self):
		return True

	def tearDown(self):
		return True

	def test_items_group_availability(self):
		pokemon_group_endpoint_list = [
			"item", "item-attribute", "item-category", "item-fling-effect", "item-pocket"
		]

		for endpoint in pokemon_group_endpoint_list:
			url = f"https://pokeapi.co/api/v2/{endpoint}"
			r = request_get(url)
			self.assertEqual(r.status_code, 200)

testcaselist_availability = [
	PokemonGroupAvailabilityTestCase,
	BerriesGroupAvailabilityTestCase,
	ContestsGroupAvailabilityTestCase,
	EncountersGroupAvailabilityTestCase,
	EvolutionGroupAvailabilityTestCase,
	GamesGroupAvailabilityTestCase,
	ItemsGroupAvailabilityTestCase
]