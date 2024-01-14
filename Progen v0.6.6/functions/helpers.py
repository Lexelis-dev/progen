import curses

from constants import Color
from .shared_functions import full_stat, full_item_print, character_print
        
def limited_choices(stdscr,player,navigation_level,ans):
    if navigation_level[-1] == "progen":
        if ans == "1" :
            return "inventory"
        elif ans == "2" :
            return "player"
    elif navigation_level[-1] == "inventory":
        if ans == "1":
            return "close"
        elif ans == "2":
            return "player"
    elif navigation_level[-1] == "player":
        if ans == "1" :
            return "close"
        elif ans == "2" :
            return "inventory"
    # User pressed the key escape
    if ans == 27:
        return "exit."
        
# Show relevant information
def prompt(player,navigation_level):
    if navigation_level[-1] == "progen":
        print("Inventory [1] | Player stats [2]")
    elif navigation_level[-1] == "inventory":
        print("Inventory")
        for i in player.inventory:
            print(full_item_print(i))
        print("Close inventory [1] | Player stats [2]")
    elif navigation_level[-1] == "player":
        print(character_print(player))
        for i in player.equipped_items:
            print(full_item_print(i))
        print("Total player's defense :",full_stat(player,"defense"))
        print("Close player stats [1] | Inventory [2]")
    
    
    
    
    
