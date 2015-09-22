__author__ = 'Nathan Mohling'

from exploration_card import AllyCard

class Player(object):
	
	def __init__(self, name):
		self.name = name
		self.hand = []
		for race in AllyCard.races:
			self.hand.append([])
		self.pearls = 1
		self.lords = []
		self.locations = []
		self.monsters = []
		self.key_tokens = 0
		
		self.affiliates = []
		for r in AllyCard.races:
			self.affiliates.append([])
			
	def __str__(self):
		return self.name


	def get_total_keys(self):
		lord_keys = 0
		for lord in self.lords:
			if (lord.free):
				lord_keys += lord.keys
				
		return lord_keys + self.key_tokens
		
	def calculate_score(self):
		"""Calculate the player's score.
		Based on locations, lords, affiliates, and monster tokens.
		
		Return - the total score.
		"""
		location_score = 0
		for location in self.locations:
			location_score += location.get_vps()
		
		lord_score = 0
		for lord in self.lords:
			lord_score += lord.vps
			
		affiliate_score = 0
		for affiliate_race in self.affiliates:
			if (affiliate_race):
				affiliate_score += min(affiliate_race)
			
		monster_score = sum(self.monsters)
		
		return location_score + lord_score + affiliate_score + monster_score
		
		
	def gain_location(self, location):
		"""Adds a location to the player's holdings
		
		location - the location to add."""
		self.locations.append(location)
		self.choose_which_keys_to_use()
		
		
	def choose_which_keys_to_use(self):
		pass
		
	def wants_ally(self, card, cost):
		pass
		
	def encounter_monster(self, threat_track_counter):
		pass
		
	def choose_affiliate(self, possible_affiliates):
		pass
		
	def choose_location(self, locations):
		pass
		
	def choose_new_location(self, new_locations):
		"""Choose a location from newly drawn locations.
		
		Return - The chosen location.
		"""
		pass