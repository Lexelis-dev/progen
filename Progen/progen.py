"""----------Progen v0.7.6 documentation----------
Progen - Roguelite RPG

Authors: Lexelis
Date: 25/01/12
Version: 0.7.7

Description:
    Fight monsters, "escape" to quit
"""

#--------------------Import--------------------#
import curses
from curses import wrapper

from classes import Player, ExitScript
from classes import GameConstants as GCon
from classes import GameVariables as GVar
from classes import GameWindows as GWin
from functions import (
    start_combat, ask_key,
    create_color, exit_check, show_pause_menu,
    combat, starter_equipments, starter_skills, show_game_over,
    show_room_transition, skip_next_input, campfire
)
#--------------------The main function--------------------#
def main(stdscr):
    
    # Assign the main screen to the global GameWindows module
    GWin.stdscr = stdscr
    # Initialisation
    curses.curs_set(0)  # Hide the cursor
    
    curses.resize_term(GCon.GAME_HEIGHT+5, GCon.GAME_WIDTH+14)  # Resize window
    screen_height, screen_width = stdscr.getmaxyx()  # Get screen dimensions
    
    # Initialize color settings
    for i in GCon.colors:
        GCon.colors[i] = create_color(*GCon.colors[i])
    
    # Create main game windows
    main_win = curses.newwin(GCon.GAME_HEIGHT, GCon.GAME_WIDTH, 0, 0)
    pause_menu = curses.newwin(GCon.GAME_HEIGHT//2, GCon.GAME_WIDTH, GCon.GAME_HEIGHT//4, 0)
    
    # Create sub-windows for combat and room transitions
    combat_monster = main_win.subwin(25, 78, 0, 0)
    combat_player = main_win.subwin(25, 78, 25, 0)
    combat_logs = main_win.subwin(45, 42, 5, 78)
    combat_location = main_win.subwin(5, 42, 0, 78)
    
    room_transition_location = main_win.subwin(6, GCon.GAME_WIDTH, 0, 0)
    room_transition_room_1 = main_win.subwin(GCon.GAME_HEIGHT-6,
                                             GCon.GAME_WIDTH//2, 6, 0)
    room_transition_room_2 = main_win.subwin(GCon.GAME_HEIGHT-6,
                                             GCon.GAME_WIDTH//2, 6, GCon.GAME_WIDTH//2)
    
    # Assign created windows to GameWindows module
    GWin.main_win = main_win
    GWin.pause_menu = pause_menu
    
    GWin.combat_monster = combat_monster
    GWin.combat_player = combat_player
    GWin.combat_logs = combat_logs
    GWin.combat_location = combat_location
    
    GWin.room_transition_location = room_transition_location
    GWin.room_transition_room_1 = room_transition_room_1
    GWin.room_transition_room_2 = room_transition_room_2
    
    # Center the windows on the screen
    GWin.pause_menu.mvwin(screen_height//2-GCon.GAME_HEIGHT//4, screen_width//2-GCon.GAME_WIDTH//2)
    GWin.main_win.mvwin(screen_height//2-GCon.GAME_HEIGHT//2, screen_width//2-GCon.GAME_WIDTH//2)
    
    
    # Initialize the main player
    player = Player("Lexelis") #TODO select name
    GVar.main_player = player
    GCon.colors["player_color"] = create_color(*player.color)
        
    starter_equipments(player)
    starter_skills(player)
    
    # Configure the main screen for non-blocking input
    stdscr.nodelay(True)
    
    def inner_main():
        while True:
            GWin.main_win.clear()
            GWin.main_win.border()
            GWin.main_win.refresh()
            
            # Display the pause menu -- if GVar.paused == True
            show_pause_menu() 
            
            # Change initial state to a combat
            # TODO have an initial encounter
            if GVar.game_nav == "progen":
                GVar.game_nav = "combat"
                
            elif GVar.game_nav == "combat":
                # Create monsters, get a list with instances
                current_monsters = start_combat(player)
                # Go into the combat loop
                combat(player, current_monsters)
                
            elif GVar.game_nav == "boss_room": #TODO boss room
                current_monsters = start_combat(player)
                combat(player, current_monsters)
                
            elif GVar.game_nav == "game_over":
                show_game_over()
                
            elif GVar.game_nav == "room_transition":
                show_room_transition()
                
            elif GVar.game_nav == "campfire":
                campfire()
                
                
            if not GVar.skip_next_input:
                key = ask_key()
            
            else:
                skip_next_input(False)
    
    try:
        inner_main()
    except ExitScript:
        pass
    
#--------------------Dictionaries--------------------#

# Initialise if the script is executed
if __name__ == "__main__":
    wrapper(main)
    
#TODO
    # Show skill info
    # Start of game
    # Save and load?
    # Level up