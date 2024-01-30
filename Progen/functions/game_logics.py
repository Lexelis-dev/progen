import random

from .shared_functions import item_print, full_stat, character_print
from classes import Equippable
from .curses_functions import combat_screen, refresh_main_win, ask_key, exit_check


def create_item():
    item = Equippable()
    return item
    
# Give a certain amount of items to the player
def open_chest(window,player,x):
    window.addstr(1,1,f"Woaw you found a chest of {str(x)} items!")
    for _ in range(x):
        item = create_item()
        window.addstr(2+_, 5, f"{item.name}")
    window.getch()
    
def starter_equipments(player, equipment_type):
    pass
    
    
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
    actual_damage = max (0, damage +  - 5)
    target.current_hp -= actual_damage 
    return (f"{target.name} received {actual_damage} damage\n")
    
def print_logs(combat_logs, message):
    combat_logs.addstr(1, 0, message)



"""
What to do during a fight

easy version

let player attack
let monster attack



advanced version

let player attack
poison player

let monster attack
poison monster


even more advanced

player attack
end player turn buffs and debuffs

monster attack
end monster turn buffs and debuffs
"""