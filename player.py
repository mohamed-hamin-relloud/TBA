# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []

    def deplacer_player(self, newroom):
        self.newroom= newroom
    
    def get_history(self):
        if self.current_room is None:
            return "le joueur n'a pas encore commencer à explorer."
        if self.current_room in self.historique_room:
            message= "vous avez déjà visité les pièces suivantes:\n"
            message+= ",".join(self.historique_room)
            return message
        else:
            self.historique_room.add(self.current_room)
            message= f"vous êtes dans la pièce :{self.current_room}\n"
            message+= "vous pouvez aller dans les directions suivantes : nord, sud,est, ouest."
            return message

    def get_history(self):
        set_history = set(self.history)
        print("vous avez visité les lieux suivant :\n")
        for i in set_history:
            print(f"\t {i.description}") 
        return " "
       
    
                    
        
       
    

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
       
        if direction = 

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        print(self.get_history())
        return True

    