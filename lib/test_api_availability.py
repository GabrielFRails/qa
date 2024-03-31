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

class ContestGroupAvailabilityTestCase(unittest.TestCase):
	def setUp(self):
		return True

	def tearDown(self):
		return True

	def test_contest_group_availability(self):
		pokemon_group_endpoint_list = [
			"contest-type", "contest-effect", "super-contest-effect"
		]

		for endpoint in pokemon_group_endpoint_list:
			url = f"https://pokeapi.co/api/v2/{endpoint}"
			r = request_get(url)
			self.assertEqual(r.status_code, 200)

class EncounterGroupAvailabilityTestCase(unittest.TestCase):
	def setUp(self):
		return True

	def tearDown(self):
		return True

	def test_encounter_group_availability(self):
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

class ItemGroupAvailabilityTestCase(unittest.TestCase):
	def setUp(self):
		return True

	def tearDown(self):
		return True

	def test_item_group_availability(self):
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
	ContestGroupAvailabilityTestCase,
	EncounterGroupAvailabilityTestCase,
	EvolutionGroupAvailabilityTestCase,
	GamesGroupAvailabilityTestCase,
	ItemGroupAvailabilityTestCase
]