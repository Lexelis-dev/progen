import random
from math import ceil

from .curses_functions import refresh_main_win, ask_key, exit_check
from .shared_functions import full_stat
from classes import spawn_monster

def start_combat(navigation_level, player):
    navigation_level.append("combat")
    current_monsters = []
    for i in range(2):
        monster = spawn_monster(player.level)
        current_monsters.append(monster)
    return current_monsters

def combat(stdscr, main_win, combat_player, combat_monster, combat_logs,
              combat_location, pause_menu, GAME_HEIGHT, GAME_WIDTH, player,
              current_monsters, current_floor, current_room, colors):
    
    combat_screen(main_win, combat_player, combat_monster, combat_logs,
                  combat_location, player, current_monsters,
                  current_floor, current_room, colors)
    
    while True:
        key = ask_key(stdscr, main_win, pause_menu, GAME_HEIGHT, GAME_WIDTH)
        exit_check(stdscr, main_win, pause_menu, GAME_HEIGHT,
                         GAME_WIDTH, key)
        
        
        combat_screen(main_win, combat_player, combat_monster, combat_logs,
                      combat_location, player, current_monsters,
                      current_floor, current_room, colors)
        
        refresh_main_win(stdscr, main_win, GAME_HEIGHT, GAME_WIDTH,
                             combat_monster, combat_player,combat_logs,
                             combat_location)
        
        combat_turn(combat_logs, player, current_monsters)
        
        
        if player.current_hp == 0 or sum(
                monster.current_hp for monster in current_monsters) == 0:
            break

def combat_turn(combat_logs, player, current_monsters):
    player_combat_turn()
    
    log_message=""
    for i in current_monsters:
        new_message = monster_combat_turn(i, player)
        log_message += new_message
    print_logs(combat_logs, log_message)
            
    
    
def player_combat_turn():
    pass

def monster_combat_turn(monster, player):
    if monster.current_hp != 0:
        chosen_skill = random.choice(monster.skills)
        dealt_damage = (chosen_skill.damage
                        + monster.level
                        *random.randint(*chosen_skill.damage_multiplier))
        log_message = f" {monster.name} uses {chosen_skill.name}\n"
        
        #Calculate  and get the hurt message
        log_message += f" {receive_damage(player, dealt_damage)}"
        return log_message
        
# Calculate and gives damage to any character
def receive_damage(target, damage):
    
    ############### actual_damage = max (0, damage - full_stat(character,"defense"))
    actual_damage = max (0, damage - full_stat(target,"defense"))
    target.current_hp -= actual_damage 
    return (f"{target.name} received {actual_damage} damage\n")
    
def print_logs(combat_logs, message):
    combat_logs.addstr(1, 0, message)
    
def combat_screen(main_win, combat_player, combat_monster, combat_logs,
                  combat_location, player, current_monsters,
                  current_floor, current_room, colors):
    health_length = 60
    combat_monster.clear()
    combat_player.clear()
    
    combat_monster.border()
    combat_player.border()
    combat_logs.border()
    combat_location.border()
    
    # Show the current location
    combat_location.addstr(1, 1, f"Current floor : {current_floor}")
    combat_location.addstr(3, 1, f"Current room : {current_room}")
    
    # Show the monsters
    for number, monster in enumerate(current_monsters):
        combat_monster.addstr(1+5*number, 1,
                              f"{monster.name}   lvl {monster.level}")
        combat_monster.addstr(2+5*number, 1,
                              f"{monster.current_hp} / {monster.stats['max_hp']}")
        
        show_remaining_hp = ceil(monster.current_hp / monster.stats['max_hp'] * health_length)
        combat_monster.addstr(3+5*number, 1, "░"*health_length)
        combat_monster.addstr(3+5*number, 1, "█"*show_remaining_hp)
        
    #Show the player
    combat_player.addstr(1, 1,
                         f"{player.name}   lvl {player.level}",
                         colors["player_color"])
    
    combat_player.addstr(2, 1, f"{player.current_hp} / {player.max_hp}")
    
    show_remaining_hp = ceil(player.current_hp / player.max_hp * health_length)
    combat_player.addstr(3, 1, "░"*health_length)
    combat_player.addstr(3, 1, "█"*show_remaining_hp)
    
    # Show the player's skills
    skill_offset = 0
    for i, skill in enumerate(player.equipped_skills):
        combat_player.addstr(5, 1+skill_offset, f"[{i}] {skill.name} | ")
        skill_offset += len(f"[{i}] {skill.name} | ")