from random import choice

from player import Player
from exploration_card import AllyCard
from threat_track import ThreatTrack
from lord import Lord

class SimpleAiPlayer(Player):
	"""A simple (very simple) AI to play PyByss."""
	
	def __init__(self, name):
		super(self.__class__, self).__init__(name)
		
	#################
	# Inherited functions
	def start_turn(self, game):
		"""Starts the turn for the player.
		The player will choose one of three actions:
		Explore the Depths, Request_Support_From the Council,
		or Recruit a Lord
		
		game - reference to the game
		"""
		print "It's %s's turn!" % (self)
		
		lord, payment, pearls = self.evaluate_lords(game)
		if (lord):
			game.recruit_a_lord(self, lord, payment, pearls)
		else:
			races_with_most_cards = []
			most_cards = 0
			for race in AllyCard.races:
				if (len(game.council_decks[race]) > most_cards):
					most_cards = len(game.council_decks[race])
					races_with_most_cards = [race]
				elif (len(game.council_decks[race]) == most_cards):
					races_with_most_cards.append(race)
			if (most_cards > 3):
				game.request_support_from_the_council(self, \
				  choice(races_with_most_cards))
			else:
				game.explore_the_depths(self)
			
			
	def wants_ally(self, card, cost):
		"""Whether the player wants to buy an ally while
		another player is exploring.
		
		return - Whether the player wants to buy the ally.
		"""
		return cost <= self.pearls and card.value >= 4
		
		
	def encounter_monster(self, threat_track_counter):
		"""What to do when a monster is encountered.
		
		Return - Whether to fight the monster
		       - Which reward - pearls or monster tokens.
		"""
		return True, ThreatTrack.all_monster_tokens
		
	def choose_affiliate(self, possible_affiliates):
		"""Choose which ally card to affiliate.
		
		Return - The affiliate choice.
		"""
		return choice(possible_affiliates)
		
	def choose_location(self, locations):
		"""Choose a location from the revealed locations.
		
		Return - The chosen location or the number of locations
		         to draw from the top of the deck.
		"""
		if (locations):
			max_location = locations[0]
			max_vps = 0
			for location in locations:
				vps = location.get_vps(self)
				if (vps > max_vps):
					max_vps = vps
					max_location = location
					
			return max_location
		else:
			return 4
			
			
	def choose_new_location(self, new_locations):
		"""Choose a location from newly drawn locations.
		
		Return - The chosen location.
		"""
		max_location = locations[0]
		max_vps = 0
		for location in locations:
			vps = location.get_vps(self)
			if (vps > max_vps):
				max_vps = vps
				max_location = location
				
		return max_location
		
		
	def choose_which_keys_to_use(self):
		"""Choose which keys to use when you get a location."""
		keys_from_lords = 0
		for lord in self.lords:
			if (not lord.attached and lord.keys > 0):
				keys_from_lords += lord.keys
				lord.free = False
		self.keys -= (3 - keys_from_lords)
		
	
	#################
	# Non-Inherited functions
	def evaluate_lords(self, game):
		"""Choose which lord to purchase.
		
		game - Reference to game
		Return - The lord to purchase.
		       - The cards to pay with.
			   - The pearls to pay with.
		"""
		max_utility = 0
		best_lord = None
		pay_for_best_lord = []
		pearls_for_best_lord = 0
		for lord in game.lord_court:
			lord_utility, payment, pearls = \
			  self.calculate_lord_utility(lord)
			if (lord_utility > max_utility):
				max_utility = lord_utility
				best_lord = lord
				pay_for_best_lord = payment
				pearls_for_best_lord = pearls
			
		return best_lord, pay_for_best_lord, pearls_for_best_lord
		
		
	def calculate_lord_utility(self, lord):
		"""Calculate the desirability of a lord,
		and whether it can be afforded.
		
		lord - The lord to evaluate.
		Return - The desirability of the lord.
		       - The cards to pay with.
			   - The pearls to pay with.
		"""
		purchasable = False
		utility = 0
		payment = []
		pearls = 0
		
		if (lord.guild == Lord.ambassador):
			purchasable = True
			card_total = 0
			for race in self.hand:
				if (len(race) == 0):
					purchasable = False
					break
				else:
					card_total += sum(race)
			purchasable = purchasable and card_total + self.pearls >= lord.cost
			
			if (purchasable):
				for race in self.hand:
					payment.append(race.pop())
				while (sum(payment) + self.pearls < lord.cost):
					if (self.hand[AllyCard.jellyfish]):
						payment.append(self.hand[AllyCard.jellyfish].pop())
					elif (self.hand[AllyCard.crab]):
						payment.append(self.hand[AllyCard.crab].pop())
					elif (self.hand[AllyCard.seahorse]):
						payment.append(self.hand[AllyCard.seahorse].pop())
					elif (self.hand[AllyCard.shellfish]):
						payment.append(self.hand[AllyCard.shellfish].pop())
					elif (self.hand[AllyCard.squid]):
						payment.append(self.hand[AllyCard.squid].pop())
					else:
						purchasable = False
						break
			
		elif (lord.bubbles == 1 and \
		      sum(self.hand[lord.primary_race]) + self.pearls >= lord.cost and \
			  sum(self.hand[lord.primary_race]) > 0):
			purchasable = True
			payment.append(self.hand[lord.primary_race].pop())
			while (sum(payment) + self.pearls < lord.cost):
				if (self.hand[lord.primary_race]):
					payment.append(self.hand[lord.primary_race].pop())
				else:
					purchasable = False
					break
					
		elif (lord.bubbles == 2):
			secondary_race = 0
			secondary_race_value = 0
			for race in range(len(self.hand)):
				if (race != lord.primary_race and sum(self.hand[race]) > secondary_race_value):
					secondary_race = race
					secondary_race_value = sum(self.hand[race])
			if (secondary_race_value > 0 and sum(self.hand[lord.primary_race]) > 0 and \
			    secondary_race_value + sum(self.hand[lord.primary_race]) + self.pearls >= lord.cost):
				purchasable = True
				payment.append(self.hand[lord.primary_race].pop())
				payment.append(self.hand[secondary_race].pop())
				while (sum(payment) + self.pearls < lord.cost):
					if (self.hand[lord.primary_race]):
						payment.append(self.hand[lord.primary_race].pop())
					elif (self.hand[secondary_race]):
						payment.append(self.hand[secondary_race].pop())
					else:
						purchasable = False
						break
					
		elif (lord.bubbles == 3):
			secondary_race = 0
			secondary_race_value = 0
			tertiary_race = 0
			tertiary_race_value = 0
			for race in range(len(self.hand)):
				if (race != lord.primary_race):
					race_sum = sum(self.hand[race])
					if (race_sum > secondary_race_value):
						tertiary_race = secondary_race
						tertiary_race_value = secondary_race_value
						secondary_race = race
						secondary_race_value = race_sum
					elif (race_sum > tertiary_race_value):
						tertiary_race = race
						tertiary_race_value = race_sum
			if (secondary_race_value > 0 and tertiary_race_value > 0 and sum(self.hand[lord.primary_race]) > 0 and\
			    secondary_race_value + tertiary_race_value + sum(self.hand[lord.primary_race]) + self.pearls >= lord.cost):
				purchasable = True
				payment.append(self.hand[lord.primary_race].pop())
				payment.append(self.hand[secondary_race].pop())
				payment.append(self.hand[tertiary_race].pop())
				while (sum(payment) + self.pearls < lord.cost):
					if (self.hand[lord.primary_race]):
						payment.append(self.hand[lord.primary_race].pop())
					elif (self.hand[secondary_race]):
						payment.append(self.hand[secondary_race].pop())
					elif (self.hand[tertiary_race]):
						payment.append(self.hand[tertiary_race].pop())
					else:
						purchasable = False
						break
		
		if (purchasable):
			utility = lord.vps + 2*lord.keys
			if (sum(payment) < lord.cost):
				pearls = lord.cost - sum(payment)
			
		return utility, payment, pearls
