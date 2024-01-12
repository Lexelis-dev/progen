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
        player.add_inventory(item)
        window.addstr(5+_,10,f"▣ {item.name}")

# Calculate and gives damage to any character
def receive_damage(character,damage):
    actual_damage = max (0, damage - full_stat("defense"))
    print(character_print(character),"receive",actual_damage,"damage")
    character.current_health -= actual_damage 