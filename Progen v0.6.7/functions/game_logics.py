from .shared_functions import item_print, full_stat, character_print
from classes import Equippable


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

# Calculate and gives damage to any character
def receive_damage(combat_logs, character, damage, log_position):
    actual_damage = max (0, damage - full_stat("defense"))
    combat_logs.addstr(f"{character} receive {actual_damage} damage")
    character.current_health -= actual_damage 
    
def combat(player, current_monsters):
    while True:
        player_combat_turn
        
        for i in current_monsters:
            monster_combat_turn
        
        if player.current_hp == 0 or sum(
                monster.current_hp for monster in current_monsters) == 0:
            break
            
    
    
def player_combat_turn():
    pass

def monster_combat_turn():
    pass



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