import random

class Equippable:
    def __init__(self):
        self.rarity = self.set_rarity()
        self.name = self.set_name()
        self.level = self.set_level()
        self.color = self.set_color()
        self.stats = {
            "defense" : self.set_defense()
        }
        
    def set_rarity(self):
        return random.choices(["white","green","blue","purple","yellow"],
                              weights=[0.6, 0.3, 0.2, 0.01, 0.001], k=1)[0]
    
    def set_name(self):
        item_type = random.choice(equippable_types)
        adjective = random.choice(names["adjective"])
        return f"{adjective} {item_type}"
    
    def set_level(self):
        return random.randint(0, 25)
    
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
names = {
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