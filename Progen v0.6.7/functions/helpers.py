import curses

from .shared_functions import full_stat, full_item_print, character_print
from .curses_functions import ask_key

# Used to fully exit the script  
class ExitScript(Exception):
    pass
        
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
    
    
def exit_check(stdscr, main_win, pause_menu, GAME_HEIGHT, GAME_WIDTH, key):
    # Key is Escape
    if key == 27:
        while True:
            show_pause_menue(stdscr, main_win, pause_menu, GAME_HEIGHT, GAME_WIDTH)
            main_win.refresh()
            key = ask_key(stdscr, main_win, GAME_HEIGHT, GAME_WIDTH)
            if key == 27:
                return "leave"
            
            # Key is either Enter or Space
            elif key in (32,10):
                break
    
def show_pause_menue(stdscr, main_win, pause_menu, GAME_HEIGHT, GAME_WIDTH):
    pause_menu.border()
    message = "Press escape again to leave"
    pause_menu.addstr(GAME_HEIGHT//4, GAME_WIDTH//2-len(message)//2, message)
    pause_menu.refresh()
    main_win.refresh()