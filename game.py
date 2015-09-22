
from random import shuffle

from exploration_card import ExplorationCard, MonsterCard, AllyCard
from threat_track import ThreatTrack
from lord import lords
from location import locations, Location


__author__ = 'Nathan Mohling'

class Game(object):
	"""Controls the mechanics for the game."""

	max_exploration = 5
	max_lords_in_court = 6
	lord_refill_level = 2

	def __init__(self, player_list):
		self.create_decks()
		self.players = player_list
		self.num_players = len(self.players)
		self.current_player = 0
		self.threat_track = ThreatTrack()
		self.cant_fully_refill_court = False
		
		self.run_game()
		
		
	def create_decks(self):
		"""Creates all the decks by calling helper functions"""
		self.create_exploration_deck()
		self.create_council_decks()
		self.create_lord_deck()
		self.create_location_deck()

		
	def create_exploration_deck(self):
		"""Creates the exploration deck"""
		self.exploration_deck = []
		self.exploration_discard = []
		self.revealed_exploration_cards = []
		
		for _ in range(6):
			self.exploration_deck.append(MonsterCard())

		for race in AllyCard.races:
			for value in AllyCard.ally_card_value_distribution:
				self.exploration_deck.append(AllyCard(value, race))
				
		shuffle(self.exploration_deck)
		
		
	def create_council_decks(self):
		"""Creates the council decks"""
		self.council_decks = []
		for race in AllyCard.races:
			self.council_decks.append([])
			
			
	def create_lord_deck(self):
		"""Creates the lord deck"""
		self.lord_deck = lords
		self.lord_discard = []
		self.lord_court = []
		
		shuffle(self.lord_deck)
		
		for _ in range(Game.max_lords_in_court):
			self.lord_court.append(self.lord_deck.pop())
		
	def create_location_deck(self):
		"""Creates the location deck"""
		self.location_deck = locations
		self.revealed_locations = []
		
		shuffle(self.location_deck)
		self.revealed_locations.append(self.location_deck.pop())
		
	
	def run_game(self):
		"""Main loop to run the game."""
		while (True):
			self.players[self.current_player].start_turn(self)
			if (self.end_condition_met()):
				break
			self.current_player = \
			  (self.current_player + 1) % self.num_players
		
		self.end_game()
				
		
	
	def explore_the_depths(self, player):
		"""For the action, Explore the Depths.
		
		player - the current exploring.
		"""
		print "%s is going exploring!" % player
		self.player_has_taken_card = []
		self.exploration_card_cost = 1
		self.explore_loop(player)
		self.discard_from_exploration()
		
		
	def explore_loop(self, player):
		"""A recursive loop for exploring
		
		player - the current exploring.
		"""
		card = self.draw_exploration_card()
		if (card.type == ExplorationCard.ally):
			print "  %s encounters an ally: %s" % (player, card)
			card_taken = False
			for i in range(self.num_players):
				player_to_check_num = (i+self.current_player+1)%self.num_players
				if (not player_to_check_num in self.player_has_taken_card and \
				      self.players[player_to_check_num].wants_ally(card, self.exploration_card_cost)):
					self.player_has_taken_card.append(player_to_check_num)
					self.players[player_to_check_num].hand[card.race].append(card)
					self.players[player_to_check_num].hand[card.race].sort()
					card_taken = True
					break
			if (card_taken):
				if (not self.players[player_to_check_num] is player):
					print "    %s buys %s from %s for %d pearl" % \
					  (self.players[player_to_check_num], card, player, self.exploration_card_cost)
					self.players[player_to_check_num].pearls -= self.exploration_card_cost
					player.pearls += self.exploration_card_cost
					self.exploration_card_cost += 1
					self.explore_loop(player)
				else:
					print "    %s takes %s" % (player, card)
			else:
				if (self.end_of_exploration()):
					print "    %s takes %s and a pearl" % (player, card)
					player.pearls += 1
					player.hand[card.race].append(card)
					player.hand[card.race].sort()
				else:
					self.revealed_exploration_cards.append(card)
					self.explore_loop(player)
					
		elif (card.type == ExplorationCard.monster):
			print "  %s encounters a monster!" % player
			wants_to_fight, chosen_reward = \
			  player.encounter_monster(self.threat_track.counter)
			if (wants_to_fight):
				self.fight_reward(player, chosen_reward)
				self.threat_track.counter = 0
				self.check_keys(player)
			elif (self.end_of_exploration()):
				player.pearls += 1
				self.fight_reward(player, chosen_reward)
				self.threat_track.counter = 0
				check_keys(self, player)
			else:
				if (self.threat_track.counter < ThreatTrack.max):
					self.threat_track.counter += 1
				self.revealed_exploration_cards.append(card)
				self.explore_loop(player)
				
				
	def draw_exploration_card(self):
		"""Draw an exploration card.
		
		Return - The drawn card."""
		if (not self.exploration_deck):
			self.exploration_deck = self.exploration_discard
			self.exploration_discard = []
			shuffle(self.exploration_deck)
		return self.exploration_deck.pop()
				
				
	def end_of_exploration(self):
		"""Check to see if we've reached the end of the exploration track."""
		return len(self.revealed_exploration_cards) >= Game.max_exploration - 1
		

	def discard_from_exploration(self):
		"""Discards the leftover cards from exploring."""
		while (self.revealed_exploration_cards):
			card = self.revealed_exploration_cards.pop()
			if (card.type == ExplorationCard.monster):
				self.exploration_discard.append(card)
			elif (card.type == ExplorationCard.ally):
				self.council_decks[card.race].append(card)
				
	def fight_reward(self, player, chosen_reward):
		"""Rewards the player after fighting a monster while exploring.
		
		player - The player exploring.
		chosen_reward - The reward they chose--pearls or monster tokens or both.
		"""
		pearls, monster_tokens, keys = \
		  self.threat_track.get_reward(chosen_reward)
		player.pearls += pearls
		player.monsters += monster_tokens
		player.key_tokens += keys
		
		
	def request_support_from_the_council(self, player, race):
		"""For the action Request Support from the Council.
		Gives a player a stack of cards from the council area.
		
		player - The player requesting support.
		race - The race stack to pick up.
		"""
		print "%s picks up %d cards from the %s deck" % \
		     (player, len(self.council_decks[race]), AllyCard.race_strings[race])
		player.hand[race] += self.council_decks[race]
		player.hand[race].sort()
		self.council_decks[race] = []
		
		
	def recruit_a_lord(self, player, lord, allies, pearls):
		"""For the action Recruit a Lord.
		
		player - The player recruiting the lord.
		lord - The lord to be recruited.
		allies - The allies used to purchase the lord.
		pearls - Supplemental pearls to pay for the lord.
		"""
		print "%s recruits %s" % (player, lord)
		possible_affiliates = []
		if (lord in self.lord_court and \
		    self.calculate_payment(lord, allies, pearls, \
			                       possible_affiliates)):
			player.lords.append(lord)
			for ally in allies:
				self.exploration_discard.append(ally)
			player.pearls -= pearls
			self.lord_court.remove(lord)
			if (1 == len(possible_affiliates)):
				player.affiliates[possible_affiliates[0].race].append(possible_affiliates[0])
			else:
				affiliate = player.choose_affiliate(possible_affiliates)
				if (affiliate in possible_affiliates):
					player.affiliates[affiliate.race].append(affiliate)
					
			if (len(self.lord_court) <= Game.lord_refill_level):
				# Refill the court if it gets too low.
				player.pearls += 2
				while (len(self.lord_court) < Game.max_lords_in_court):
					if (self.lord_deck):
						self.lord_court.append(self.lord_deck.pop())
					else:
						self.cant_fully_refill_court = true
						break
			self.check_keys(player)
			
	
	def calculate_payment(self, lord, allies, pearls, affiliates):
		"""To calculate whether payment is sufficient to purchase the lord
		
		lord - The lord to be recruited.
		allies - The allies used to purchase the lord.
		pearls - Supplemental pearls to pay for the lord.
		affiliates - Output - A list of possible affiliated allies.
		return - Whether the payment is sufficient.
		"""
		total = pearls
		races = []
		lowest_value = allies[0].value
		for ally in allies:
			total += ally.value
			if (not ally.race in races):
				races.append(ally.race)
			if (ally.value < lowest_value):
				lowest_value = ally.value
				affiliates = [ally]
			elif (ally.value == lowest_value):
				affiliates.append(ally)
		
		return len(races) == lord.bubbles and total >= lord.cost
		
		
	def check_keys(self, player):
		"""Check to see if a player has 3 keys to claim a location.
		
		player - The player possibly claiming a location.
		"""
		if (player.get_total_keys() >= 3):
			chosen = player.choose_location(self.revealed_locations)
			if (chosen is Location):
				player.gain_location(chosen)
				self.revealed_locations.remove(chosen)
			elif (chosen == 1):
				player.locations.append(self.location_deck.pop())
			elif (chosen >= 2 and chosen <= 4):
				new_locations = []
				for _ in range(chosen):
					new_locations.append(self.location_deck.pop())
				chosen = player.choose_new_location(new_locations)
				if (chosen is Location):
					player.gain_location(chosen)


	def end_condition_met(self):
		"""Checks if the end conditions of the game are met.
		Either someone has 7 lords or no more lords can be drawn.
		"""
		return len(self.players[self.current_player].lords) >= 7 or \
		           self.cant_fully_refill_court
				
				
	def end_game(self):
		"""Ends the game and calculates everyone's score."""
		print "    ----Final Score:----"
		high_score = 0
		high_pearls = 0
		winners = []
		for player in self.players:
			score = player.calculate_score()
			print "%s:  %d influence points  %d pearls" % (player, score, player.pearls)
			if (score > high_score):
				winners = [player]
				high_score = score
				high_pearls = player.pearls
			elif (score == high_score):
				if (player.pearls > high_pearls):
					winners = [player]
					high_score = score
					high_pearls = player.pearls
				elif (player.pearls == high_pearls):
					winners.append(player)
					
		print ""
		if (len(winners) == 1):
			print "The winner is %s with %d influence points" % \
			       (winners[0], high_score)
		else:
			print "The winners are "
			for winner in winners:
				print winner
				print ", "
			print "with %d influence points" % (high_score)