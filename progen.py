"""----------This is the progen v.0.4 documentation----------
Progen - Item Generator Script

Author: Lexelis
Date: 24/01/10
Version: 0.4

Description:
This script generates and displays equippable items for a player.



General inputs:
    
        
Version : 0.4
"""

#--------------------Import--------------------#
import os
import random
import colorama
colorama.init()

#--------------------Classes--------------------#
# See LexeCMD for more informations
class BaseColor :
    sys_red = [145, 32, 49]
    sys_purple = [161, 141, 181]
    rarity_white = [200, 200, 200]
    rarity_green = [101, 153, 104]
    rarity_blue = [116, 130, 176]
    rarity_purple = [130, 73, 115]
    rarity_yellow = [181, 179, 110]
    
    
class Color :
    pass

for i in {k: v for k, v in vars(BaseColor).items() if not k.startswith('__')}:
    setattr(Color, i, "\x1b[38;2;{};{};{}m".format(*getattr(BaseColor, i)))
    
    
Color.rarity_colors = {
    "white": Color.rarity_white,
    "green": Color.rarity_green,
    "blue": Color.rarity_blue,
    "purple": Color.rarity_purple,
    "yellow": Color.rarity_yellow
}


# Create an equipable item
class Equippable:
    def __init__(self):
        # Give a unique id
        self.item_id = len(created_items)
        self.rarity = self.set_rarity()
        self.name = self.set_name()
        self.level = self.set_level()
        self.color = self.set_color()
        self.stats = {
            "defense" : self.set_defense()
        }
        
    # Rarity
    def set_rarity(self):
        return random.choices(["white","green","blue","purple","yellow"],
                              weights=[0.6, 0.3, 0.2, 0.01, 0.001], k=1)[0]
    
    # Not a unique name
    def set_name(self):
        item_type = random.choice(item_types["equipable"])
        adjective = random.choice(names["adjective"])
        return f"{adjective} {item_type}"
    
    # Current power
    def set_level(self):
        return random.randint(0, 25)
    
    # Printed color
    def set_color(self):
        return (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
    
    # Stats
    def set_defense(self):
        return self.level + self.level * random.randint(0, 1) * 0.25
    
    
# Player's attributes
class Player:
    def __init__(self):
        ########self.name = input("Enter your name\n")
        self.name = "Lexelis"
        self.color = [207, 133, 214]
        
        self.max_health = 50
        self.current_health = self.max_health
        self.equipped_items = []
        self.inventory = []
        
    def equip_item(self,item):
        self.equipped_items.append(item)
        self.inventory.remove(item)
        
    def unequip_item(self,item):
        self.inventory.append(item)
        self.equipped_items.remove(item)
        
    def add_inventory(self,item):
        self.inventory.append(item)
        
    def remove_inventory(self,item):
        self.inventory.remove(item)
        
    # Use the equip_item but find the corresponding id
    def equip_item_with_id(self,num):
        #################Surely I can simplify this
        for i in self.inventory:
            if i.item_id == int(num):
                self.equip_item(i)
                return None
        error("Id not found in inventory")
            
    def unequip_item_with_id(self,num):
        for i in self.equipped_items:
            if i.item_id == int(num):
                self.unequip_item(i)
                return None
        error("Id not found in inventory")
    
    def remove_inventory_with_id(self,num):
        for i in self.inventory:
            if i.item_id == int(num):
                self.remove_inventory(i)
                return None
        error("Id not found in inventory")
    
#--------------------The CLI functions--------------------#

created_items = []
def main():
    # Initialisation
    global player, created_items
    open_chest(5)
    
    while True:
        ans = entry()
        clear_screen()
        # Seperate the input words into a list
        ans_parts = ans.split()
        first_part = ans_parts[0]
        
        # Quit the game, whitout saving!
        if ans == "exit.":
            break
        
        elif ans == "close":
            if L[-1] in end_correct:
                del L[-1]
        
        elif ans in end_correct:
            # The last level is already a menue
            if L[-1] in end_correct:
                L[-1]=ans
                
            #The player opens a menue
            else:
                L.append(ans)
        
        # Input is accepted
        elif first_part in correct[L[-1]]:
            
            # Input activates a command
            if first_part in end_functions_player_1arg["end_fun_name"]:
                if len(ans_parts) == 2:
                    end_functions_player_1arg["end_fun"][end_functions_player_1arg["end_fun_name"].index(first_part)](player,ans_parts[1])
                else:
                    error("This function only accept one argument")
                    
            # Input is already a used values and goes to another level
            else:
                L.append(ans)
                
        elif ans == "help":
            lexhelp()
        
        elif ans == "alias":
            alias()
            
        # Input is found nowhere in our data
        else:
            print("Sorry, but this entry wasn't recognized. Enter 'help' for more information")
        
    return player

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For other operating systems (Linux, macOS)
    else:
        _ = os.system('clear')

def entry():
    prompt()
    try: 
        # Attempt to translate the input
        return translate(lexinput())
    
    # The current level doesn't have any correct input available
    # Caused by mistakes in the dictionary 'correct' or unfinished level 
    except KeyError:
        error("Input can't be accepted")
        # Remove the last level as it will create an infinite loop
        del L[-1]
        
# Show relevant information
def prompt():
    if L[-1] == "inventory":
        print("Inventory")
        for i in player.inventory:
            print(full_item_print(i))
    elif L[-1] == "player":
        print(character_print(player))
        for i in player.equipped_items:
            print(full_item_print(i))
        print("Total player's defense :",full_stat("defense"))

# Dynamic input function changing with current level
def lexinput():
    u=""
    # Write the current levels
    for i, v in enumerate(L):
        if i == len(L) - 1:
            u+= v + ">"
        else:
            u+= v + "/"
    return input(u).lower()
    
def translate(ans):
    command_parts = ans.split()
    command_name = command_parts[0]
    
    for i in end_correct:
        try :
            
            # Input is found within the lists to translate
            if ans in end_correct[i]:
                return i
        # Input isn't found in said lists, can still be a correct input
        except TypeError:
            continue
        
    for i in correct[L[-1]]:
        try :
            
            # Input is found within the lists to translate
            if command_name in correct[L[-1]][i]:
                command_parts[0] = i
                return " ".join(command_parts)
        # Input isn't found in said lists, can still be a correct input
        except TypeError:
            continue 
    
    return ans

# Give a list of possible entries
def lexhelp():
    try:
        print("\nHere is the list of entries possible:\n", ", ".join(sorted((correct[L[-1]]))))
    
    except KeyError:
        error("Help list not found")
        
# Give a list of aliases
def alias():
    
    temp_alias = {k: v for k, v in correct[L[-1]].items() if v is not None}
    if temp_alias != {}:
        print("\nHere is the list of aliases")
    else:
        print("There is no current aliases")
    for i in sorted(temp_alias):
        print(str(i)+":",", ".join(sorted(temp_alias[i])))

def error(message):
    print("\n" + Color.sys_red + "Lexerror " + Color.sys_purple + message + "\033[39m")
    
#--------------------The game functions--------------------#
def create_item():
    global created_items
    item = Equippable()
    created_items.append(item)
    return item

# Return a simple colored string with the item symbol and name
def item_print(item):
    return (f"\x1b[38;2;{item.color[0]};{item.color[1]};{item.color[2]}m"
          f"▣ "
          f"{Color.rarity_colors[item.rarity]}"
          f"{item.name}" 
          f"\033[39m"
          )
    
# Return an advance colored string with the item symbol, name, id, and stats
def full_item_print(item):
    return (f"\x1b[38;2;{item.color[0]};{item.color[1]};{item.color[2]}m"
          f"▣ " 
          f"{Color.rarity_colors[item.rarity]}"
          f"{item.name}" 
          f"\033[39m"
          f" ["
          f"{str(item.item_id)}"
          f"]\n"
          f"{str(item.stats['defense'])}"
          f" defense\n"
          )

# Return a simple colored string the character's name
def character_print(character):
    return (f"\x1b[38;2;{character.color[0]};{character.color[1]};{character.color[2]}m"
            f"{character.name}"
            f"\033[39m"
            )
    
# Give a certain amount of items to the player
def open_chest(x):
    print(f"Woaw you found a chest of {str(x)} items!")
    for _ in range(x):
        item = create_item()
        player.add_inventory(item)
        print(item_print(item))
        
# Return the total stats of the player from their gears
def full_stat(stat_type):
    return sum(item.stats[stat_type] for item in player.equipped_items)

# Calculate and gives damage to any character
def receive_damage(character,damage):
    actual_damage = max (0, damage - full_stat("defense"))
    print(character_print(character),"receive",actual_damage,"damage")
    character.current_health -= actual_damage 

#--------------------Dictionaries--------------------#
# Types of items
item_types = {
    "equipable":[
        "helmet",
        "chestpiece",
        "gloves",
        "pants",
        "boots"
    ]
}

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

# List of possible entries
correct = {
    # Level1
    "progen":{
        None
    },
    
    # Level2
    "inventory":{
        "Player.equip_item_with_id":["equip"],
        "Player.remove_inventory_with_id":["discard"]
    },
    
    "player":{
        "Player.unequip_item_with_id":["unequip"],
    }
}

# The menues
end_correct = {
    "inventory":["inv"],
    "player":["plr"],
    "stats":None

}

# List of functions that affect the player and that the user needs to put one argument
end_functions_player_1arg = {
    "end_fun":[Player.equip_item_with_id, Player.unequip_item_with_id, Player.remove_inventory_with_id],
    "end_fun_name":[]
    }
for i in end_functions_player_1arg["end_fun"]:
    end_functions_player_1arg["end_fun_name"].append("Player."+i.__name__)
    
current_floor=0
current_room=0
    
# Initialise if the script is executed
if __name__ == "__main__":
    L = ["progen"]
    player = Player()
    
    main()
    
#Todo
