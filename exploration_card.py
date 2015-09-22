__author__ = 'Nate'

class ExplorationCard(object):
	"""Cards gotten when exploring the depths."""

	monster = 0
	ally = 1

	def __init__(self, type):
		self.type = type
		
class AllyCard(ExplorationCard):
	"""Ally cards are used to purchase power lord cards."""
	
	jellyfish = 0
	crab = 1
	seahorse = 2
	shellfish = 3
	squid = 4
	races = [jellyfish, crab, seahorse, shellfish, squid]
	race_strings = \
	  ["Jellyfish", "Crab", "Seahorse", "Shellfish", "Squid"]
	ally_card_value_distribution = \
	  [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5]

	def __init__(self, v, r):
		super(self.__class__, self).__init__(ExplorationCard.ally)
		self.value = v
		self.race = r
		
	def __str__(self):
		return "%s %d" % (AllyCard.race_strings[self.race], self.value)
		
	def __repr__(self):
		return "%s %d" % (AllyCard.race_strings[self.race], self.value)
		
	def __add__(self, other):
		return other + self.value
		
	def __radd__(self, other):
		return other + self.value
		
	def __lt__(self, other):
		return self.value < other
		
	def __le__(self, other):
		return self.value <= other
		
	def __eq__(self, other):
		return self.value == other
		
	def __ne__(self, other):
		return self.value != other
		
	def __gt__(self, other):
		return self.value > other
		
	def __ge__(self, other):
		return self.value >= other

		
class MonsterCard(ExplorationCard):
	"""Monster cards give you rewards when you fight them."""
	def __init__(self):
		super(self.__class__, self).__init__(ExplorationCard.monster)
		
	def __str__(self):
		return "Monster!"
		
	def __repr__(self):
		return "Monster!"