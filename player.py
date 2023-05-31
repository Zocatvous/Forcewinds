from util.d10 import roll
import os

class Player:
	_base_dir = os.path.dirname(os.path.abspath(__file__))
	_player_list_obj = {"galan":"","voom":"","contrus":"",}
	_player_file_path = os.path.join(_base_dir, "json",)

	def __init__(self,player="galan"):
		self.player_obj = 
		self.hp = 

	@classmethod
	def _read_json(cls, file_name, player_name):
		with open(file_name, 'r') as f:
			return json.load(f)