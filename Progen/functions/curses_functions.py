import curses

from classes import EngineSettings, ExitScript, EngineConstants

def ask_key():
    while True:
        try :
            key = EngineConstants.stdscr.getch()
            
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
            resize_screen(EngineConstants.main_win, EngineConstants.GAME_HEIGHT, EngineConstants.GAME_WIDTH)
            if EngineSettings.paused == True:
                resize_screen(EngineConstants.pause_menu, EngineConstants.GAME_HEIGHT//2, EngineConstants.GAME_WIDTH)
            
# If the user tries to modify the terminal size
def resize_screen(window, win_height, win_width): # TODO get rid of argument, have windows resize with the correct size
    screen_height, screen_width = EngineConstants.stdscr.getmaxyx()
    
    if screen_height > win_height+5 or screen_width > win_width+14:
        window.mvwin(screen_height//2 - win_height//2,
                     screen_width//2 - win_width//2)
    
    else:
        curses.resize_term(win_height+5, win_width+14)
        screen_height, screen_width = EngineConstants.stdscr.getmaxyx()
        try:
            window.mvwin(screen_height//2 - win_height//2,
                         screen_width//2 - win_width//2)
        except curses.error:
            pass
    curses.curs_set(0)
    window.refresh()
        
def refresh_main_win():
    resize_screen(EngineConstants.main_win, EngineConstants.GAME_HEIGHT, EngineConstants.GAME_WIDTH)

def create_color(r, g, b, color_number=[2]):
    curses.init_color(color_number[0], r, g, b)
    curses.init_pair(color_number[0], color_number[0], curses.COLOR_BLACK)
    actual_color = curses.color_pair(color_number[0])
    color_number[0]+=1
    return actual_color

def exit_check(key):
    # Key is Escape
    if EngineSettings.paused == True:
        while True:
            show_pause_menu()
            EngineConstants.main_win.refresh()
            key = ask_key()
            
            if key == "leave":
                raise ExitScript
            
            # Key is either Enter or Space
            elif key in (32,10):
                EngineSettings.paused = False
                EngineConstants.pause_menu.clear()
                EngineConstants.pause_menu.refresh()
                EngineConstants.main_win.refresh()
                break
            
def show_pause_menu():
    if EngineSettings.paused == True:
        resize_screen(EngineConstants.pause_menu, EngineConstants.GAME_HEIGHT//2, EngineConstants.GAME_WIDTH)
        EngineConstants.pause_menu.border()
        message = "Press escape again to leave"
        EngineConstants.pause_menu.addstr(EngineConstants.GAME_HEIGHT//4,
                            EngineConstants.GAME_WIDTH//2-len(message)//2,
                            message)
        
        EngineConstants.pause_menu.refresh()
        EngineConstants.main_win.refresh()
    else:
        EngineConstants.pause_menu.clear()