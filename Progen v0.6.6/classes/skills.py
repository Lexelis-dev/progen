import random

class Skill:
    def __init__(self, player_level):
        self.rarity = self.set_rarity()
        self.name = random.choice(skill_types)
        self.level = player_level + random.randint(0,3)
        self.damage = 7 * self.level*(4, 8)
        
    def set_rarity(self):
        return random.choices(["white","green","blue","purple","yellow"],
                              weights=[0.6, 0.3, 0.2, 0.01, 0.001], k=1)[0]
    
skill_types = [
        "fireball",
        "slash",
        "dark bolt",
        "charge"
    ]

def create_skill(player_level):
    return Skill(player_level)