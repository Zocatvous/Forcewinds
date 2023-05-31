from d10 import roll, dam_roll
from colorama import Fore, Style


weapon_acc = 17
weapon_dam = 16
channel = 0

opp_dv = 10
opp_soak = 1

def strike(weap_name,strike_count, weapon_acc, weapon_dam, opp_dv, opp_soak, heavy=False):
	total_damage = 0
	#strike_count = int(input(f'How many strikes with {weapon_acc}Acc {weapon_dam}Dam? >'))
	print(f"{Fore.YELLOW}\nStriking w/ [{Fore.CYAN}{weap_name}{Fore.YELLOW}]{Style.RESET_ALL}")
	channel = int(input(f'what level will you be channelling? >'))
	auto_succ_acc = int(input(f'How many Auto-successes to accuracy? >'))
	auto_succ_dam = int(input(f'How many Auto-successes to damage? >'))

	xtr_acc_dice = int(input(f'Extra Dice for Acc? >'))
	xtr_dam_dice = int(input(f'Extra Dice for Dam? >'))

	print("###########################")
	print(f'{Fore.CYAN}{strike_count} Striking Attack(s){Style.RESET_ALL} w/ {Fore.GREEN}{weapon_acc+channel}{Style.RESET_ALL} Dice!')
	print("###########################")

	for i in range(0,strike_count):
		damage = 0
		penalty = 0 if (strike_count==1) else strike_count+i
		#print(f'acc{weapon_acc}+chan{channel}-pen{penalty}')
		print(f'Rolling {weapon_acc-penalty+channel} dice for attack {i+1}')
		successes = roll(weapon_acc+channel-penalty) + auto_succ_acc
		threshold = successes-(opp_dv-i)

		print(f'	Attack {i+1} rolled {successes} successes against (DV {opp_dv-i}) {Fore.CYAN}({successes-(opp_dv-i)} Threshold!){Style.RESET_ALL}')
		if (successes+auto_succ_acc) > (opp_dv-i):
			damage_pool = successes+(weapon_dam-opp_soak) if (heavy==True) else (weapon_dam-opp_soak)+threshold
			print(f'		DamageRoll {i+1} is ({damage_pool}) dice after ({opp_soak}) soak w/ ({weapon_dam}) + {threshold} threshold)')
			damage = dam_roll(damage_pool) + auto_succ_dam	
			colored_damage = f'{Fore.RED}{damage} damage!{Style.RESET_ALL}'
			print(f'  		{colored_damage}')
			total_damage += damage
		elif opp_soak>damage: 
			print(f'{Fore.YELLOW}	**DEFENDED**{Style.RESET_ALL} Rolled({successes}) {abs(successes-(opp_dv-i))} short of (DV {opp_dv-i})')
		if i == strike_count-1:
			print(f'({Fore.RED}{total_damage}{Style.RESET_ALL}) TOTAL DAMAGE')


if __name__ == '__main__':
	# uncomment for VOOM
	# strike("Blue/Red",3, 17,16,10,1)
	# #bareth
	# strike("Bareth",4,46,77,10,1)
	# #Racor
	# strike("Rancor",8, 27,22,10,1)
	# #Typho
	# strike("Typhe",1, 19, 19,10,1)
	# #Contrus
	# strike("Contrus",4,25,30,10,1)
	
	#normal Anakin Strike
	strike("Anakin Strike",1, 95, 125, 10, 1, heavy=True)