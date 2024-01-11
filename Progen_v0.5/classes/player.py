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
        print("Id not found in inventory")
            
    def unequip_item_with_id(self,num):
        for i in self.equipped_items:
            if i.item_id == int(num):
                self.unequip_item(i)
                return None
        print("Id not found in inventory")
    
    def remove_inventory_with_id(self,num):
        for i in self.inventory:
            if i.item_id == int(num):
                self.remove_inventory(i)
                return None
        print("Id not found in inventory")