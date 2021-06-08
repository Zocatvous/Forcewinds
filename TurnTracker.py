import math
from util.d10 import roll

class TurnTracker:
	def __init__(self,character_list_of_tuples):
		self.raster = 0
		self.character_list = character_list_of_tuples
		self.acting_players = []
		self.action_stack = []
	def _adv(self):
		self.raster += 1 
	def turn(self):
		return math.floor(self.raster/7) +1
	def tick(self):
		return (self.raster % 7) + 1

	def join_combat(self):
		results=[]
		raster_indexed_players = []
		def get_player_roll(playerlist):
			return playerlist[1]
		for player in self.character_list:
			name = player[0]
			dpool = player[1]
			ri = roll(dpool)
			results.append([name,ri])
		sorted_players_list = sorted(results,key=get_player_roll,reverse=True)
		i=0
		rc=sorted_players_list[0][1]
		for player in sorted_players_list:
			player.append(rc-player[1])
		for player in sorted_players_list:
			if player[2] > 6:
				player[2] = 6
			else:pass
		self.character_list=sorted_players_list
		return sorted_players_list
#gets a list of players acting at the current raster val
	def compile_acting_players_to_list(self):
		acting_players=[]
		for player in self.character_list:
			if player[2] == self.raster:
				#self.acting_players=self.acting_players.append(player[0])
				acting_players.append(player[0])
			else:pass
		return acting_players

#add some new player by tuple NEEDS TO HAVE A CORRECT TUPLE! add a checkmethod
	def _add_player(self,new_player_tuple):
		def get_player_roll(playerlist):
			return playerlist[1]
		if self.raster == 0:
			pass
		else:
			name = new_player_tuple[0]
			dpool = new_player_tuple[1]
			ri = roll(dpool)
			#input('ri for {} is {}'.format(name,ri))
			# new_player_acting_raster = self.raster 
			#grab the RC from the top player and assign new players raster val
			rc=self.character_list[0][1]
			#print('Current RC from {} is {}'.format(self.character_list[0][0],self.character_list[0][1]))
			#input('New Char Join Succ is {} so rc-ri= {}'.format(ri,rc-ri))
			if rc-ri <= 0: 
				new_player_acting_raster = self.raster
			else:
				new_player_acting_raster = self.raster + (rc-ri)
			#diff the rc from the new players join battle roll and round up to the raster if they exceed the best players roll
			new_player_tuple = [name,ri,new_player_acting_raster]
			#add new character to the list and resort the character_list attribute
			self.character_list.append(new_player_tuple)
			#sort the new char list
			self.character_list = sorted(self.character_list,key=get_player_roll,reverse=True)

	def _clear_action_stack(self):
		self.action_stack == []

	def _process_attacks(self):
		for attack in self.action_stack:
			pass



