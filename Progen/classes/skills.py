import random


# TODO
    # Increase chances of getting skill type
    # Side effects


class Skill:
    def __init__(self, level, rarity, skill_type=None):
        self.rarity = rarity
        
        if skill_type == None :
            random_skill = random.choice(tuple(skill_list[rarity]))
            chosen_skill = skill_list["white"][random_skill]
        
        self.name = chosen_skill["name"]
        self.level = level
        
        if chosen_skill["attack"] == None :
            self.damage = None
        else :
            attack_stats = chosen_skill["attack"]
            self.precision = attack_stats["precision"
                                          ]
            base_damage = attack_stats["damage"]
            damage_multiplier = attack_stats["damage_multiplier"]
            self.damage = (base_damage 
                           + self.level*random.randint(*damage_multiplier))
            if attack_stats["side_effect"] == None :
                pass #TODO
    
skill_list = {
#--------------------------Rarity white--------------------------
    "white" : 
        {
        "firebolt" : {
            "name" : "Fire Bolt",
            "skill_type" : "attack",
            "damage_type" : "divine",
            "target" : "single",
            "attack" : {
                "precision" : 1,
                "damage" : 15+5000,
                "damage_multiplier" : (3, 6),
                "side_effect" : None
            },
            "effect" : None,
            "heal" : None
        },
        
        "charge" : {
            "name" : "Charge",
            "skill_type" : "attack",
            "damage_type" : "blunt",
            "target" : "single",
            "attack" : {
                "precision" : 1,
                "damage" : 23,
                "damage_multiplier" : (1, 3),
                "side_effect" : None
            },
            "effect" : None,
            "heal" : None
        },
        
        "slash" : {
            "name" : "Slash",
            "skill_type" : "attack",
            "damage_type" : "piercing",
            "target" : "single",
            "attack" : {
                "precision" : 1,
                "damage" : 14,
                "damage_multiplier" : (3, 5),
                "side_effect" : None
            },
            "effect" : None,
            "heal" : None
        },
        
        "dark_bolt" : {
            "name" : "Dark Bolt",
            "skill_type" : "attack",
            "damage_type" : "dark",
            "target" : "single",
            "attack" : {
                "precision" : 1,
                "damage" : 10,
                "damage_multiplier" : (5, 9),
                "side_effect" : None
            },
            "effect" : None,
            "heal" : None
        },
        
        "sharp_claws" : {
            "name" : "Sharp Claws",
            "skill_type" : "attack",
            "damage_type" : "piercing",
            "target" : "single",
            "attack" : {
                "precision" : 1,
                "damage" : 30,
                "damage_multiplier" : (1, 2),
                "side_effect" : None
            },
            "effect" : None,
            "heal" : None
        }
    },
#--------------------------Rarity green--------------------------
    "green" : 
        {
        "fireball" : {
            "name" : "Fire Ball",
            "skill_type" : "attack",
            "damage_type" : "divine",
            "target" : "single",
            "attack" : {
                "precision" : 1,
                "damage" : 12,
                "damage_multiplier" : (2, 7),
                "side_effect" : None
            },
            "effect" : None,
            "heal" : None
        }
    }
#--------------------------Rarity blue--------------------------
#--------------------------Rarity purple--------------------------
#--------------------------Rarity yellow--------------------------
}