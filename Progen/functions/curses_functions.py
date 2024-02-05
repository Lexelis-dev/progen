import curses

from classes import EngineSettings, ExitScript

def ask_key(stdscr, main_win, pause_menu, GAME_HEIGHT, GAME_WIDTH):
    while True:
        try :
            key = stdscr.getch()
            
        except curses.error:
            pass
        
        if (key != -1) and (key != curses.KEY_RESIZE):
            if key == 27:
                if EngineSettings.paused == True:
                    return "leave"
                else:
                    EngineSettings.paused = True
                    return ""
            else:
                return key
        
        elif key !=-1 and key == curses.KEY_RESIZE:
            resize_screen(stdscr, main_win, GAME_HEIGHT, GAME_WIDTH)
            if EngineSettings.paused == True:
                resize_screen(stdscr,pause_menu,GAME_HEIGHT//2,GAME_WIDTH)
            
# If the user tries to modify the terminal size
def resize_screen(stdscr,window,GAME_HEIGHT,GAME_WIDTH):
    screen_height, screen_width = stdscr.getmaxyx()
    
    if screen_height > GAME_HEIGHT+5 or screen_width > GAME_WIDTH+14:
        window.mvwin(screen_height//2-GAME_HEIGHT//2,
                     screen_width//2-GAME_WIDTH//2)
    
    else:
        curses.resize_term(GAME_HEIGHT+5, GAME_WIDTH+14)
        screen_height, screen_width = stdscr.getmaxyx()
        try:
            window.mvwin(screen_height//2-GAME_HEIGHT//2,
                         screen_width//2-GAME_WIDTH//2)
        except curses.error:
            pass
    curses.curs_set(0)
    window.refresh()
        
def refresh_main_win(stdscr, main_win, GAME_HEIGHT, GAME_WIDTH,
                     combat_monster, combat_player,combat_logs,
                     combat_location):
    resize_screen(stdscr, main_win, GAME_HEIGHT, GAME_WIDTH)

def create_color(r, g, b, color_number=[2]):
    curses.init_color(color_number[0], r, g, b)
    curses.init_pair(color_number[0], color_number[0], curses.COLOR_BLACK)
    actual_color = curses.color_pair(color_number[0])
    color_number[0]+=1
    return actual_color

def exit_check(stdscr, main_win, pause_menu, GAME_HEIGHT, GAME_WIDTH, key):
    # Key is Escape
    if EngineSettings.paused == True:
        while True:
            show_pause_menu(stdscr, main_win, pause_menu, GAME_HEIGHT, GAME_WIDTH)
            main_win.refresh()
            key = ask_key(stdscr, main_win, pause_menu, GAME_HEIGHT, GAME_WIDTH)
            
            if key == "leave":
                raise ExitScript
            
            # Key is either Enter or Space
            elif key in (32,10):
                EngineSettings.paused = False
                pause_menu.clear()
                pause_menu.refresh()
                main_win.refresh()
                break
            
def show_pause_menu(stdscr, main_win, pause_menu, GAME_HEIGHT, GAME_WIDTH):
    if EngineSettings.paused == True:
        pause_menu.border()
        message = "Press escape again to leave"
        pause_menu.addstr(GAME_HEIGHT//4, GAME_WIDTH//2-len(message)//2, message)
        pause_menu.refresh()
        main_win.refresh()
    else:
        pause_menu.clear()