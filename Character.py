import math
from util.d10 import roll, dam_roll, adv_roll, adv_roll_dam


class Character
	def __init__(self,character_name,lethal_soak,dex,martial_arts,health):
		self.dex = dex
		self.name = name
		self.soak = lethal_soak
		self.hp = health
		self.martial_arts = martial_arts
	def damage(self,damage):
		self.hp = self.hp - damage

