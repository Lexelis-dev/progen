import random
"""from constants import equippable_types, equippable_names"""

class Equippable:
    def __init__(self, rarity, eq_type, name, level):
        
        # How many attributes it has, have at least one attribute of the same rarity of the item
        self.rarity = rarity
        self.eq_type = eq_type # TODO have subtypes that skew attributes spawn chance
            # "helmet"
            # "chestpiece"
            # "gloves"
            # "pants"
            # "boots"
            # "weapon"
        self.name = name
        self.level = level
        self.stats = { # TODO add all the stats, see spreadsheet
            "defense" : self.set_defense()
        }
        
    def set_rarity(self): 
        return random.choices(["white","green","blue","purple","yellow"],
                              weights=[0.6, 0.3, 0.2, 0.01, 0.001], k=1)[0]
    
    def set_name(self, eq_type): # TODO change type to subtype
        adjective = random.choice(equippable_names["adjective"])
        return f"{adjective} {eq_type}"
    
    def set_level(self, player_level):
        return player_level + random.choices([0,1,2,3,4], # May be higher than player
                              weights=[0.7, 0.4, 0.15, 0.06, 0.02], k=1)[0]
    
    # Will probably get removed, colours and curses are weird
    # Have a color to be set on a type slot?
    # TODO
    def set_color(self):
        return (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
    
    def set_defense(self):
        return self.level + self.level * random.randint(0, 1) * 0.25
    
    
# Types of items
equippable_types = [
        "helmet",
        "chestpiece",
        "gloves",
        "pants",
        "boots",
        "weapon"
    ]

# Will be picked in names
equippable_names = {
    "adjective": [
        "sturdy",
        "beautiful",
        "quick",
        "broken",
        "voided",
        "spiky",
        "dangerous",
        "menacing"
    ]
}