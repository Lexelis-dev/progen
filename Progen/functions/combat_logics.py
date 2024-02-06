import random
from math import ceil

from .curses_functions import refresh_main_win, ask_key, exit_check
from .shared_functions import full_stat
from classes import spawn_monster, EngineConstants

"""
What to do during a fight

easy version

let player attack
let monster attack      v



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

def start_combat(navigation_level, player):
    navigation_level.append("combat")
    current_monsters = []
    for i in range(2):
        monster = spawn_monster(player.level)
        current_monsters.append(monster)
    return current_monsters

def combat(player, current_monsters, current_floor, current_room, colors):
    
    combat_screen(player, current_monsters, current_floor, current_room, colors)
    
    while True:
        key = ask_key()
        exit_check(key)
        
        combat_screen(player, current_monsters, current_floor, current_room, colors)
        refresh_main_win()
        combat_turn(player, current_monsters)
        
        
        if player.current_hp == 0 or sum(
                monster.current_hp for monster in current_monsters) == 0:
            break

def combat_turn(player, current_monsters):
    player_combat_turn()
    
    log_message=""
    for i in current_monsters:
        new_message = monster_combat_turn(i, player)
        log_message += new_message
    print_logs(log_message)
            
    
    
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
    actual_damage = max (0, damage - full_stat(target,"defense"))
    target.current_hp -= actual_damage 
    return (f"{target.name} received {actual_damage} damage\n")
    
def print_logs(message):
    EngineConstants.combat_logs.addstr(1, 0, message)
    
def combat_screen(player, current_monsters,
                  current_floor, current_room, colors):
    health_length = 60
    EngineConstants.combat_monster.clear()
    EngineConstants.combat_player.clear()
    
    EngineConstants.combat_monster.border()
    EngineConstants.combat_player.border()
    EngineConstants.combat_logs.border()
    EngineConstants.combat_location.border()
    
    # Show the current location
    EngineConstants.combat_location.addstr(1, 1, f"Current floor : {current_floor}")
    EngineConstants.combat_location.addstr(3, 1, f"Current room : {current_room}")
    
    # Show the monsters
    for number, monster in enumerate(current_monsters):
        EngineConstants.combat_monster.addstr(1+5*number, 1,
                              f"{monster.name}   lvl {monster.level}")
        EngineConstants.combat_monster.addstr(2+5*number, 1,
                              f"{monster.current_hp} / {monster.stats['max_hp']}")
        
        show_remaining_hp = ceil(monster.current_hp / monster.stats['max_hp'] * health_length)
        EngineConstants.combat_monster.addstr(3+5*number, 1, "░"*health_length)
        EngineConstants.combat_monster.addstr(3+5*number, 1, "█"*show_remaining_hp)
        
    #Show the player
    EngineConstants.combat_player.addstr(1, 1,
                         f"{player.name}   lvl {player.level}",
                         colors["player_color"])
    
    EngineConstants.combat_player.addstr(2, 1, f"{player.current_hp} / {player.max_hp}")
    
    show_remaining_hp = ceil(player.current_hp / player.max_hp * health_length)
    EngineConstants.combat_player.addstr(3, 1, "░"*health_length)
    EngineConstants.combat_player.addstr(3, 1, "█"*show_remaining_hp)
    
    # Show the player's skills
    skill_offset = 0
    for i, skill in enumerate(player.equipped_skills):
        EngineConstants.combat_player.addstr(5, 1+skill_offset, f"[{i}] {skill.name} | ")
        skill_offset += len(f"[{i}] {skill.name} | ")