class Player:
    def __init__(self, name):
        self.name = name
        self.color = [207, 133, 214]
        
        self.max_hp = 200
        self.current_hp = self.max_hp
        
        self.exp = 0
        self.level = 1
    
        self.gold = 0    
    
        self.equipped_items = {
            "helmet" : None,
            "chestpiece" : None,
            "gloves" : None,
            "pants" : None,
            "boots" : None,
            "weapon" : None
        }
        
        
        
    def equip_item(self,item):
        self.equipped_items.append(item)