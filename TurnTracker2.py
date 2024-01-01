import math
import datetime
from util.d10 import roll

class TurnTrackerTwo:
    def __init__(self, characters, verbose=False):
        self.verbose = verbose
        self.raster = 0
        self.character_list = sorted([(name, roll(pool), 0) for name, pool in characters], key=lambda x: -x[1])
        
    def _adv(self):
        self.raster += 1
        
    def turn(self):
        return math.ceil(self.raster / 7)
    
    def tick(self):
        return self.raster % 7 + 1
    
    def roll_join_combat(self):
        results = [(name, roll(pool), 0) for name, pool, _ in self.character_list]
        self.character_list = sorted(results, key=lambda x: -x[1])
        return self.character_list
    
    def compile_acting_players_to_list(self):
        return [name for name, _, raster in self.character_list if raster == self.raster]
    
    def _add_player(self, name, pool):
        if self.raster == 0:
            return
        ri = roll(pool)
        rc = self.character_list[0][1]
        new_player_acting_raster = self.raster + max(0, rc - ri)
        new_player_tuple = (name, ri, new_player_acting_raster)
        self.character_list.append(new_player_tuple)
        self.character_list.sort(key=lambda x: -x[1])
        if self.verbose:
            print(f"New character added: {name}")
            print(self.character_list)
    
    def _check_inputs(self, event):
        if event == 'n':
            newcharnum = int(input('# of new characters: '))
            for i in range(newcharnum):
                name = str(input(f"Enter character {i+1}'s name: "))
                pool = int(input(f"{name}'s Join Combat Die pool: (+num) "))
                self._add_player(name, pool)
        elif event == 'h':
            with open('./text/help_string.txt') as f:
                print(f.read())
            input("** Press Enter to Proceed... **")
        elif event == 's':
            with open(f"./text/saves/save_{datetime.datetime.now().strftime('%Y%h%d_%-H%M.txt')}", "w") as f:
                f.write(str(self.character_list))
            print(f"Made savepoint @ save_{datetime.datetime.now().strftime('%Y%h%d_%-H%M.txt')}")
        else:
            pass
    
    def run_combat(self):
        while True:
            ontickplayernames = self.compile_acting_players_to_list()
            event = input(f"Tick: {self.tick()} Turn: {self.turn()} - Players Acting {ontickplayernames}")
            self._check_inputs(event)
            for name, _, raster in self.character_list:
                if name in ontickplayernames:
                    try:
                        player_tick_adv = int(input(f"Ticks ahead to place {name}? "))
                    except ValueError:
                        player_tick_adv = 1
                        print(f"Invalid input, defaulting to 1 tick.")
                    self.character_list = [(n, r, r + player_tick_adv if n == name else r) for n, r, _ in self.character_list]
            self._adv()
