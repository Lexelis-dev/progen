import curses
from curses import wrapper

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
        
        message = f"Hello, borderless world! {game_height} {game_width}"
        main_win.addstr(game_height // 2, (game_width - len(message)) // 2, message)
        stdscr.refresh()
        main_win.refresh()
        while True:
            try :
                key = stdscr.getch()
                
            except curses.error:
                pass
            
            if (key != -1) and (key != curses.KEY_RESIZE):
                break
        
        if key !=-1:
            i+=1
            message2 = f"You pressed '{chr(key)}' with ASCII value {key}."
            main_win.addstr(game_height//2 + 1, (game_width - len(message2)) // 2, message2)
            
            main_win.addstr(game_height//2 + 3, (game_width - len(str(i))) // 2, str(i))
        if key == curses.KEY_RESIZE or key == ord("$"):
            break
    
wrapper(main)