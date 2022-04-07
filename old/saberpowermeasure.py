import pandas as pd
import math
from util.d10 import roll, dam_roll, adv_roll, adv_roll_dam
import TurnTracker

class SaberTester:
	def __init__(self,name,speed,rate,acc,defe,dam,abil,dex):		
		self.ability= abil
		self.speed = speed
		self.rate = rate
		self.accuracy = acc #this is the combined accuracy pool of the weapon = abil+acc+
		self.damage = dam #this is the damage of the offensive attack in lethal damage
		self.defense_val = defe #this is the DV of the opponent
		self.name = name
		self.attack=self.ability+self.accuracy+dex
		print('_______SaberTester Init w/ {}_______'.format(name))
		print('Speed:{}\nRate:{}\nAccuracy:{}\nDV:{}\nDam:{}\nMartial Arts:{}\nTotal Attack Die Pool:{}'.format(self.speed,self.rate,self.accuracy,self.defense_val,self.damage,self.ability,self.attack))
	def _attack(self,attack_count,opponent_soak,opp_dv,speed):
		#print(' attacking Opp. DV:{} Soak:{}'.format(self.defense_val,opponent_soak))
		i=0
		for i in range(0,attack_count):
			roll_result = roll(self.attack-(attack_count+i))
			threshold_succ = 0 if roll_result-(opp_dv-i) <= 0 else roll_result-self.defense_val
			damage = dam_roll((threshold_succ+self.damage)-opponent_soak) if threshold_succ > 0 else 0
			print('Attack {}:Rolled {} successes w/ {} Threshold {} Damage '.format(i+1,roll_result,threshold_succ,damage))
			i+=1
		return [roll_result,threshold_succ,damage,speed]
	def profile_weapon(num_enemies):
		pass
		#return [roll_result,threshold_succ,damage]
		#this method only returns the damage resulting from an attack.


def main():
	i=0
	j=0
	Tracker = TurnTracker.TurnTracker([("Diametria",18)])
	Tracker.character_list = Tracker.roll_join_combat()
	x = SaberTester("Normal Lightsaber",5,3,6,5,20,10,20)
	#loop for TESTING dv VS
	for i in range(40):
		Tracker._auto_combat(x._attack(1,0,0,x.speed),40,verbose=True)
	
if __name__ =="__main__":
	main()


