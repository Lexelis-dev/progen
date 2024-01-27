import curses
from curses import wrapper

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    curses.start_color()
    GAME_HEIGHT, GAME_WIDTH = 50, 120  # The default game size
    
    curses.resize_term(GAME_HEIGHT+5, GAME_WIDTH+14)
    screen_height, screen_width = stdscr.getmaxyx()

    main_win = curses.newwin(GAME_HEIGHT, GAME_WIDTH, 0, 0)
    
    pause_menu = curses.newwin(GAME_HEIGHT//2, GAME_WIDTH, GAME_HEIGHT//4, 0)
    
    combat_monster = main_win.subwin(25, 78, 0, 0)
    combat_player = main_win.subwin(25, 78, 25, 0)
    combat_logs = main_win.subwin(45, 42, 5, 78)
    combat_location = main_win.subwin(5, 42, 0, 78)
    
    
    pause_menu.mvwin(screen_height//2-GAME_HEIGHT//4, screen_width//2-GAME_WIDTH//2)
    main_win.mvwin(screen_height//2-GAME_HEIGHT//2, screen_width//2-GAME_WIDTH//2)
    
    stdscr.nodelay(False)
    curses.curs_set(0)
    
    pause=False
    # Display a message
    while True:
        
        if pause == True:
            pause_menu.border()
            pause_menu.refresh()
        else:
            pause_menu.clear()
        
        main_win.border()
        combat_screen(main_win, combat_player, combat_monster, combat_logs, combat_location, pause_menu)
        main_win.refresh()
        while True:
            try:
                if pause == True:
                    pause_menu.border()
                    pause_menu.refresh()
                else:
                    pause_menu.clear()
                key = stdscr.getch()
                
            except curses.error:
                pass
            
            if key !=-1 and key != curses.KEY_RESIZE:
                break
            
            elif key !=-1 and key == curses.KEY_RESIZE:
                resize_screen(stdscr,main_win,GAME_HEIGHT,GAME_WIDTH)
                if pause == True:
                    resize_screen(stdscr,pause_menu,GAME_HEIGHT//2,GAME_WIDTH)
                
            
        if key == 27 :
            break
        
        elif key == 112 :
            pause=True
            
        elif key == 109 :
            pause=False


def combat_screen(main_win, combat_player, combat_monster, combat_logs, combat_location, pause_menu):
    combat_monster.border()
    combat_player.border()
    combat_logs.border()
    combat_location.border()

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
    
    
    
    
    
    
wrapper(main)