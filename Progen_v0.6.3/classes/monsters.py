import random

class Monster:
    def __init__(self, player_level):
        
        species_names, spawn_chances = zip(*species)
        
        chosen_species = random.choices(species_names, weights=spawn_chances, k=1)[0]
        
        if chosen_species == "goblin":
            
            self.name = "Goblin"
            self.color = (81, 176, 108)
            
            self.level = max(1, player_level + random.randint(-1, 2))
            
            self.exp_drop = 50 + self.level*10
            self.gold_drop = 10 + self.level*random.randint(5, 7)   
        
            self.stats = base_stats
            self.stats["max_hp"] = 50 + self.level*random.randint(10, 15)
            self.stats["res_add"] = 8 + self.level*random.randint(1, 4)
            self.stats["eva"] = min(95, 2 + round(self.level * random.uniform(0, 1.5), 1))
            self.stats["acu"] = min(100, 2 + round(self.level * random.uniform(0, 1.5), 1))
            
            self.current_hp = self.stats["max_hp"]
            
        elif chosen_species == "ghost":
            
            self.name = "ghost"
            self.color = (153, 220, 222)
            
            self.level = max(1, player_level + random.randint(0, 3))
            
            self.exp_drop = 70 + self.level*9
            self.gold_drop = 2 + self.level*random.randint(3, 5)   
        
            self.stats = base_stats
            self.stats["max_hp"] = 20 + self.level*random.randint(8, 14)
            self.stats["res_add"] = 12 + self.level*random.randint(3, 4)
            self.stats["prot"] = min(95, 4 + round(self.level * random.uniform(0.3, 2), 1))
            self.stats["eva"] = min(95, 4 + round(self.level * random.uniform(0.3, 2), 1))
            
            self.current_hp = self.stats["max_hp"]
            
        elif chosen_species == "orc":
            
            self.name = "orc"
            self.color = (153, 220, 222)
            
            self.level = player_level + random.randint(1, 4)
            
            self.exp_drop = 70 + self.level*9
            self.gold_drop = 2 + self.level*random.randint(3, 5)   
        
            self.stats = base_stats
            self.stats["max_hp"] = 20 + self.level*random.randint(8, 14)
            self.stats["res_add"] = 12 + self.level*random.randint(3, 4)
            
            self.current_hp = self.stats["max_hp"]
            
        elif chosen_species == "baby dragon":
            
            self.name = "baby dragon"
            self.color = (153, 220, 222)
            
            self.level = player_level + random.randint(1, 7)
            
            self.exp_drop = 70 + self.level*9
            self.gold_drop = 2 + self.level*random.randint(3, 5)   
        
            self.stats = base_stats
            self.stats["max_hp"] = 100 + self.level*random.randint(20, 80)
            self.stats["res_add"] = 20 + self.level*random.randint(7, 8)
            
            self.current_hp = self.stats["max_hp"]
            
species = (
    # Name, Chance of appearing
    ("goblin", 0.30),
    ("ghost", 0.13),
    ("orc", 0.13),
    ("baby dragon", 0.01)
        
)

base_stats = {
    "max_hp" : 0,
    "res_add" : 0,
    "weak_add" : 0,
    "safe" : 0,
    "ins" : 0,
    "prot" : 0,
    "expo" : 0,
    "eva" : 0,
    "ent" : 0,
    "acu" : 0,
    "fer" : 0,
    "vamp" : 0
}

def spawn_monster():
    return Monster(2)

for i in range(10):
    monster = spawn_monster()
    print(f"{monster.name} lvl {monster.level} hp {monster.stats['max_hp']}")