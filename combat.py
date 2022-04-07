import json
import TurnTracker
import pprint

x = TurnTracker.TurnTracker([("Contras",10),("Galan",8),("Tyrell",7),("Voom",12),("Enemies",10)])
x.character_list = x.roll_join_combat(verbose=True)
x.run_combat()

