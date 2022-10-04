import math
import os
from util.d10 import roll
from load_most_recent import load_most_recent_filestring, save_path
import datetime

class TurnTracker:
	def __init__(self,character_list_of_tuples,**kwargs):
		self.verbose = kwargs.get('verbose',None)
		if self.verbose == True:
			self._welcome_print_seq()
		else:pass	
		self.raster = 0
		self.character_list = character_list_of_tuples
		self.acting_players = []
		self.action_stack = []
		self.attack_number = 0
		self.active_player = None
	def _adv(self):
		self.raster += 1 
	def turn(self):
		return math.floor(self.raster/7) +1
	def tick(self):
		return (self.raster % 7) + 1

	def roll_join_combat(self,**kwargs):		
		
		verbose = kwargs.get('verbose',None)		
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
				player[2] == 6
			else:pass
		self.character_list=sorted_players_list
		if verbose == True:
			print('Results of Join Combat [Name,Succ,Rastr]')
			print(self.character_list)
		else:pass
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

#TODO (JAKE) makeing a loading savepoint method
	def _load_savepoint(self):
		print(f"Loading savepoint ({load_most_recent_filestring()})")
	def _make_savepoint(self):
		with open(f"./text/saves/save_{datetime.datetime.now().strftime('%Y%h%d_%-H%M.txt')}","w") as f:f.write(str(self.character_list))
		f.close()
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
			print('	New Character Added - {}'.format(self.character_list))
	def _clear_action_stack(self):
		self.action_stack == []
	def _check_inputs(self,event):
		#Method to be run at the top of the while loop for combat implementation - terminal usage primarily
		#add a new character midcombat
		if event == 'n':
			newcharnum = int(input('# of new characters: '))
			i=0
			for i in range(newcharnum):
				lst1 = str(input('	*Enter Character {}s name: (str) '.format(i+1)))
				lst2 = int(input("	*{}'s Join Combat Die pool: (+num) ".format(lst1)))
				newplayertuple =(lst1,lst2)
				self._add_player(newplayertuple)		
				i+=1
		else:pass
		if event == "d":
			print('#Placeholder for Delete Method#')		
		if event == 'h':
			with open('./text/help_string.txt',"r+") as f:print(f.read())
			input("** Press Enter to Proceed... **")
			f.close()
		if event == 'a':
			player_tech = self.get_player_techniques(self.active_player)
			#pprint active techniques on player
		if event == 's':
			self._make_savepoint()
			print(f"Made savepoint @ save_{datetime.datetime.now().strftime('%Y%h%d_%-H%M.txt')}")
		if event == "l":
			self._load_savepoint()
		else:
			return None

	def run_combat(self):
		while True:
			ontickplayernames = self.compile_acting_players_to_list()
			event = input("Tick:{} Turn:{} - Players Acting {}".format(self.tick(),self.turn(),self.compile_acting_players_to_list()))
			if type(event) != None:
				self._check_inputs(event)
			else:pass
			for player in self.character_list:
				if player[0] in ontickplayernames:
				#	print(x.character_list)
					# print('	Players Acting this tick: {}'.format(ontickplayernames))
					try:
						#METHOD FOR EXPANDING LIST OF VALID ACTIONS - HEALTH BARS ETC.
						player_tick_adv=int(input('	ticks ahead to place {}? '.format(player[0])))
					except Exception as e:
						player_tick_adv = 1
						print('!#!#! {} is a BAD INPUT adv {} 1 tick #!#!#!#'.format(player_tick_adv,player[0]))
					player[2] = player[2]+player_tick_adv
				else:pass
			self._adv()
		#delete a character from turn order midcombat
		#pprint character list with indexes 
		#specify the index of the character to be deleted.
		#re-pprint the character list

	def _auto_combat(self,attack_obj,ticks_of_combat,**kwargs):
		verbose = kwargs.get('verbose',None)
		accuracy_roll = 0
		threshold = 0
		dmg = 0
		total_damage = []
		thresholds = []
		self.character_list = self.roll_join_combat()
		for i in range(ticks_of_combat):
			ontickplayernames = self.compile_acting_players_to_list()
			for player in self.character_list:
				if player[0] in ontickplayernames:
					self.active_player = player
				#	print(x.character_list)
					# print('	Players Acting this tick: {}'.format(ontickplayernames))
					try:
						player_tick_adv=attack_obj[3]
						#self.attack_number = input('how many times does {} attack?'.format())
						accuracy_roll = attack_obj[0]
						threshold = attack_obj[1]
						dmg = attack_obj[2]
						if verbose == True:
							print('Tick {} Turn {}: {} Succ, {} Dam'.format(self.tick(),self.turn(),accuracy_roll,dmg))
					except Exception as e:
						print('!#!#! {} is a BAD INPUT adv {} 1 tick #!#!#!#'.format(player_tick_adv,player[0]))
						player_tick_adv = 1
					player[2] = player[2]+player_tick_adv
				else:pass
			total_damage.append(dmg)
			thresholds.append(threshold)
			self._adv()
		misses = []
		for item in total_damage:
			if item == 0:
				misses.append(1)
		return [thresholds,misses,total_damage]

	def _welcome_print_seq(self):
		print('________________TurnTracker_________________')
		print('\nNote:\n-![Events marked with (*) have no error handling]!-\n')
