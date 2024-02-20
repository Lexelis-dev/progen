import curses

from classes import ExitScript
from classes import GameConstants as GCon
from classes import GameVariables as GVar
from classes import GameWindows as GWin
from .game_logics import generate_room
from .shared_functions import skip_next_input

def ask_key(checking_exit = True):
    while True:
        try :
            key = GWin.stdscr.getch()
            
        except curses.error:
            pass
        
        if (key != -1) and (key != curses.KEY_RESIZE):
            if key == 27:
                if GVar.paused == True:
                    return "leave"
                else:
                    GVar.paused = True
                    return ""
            else:
                return key
        
        elif key !=-1 and key == curses.KEY_RESIZE:
            resize_screen(GWin.main_win, GCon.GAME_HEIGHT, GCon.GAME_WIDTH)
            if GVar.paused == True:
                resize_screen(GWin.pause_menu, GCon.GAME_HEIGHT//2, GCon.GAME_WIDTH)
        
        if checking_exit:
            exit_check(key)
            
# If the user tries to modify the terminal size
def resize_screen(window, win_height, win_width): # TODO get rid of argument, have windows resize with the correct size
    screen_height, screen_width = GWin.stdscr.getmaxyx()
    
    if screen_height > win_height+5 or screen_width > win_width+14:
        window.mvwin(screen_height//2 - win_height//2,
                     screen_width//2 - win_width//2)
    
    else:
        curses.resize_term(win_height+5, win_width+14)
        screen_height, screen_width = GWin.stdscr.getmaxyx()
        try:
            window.mvwin(screen_height//2 - win_height//2,
                         screen_width//2 - win_width//2)
        except curses.error:
            pass
    curses.curs_set(0)
    window.refresh()
        
def refresh_main_win():
    resize_screen(GWin.main_win, GCon.GAME_HEIGHT, GCon.GAME_WIDTH)

def create_color(r, g, b, color_number=[2]):
    curses.init_color(color_number[0], r, g, b)
    curses.init_pair(color_number[0], color_number[0], curses.COLOR_BLACK)
    actual_color = curses.color_pair(color_number[0])
    color_number[0]+=1
    return actual_color

def exit_check(key):
    # Key is Escape
    if GVar.paused == True:
        while True:
            show_pause_menu()
            GWin.main_win.refresh()
            key = ask_key(False)
            
            if key == "leave":
                raise ExitScript
            
            # Key is either Enter or Space
            elif key in (32,10):
                GVar.paused = False 
                GWin.pause_menu.clear()
                GWin.pause_menu.refresh()
                refresh_main_win()
                break
            
def show_pause_menu():
    if GVar.paused == True:
        resize_screen(GWin.pause_menu, GCon.GAME_HEIGHT//2, GCon.GAME_WIDTH)
        GWin.pause_menu.border()
        message = "Press escape again to leave"
        GWin.pause_menu.addstr(GCon.GAME_HEIGHT//4,
                            GCon.GAME_WIDTH//2-len(message)//2,
                            message) # TODO function to print middle
        
        GWin.pause_menu.refresh()
        GWin.main_win.refresh()
    else:
        GWin.pause_menu.clear()
        
def show_game_over():
    GWin.main_win.clear()
    message = "Oww you dead :c"
    GWin.main_win.addstr(GCon.GAME_HEIGHT//2,
                        GCon.GAME_WIDTH//2-len(message)//2,
                        message) # TODO function middle
                        
    GWin.main_win.refresh()
    show_pause_menu() 
    
def show_room_transition():
    if ((GVar.current_room+1) %5) != 0:
        GVar.current_room += 1
    else:
        GVar.current_room = 1
        GVar.current_floor += 1
        
    GWin.main_win.clear()
    GWin.room_transition_location.border()
    GWin.room_transition_room_1.border()
    GWin.room_transition_room_2.border()
    # TODO create a function to automatically put a message in the middle
    message = f"Next floor : {GVar.current_floor}"
    GWin.room_transition_location.addstr(2,
                        GCon.GAME_WIDTH//2-len(message)//2, message)
    message = f"Next room : {GVar.current_room}"
    GWin.room_transition_location.addstr(3,
                        GCon.GAME_WIDTH//2-len(message)//2, message)
    
    if ((GVar.current_room) %5) != 0:
        
        rooms = generate_room(2)
        
        GWin.room_transition_room_1.addstr(2, 1, f"{rooms[0]}")
        GWin.room_transition_room_2.addstr(2, 1, f"{rooms[1]}")
        refresh_main_win()
        
        key = 0 
        while key not in (49, 50):
            key = ask_key()
        chosen_room = rooms[key - 49]
        GVar.game_nav = f"{chosen_room}"
        skip_next_input()
        
    else:
        ask_key()
        chosen_room = "boss_room"
        GVar.game_nav = f"{chosen_room}"
        skip_next_input()