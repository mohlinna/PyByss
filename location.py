__author__ = 'Nathan Mohling'

from exploration_card import AllyCard
from lord import Lord, MageLord, SoldierLord, FarmerLord, MerchantLord, PoliticianLord

class Location(object):
	"""Locations are acquired with keys and are a source of high Influence Points."""
	
	def get_vps(self, player):
		return 0
		
		
class TheSanctuary(Location):

	def get_vps(self, player):
		
		return len(player.affiliates[AllyCard.jellyfish]) + 4
		
		
class TheChasm(Location):

	def get_vps(self, player):
		
		return len(player.affiliates[AllyCard.crab]) + 5
		
		
class TheSargassoFields(Location):

	def get_vps(self, player):
		
		return len(player.affiliates[AllyCard.seahorse]) + 3
		
		
class NestOfGiantClams(Location):

	def get_vps(self, player):
		
		return len(player.affiliates[AllyCard.shellfish]) + 3
		
		
class OceanicSenateAssembly(Location):

	def get_vps(self, player):
		
		return len(player.affiliates[AllyCard.squid]) + 4
		
		
class TheChamberOfAllies(Location):

	def get_vps(self, player):
		
		vps = 3
		
		for racePile in player.affiliates:
			if (racePile):
				vps += min(racePile)
			
		return vps
		
		
class TheCoralBarrier(Location):

	def get_vps(self, player):
		
		vps = 20
		
		for racePile in player.affiliates:
			vps -= len(racePile)
			
		return vps
		
		
class HydrozaReserves(Location):

	def get_vps(self, player):
		
		vps = 6
		for lord in player.lords:
			if lord is MageLord:
				vps += 2
				
		return vps
		
		
class TheBarracks(Location):

	def get_vps(self, player):
		
		vps = 7
		for lord in player.lords:
			if lord is SoldierLord:
				vps += 2
				
		return vps
		
		
class SargassoSilos(Location):

	def get_vps(self, player):
		
		vps = 5
		for lord in player.lords:
			if lord is FarmerLord:
				vps += 2
				
		return vps
		
		
class TheDockworks(Location):

	def get_vps(self, player):
		
		vps = 5
		for lord in player.lords:
			if lord is MerchantLord:
				vps += 2
				
		return vps
		

class Parliament(Location):

	def get_vps(self, player):
		
		vps = 6
		for lord in player.lords:
			if lord is PoliticianLord:
				vps += 2
				
		return vps
		

class TheAbyss(Location):

	def get_vps(self, player):
		
		guilds_covered = []
		for guild in Lord.guilds:
			guilds_covered.append(0)
		
		for lord in player.lords:
			guilds_covered[lord.guild] = 1
			
		return 2 * sum(guilds_covered)
		

class TheClosedTower(Location):

	def get_vps(self, player):
		
		vps = 0
		for lord in player.lords:
			if lord.keys >= 1:
				vps += 3
				
		return vps
		

class TheLostTower(Location):

	def get_vps(self, player):
		
		vps = 0
		for lord in player.lords:
			if lord.keys == 0:
				vps += 3
				
		return vps
		

class TheDepths(Location):

	def get_vps(self, player):
		
		weakest_lord_points = player.lords[1].vps
		for lord in player.lords:
			if lord.vps < weakest_lord_points:
				weakest_lord_points = lord.vps
				
		return weakest_lord_points * 2
		

class TheThroneRoom(Location):

	def get_vps(self, player):
		
		strongest_lord_points = player.lords[1].vps
		for lord in player.lords:
			if lord.vps > strongest_lord_points:
				strongest_lord_points = lord.vps
				
		return strongest_lord_points
		

class TheJail(Location):

	def get_vps(self, player):
		
		return 15 - len(player.lords)
		

class CityOfMirrors(Location):

	def get_vps(self, player):
		
		return 0
		

class BlackSmokers(Location):

	def get_vps(self, player):
		
		return 0
		
locations = \
  [TheSanctuary(), TheChasm(), TheSargassoFields(), NestOfGiantClams(), \
   OceanicSenateAssembly(), TheChamberOfAllies(), TheCoralBarrier(), \
   HydrozaReserves(), TheBarracks(), SargassoSilos(), TheDockworks(), \
   Parliament(), TheAbyss(), TheClosedTower(), TheLostTower(), TheDepths(), \
   TheThroneRoom(), TheJail(), CityOfMirrors(), BlackSmokers()]