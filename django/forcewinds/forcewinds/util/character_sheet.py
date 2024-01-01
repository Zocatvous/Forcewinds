import json
from util.d10 import *




class Character():	
	def __init__(self):
		self.attr = json.load(open("./config/sheet.json","r"))["attr"]
		self.skills = json.load(open("./config/sheet.json","r"))["skills"]
		self.techniques = json.load(open("./config/techniques.json","r"))["techniques"]
		self.status = "Alive"

	def set_atr(attr_to_set,value):
		pass

	def set_dmg(attr,value,type):
		pass	



print(Character().attr)