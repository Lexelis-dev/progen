"""----------This is the progen v.0.6.4 documentation----------
Progen - Item Generator Script

Author: Lexelis
Date: 24/01/14
Version: 0.6.4

Description:
    Show items and monsters, "escape" to quit
        
Version : 0.6.4
"""

#--------------------Import--------------------#
import curses
from curses import wrapper

from classes import Player, Monster, spawn_monster, Equippable
from functions import limited_choices, error, open_chest
#--------------------The main function--------------------#
def main(stdscr):
    # Initialisation
    curses.curs_set(0)  # Hide the cursor
    GAME_HEIGHT, GAME_WIDTH = 50, 120  # The default game size
    
    curses.resize_term(GAME_HEIGHT+5, GAME_WIDTH+14)
    screen_height, screen_width = stdscr.getmaxyx()
    
    main_win = curses.newwin(GAME_HEIGHT, GAME_WIDTH, 0, 0)
    combat_monster = main_win.subwin(25, 78, 0, 0)
    combat_player = main_win.subwin(25, 78, 25, 0)
    combat_logs = main_win.subwin(50, 42, 0, 78)
    main_win.mvwin(screen_height//2-GAME_HEIGHT//2, screen_width//2-GAME_WIDTH//2)
    
    navigation_level = ["progen"]
    player = Player("Lexelis")
    
    stdscr.nodelay(True)
    skip_input = False
    
    while True:
        main_win.clear()
        main_win.border()
        
        if navigation_level[-1] == "progen":
            open_chest(main_win, player, 5)
            current_monsters = start_combat(navigation_level, player)
            skip_input = True
            
        elif navigation_level[-1] == "combat":
            combat_screen(main_win, combat_player, combat_monster, combat_logs, player, current_monsters)
        main_win.refresh()
        
        if skip_input:
            skip_input = False
        else:
            while True:
                try :
                    key = stdscr.getch()
                    
                except curses.error:
                    pass
                
                if (key != -1) and (key != curses.KEY_RESIZE):
                    break
                
                elif key !=-1 and key == curses.KEY_RESIZE:
                    resize_screen(stdscr,main_win,GAME_HEIGHT,GAME_WIDTH)
                    
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

# If the user tries to modify the terminal size
def resize_screen(stdscr,window,GAME_HEIGHT,GAME_WIDTH):
    screen_height, screen_width = stdscr.getmaxyx()
    
    if screen_height > GAME_HEIGHT+5 or screen_width > GAME_WIDTH+14:
        window.mvwin(screen_height//2-GAME_HEIGHT//2, screen_width//2-GAME_WIDTH//2)
    
    else:
        curses.resize_term(GAME_HEIGHT+5, GAME_WIDTH+14)
        screen_height, screen_width = stdscr.getmaxyx()
        try:
            window.mvwin(screen_height//2-GAME_HEIGHT//2, screen_width//2-GAME_WIDTH//2)
        except curses.error:
            pass
    window.refresh()
    
def combat_screen(main_win, combat_player, combat_monster, combat_logs, player, current_monsters):
    combat_monster.border()
    combat_player.border()
    combat_logs.border()
    for number, monster in enumerate(current_monsters):
        combat_monster.addstr(1+5*number, 1, f"{monster.name}   lvl {monster.level}")
        combat_monster.addstr(2+5*number, 1, f"{monster.current_hp} / {monster.stats['max_hp']}")
    combat_player.addstr(1, 1, f"{player.name}")
    combat_player.addstr(2, 1, f"{player.current_hp} / {player.max_hp}")
    
    
def start_combat(navigation_level, player):
    navigation_level.append("combat")
    current_monsters = []
    for i in range(2):
        monster = spawn_monster(player.level)
        current_monsters.append(monster)
    return current_monsters
    
    
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