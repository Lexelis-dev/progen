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

# Dynamic input function changing with current level
def lexinput(navigation_level):
    u=""
    # Write the current levels
    for i, v in enumerate(navigation_level):
        if i == len(navigation_level) - 1:
            u+= v + ">"
        else:
            u+= v + "/"
    return input(u).lower()

def error(message):
    print("\n" + Color.SYS_RED + "Lexerror " + Color.SYS_PURPLE + message + "\033[39m")
    
    
    
    
    
