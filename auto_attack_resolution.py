from util.d10 import roll, dam_roll, adv_roll, adv_roll_dam
import pprint
#Create templates for each of the characters and potentially for the enemies that attack.
#Probably need them to be at least mostly on the fly, 

#number of attacks
#targeting whom
#exact number of flurries and of how many attacks()
#final report on damage

#which ones can I block?
#need to see which of all the attacks he can block, so i need a method that lays out each of the thresholds.


VOOM ={"ddv":5,"pdv":10,"soak":10}
GALAN ={"ddv":6,"pdv":14,"soak":11}
TYRELL = {}
CONTRAS = {}

def _flurry(flurry_num,accuracy_pool,num,character_to_target):
	t=[]
	i,j = 0
	for j in range(0,num):
		for i in range(0,flurry_num):
			roll_result = roll(accuracy_pool-(flurry_num+i))
			t.append(roll_result)
	return sort(t)

def _attack(accuracy_pool:int,num:int,character_to_target:dict,dice_of_damage:int):
	i=0
	raw = []
	#gather all attacks into a list and print them to screen. then assign id's to each of the attacks and delete them from the incoming list and THEN roll the damage
	for i in range(0,num):
		raw.append(roll(accuracy_pool))
	return raw

def _resolve_defense(character,list_of_damage,dice_of_damage):
	result=[]
	blkcnt=0
	dgcnt=0
	for i in range(0,len(list_of_damage)):
		if list_of_damage[i] > character['ddv'] and list_of_damage[i] > character['pdv']:
			result.append(list_of_damage[i])
		else:
			dbool = input('Dodge,Block,Other Def against attack w/ {} succ? (0/1/2)')
			if dbool == 0:
				dgcnt+=1
				list_of_damage.pop(i)
			elif dbool ==1:
				blkcnt+=1
				list_of_damage.pop(i)
			elif dbool == 2:
				list_of_damage.pop(i)
		damage = dam_roll((threshold_succ+dice_of_damage)-character['soak']) if threshold_succ > 0 else 0
		result.append(damage)
	return sum(result)

	if dbool == 0:
		threshold_succ = 0 if roll_result-(character_to_target['ddv']-i) <= 0 else roll_result-character_to_target['ddv']
		damage = dam_roll((threshold_succ+dice_of_damage)-character_to_target['soak']) if threshold_succ > 0 else 0
		r.append(damage)
	else:
		threshold_succ = 0 if roll_result-(character_to_target['pdv']-i) <= 0 else roll_result-character_to_target['pdv']
		damage = dam_roll((threshold_succ+dice_of_damage)-character_to_target['soak']) if threshold_succ > 0 else 0
		r.append(damage)




def main():
	#GALAN
	attacks = _flurry(3,10,1,GALAN) + _flurry(2,10,2,GALAN) + _attack(10,6,GALAN)
	print(sort(attacks))



if __name__ == "__main__":
	main()
	

