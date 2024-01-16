"""----------Progen v.0.6.8 documentation----------
Progen - Roguelite RPG

Author: Lexelis
Date: 24/01/14
Version: 0.6.8

Description:
    Show items and monsters, "escape" to quit
        
Version : 0.6.8
"""

#--------------------Import--------------------#
import curses
from curses import wrapper

from classes import Player, create_skill
from functions import (
    limited_choices, resize_screen, combat_screen, start_combat, ask_key,
    create_color, exit_check, combat
)
#--------------------The main function--------------------#
def main(stdscr):
    # Initialisation
    curses.curs_set(0)  # Hide the cursor
    GAME_HEIGHT, GAME_WIDTH = 50, 120  # The default game size
    
    curses.resize_term(GAME_HEIGHT+5, GAME_WIDTH+14)
    screen_height, screen_width = stdscr.getmaxyx()
    
    for i in colors:
        colors[i] = create_color(*colors[i])
    
    main_win = curses.newwin(GAME_HEIGHT, GAME_WIDTH, 0, 0)
    
    pause_menu = curses.newwin(GAME_HEIGHT//2, GAME_WIDTH, 0, 0)
    
    combat_monster = main_win.subwin(25, 78, 0, 0)
    combat_player = main_win.subwin(25, 78, 25, 0)
    combat_logs = main_win.subwin(45, 42, 5, 78)
    combat_location = main_win.subwin(5, 42, 0, 78)
    
    
    pause_menu.mvwin(screen_height//2-GAME_HEIGHT//4, screen_width//2-GAME_WIDTH//2)
    main_win.mvwin(screen_height//2-GAME_HEIGHT//2, screen_width//2-GAME_WIDTH//2)
    
    current_floor=1
    current_room=1
    navigation_level = ["progen"]
    player = Player("Lexelis")
    colors["player_color"] = create_color(*player.color)
    
    for i, j in enumerate(player.equipped_skills):
        player.equipped_skills[i] = create_skill(1)
    
    stdscr.nodelay(True)
    while True:
        main_win.clear()
        main_win.border()
        
        if navigation_level[-1] == "progen":
            current_monsters = start_combat(navigation_level, player)
            
        elif navigation_level[-1] == "combat":
            combat_screen(main_win, combat_player, combat_monster, combat_logs,
                          combat_location, player, current_monsters,
                          current_floor, current_room, colors)
            
            while True:
                key = ask_key(stdscr, main_win, GAME_HEIGHT, GAME_WIDTH)
                leave = exit_check(stdscr, main_win, pause_menu, GAME_HEIGHT, GAME_WIDTH, key)
                
                # Quit the game, whitout saving!
                if leave == "leave":
                    break
                
                combat(combat_logs, player, current_monsters)
                main_win.refresh()
                
                if player.current_hp == 0 or sum(
                        monster.current_hp for monster in current_monsters) == 0:
                    break
                
        main_win.refresh()
        
        key = ask_key(stdscr, main_win, GAME_HEIGHT, GAME_WIDTH)
        leave = exit_check(stdscr, main_win, pause_menu, GAME_HEIGHT, GAME_WIDTH, key)
        ans = limited_choices(stdscr,player,navigation_level,key)
        
        # Quit the game, whitout saving!
        if leave == "leave":
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
    
    
#--------------------Dictionaries--------------------#
# The menues
end_correct = {
    "inventory",
    "player",
    "stats"
}

colors = {
    "white": (785, 785, 785),
    "green": (400, 600, 408),
    "blue": (455, 510, 702),
    "purple": (510, 73, 115),
    "yellow": (710, 702, 431),
    "player_color" : (1000, 1000, 1000)
}

# Initialise if the script is executed
if __name__ == "__main__":
    wrapper(main)
    
#Todo
    # Pause menu is glitched