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