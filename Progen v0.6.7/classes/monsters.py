import random

class Monster:
    def __init__(self, player_level,chosen_species):
        species_info = species[chosen_species]
        
        self.name = species_info["name"]
        self.color = species_info["color"]
        
        self.level = max(1, player_level 
            +random.randint(*species_info["level_range"]))
        
        self.exp_drop = (species_info["exp_drop"]
            + self.level*species_info["exp_drop_multiplier"])
        
        self.gold_drop = (species_info["gold_drop"]
            + self.level*random.randint(*species_info["gold_drop_multiplier"]))
        
        self.skills = []
        for i in species_info["skills"]:
            self.skills.append(MonsterSkill(self.level, species_info["skills"][i]))
        
        # Set all stats at 0
        self.stats = base_stats.copy()
        
        for stat in base_stats:
            multiplier_key = f"{stat}_multiplier"
    
            # The stat is affected by the species, and does not have a maximum
            if stat in species_info["stats"] and max_stats[stat] == None :
                self.stats[stat] = (species_info["stats"][stat]
                    + self.level
                    *random.randint(*species_info["stats"][multiplier_key]))
            
            # The stat is affected by the species, and have a maximum
            elif stat in species_info["stats"] and max_stats[stat] != None :
                self.stats[stat] = min(max_stats[stat],
                    species_info["stats"][stat] 
                    + round(self.level 
                        *random.uniform(*species_info["stats"][multiplier_key]),
                        1))
            
            # The stat stays at 0
            else:
                pass
            
        self.current_hp = self.stats["max_hp"]
        
class MonsterSkill:
    def __init__(self, monster_level, attack):
        self.name = attack["name"]
        self.damage = attack["damage"] + monster_level*random.randint(*attack["damage_multiplier"])
        
            
species = {
    "goblin" : {
        "name" : "Goblin",
        "spawn_chance" : 0.3,
        "color" : (81, 176, 108),
        "level_range" : (-1, 2),
        "exp_drop" : 50,
        "exp_drop_multiplier" : 10,
        "gold_drop" : 10,
        "gold_drop_multiplier" : (5, 7),
        
        "skills" : {
            "stab" : {
                "name" : "Stab",
                "damage" : 28,
                "damage_multiplier" : (4, 7)
            }
        },
        
        "stats" : {
            "max_hp" : 20,
            "max_hp_multiplier" : (10, 15),
            "res_add" : 8,
            "res_add_multiplier" : (1, 4),
            "eva" : 2,
            "eva_multiplier" : (0, 1.5),
            "acu" : 2,
            "acu_multiplier" : (0, 1.5)
        }
    },

    "ghost" : {
        "name" : "Ghost",
        "spawn_chance" : 0.13,
        "color" : (153, 220, 222),
        "level_range" : (0, 3),
        "exp_drop" : 70,
        "exp_drop_multiplier" : 9,
        "gold_drop" : 2,
        "gold_drop_multiplier" : (3, 5),
        
        "skills" : {
            "scream" : {
                "name" : "Scream",
                "damage" : 14,
                "damage_multiplier" : (7, 10)
            }
        },
        
        "stats" : {
            "max_hp" : 20,
            "max_hp_multiplier" : (8, 14),
            "res_add" : 12,
            "res_add_multiplier" : (3, 4),
            "acu" : 4,
            "acu_multiplier" : (0.3, 2),
            "eva" : 4,
            "eva_multiplier" : (0.3, 2)
        }
    },
    
    "orc" : {
        "name" : "Orc",
        "spawn_chance" : 0.13,
        "color" : (119, 161, 131),
        "level_range" : (1, 4),
        "exp_drop" : 70,
        "exp_drop_multiplier" : 9,
        "gold_drop" : 2,
        "gold_drop_multiplier" : (3, 5),
        
        "skills" : {
            "punch" : {
                "name" : "Punch",
                "damage" : 30,
                "damage_multiplier" : (2, 6)
            },
            "rock_thow" : {
                "name" : "Rock Throw",
                "damage" : 25,
                "damage_multiplier" : (7, 8)
            }
        },
        
        "stats" : {
            "max_hp" : 20,
            "max_hp_multiplier" : (8, 14),
            "res_add" : 12,
            "res_add_multiplier" : (3, 4)
        }
    },
    
    "baby dragon" : {
        "name" : "Baby Dragon",
        "spawn_chance" : 0.01,
        "color" : (171, 82, 106),
        "level_range" : (1, 7),
        "exp_drop" : 70,
        "exp_drop_multiplier" : 9,
        "gold_drop" : 2,
        "gold_drop_multiplier" : (3, 5),
        
        "skills" : {
            "fire_breath" : {
                "name" : "Fire Breath",
                "damage" : 50,
                "damage_multiplier" : (10, 17)
            }
        },
        
        "stats" : {
            "max_hp" : 100,
            "max_hp_multiplier" : (20, 80),
            "res_add" : 20,
            "res_add_multiplier" : (7, 8)
        }
    }
}

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

max_stats = {
   "max_hp" : None,
   "res_add" : None,
   "weak_add" : 100,
   "safe" : None,
   "ins" : 100,
   "prot" : 100,
   "expo" : None,
   "eva" : 95,
   "ent" : None,
   "acu" : 100,
   "fer" : None,
   "vamp" : None 
}

def spawn_monster(player_level):
    
    species_names = tuple(species)
    spawn_chances = (species_info["spawn_chance"] for species_info in species.values())
    
    chosen_species = random.choices(species_names, weights=spawn_chances, k=1)[0]
    
    return Monster(player_level, chosen_species)