import random
from math import ceil

from .curses_functions import refresh_main_win, ask_key, exit_check
from .shared_functions import full_stat
from classes import spawn_monster, EngineConstants, EngineSettings

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
""" # TODO

def start_combat(player):
    EngineSettings.game_nav = "combat"
    current_monsters = []
    for i in range(2):
        monster = spawn_monster(player.level)
        current_monsters.append(monster)
    return current_monsters

def combat(player, current_monsters, current_floor, current_room, colors):
    
    combat_screen(player, current_monsters, current_floor, current_room, colors)
    
    while EngineSettings.game_nav == "combat":
        combat_screen(player, current_monsters, current_floor, current_room, colors)
        refresh_main_win()
        combat_turn(player, current_monsters)
        
        if player.current_hp <= 0 or sum(
                monster.current_hp for monster in current_monsters) <= 0:
            EngineSettings.game_nav = "room_transition"

def combat_turn(player, current_monsters):
    
    
    log_message= player_combat_turn(player, current_monsters)
    for entity in current_monsters:
        if entity.current_hp > 0:
            new_message = monster_combat_turn(entity, player)
            log_message += new_message
    print_logs(log_message)
            
    
    
def player_combat_turn(player, current_monsters):
    while True :
        while True: # Choose skill
            key = ask_key()
            exit_check(key)
            if key in (49, 50, 51, 52): # 1, 2, 3, 4
                chosen_skill = player.equipped_skills[key - 49]
                dealt_damage = chosen_skill.damage
                break
    
        while True: # Choose target or cancel
            key = ask_key()
            exit_check(key)
            if key in range(49, 49 + len(current_monsters)): # 1, 2, etc.
                target = current_monsters[key - 49]
                damage_received = receive_damage(target, dealt_damage)
                log_message = (f" {player.name} uses {chosen_skill.name}\n"
                                f" {damage_received}\n")
                return log_message
            
            elif key == 8: # Cancel selection with backspace
                break

def monster_combat_turn(monster, player):
    if monster.current_hp != 0:
        chosen_skill = random.choice(monster.skills)
        dealt_damage = (chosen_skill.damage
                        + monster.level
                        *random.randint(*chosen_skill.damage_multiplier))
        
        #Calculate  and get the hurt message
        damage_received = receive_damage(player, dealt_damage)
        log_message = f" {monster.name} uses {chosen_skill.name}\n"
        log_message += f" {damage_received}"
        return log_message
        
# Calculate and gives damage to any character
def receive_damage(target, damage):
    try :
        actual_damage = max(0, damage - full_stat(target,"defense"))
        # If damage exceed target health
        actual_damage = min(actual_damage, target.current_hp - actual_damage)
        
    except AttributeError:
        actual_damage = max(0, damage - target.stats["res_add"])
        # If damage exceed target health
        actual_damage = min(actual_damage, target.current_hp)
    target.current_hp -= actual_damage
    return (f"{target.name} received {actual_damage} damage\n")
    
def print_logs(message):
    EngineConstants.combat_logs.clear()
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
                              f"[{number+1}] {monster.name}   lvl {monster.level}")
        EngineConstants.combat_monster.addstr(2+5*number, 1,
                              f"{monster.current_hp} / {monster.stats['max_hp']}")
        
        show_remaining_hp = ceil(monster.current_hp / monster.stats['max_hp']
                                 * health_length)
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
        EngineConstants.combat_player.addstr(5, 1+skill_offset, f"[{i+1}] {skill.name} | ")
        skill_offset += len(f"[{i+1}] {skill.name} | ")