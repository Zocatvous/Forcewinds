import json
import TurnTracker
import pprint

x = TurnTracker.TurnTracker([('Contras',18),("Enemies",7),("Galan",16),("Voom",9)])
x.character_list = x.roll_join_combat(verbose=True)
x.run_combat()

