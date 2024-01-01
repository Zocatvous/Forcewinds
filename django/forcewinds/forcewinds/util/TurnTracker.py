import math
import os
from .d10 import roll
import datetime
import sys
#do I need to split the "internal raster number from the property that returns the current tick which would be a mod 7 of that raster number"




#This classes responsibility is ONLY to track what turn or tick we are at and to handle anything related to player/NPC position in the lineup (NOTHING ELSE)
class TurnTracker():
	def __init__(self):
		self.raster = 0

	def _adv_tick(self):
		self.raster += 1

	#list all propert
	#for returning whatever the current turn is 
	@property
	def current_turn(self):
		return math.floor(self.raster/7) + 1
	@property
	def current_tick(self):
		return math.floor(self.raster % 7)

	






	#methods



	#a method for rolling (maybe this should be a different object) 