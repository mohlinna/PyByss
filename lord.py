__author__ = 'Nathan Mohling'

from exploration_card import AllyCard

class Lord(object):
	"""Lords are powerful entities that can you lots of influence points."""

	mage = 0
	soldier = 1
	farmer = 2
	merchant = 3
	politician = 4
	ambassador = 5
	guilds = [mage, soldier, farmer, merchant, politician, ambassador]

	def __init__(self, g, pr, v, c, b, k):
		self.guild = g
		self.primary_race = pr
		self.vps = v
		self.cost = c
		self.bubbles = b
		self.keys = k
		self.free = True
		
	def __str__(self):
		return self.__class__.__name__
		
	def __repr__(self):
		return self.__class__.__name__

#-----------------------------------------------

class MageLord(Lord):
	def __init__(self, v, c, b, k):
		super(MageLord, self).__init__(Lord.mage, AllyCard.jellyfish, v, c, b, k)

		
class TheShaman(MageLord):
	def __init__(self):
		super(self.__class__, self).__init__(5, 6, 3, 1)

		
class TheApprentice(MageLord):
	def __init__(self):
		super(self.__class__, self).__init__(9, 6, 3, 0)

		
class TheAlchemist(MageLord):
	def __init__(self):
		super(self.__class__, self).__init__(5, 7, 1, 1)

		
class TheOracle(MageLord):
	def __init__(self):
		super(self.__class__, self).__init__(5, 8, 2, 1)

		
class TheInvoker(MageLord):
	def __init__(self):
		super(self.__class__, self).__init__(8, 8, 1, 0)

		
class TheIllusionist(MageLord):
	def __init__(self):
		super(self.__class__, self).__init__(9, 10, 1, 0)

		
class TheMasterOfMagic(MageLord):
	def __init__(self):
		super(self.__class__, self).__init__(6, 10, 3, 1)

mage_lords = [TheShaman(), TheApprentice(), TheAlchemist(), TheOracle(), TheInvoker(), TheIllusionist(), TheMasterOfMagic()]

#-----------------------------------------------

class SoldierLord(Lord):
	def __init__(self, v, c, b, k):
		super(SoldierLord, self).__init__(Lord.soldier, AllyCard.crab, v, c, b, k)

		
class TheTamer(SoldierLord):
	def __init__(self):
		super(self.__class__, self).__init__(4, 6, 3, 1)

		
class TheJailer(SoldierLord):
	def __init__(self):
		super(self.__class__, self).__init__(7, 6, 3, 0)

		
class TheSeeker(SoldierLord):
	def __init__(self):
		super(self.__class__, self).__init__(7, 7, 2, 0)

		
class TheCommander(SoldierLord):
	def __init__(self):
		super(self.__class__, self).__init__(4, 8, 1, 1)

		
class TheHunter(SoldierLord):
	def __init__(self):
		super(self.__class__, self).__init__(6, 8, 2, 0)

		
class TheRecruiter(SoldierLord):
	def __init__(self):
		super(self.__class__, self).__init__(4, 10, 2, 1)

		
class TheAssassin(SoldierLord):
	def __init__(self):
		super(self.__class__, self).__init__(6, 10, 1, 0)

soldier_lords = [TheTamer(), TheJailer(), TheSeeker(), TheCommander(), TheHunter(), TheRecruiter(), TheAssassin()]

#-----------------------------------------------

class FarmerLord(Lord):
	def __init__(self, v, c, b, k):
		super(FarmerLord, self).__init__(Lord.farmer, AllyCard.seahorse, v, c, b, k)

		
class TheKeeper(FarmerLord):
	def __init__(self):
		super(self.__class__, self).__init__(6, 6, 3, 1)

		
class TheReaper(FarmerLord):
	def __init__(self):
		super(self.__class__, self).__init__(6, 7, 2, 1)

		
class TheShepherd(FarmerLord):
	def __init__(self):
		super(self.__class__, self).__init__(6, 8, 1, 1)

		
class TheMiller(FarmerLord):
	def __init__(self):
		super(self.__class__, self).__init__(10, 8, 2, 0)

		
class TheAquaculturalist(FarmerLord):
	def __init__(self):
		super(self.__class__, self).__init__(11, 9, 3, 0)

		
class TheLandowner(FarmerLord):
	def __init__(self):
		super(self.__class__, self).__init__(12, 10, 1, 0)

farmer_lords = [TheKeeper(), TheReaper(), TheShepherd(), TheMiller(), TheAquaculturalist(), TheLandowner()]

#-----------------------------------------------

class MerchantLord(Lord):
	def __init__(self, v, c, b, k):
		super(MerchantLord, self).__init__(Lord.merchant, AllyCard.shellfish, v, c, b, k)

		
class TheShipMaster(MerchantLord):
	def __init__(self):
		super(self.__class__, self).__init__(5, 6, 3, 1)

		
class TheShopKeeper(MerchantLord):
	def __init__(self):
		super(self.__class__, self).__init__(9, 6, 3, 0)

		
class TheSlaver(MerchantLord):
	def __init__(self):
		super(self.__class__, self).__init__(5, 8, 1, 1)

		
class ThePeddler(MerchantLord):
	def __init__(self):
		super(self.__class__, self).__init__(9, 8, 1, 0)

		
class TheLandlord(MerchantLord):
	def __init__(self):
		super(self.__class__, self).__init__(5, 10, 2, 1)

		
class TheTrader(MerchantLord):
	def __init__(self):
		super(self.__class__, self).__init__(9, 10, 3, 0)

merchant_lords = [TheShipMaster(), TheShopKeeper(), TheSlaver(), ThePeddler(), TheLandlord(), TheTrader()]

#-----------------------------------------------

class PoliticianLord(Lord):
	def __init__(self, v, c, b, k):
		super(PoliticianLord, self).__init__(Lord.politician, AllyCard.squid, v, c, b, k)

		
class TheOpportunist(PoliticianLord):
	def __init__(self):
		super(self.__class__, self).__init__(5, 6, 3, 1)

		
class TheDiplomat(PoliticianLord):
	def __init__(self):
		super(self.__class__, self).__init__(5, 8, 1, 1)

		
class TheSchemer(PoliticianLord):
	def __init__(self):
		super(self.__class__, self).__init__(6, 8, 3, 0)

		
class TheTreasurer(PoliticianLord):
	def __init__(self):
		super(self.__class__, self).__init__(5, 10, 2, 1)

		
class TheCorruptor(PoliticianLord):
	def __init__(self):
		super(self.__class__, self).__init__(6, 10, 1, 0)

		
class TheTraitor(PoliticianLord):
	def __init__(self):
		super(self.__class__, self).__init__(6, 12, 3, 0)

politician_lords = [TheOpportunist(), TheDiplomat(), TheSchemer(), TheTreasurer(), TheCorruptor(), TheTraitor()]

#-----------------------------------------------

class AmbassadorLord(Lord):
	def __init__(self, v, c, b, k):
		super(AmbassadorLord, self).__init__(Lord.ambassador, None, v, c, b, k)

		
class TheElder(AmbassadorLord):
	def __init__(self):
		super(self.__class__, self).__init__(3, 10, 5, 3)

		
class TheSage(AmbassadorLord):
	def __init__(self):
		super(self.__class__, self).__init__(4, 10, 5, 3)

		
class TheHermit(AmbassadorLord):
	def __init__(self):
		super(self.__class__, self).__init__(5, 10, 5, 3)

ambassador_lords = [TheElder(), TheSage(), TheHermit()]

#-----------------------------------------------

lords = mage_lords + soldier_lords + farmer_lords + merchant_lords + politician_lords + ambassador_lords
