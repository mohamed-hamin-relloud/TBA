# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name, history = None, max_weight = 30):
        self.name = name
        self.current_room = None
        self.max_weight = max_weight
        self.inventory = {}
        if not history:
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
        next_room = self.current_room.exits[direction]
        
        if self.history == []:
            self.history.append(self.current_room)
            


        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        else:
            self.history.append(next_room)
        

        
            
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        print(self.get_history())
        return True

    