"""----------This is the progen v.0.2 documentation----------
Progen - Item Generator Script

Author: Lexelis
Date: 24/01/09
Version: 0.2

Description:
This script generates and displays equippable items for a player.



General inputs:
    
        
Version : 0.2
"""

#--------------------Import--------------------#
import random
from colorama import Fore

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
        return random.choices(["white","green","blue","purple","yellow"], weights=[0.6, 0.3, 0.2, 0.01, 0.001], k=1)[0]
    
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
        for i in self.inventory:
            if i.item_id == num:
                self.equip_item(i)
                return None
        error("Id not found in inventory")
            
    def unequip_item_with_id(self,num):
        for i in self.equipped_items:
            if i.item_id == num:
                self.unequip_item(i)
                return None
        error("Id not found in inventory")
    
    def remove_inventory_with_id(self,num):
        for i in self.inventory:
            if i.item_id == num:
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
                    
            # Print the player's inventory
            if ans == "inventory":
                print("\nInventory")
                for i in range(len(player.inventory)):
                    print(full_item_print(player.inventory[i]))
                    
            elif ans == "player":
                print("\n"+character_print(player))
                for i in range(len(player.equipped_items)):
                    print(full_item_print(player.equipped_items[i]))
                print("Total player's defense :",full_stat("defense"))
        
        # Input is accepted
        elif ans in correct[L[-1]]:
            
            # Input activates a command
            if ans in end_functions["end_fun_name"]:
                end_functions["end_fun"][end_functions["end_fun_name"].index(ans)]()
                    
            # Input is already a used values and goes to another level
            else:
                L.append(ans)
                
        # User asks for help
        elif ans == "help":
            lexhelp()
        
        # User asks for aliases
        elif ans == "alias":
            alias()
            
        # Input is found nowhere in our data
        else:
            print("Sorry, but this entry wasn't recognized. Enter 'help' for more information")
        
    return player

def entry():
    try: 
        # Attempt to translate the input
        return translate(lexinput())
    
    # The current level doesn't have any correct input available
    # Caused by mistakes in the dictionary 'correct' or unfinished level 
    except KeyError:
        error("Input can't be accepted")
        # Remove the last level as it will create an infinite loop
        del L[-1]

# Dynamic input function changing with current level
def lexinput():
    u="\n"
    # Write the current levels
    for i in range(len(L)):
        if i == len(L) - 1:
            u+= L[i] + ">"
        else:
            u+= L[i] + "/"
    return input(u).lower()

def error(message):
    print("\n" + Color.sys_red + "Lexerror " + Color.sys_purple + message + "\033[39m")
    
def translate(ans):
    
    for i in end_correct:
        try :
            
            # Input is found within the lists to translate
            if ans in end_correct[i]:
                return i
                break
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
    
#--------------------The game functions--------------------#
    
def create_item():
    global created_items
    item = Equippable()
    created_items.append(item)
    return item

def item_print(item):
    return ("\x1b[38;2;{};{};{}m".format(item.color[0],item.color[1],item.color[2]) 
          + "▣ " 
          + Color.rarity_colors[item.rarity]
          + item.name 
          + "\033[39m"
          )
    
def full_item_print(item):
    return ("\x1b[38;2;{};{};{}m".format(item.color[0],item.color[1],item.color[2]) 
          + "▣ " 
          + Color.rarity_colors[item.rarity]
          + item.name 
          + "\033[39m"
          +" ["
          +str(item.item_id)
          +"]\n"
          +str(item.stats["defense"])
          +" defense\n"
          )

def character_print(character):
    return ("\x1b[38;2;{};{};{}m".format(character.color[0],character.color[1],character.color[2]) 
            + character.name 
            + "\033[39m"
            )
    
def open_chest(x):
    print("Woaw you found a chest of "+str(x)+" items!")
    for _ in range(x):
        item = create_item()
        player.add_inventory(item)
    
    for i in range(len(created_items)):
        print(item_print(created_items[i]))
        
def full_stat(stat_type):
    return sum(item.stats[stat_type] for item in player.equipped_items)


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
    "main":{
        "combat"
    },
    
    # Level2
    "inventory":{
        "player.equip_item()":["equip"]
            }
}

# The menues
end_correct = {
    "inventory":["inv"],
    "player":["plr"],
    "stats":None

}

if __name__ == "__main__":
    L = ["main"]
    player = Player()
    
    # List functions that won't make main() move forward
    end_functions = {
        "end_fun":[player.equip_item_with_id, player.unequip_item_with_id, player.remove_inventory_with_id],
        "end_fun_name":[]
        }
    
    main()
    
#Todo
