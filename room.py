# Define the Room class.

class Room:

    # Define the constructor. 
    def __init__(self, name, description, inventory = None, characters = None):
        self.name = name
        self.description = description
        self.exits = {}
        if not inventory:
            self.inventory = {}
        else:
            self.inventory = inventory
        if not characters:
            self.characters = {}
        else:
            self.characters = characters
        

        

    # Define the inventory of the current room
    def get_inventory(self):
        dict_inventory= self.inventory
        dict_character = self.characters
        if dict_inventory == {} and dict_character == {}:
            return "il n'y a rien ici"
        print("la pièce contient :\n")
        for i in dict_inventory:
            if i == None:
                continue
            else :
                print(f"\t {dict_inventory.get(i).description}")
        for i in dict_character:
            if i == None:
                continue
            else:
                print(f"\t {dict_character.get(i).description}")
        return ""

        
    
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
