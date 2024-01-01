from django.db import models
from .util.d10 import roll

class Technique(models.Model):
		#array of comma delimited stings
	cost = models.JSONField()
		#array of comma delimited stings
	minimums = models.JSONField()
		#array of comma delimited stings
	keywords = models.CharField(max_length=255)
	duration = models.IntegerField()
	activation_time = models.IntegerField()
	prerequisites = models.JSONField()
	effect = models.TextField()

class ForcePower(models.Model):
	prereqs = models.CharField(max_length=255)
	cost = models.JSONField()
	#array of comma delimited stings
	die_pool = models.CharField()
	activation_time = models.IntegerField()
	targets = models.CharField(max_length=255)
	defenses = models.CharField(max_length=255)
	power_range = models.CharField(max_length=255)
	effect = models.TextField()

class Character(models.Model):
	name= models.CharField()
	strength = models.IntegerField()
	dexterity = models.IntegerField()
	stamina = models.IntegerField()
	charisma = models.IntegerField()
	manipulation = models.IntegerField()
	appearance = models.IntegerField()
	perception = models.IntegerField()
	intelligence = models.IntegerField()
	wits = models.IntegerField()
	xp = models.IntegerField()
	marksman = models.IntegerField()
	martial_arts = models.IntegerField()
	melee = models.IntegerField()
	thrown = models.IntegerField()
	war = models.IntegerField()
	integrity = models.IntegerField()
	performance = models.IntegerField()
	presence = models.IntegerField()
	resistance = models.IntegerField()
	survival = models.IntegerField()
	science = models.IntegerField()
	investigation = models.IntegerField()
	lore = models.IntegerField()
	medicine = models.IntegerField()
	astrogation = models.IntegerField()
	athletics = models.IntegerField()
	awareness = models.IntegerField()
	dodge = models.IntegerField()
	larceny = models.IntegerField()
	stealth = models.IntegerField()
	bureaucracy = models.IntegerField()
	linguistics = models.IntegerField()
	drive = models.IntegerField()
	pilot = models.IntegerField()
	socialize = models.IntegerField()
	computers = models.IntegerField()
	engineering = models.IntegerField()
	craft = models.IntegerField()
	sense = models.IntegerField()
	alter = models.IntegerField()
	control = models.IntegerField()
	alignment = models.CharField(max_length=100)
	force_sensitivity = models.IntegerField()
	shii_cho = models.IntegerField()
	makashi = models.IntegerField()
	soresu = models.IntegerField()
	ataru = models.IntegerField()
	djem_so = models.IntegerField()
	niman = models.IntegerField()
	juyo = models.IntegerField()
	powers = models.ManyToManyField(ForcePower)
	techniques = models.ManyToManyField(Technique)
	willpower = models.IntegerField()
	hitpoints = models.IntegerField()


	@property
	def hp(self):
		# Implement calculation for hp
		pass
	
	@property
	def aitizen(self):
		# Implement calculation for aitizen
		pass
	
	@property
	def fp(self):
		# Implement calculation for fp
		pass