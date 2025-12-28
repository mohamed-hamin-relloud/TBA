# Define the Door helper used to represent an exit that can be locked.
class Door:
    """Représente une porte vers une autre salle.

    Attributes:
        room (Room): la salle vers laquelle la porte mène
        id (str|None): identifiant optionnel de la porte (utile pour les clés)
        locked (bool): indique si la porte est verrouillée
    """
    def __init__(self, room, door_id: str | None = None, locked: bool = False):
        self.room = room
        self.id = door_id
        self.locked = locked

    def __repr__(self):
        state = "verrouillée" if self.locked else "ouverte"
        return f"Door({self.room.name}, id={self.id}, {state})"


# Define the Room class.

from item import Item

class Room:

    # Define the constructor. 
    def __init__(self, name, description, items=None, dark=False):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = items if items else []
        self.dark = dark  # Pièce sombre ou éclairée

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
    


