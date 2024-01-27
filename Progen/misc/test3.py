import curses
from curses import wrapper
from math import roof

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    curses.start_color()

    game_height, game_width = 50, 120
    screen_height, screen_width = game_height+2, game_width+2
    curses.resize_term(screen_height, screen_width)
    
    stdscr.border()
    
    main_win = curses.newwin(game_height, game_width, 1, 1)
    i=0
    stdscr.nodelay(True)
    # Display a message
    while True:
        current_hp = 40
        max_hp = 60
        health_length = 20
        
        show_remaining_hp = roof(current_hp / max_hp * health_length)
        
        
        main_win.addstr(1,1,"░"*health_length)
        main_win.addstr(1,1,"█"*show_remaining_hp)
        
        stdscr.refresh()
        main_win.refresh()
        try:
            key = stdscr.getch()
        except curses.error:
            continue
        main_win.clear()
        
        if key !=-1:
            main_win.addstr(10,10,"hi")
            
        if key == curses.KEY_RESIZE or key == ord("$"):
            break
    
wrapper(main)