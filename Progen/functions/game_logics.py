import random

from classes import Equippable, Skill
from constants import equippable_types, equippable_names

def random_rarity():
    return random.choices(["white","green","blue","purple","yellow"],
                          weights=[0.6, 0.3, 0.2, 0.01, 0.001], k=1)[0]

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
    
def starter_skills(player):
    for eq_type in equippable_types:
        for i, j in enumerate(player.equipped_skills):
            new_skill = Skill(1, "white")
            player.equipped_skills[i] = new_skill