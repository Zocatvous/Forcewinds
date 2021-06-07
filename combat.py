import json
import TurnTracker

x = TurnTracker.TurnTracker([('Galan',8),('Voom',9),('Contras',10),('Tyrell',8),('Draggy',7)])
x.character_list = x.join_combat()
print('Results of Join Combat [Name,Succ,Rastr]')
print(x.character_list)
while True:
	if x.raster ==0:
		pass
	else:
		newplayercheck = input('new characters to add? (y/n)')
		if newplayercheck == 'y':
			newcharnum = int(input('# of new characters: '))
			i=0
			for i in range(newcharnum):
				lst1 = str(input('Enter Character {}s name: '.format(i+1)))
				lst2 = int(input("{}'s Join Combat Die pool: ".format(lst1)))
				newplayertuple =(lst1,lst2)
				x._add_player(newplayertuple)
				print('New Character Added - {}'.format(x.character_list))
				i+=1
		else:pass
	#comment all above to While for old functionality
	playerlist = x.character_list
	ontickplayernames = x.compile_acting_players_to_list()
	input("Tick:{} Turn:{} - Players Acting {}".format(x.tick(),x.turn(),ontickplayernames))
	for player in x.character_list:
		if player[0] in ontickplayernames:
		#	print(x.character_list)
			# print('	Players Acting this tick: {}'.format(ontickplayernames))
			player_tick_adv=int(input('	ticks ahead to place {}? '.format(player[0])))
			# if type(player_tick_adv) != type(int())
			# 	print('bad input')
			player[2] = player[2]+player_tick_adv
		else:pass
	x._adv()