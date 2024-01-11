from .shared_functions import item_print, full_stat, character_print
from classes import Equippable

def create_item(created_items):
    item = Equippable(created_items)
    created_items.append(item)
    return item
    
# Give a certain amount of items to the player
def open_chest(player,created_items,x):
    print(f"Woaw you found a chest of {str(x)} items!")
    for _ in range(x):
        item = create_item(created_items)
        player.add_inventory(item)
        print(item_print(item))

# Calculate and gives damage to any character
def receive_damage(character,damage):
    actual_damage = max (0, damage - full_stat("defense"))
    print(character_print(character),"receive",actual_damage,"damage")
    character.current_health -= actual_damage 