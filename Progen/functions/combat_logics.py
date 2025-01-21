import random
from math import ceil

from classes import spawn_monster
from classes import GameConstants as GCon
from classes import GameVariables as GVar
from classes import GameWindows as GWin
from .curses_functions import refresh_main_win, ask_key, exit_check
from .shared_functions import full_stat
from .shared_functions import skip_next_input

"""
What to do during a fight

easy version            vvv

let player attack       v
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

# Create monsters, get a list with instances
def start_combat(player):
    current_monsters = []
    for i in range(2): #TODO randomise nmbr
        monster = spawn_monster(player.level)
        current_monsters.append(monster)
    return current_monsters

# Main combat loop
def combat(player, current_monsters):
    
    # Change screen state
    combat_screen(player, current_monsters)
    
    while GVar.game_nav == "combat":
        combat_screen(player, current_monsters)
        
        # Execute a single turn
        combat_turn(player, current_monsters)
        
        if player.current_hp <= 0:
            GVar.game_nav = "game_over"
            
        elif sum(monster.current_hp for monster in current_monsters) <= 0:
            # TODO have a reward screen before room_transition
            player.gold += sum(monster.gold_drop for monster in current_monsters)
            player.exp += sum(monster.exp_drop for monster in current_monsters)
            GVar.game_nav = "room_transition"
            
    skip_next_input()

def combat_turn(player, current_monsters):
    
    # Player turn (and return what the player did)
    log_message = player_combat_turn(player, current_monsters)
    
    # Monsters turn
    for entity in current_monsters:
        if entity.current_hp > 0: # Skip dead monsters
            new_message = monster_combat_turn(entity, player)
            log_message += new_message
            
    print_logs(log_message)
            
    
def player_combat_turn(player, current_monsters):
    while True :
        
        while True: # Choose skill
            
            key = ask_key()
            if key in (49, 50, 51, 52): # 1, 2, 3, 4
                skill_selected = key - 49
                chosen_skill = player.equipped_skills[skill_selected]
                dealt_damage = chosen_skill.damage
                break
    # TODO tell the player they can cancel
    # TODO shows damage it will deal??
        
        while True: # Choose target or cancel
            combat_screen(player, current_monsters, skill_selected)
            key = ask_key()
            
            if (key in range(49, 49 + len(current_monsters)) # 1, 2, etc.
                       and current_monsters[key - 49].current_hp > 0): 
                target = current_monsters[key - 49]
                damage_received = receive_damage(target, dealt_damage)
                log_message = (f" {player.name} uses {chosen_skill.name}\n"
                                f" {damage_received}\n")
                return log_message
            
            elif key == 8: # Cancel selection with backspace
            
                combat_screen(player, current_monsters)
                break
            

def monster_combat_turn(monster, player):
    # TODO maybe have AI logic
    if monster.current_hp > 0:
        chosen_skill = random.choice(monster.skills)
        dealt_damage = (chosen_skill.damage
                        + monster.level
                        *random.randint(*chosen_skill.damage_multiplier))
        
        #Calculate and get the hurt message
        damage_received = receive_damage(player, dealt_damage)
        log_message = f" {monster.name} uses {chosen_skill.name}\n"
        log_message += f" {damage_received}"
        return log_message
        
# Calculate and gives damage to any character
def receive_damage(target, damage):
    try : # If player
        actual_damage = max(0, damage - full_stat(target,"defense"))
        # If damage exceed target health
        actual_damage = min(actual_damage, target.current_hp)
        
    # If monster
    except AttributeError:
        actual_damage = max(0, damage - target.stats["res_add"])
        # If damage exceed target health
        actual_damage = min(actual_damage, target.current_hp)
        
    target.current_hp -= actual_damage
    return (f"{target.name} received {actual_damage} damage\n")
    
def print_logs(message):
    GWin.combat_logs.clear()
    GWin.combat_logs.addstr(1, 0, message)
    
def combat_screen(player, current_monsters, skill_selected = -1):
    health_length = 60
    GWin.combat_monster.clear()
    GWin.combat_player.clear()
    
    GWin.combat_monster.border()
    GWin.combat_player.border()
    GWin.combat_logs.border()
    GWin.combat_location.border()
    
    # Show the current location
    GWin.combat_location.addstr(1, 1, f"Current floor : {GVar.current_floor}")
    GWin.combat_location.addstr(3, 1, f"Current room : {GVar.current_room}")
    
    # Show the monsters
    for number, monster in enumerate(current_monsters):
        if monster.current_hp != 0 and skill_selected > -1:
            selection_color = "GREEN"
            monster_color = "WHITE"
        elif monster.current_hp == 0:
            selection_color = "RED"
            monster_color = "GRAY4"
            remaining_hp_color = "GRAY4"
            missing_hp_color = "GRAY4"
        else:
            selection_color = "WHITE"
            monster_color = "WHITE"
            
        GWin.combat_monster.addstr(1+5*number, 1, f"[{number+1}]",
                                   GCon.colors[selection_color])
        
        GWin.combat_monster.addstr(1+5*number, 1+3,
                                   f" {monster.name}   lvl {monster.level}",
                                   GCon.colors[monster_color])
        
        GWin.combat_monster.addstr(2+5*number, 1,
                              f" {monster.current_hp} / {monster.stats['max_hp']}",
                              GCon.colors[monster_color])
        
        show_remaining_hp = ceil(monster.current_hp / monster.stats['max_hp']
                                 * health_length)
        
        if monster.current_hp != 0:
            remaining_hp_color = "health_green"
            missing_hp_color = "RED"
        GWin.combat_monster.addstr(3+5*number, 1, "░"*health_length,
                                   GCon.colors[missing_hp_color])
        GWin.combat_monster.addstr(3+5*number, 1, "█"*show_remaining_hp,
                                   GCon.colors[remaining_hp_color])
        
    #Show the player
    player_info_1 = f"{player.name}   lvl {player.level}"
    GWin.combat_player.addstr(1, 1, player_info_1, GCon.colors["player_color"])
    
    player_info_2 = f" | {player.exp} / xxxexp" # TODO show required exp for next lvl
    GWin.combat_player.addstr(1, 1+len(player_info_1), player_info_2)
    
    player_info_3 = f" | {player.gold}g"
    GWin.combat_player.addstr(1, 1+len(player_info_1)+len(player_info_2), player_info_3)
    
    GWin.combat_player.addstr(2, 1, f"{player.current_hp} / {player.max_hp}")
    
    remaining_hp_color = "health_green"
    missing_hp_color = "RED"
    
    show_remaining_hp = ceil(player.current_hp / player.max_hp * health_length)
    GWin.combat_player.addstr(3, 1, "░"*health_length, GCon.colors[missing_hp_color])
    GWin.combat_player.addstr(3, 1, "█"*show_remaining_hp, GCon.colors[remaining_hp_color])
    
    # Show the player's skills
    skill_offset = 0
    for i, skill in enumerate(player.equipped_skills):
        if skill_selected == -1 or skill_selected == i:
            selection_color = "GREEN"
            skill_color = "WHITE"
        else:
            selection_color = "GRAY4"
            skill_color = "GRAY4"
            
        
        message = f"[{i+1}]"
        GWin.combat_player.addstr(5, 1+skill_offset, message, GCon.colors[selection_color])
        skill_offset += len(message)
        
        message = f" {skill.name} | "
        GWin.combat_player.addstr(5, 1+skill_offset, message,GCon.colors[skill_color])
        
        skill_offset += len(message)
        
    refresh_main_win()
    