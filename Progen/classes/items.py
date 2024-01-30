import random
from constants import equippable_types, equippable_names

class Equippable:
    def __init__(self, rarity, eq_type, name, level):
        self.rarity = rarity
        self.eq_type = eq_type
        self.name = name
        self.level = level
        self.stats = {
            "defense" : self.set_defense()
        }
        
    def set_rarity(self):
        return random.choices(["white","green","blue","purple","yellow"],
                              weights=[0.6, 0.3, 0.2, 0.01, 0.001], k=1)[0]
    
    def set_name(self, eq_type):
        adjective = random.choice(equippable_names["adjective"])
        return f"{adjective} {eq_type}"
    
    def set_level(self, player_level):
        return player_level + random.choices([0,1,2,3,4],
                              weights=[0.7, 0.4, 0.15, 0.06, 0.02], k=1)[0]
    
    def set_color(self):
        return (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
    
    def set_defense(self):
        return self.level + self.level * random.randint(0, 1) * 0.25