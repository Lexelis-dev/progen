from classes import Equippable
from constants import equippable_types, equippable_names


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
    
def starter_equipments(player):
    for eq_type in equippable_types:
        item_name = f"starter {eq_type}"
        item = Equippable("white", eq_type, item_name, 1)
        player.equipped_items[eq_type] = item
    
    




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