import json



class Character():
	def __init__():
		self.attr = json.load(open("./config/sheet.json","r"))["attr"]
		self.skills = json.load(open("./config/sheet.json","r"))["skills"]
		self.techniques = json.load(open("./config/techniques.json","r"))["techniques"]
		self.status = "Alive"
		self.stance_bool = False

	def set_atr(attr_to_set,value):
		pass

	def set_dmg(attr,value,type):
		pass


print(Character().attr)