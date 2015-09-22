
from random import shuffle

class ThreatTrack(object):
	"""The threat track increases when players run from monsters.
	The higher the threat, the greater the reward when monsters are found.
	"""

	max = 5
	all_pearls = 0
	all_monster_tokens = 1
	pearls_and_monster_tokens = 2

	def __init__(self):
		
		self.counter = 0
		self.monster_token_pool = [4]*2 + [3]*9 + [2]*9
		shuffle(self.monster_token_pool)
		
	def get_reward(self, chosen_reward):
		pearls = 0 
		monster_tokens = []
		keys = 0
		
		if (0 == self.counter or 3 == self.counter):
			if (ThreatTrack.all_monster_tokens == chosen_reward):
				monster_tokens.append(self.monster_token_pool.pop())
			else:
				pearls = 1
		elif (1 == self.counter or 4 == self.counter):
			if (ThreatTrack.all_monster_tokens == chosen_reward):
				monster_tokens.append(self.monster_token_pool.pop())
				monster_tokens.append(self.monster_token_pool.pop())
			elif (all_pearls == chosen_reward):
				pearls = 2
			else:
				monster_tokens.append(self.monster_token_pool.pop())
				pearls = 1
		
		if (self.counter >= max):
			keys = 2
		elif (self.counter >= 2):
			keys = 1
			
		return pearls, monster_tokens, keys