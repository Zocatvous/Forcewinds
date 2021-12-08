import json
import TurnTracker
import pprint

x = TurnTracker.TurnTracker([("Someone else",12)("Voom",15),('Mace Windu',21)])
x.character_list = x.roll_join_combat(verbose=True)
x.run_combat()

