import json
from TurnTracker import TurnTracker
# from TurnTracker2 import TurnTrackerTwo
import pprint

#x = TurnTracker.TurnTracker([("Contras",11),("Galan",8),("Tyrell",7),("Voom",12),("Enemies",10)])

#x = TurnTracker.TurnTracker([("Voom",12),("Taid Bareth",8),("Diametria",22),("Nomi Bareth",18),("Galan",8),("Contras",8),("Battle Suits",10),("Lorgacos",12)], verbose=True)

#x = TurnTracker.TurnTracker([("Voom",12),("Enemies",10),('Contras',14),('Galan',8)])

#x = TurnTracker([("Corrin",16),("Vitiate",29),("Galan",8),("Miarta",10),("Arctus",20),("Contrus",14)])

x = TurnTracker([("Galan",8),("Voom",13),("Contras",14),("Enemies",10)])

x.character_list = x.roll_join_combat()
x.run_combat()

# Per+Science 5
# Perc+Eng 5
# Int+Science 5
# Int+Eng 7
# 1WP 
# Wits+Medicine 7