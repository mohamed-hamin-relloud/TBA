# Define the Room class.

from item import Item
from copy import deepcopy
from door import Door

class Room:

    # Define the constructor. 
    def __init__(self, name, description, items=None, dark=False, door = None):
        self.name = name
        self.description = description
        self.exits = {}
        self.dark = dark  # Pièce sombre ou éclairée
        if not items:
            self.inventory = {}
        else:
            self.inventory = items
        self.characters = {}
        self.monsters = {}
        self.door = door if door is not None else []
        
        


    # Define the inventory of the current room
    def get_inventory(self):
        if getattr(self, 'dark', False):
            return "Il fait trop sombre pour voir les objets ici."
        dict_inventory= self.inventory
        if dict_inventory == {}:
            return "il n'y a rien ici"
        print("\nOn voit :")
        for i in dict_inventory:
            print(f"\t {dict_inventory.get(i).name} : {dict_inventory.get(i).description} ({dict_inventory.get(i).weight} kg)")
        if self.characters == {} and self.monsters == {}:
            pass
        else:
            for i in self.characters:
                print(f"\t {self.characters.get(i).name} : {self.characters.get(i).description}")
            for j in self.monsters:
                print(f"\t {self.monsters.get(j).name} : {self.monsters.get(j).description}")
        print("")  
        return True
        

        
    
    # Define the get_exit method.
    def get_exit(self, direction):
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for key, value in self.exits.items():
            if value is not None:
                # Si la sortie est une Door, indiquer si elle est verrouillée
                if isinstance(value, Door) and value.locked:
                    exit_string += f"{key} (verrouillée), "
                else:
                    exit_string += f"{key}, "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        
        if getattr(self, 'dark', False):
            return "\nIl fait très sombre ici. Vous pouvez à peine distinguer les contours.\n\n" + self.get_exit_string() + "\n"
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
    

    def add_item(self, item):
        self.inventory[item.name] = item


    def take(self, item_name, player):
        item = self.inventory.get(item_name.lower())
        if item is None:
            return False
        del self.inventory[item_name.lower()]
        player.inventory[item_name.lower()] = item
        return True

    def drop(self, item_name, player):
        """Permet de déposer un objet de l'inventaire du joueur dans la pièce."""
        item = player.inventory.get(item_name.lower())
        if item is None:
            return False
        del player.inventory[item_name.lower()]
        self.inventory[item_name.lower()] = item
        return True
    
    def check_item(self, item_name):
        if item_name.lower() in self.inventory:
            return True
        return False
    






