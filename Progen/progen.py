"""----------Progen v.0.7.3 documentation----------
Progen - Roguelite RPG

Authors: Lexelis
Date: 24/02/010
Version: 0.7.3

Description:
    Fight monsters, "escape" to quit
"""

#--------------------Import--------------------#
import curses
from curses import wrapper

from classes import Player, ExitScript, EngineConstants,EngineSettings
from functions import (
    start_combat, ask_key,
    create_color, exit_check, show_pause_menu,
    combat, starter_equipments, starter_skills, show_game_over,
    show_room_transition
)
#--------------------The main function--------------------#
def main(stdscr):
    EngineConstants.stdscr = stdscr
    # Initialisation
    curses.curs_set(0)  # Hide the cursor
    
    # TODO delete to move to class
    GAME_HEIGHT, GAME_WIDTH = 50, 120  # The default game size # TODO
    
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
    
    room_transition_location = main_win.subwin(6, EngineConstants.GAME_WIDTH, 0, 0)
    room_transition_room_1 = main_win.subwin(EngineConstants.GAME_HEIGHT-6,
                                             EngineConstants.GAME_WIDTH//2, 6, 0)
    room_transition_room_2 = main_win.subwin(EngineConstants.GAME_HEIGHT-6,
                                             EngineConstants.GAME_WIDTH//2, 6, EngineConstants.GAME_WIDTH//2)
    
    EngineConstants.main_win = main_win
    EngineConstants.pause_menu = pause_menu
    
    EngineConstants.combat_monster = combat_monster
    EngineConstants.combat_player = combat_player
    EngineConstants.combat_logs = combat_logs
    EngineConstants.combat_location = combat_location
    
    
    EngineConstants.pause_menu.mvwin(screen_height//2-GAME_HEIGHT//4, screen_width//2-GAME_WIDTH//2)
    EngineConstants.main_win.mvwin(screen_height//2-GAME_HEIGHT//2, screen_width//2-GAME_WIDTH//2)
    
    EngineConstants.room_transition_location = room_transition_location
    EngineConstants.room_transition_room_1 = room_transition_room_1
    EngineConstants.room_transition_room_2 = room_transition_room_2
    
    EngineSettings.current_floor=1
    EngineSettings.current_room=1
    player = Player("Lexelis") #TODO select name
    colors["player_color"] = create_color(*player.color)
        
    starter_equipments(player)
    starter_skills(player)
    
    stdscr.nodelay(True)
    
    def inner_main():
        while True:
            EngineConstants.main_win.clear()
            EngineConstants.main_win.border()
        
            EngineConstants.main_win.refresh()
            show_pause_menu() 
            
            if EngineSettings.game_nav == "progen":
                current_monsters = start_combat(player)
                
            elif EngineSettings.game_nav == "combat":
                combat(player, current_monsters, colors)
                
            elif EngineSettings.game_nav == "game_over":
                show_game_over()
                
            elif EngineSettings.game_nav == "room_transition":
                show_room_transition()
                
                
            if not EngineSettings.skip_next_input:
                key = ask_key()
                exit_check(key)
            
            else:
                EngineSettings.skip_next_input = False # TODO turn this into a function
                
            
            """"""""""if ans == "close":
                if navigation_level[-1] in end_correct:
                    del navigation_level[-1]
            
            elif ans in end_correct:
                # The last level is already a menue
                if navigation_level[-1] in end_correct:
                    navigation_level[-1]=ans
                    
                #The player opens a menue
                else:
                    navigation_level.append(ans)""""""""" # TODO
    
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
    # Show skill info
    # Start of game
    # Save and load?
    # Room transition
    # Have less variables, externalise the values (in packages)