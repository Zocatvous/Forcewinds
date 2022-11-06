import json
import TurnTracker
import pprint

#x = TurnTracker.TurnTracker([("Contras",11),("Galan",8),("Tyrell",7),("Voom",12),("Enemies",10)])

#x = TurnTracker.TurnTracker([("Voom",12),("Taid Bareth",8),("Diametria",22),("Nomi Bareth",18),("Galan",8),("Contras",8),("Battle Suits",10),("Lorgacos",12)], verbose=True)
x = TurnTracker.TurnTracker	([("Contras",14),("Enemies",8)])
x.character_list = x.roll_join_combat(verbose=True)
x.run_combat()