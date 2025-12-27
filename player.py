# Define the Player class.
from item import Item

class Player():

    # Define the constructor.
    def __init__(self, name, history = None):
        self.name = name
        self.current_room = None
        self.inventory = []
        if not history:
            self.history = []
        else:
            self.history = history

            
    def get_history(self):
        set_history = set(self.history)
        print("vous avez visité les lieux suivant :\n")
        for i in set_history:
            if i == None:
                continue
            else :
                print(f"\t {i.description}")
        return ""
       
    
       
    

    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        Directions = ['NORD','Nord','nord','n','N', "S", 'sud','s','Sud','SUD', "O", 'o', 'ouest', 'Ouest','OUEST','E', 'e','est','EST', 'Est', "U", 'u', 'up', 'Up', 'UP',"D", 'd','down','Down', 'DOWN']
        if direction not in Directions:
            print(f"la commande {direction} n'est pas valide ! Vous ne vous déplacez.")
            return None
        direction = direction[0].upper()
        next_room = self.current_room.exits[direction]
        self.history.append(next_room)

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        print(self.get_history())
        return True
    
    def get_inventory(self):
        if not self.inventory:
            return "Votre inventaire est vide."
        items_str = "\n".join(f"    - {item}" for item in self.inventory)
        return f"Vous disposez des items suivants :\n{items_str}"
