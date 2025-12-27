# Define the Room class.

from player import Item

class Room:

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = []

    # Define the inventory of the current room

        
    
    # Define the get_exit method.
    def get_exit(self, direction):
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
    
    def get_inventory(self):
        if not self.inventory:
            return "Il n'y a rien ici."
        items_str = "\n".join(f"    - {item}" for item in self.inventory)
        return f"La pièce contient :\n{items_str}"
    
    def add_item(self, item: Item):
        self.inventory.append(item)

    def take(self, item_name, player):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                self.inventory.remove(item)
                player.inventory.append(item)
                return True
        return False

    def drop(self, item_name, player):
        """Permet de déposer un objet de l'inventaire du joueur dans la pièce."""
        for item in player.inventory:
            if item.name.lower() == item_name.lower():
                player.inventory.remove(item)
                self.inventory.append(item)
                return True
        return False
    
    def check_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                return True
        return False

