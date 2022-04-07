	
import TurnTracker
import SaberTester

#(name,speed,rate,acc,defe,dam,abil,dex)
#(attack_count,opponent_soak,opp_dv,speed)

def attacks(attacks):
	i=0
	Tracker = TurnTracker.TurnTracker([("Diametria",18)])
	Tracker.character_list = Tracker.roll_join_combat()
	x = SaberTester.SaberTester("Contrus's Lightsaber",3,4,10,5,19,7,7,verbose=False)
	#x = SaberTester.SaberTester("Galan's Lightsaber",5,3,6,5,66,5,5,verbose=False)
	#loop for TESTING dv VS
	thresholds = []
	dmg = []
	combat_length = 1000 #length in ticks of the test

	for i in range(combat_length):
		att = x._attack(attacks,15,4,x.speed)
		i+=1
		thresholds.append(att[1])
		dmg.append(att[2])
	print("{} with {} attacks".format(x.name,attacks))
	print(" Dam/Tick: {}\n Thresholds/tick: {}\n Damage per Attk: {}\n Thresholds Per Attk: {}".format(round(sum(dmg)/(x.speed*combat_length),3),round(sum(thresholds)/(x.speed*combat_length),3),sum(dmg)/combat_length,sum(thresholds)/combat_length))


def main():
	# attacks(7)
	# attacks(6)
	# attacks(5)
	# attacks(4)
	attacks(3)
	attacks(2)
	attacks(1)

if __name__ == "__main__":
	main()