"""----------Progen v.0.7.0 documentation----------
Progen - Roguelite RPG

Author: Lexelis
Date: 24/02/07
Version: 0.7.0

Description:
    Get beaten by monsters, "escape" to quit
"""

#--------------------Import--------------------#
import curses
from curses import wrapper

from classes import Player, ExitScript, EngineConstants,EngineSettings
from functions import (
    start_combat, ask_key,
    create_color, exit_check, show_pause_menu,
    combat, starter_equipments, starter_skills
)
#--------------------The main function--------------------#
def main(stdscr):
    EngineConstants.stdscr = stdscr
    # Initialisation
    curses.curs_set(0)  # Hide the cursor
    
    # TODO delete to move to class
    GAME_HEIGHT, GAME_WIDTH = 50, 120  # The default game size
    
    curses.resize_term(GAME_HEIGHT+5, GAME_WIDTH+14)
    screen_height, screen_width = stdscr.getmaxyx()
    
    for i in colors:
        colors[i] = create_color(*colors[i])
    
    main_win = curses.newwin(GAME_HEIGHT, GAME_WIDTH, 0, 0)
    pause_menu = curses.newwin(GAME_HEIGHT//2, GAME_WIDTH, GAME_HEIGHT//4, 0)
    
    combat_monster = main_win.subwin(25, 78, 0, 0)
    combat_player = main_win.subwin(25, 78, 25, 0)
    combat_logs = main_win.subwin(45, 42, 5, 78)
    combat_location = main_win.subwin(5, 42, 0, 78)
    
    EngineConstants.main_win = main_win
    EngineConstants.pause_menu = pause_menu
    
    EngineConstants.combat_monster = combat_monster
    EngineConstants.combat_player = combat_player
    EngineConstants.combat_logs = combat_logs
    EngineConstants.combat_location = combat_location
    
    
    pause_menu.mvwin(screen_height//2-GAME_HEIGHT//4, screen_width//2-GAME_WIDTH//2)
    main_win.mvwin(screen_height//2-GAME_HEIGHT//2, screen_width//2-GAME_WIDTH//2)
    
    current_floor=1
    current_room=1
    player = Player("Lexelis") #TODO select name
    colors["player_color"] = create_color(*player.color)
        
    starter_equipments(player)
    starter_skills(player)
    
    stdscr.nodelay(True)
    
    def inner_main():
        while True:
            main_win.clear()
            main_win.border()
            
            if EngineSettings.game_nav == "progen":
                current_monsters = start_combat(player)
                
            elif EngineSettings.game_nav == "combat":
                combat(player, current_monsters, current_floor,
                       current_room, colors)
            
            main_win.refresh()
            show_pause_menu()
            
            key = ask_key()
            exit_check(key)
            
            """"""""""if ans == "close":
                if navigation_level[-1] in end_correct:
                    del navigation_level[-1]
            
            elif ans in end_correct:
                # The last level is already a menue
                if navigation_level[-1] in end_correct:
                    navigation_level[-1]=ans
                    
                #The player opens a menue
                else:
                    navigation_level.append(ans)"""""""""
    
    try:
        inner_main()
    except ExitScript:
        pass
    
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
    
#TODO
    # Combat ends after deaths
    # Use defense in attack
    # Player can attack
    # Show skill info
    # Start of game
    # Save and load?
    # Have less variables, externalise the values (in packages)