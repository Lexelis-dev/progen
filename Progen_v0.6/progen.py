"""----------This is the progen v.0.6 documentation----------
Progen - Item Generator Script

Author: Lexelis
Date: 24/01/11
Version: 0.6

Description:
    Does nothing
        
Version : 0.6
"""

#--------------------Import--------------------#
import curses
from curses import wrapper

from classes import Player, Equippable
from functions import limited_choices, error, open_chest
#--------------------The main function--------------------#
def main(stdscr):
    # Initialisation
    # Hide the cursor
    curses.curs_set(0)
    curses.resize_term(40, 80)
    stdscr.clear()
    
    
    navigation_level = ["progen"]
    player = Player()
    open_chest(stdscr,player,5)
    stdscr.refresh()
    
    while True:
        ans = limited_choices(player,navigation_level)
        if ans is None:
            ans=""
        # Seperate the input words into a list
        
        # Quit the game, whitout saving!
        if ans == "exit.":
            break
        
        elif ans == "close":
            if navigation_level[-1] in end_correct:
                del navigation_level[-1]
        
        elif ans in end_correct:
            # The last level is already a menue
            if navigation_level[-1] in end_correct:
                navigation_level[-1]=ans
                
            #The player opens a menue
            else:
                navigation_level.append(ans)
        
    return player
#--------------------Dictionaries--------------------#
# The menues
end_correct = {
    "inventory":["inv"],
    "player":["plr"],
    "stats":None
}
    
current_floor=0
current_room=0
    
# Initialise if the script is executed
if __name__ == "__main__":
    wrapper(main)
    
#Todo