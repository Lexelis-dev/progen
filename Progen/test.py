import curses
from curses import wrapper

from classes import Player, create_skill
from functions import (
    limited_choices, resize_screen, combat_screen, start_combat, ask_key,
    create_color
)

colors = {
    "white": (785, 785, 785),
    "green": (400, 600, 408),
    "blue": (455, 510, 702),
    "purple": (510, 73, 115),
    "yellow": (710, 702, 431),
    "player_color" : (1000, 1000, 1000)
}

def main(stdscr):
    
    GAME_HEIGHT, GAME_WIDTH = 50, 120  # The default game size
    
    curses.resize_term(GAME_HEIGHT+5, GAME_WIDTH+14)
    screen_height, screen_width = stdscr.getmaxyx()
    
    for i in colors:
        colors[i] = create_color(*colors[i])
    navigation_level = ["progen"]
    player = Player("Lexelis")
    
    for i, j in enumerate(player.equipped_skills):
        player.equipped_skills[i] = create_skill(1)
    stdscr.nodelay(True)
    
    main_win = curses.newwin(GAME_HEIGHT, GAME_WIDTH, 0, 0)
    
    
    
    while True:
        main_win.clear()
        main_win.border()
        main_win.addstr(1,1,"ahhh",colors["player_color"])
        main_win.refresh()
        
        key = ask_key(stdscr, main_win, GAME_HEIGHT, GAME_WIDTH)
        ans = limited_choices(stdscr,player,navigation_level,key)
        
        # Quit the game, whitout saving!
        if ans == "exit.":
            break

curses.wrapper(main)