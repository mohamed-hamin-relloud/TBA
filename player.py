# Define the Player class.
from item import Item, Beamer
from room import Door

class Player():

    # Define the constructor.
    def __init__(self, name, current_room=None, history=None, max_weight=10.0):
        """Initialise le joueur.

        Args:
            name (str): nom du joueur
            current_room (Room|None): salle de départ
            history (list|None): historique des pièces visitées
            max_weight (float): capacité de portage maximale en kg
        """
        self.name = name
        self.current_room = current_room
        self.max_weight = max_weight
        self.current_weight = 0
        self.inventory = {}
        if history is None:
            self.history = []
        else:
            self.history = [d for d in self.history if d is not None]

        
       

            
    def get_history(self):
        print("vous avez visité les lieux suivant :\n")
        for i in self.history[:len(self.history)-1]:
            if i == None:
                continue
            else :
                print(f"\t {i.description}")
        return ""
       
    
    def get_inventory(self):
        inventory = self.inventory
        if inventory == {}:
            print("votre inventaire est vide")
            return False
        else:
            return f"Vous disposez des items suivants :\n {inventory.get()}"
    
       
    

    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        Directions = ['NORD','Nord','nord','n','N', "S", 'sud','s','Sud','SUD', "O", 'o', 'ouest', 'Ouest','OUEST','E', 'e','est','EST', 'Est', "U", 'u', 'up', 'Up', 'UP',"D", 'd','down','Down', 'DOWN']
        if direction not in Directions:
            print(f"la commande {direction} n'est pas valide ! Vous ne vous déplacez.")
            return None
        direction = direction[0].upper()
        next_exit = self.current_room.exits.get(direction)
        
        if self.history == []:
            self.history.append(self.current_room)
            

        # If the next exit is None, print an error message and return False.
        if next_exit is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        # If the exit is a Door, check its lock state and get the target room
        if isinstance(next_exit, Door):
            if next_exit.locked:
                print("\nLa porte est verrouillée.\n")
                return False
            next_room = next_exit.room
        else:
            next_room = next_exit

        # Record visit in history and move
        self.history.append(next_room)
        self.current_room = next_room
        print(self.current_room.get_long_description())
        print(self.get_history())
        return True
    
    def get_inventory(self):
        if not self.inventory:
            return f"Votre inventaire est vide. Poids actuel: {self.current_weight}/{self.max_weight} kg."
        items_str = "\n".join(f"    - {item}" for item in self.inventory)
        return f"Vous disposez des items suivants :\n{items_str}\nPoids actuel: {self.current_weight}/{self.max_weight} kg." 
    
    def use_beamer(self):
        for item in self.inventory:
            if isinstance(item, Beamer):
                return item.use(self)
        return "Vous ne possédez pas de beamer."
