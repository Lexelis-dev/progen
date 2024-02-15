import curses

from classes import EngineSettings, ExitScript, EngineConstants
from .game_logics import generate_room

def ask_key(checking_exit = True):
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
            key = ask_key(False)
            
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
                            message) # TODO function to print middle
        
        EngineConstants.pause_menu.refresh()
        EngineConstants.main_win.refresh()
    else:
        EngineConstants.pause_menu.clear()
        
def show_game_over():
    EngineConstants.main_win.clear()
    message = "Oww you dead :c"
    EngineConstants.main_win.addstr(EngineConstants.GAME_HEIGHT//2,
                        EngineConstants.GAME_WIDTH//2-len(message)//2,
                        message) # TODO function middle
                        
    EngineConstants.main_win.refresh()
    show_pause_menu() 
    
def show_room_transition():
    if ((EngineSettings.current_room+1) %5) != 0:
        rooms = generate_room(2)
        EngineConstants.main_win.clear()
        EngineConstants.room_transition_location.border()
        EngineConstants.room_transition_room_1.border()
        EngineConstants.room_transition_room_2.border()
        # TODO create a function to automatically put a message in the middle
        message = f"Current floor : {EngineSettings.current_floor}"
        EngineConstants.room_transition_location.addstr(2,
                            EngineConstants.GAME_WIDTH//2-len(message)//2, message)
        message = f"Current room : {EngineSettings.current_room}"
        EngineConstants.room_transition_location.addstr(3,
                            EngineConstants.GAME_WIDTH//2-len(message)//2, message)
        EngineConstants.room_transition_room_1.addstr(2, 1, f"{rooms[0]}")
        EngineConstants.room_transition_room_2.addstr(2, 1, f"{rooms[1]}")
        refresh_main_win()
        key = 0 
        while key not in (49, 50):
            key = ask_key()
        chosen_room = rooms[key - 49]
        EngineSettings.game_nav = f"{chosen_room}"
        EngineSettings.skip_next_input = True # TODO turn this into a function