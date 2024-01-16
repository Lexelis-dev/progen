import curses
from math import ceil

from classes import spawn_monster

def ask_key(stdscr, main_win, GAME_HEIGHT, GAME_WIDTH):
    while True:
        try :
            key = stdscr.getch()
            
        except curses.error:
            pass
        
        if (key != -1) and (key != curses.KEY_RESIZE):
            return key
        
        elif key !=-1 and key == curses.KEY_RESIZE:
            resize_screen(stdscr, main_win, GAME_HEIGHT, GAME_WIDTH)
            
# If the user tries to modify the terminal size
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
    curses.curs_set(0)
    window.refresh()
    
def combat_screen(main_win, combat_player, combat_monster, combat_logs,
                  combat_location, player, current_monsters,
                  current_floor, current_room, colors):
    health_length = 60
    combat_monster.border()
    combat_player.border()
    combat_logs.border()
    combat_location.border()
    
    # Show the current location
    combat_location.addstr(1, 1, f"Current floor : {current_floor}")
    combat_location.addstr(3, 1, f"Current room : {current_room}")
    
    # Show the monsters
    for number, monster in enumerate(current_monsters):
        combat_monster.addstr(1+5*number, 1, f"{monster.name}   lvl {monster.level}")
        combat_monster.addstr(2+5*number, 1, f"{monster.current_hp} / {monster.stats['max_hp']}")
        
        show_remaining_hp = ceil(monster.current_hp / monster.stats['max_hp'] * health_length)
        combat_monster.addstr(3+5*number, 1, "░"*health_length)
        combat_monster.addstr(3+5*number, 1, "█"*show_remaining_hp)
        
    #Show the player
    
    combat_player.addstr(1, 1, f"{player.name}   lvl {player.level}", colors["player_color"])
    combat_player.addstr(2, 1, f"{player.current_hp} / {player.max_hp}")
    
    show_remaining_hp = ceil(player.current_hp / player.max_hp * health_length)
    combat_player.addstr(3, 1, "░"*health_length)
    combat_player.addstr(3, 1, "█"*show_remaining_hp)
    
    # Show the player's skills
    skill_offset = 0
    for i, skill in enumerate(player.equipped_skills):
        combat_player.addstr(5, 1+skill_offset, f"[{i}] {skill.name} | ")
        skill_offset += len(f"[{i}] {skill.name} | ")
    
    
def start_combat(navigation_level, player):
    navigation_level.append("combat")
    current_monsters = []
    for i in range(2):
        monster = spawn_monster(player.level)
        current_monsters.append(monster)
    return current_monsters

def create_color(r, g, b, color_number=[2]):
    curses.init_color(color_number[0], r, g, b)
    curses.init_pair(color_number[0], color_number[0], curses.COLOR_BLACK)
    actual_color = curses.color_pair(color_number[0])
    color_number[0]+=1
    return actual_color