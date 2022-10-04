import math
import os, sys
from util.d10 import roll
from load_most_recent import load_most_recent_filestring, save_path
import datetime
import pandas as pd
from util.Colorprint import Colorprint

class Game:
	def __init__(self,character_list_of_tuples,**kwargs):
		pd.options.mode.chained_assignment = None
		self.verbose = kwargs.get('verbose',None)
		if self.verbose == True:
			self._welcome_print_seq()
		self.raster = 0
		self.crafting_columns = ["Unnamed","Player","CraftingType","ProjectName","Difficulty","TotalSuccesses","Content","RollsSoFar","RollTickType","Progress"]
		self.character_list = character_list_of_tuples
		self.acting_players = []
		self.action_stack = []
		self.attack_number = 0
		self.active_player = None
		self.world_options = {1:"Combat",2:"Explore",3:"Crafting",0:"Menu", -1:"Exit",4:"Inventory"}
		self.world_option = 0
		self.splash_string = '   |Star Wars: The Forcewinds of Iloa|  '
		self.main_menu_string = "\n[1] Combat\n[2] Explore\n[3] Crafting\n[4] Inventory\n[5] Equipment\n[-1] Exit\n>"
		self.state = "Menu"
		self.crafting_file = r'./csv/crafting_summary.csv'
		self.crafting_table = pd.read_csv(self.crafting_file,header=0, sep=',',dtype=list(zip(self.crafting_columns,[str,str,str,int,int,str,int,str,int])))
		self.load_world_options()
	def _adv(self):
		self.raster += 1
	# def _proc_world_input(self,i):
	# 	if (type(i) == int):
	# 		return True
	def _return_gamestate(self,i):
		self.state=self.world_options[i]
		if (self.state == "Menu"):
			return self.load_world_options()
		elif (self.state == "Combat"):
			self.character_list = self.roll_join_combat(verbose=True)
			self.run_combat()
		elif (self.state == "Explore"):
			self.run_explore()
		elif (self.state == "Crafting"):
			self.run_crafting()
		elif (self.state == "Inventory"):
			self.run_inventory()
		elif (self.state == "Exit"):
			os.system('cls||clear')
			exit()

	#game world running methods
	def load_world_options(self):
		os.system('cls||clear')
		while True:
			Colorprint(self.splash_string,color='bright_blue')
			i = int(input(self.main_menu_string))
			self._return_gamestate(i)

	#explore
	def run_explore(self):
		print(f'Player is Exploring....')
		while (self.state == "Explore"):
			p = int(input("[1] Search\n[2] Meditate\n[3] Train\n[-1] Exit\n>"))
			if (p == -1):
				break

	def run_inventory(self):
		print("Player is in Inventory...")
		while (self.state == "Inventory"):
			pprint.pprint('inventory')
			p=int(input("[1] Check Item\n[2] Add Item\n[-1] Exit\n>"))
			if (p == -1):
				break
	def run_equipment(self):
		print("Player is in Equipment...")
		while (self.state == "Equipment"):
			p=int(input("[1] Check Item\n[2] Add Item from Inventory\n[-1] Exit\n>"))
			if (p == -1):
				break	
	#crafting
	def run_crafting(self):
		def update_project(pdf,i):
			update_state = True
			while update_state:
				player, proj, prog, diff, sofar = pdf.at[i,'Player'],pdf.at[i,'ProjectName'],pdf.at[i,'Progress'],pdf.at[i,'Difficulty'],pdf.at[i,'RollsSoFar']
				print(f"You selected {player}s project on {proj} - {prog}% complete")
				pmt1 = int(input('\n[1] Make Rolls Towards Completing Project\n[2] Update Fields Manually\n[-1] Exit\n>'))
				if (pmt1==1):
					p112 = int(input(f"How many Rolls is {player} making?\n>"))
					p113 = int(input(f"What is {player}'s crafting die pool?\n>"))
					for i in range(p112):
						result = roll(p113)-diff
						print(f'{player} rolls {result} successes')
						pdf.at[i,'RollsSoFar'] = sofar + 1
						pdf.at[i,'Progress'] = (prog + result - diff) if (result-diff > 0) else prog
						pmt = int(input(f'{player} rolls {result} on a difficulty of {diff} for {result-diff if (result-diff > 0) else 0} threshold successes\n\n[1] Roll Again?\n[2] Show Project\n[-1] Exit.\n>'))
						if (pmt == 1):
							print(pdf)
						if (pmt==2):
							print(pdf.to_string())
						if (pmt == -1):
							print(pdf)
							break
						else:update_state = False
				if (pmt1==2):
					print(f'What field would you like to update?\n')
					pprint.pprint(list(zip((self.crafting_columns.index(c) for c in self.crafting_columns),self.crafting_columns))[1:])
					pmt2=int(input('\n>'))
					if (pmt2==1):
						pmt21 = input(f'What would you like {player} to be changed to?\n>')
				
				update_state = False
			self.crafting_table = pdf
			print('Returning to Crafting Menu...')
		def new_project(df):
			new_state = True
			while new_state:
				player=input('What Player is this Project for?\n>')
				craft_type=input('What Type of Object is being created (LoreTablet/Equipment)?\n>')
				proj_name=input('Enter a Name for the Project?\n>')
				diff=int(input('What is the Project Difficulty?\n>'))
				total_succ= int(input(f'What are the Total Successes needed to complete "{proj_name}"? Must be a positive Number\n>'))
				content=input("Breifly Describe this object?\n>")
				tick_type=input("How long should each roll take (Short - 15 min)")
				df = df.append({"Player":player,"CraftingType":craft_type,"ProjectName":proj_name,"Difficulty":diff,"TotalSuccesses":total_succ,"Content":content,"RollsSoFar":0,"RollTickType":tick_type,"Progress":0}, ignore_index=True)
				self.crafting_table = df
				new_state=False
			
		Colorprint(f'Player is Crafting....Loaded {self.crafting_file}',color='green')
		while (self.state == "Crafting"):
			p = int(input("[1] Show Existing Projects\n[2] New Project\n[-1] Exit\n>"))
			if (p==1):
				print(self.crafting_table.to_string())
				p1 = int(input("[1] Modify Project\n[-1] Exit\n>"))
				if (p1==1):
					p11 = int(input("Enter the index value of the project you wish to modify.\n>"))
					update_project(self.crafting_table,p11)
				if (p == -1):
					break
			if (p==2):
				os.system('cls||clear')
				new_project(self.crafting_table)
				break
			if (p == -1):
				print('Saving Crafting Table...')
				self.crafting_table.to_csv(self.crafting_file,sep=',',index=False)
				break
	#combat
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
	def run_combat(self):
		self._combat_print_seq()
		while (self.state == "Combat"):
			ontickplayernames = self.compile_acting_players_to_list()
			event = input("Tick:{} Turn:{} - Players Acting {}".format(self.tick(),self.turn(),self.compile_acting_players_to_list()))
			if type(event) != None:
				self._check_combat_input(event)
				if (self._check_combat_input(event) == "Exit"):
					os.system('cls||clear')
					return
			else:pass
			for player in self.character_list:
				if player[0] in ontickplayernames:
					#This is where we place a standardized "Action parser method that compiles available techniques for a player"
					try:
						#METHOD FOR EXPANDING LIST OF VALID ACTIONS - HEALTH BARS ETC.
						player_tick_adv=int(input('	ticks ahead to place {}? '.format(player[0])))
					except Exception as e:
						player_tick_adv = 1
						print('!#!#! {} is a BAD INPUT adv {} 1 tick #!#!#!#'.format(player_tick_adv,player[0]))
					player[2] = player[2]+player_tick_adv
				else:pass
			
			self._adv()
	def compile_acting_players_to_list(self):
		acting_players=[]
		for player in self.character_list:
			if player[2] == self.raster:
				#self.acting_players=self.acting_players.append(player[0])
				acting_players.append(player[0])
			else:pass
		return acting_players
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
	def _check_combat_input(self,event):
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
		if event == "e":
			return "Exit"
		else:
			return None
	def _welcome_print_seq(self):
		print('________________ForceWinds_________________')
		print('\nNote:\n-![Events marked with (*) have no error handling]!-\n')
	def _combat_print_seq(self):
		Colorprint('___________Roll Join Combat___________',color='red')
		print('[h] Help, [n] Add new Character, [s] Save, [e] Exit')