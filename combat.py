import json
import TurnTracker
import pprint

#x = TurnTracker.TurnTracker([("Contras",11),("Galan",8),("Tyrell",7),("Voom",12),("Enemies",10)])

x = TurnTracker.TurnTracker([("Contras",11),("Galan",8),("Null Matron Sister",8),("Tyrell",7),("Voom",12),("Networked Nightsister",10)], verbose=True)

x.character_list = x.roll_join_combat(verbose=True)
x.run_combat()

