import json
import TurnTracker

# with open("./config/sheet.json","r") as j:
# 	print(json.loads(j))

x = TurnTracker.TurnTracker([('Galan',8),('Voom',9),('Contras',10),('Tyrell',8),('Draggy',7)])
x.character_list = x.join_combat()
print('Results of Join Combat [Name,Succ,Rastr]')
print(x.character_list)
while True:
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
	input('new characters to add?')
	x._adv()