import random

from classes import Equippable, Skill, equippable_types, equippable_names

def random_rarity():
    return random.choices(["white","green","blue","purple","yellow"],
                          weights=[0.6, 0.3, 0.2, 0.01, 0.001], k=1)[0]
    
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
            
def generate_room(number):
    rooms = []
    while len(rooms) != number:
        new_room = random.choices(["combat","shop","campfire"],
                              weights=[0.85,0.075,0.075], k=1)[0]
        # Only adds non-combat if not present yet
        if new_room == "combat" or (new_room != "combat" and new_room not in rooms):
            rooms.append(new_room)
    return rooms