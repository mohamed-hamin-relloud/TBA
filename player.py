# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
    
    def convert(self, s):
        if self.s == self.s[0] or self.s[0].upper() or self.s[0].lower or self.s.upper() or self.s.lower() or self.s:
            self.s = self.s[0].upper()
            return self.s
        
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        Directions = ['NORD','Nord','nord','n','N', "S", 'sud','s','Sud','SUD', "O", 'o', 'ouest', 'Ouest','OUEST','E', 'e','est','EST', 'Est', "U", 'u', 'up', 'Up', 'UP',"D", 'd','down','Down', 'DOWN']
        if direction not in Directions:
            print(f"la commande {direction} n'est pas valide ! Vous ne vous déplacez.")
            return None
        direction = direction[0].upper()
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    