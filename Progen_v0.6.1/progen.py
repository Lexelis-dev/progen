"""----------This is the progen v.0.6.1 documentation----------
Progen - Item Generator Script

Author: Lexelis
Date: 24/01/12
Version: 0.6.1

Description:
    Show items, "$" to quit
        
Version : 0.6.1
"""

#--------------------Import--------------------#
import curses
from curses import wrapper

from classes import Player, Equippable
from functions import limited_choices, error, open_chest
#--------------------The main function--------------------#
def main(stdscr):
    # Initialisation
    curses.curs_set(0)  # Hide the cursor
    GAME_HEIGHT, GAME_WIDTH = 50, 120  # The default game size
    
    screen_height, screen_width = GAME_HEIGHT, GAME_WIDTH
    curses.resize_term(screen_height, screen_width)
    
    main_win = curses.newwin(GAME_HEIGHT, GAME_WIDTH, 0, 0)
    main_win.border()
    main_win.refresh()
    
    navigation_level = ["progen"]
    player = Player()
    
    stdscr.nodelay(True)
    
    while True:
        main_win.clear()
        main_win.border()
        open_chest(main_win, player, 1)
        main_win.refresh()
        
        while True:
            try :
                key = stdscr.getch()
            except curses.error:
                continue
            if (key != -1) and (key != curses.KEY_RESIZE):
                break
            elif key == curses.KEY_RESIZE:
                print("b")
                screen_height, screen_width = stdscr.getmaxyx()
                main_win.mvwin(screen_height//2, screen_width//2)
                main_win.refresh()
            
            resized = curses.is_term_resized(screen_height, screen_width)
            if resized:
                print("a")
                screen_height, screen_width = stdscr.getmaxyx()
                main_win.mvwin(screen_height//2, screen_width//2)
                main_win.refresh()
                
        ans = limited_choices(stdscr,player,navigation_level,key)
        
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