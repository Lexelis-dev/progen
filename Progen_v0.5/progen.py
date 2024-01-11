"""----------This is the progen v.0.5 documentation----------
Progen - Item Generator Script

Author: Lexelis
Date: 24/01/10
Version: 0.5

Description:
This script generates and displays equippable items for a player.



General inputs:
    
        
Version : 0.5
"""

#--------------------Import--------------------#
import os
import random
import colorama
colorama.init()

from classes import Player, Equippable
from functions import clear_screen, limited_choices, error, open_chest
#--------------------The CLI functions--------------------#

created_items = []
def main():
    # Initialisation
    global player, created_items
    open_chest(player,created_items,5)
    
    while True:
        ans = limited_choices(player,navigation_level)
        if ans is None:
            ans=""
        clear_screen()
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
    navigation_level = ["progen"]
    player = Player()
    
    main()
    
#Todo