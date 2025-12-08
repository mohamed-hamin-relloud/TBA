# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        Directions = ['nord', 'sud', 'ouest', 'est', 'up','down']
        directions = { Directions[i] for i in range(6)}
        directions.add("go")
        self.commands = dict([(Directions[i], go) for i in range(6)])
        self.commands["go"] = go
        self.commands["help"] = help
        self.commands["quit"] = quit
       

        hall = Room("Hall", "dans une grande salle de receptions reliant beaucoup de piece entre elles.")
        self.rooms.append(hall)
        diningroom = Room("Diningroom", "dans une immense salle avec une grande table rectangulaire et des dizaines de chaises anciennes.")
        self.rooms.append(diningroom)
        cave = Room("Cave", "dans une cave où il fait très sombre et où l'atmosphère pensant, une menace à l'air de planer autour de nous.")
        self.rooms.append(cave)
        kitchen = Room("Kitchen", "dans une cuisine où l'odeur des plats est reconfortant, on peut y voir des ustensiles en fonte et en bronze.")
        self.rooms.append(kitchen)
        coldroom = Room("Coldroom", "dans une chambre froide où la nourriture est stockée, l'endroit est assez préoccupant.")
        self.rooms.append(coldroom)
        livingroom = Room("Livingroom", "dans une grande salle avec des canapé, une cheminée et un endroit pour grignotter avec des meubles rustiques.")
        self.rooms.append(livingroom)
        library = Room("Library", "dans une énorme bibliothèque avec plusieurs étages et des livres qui paraissent très ancien.")
        self.rooms.append(library)
        stairs = Room("Stairs", "un grand esclalier reliant l'étage au hall d'entrée fait de marbre et de bois ancien.")
        self.rooms.append(stairs)

        # Create exits for rooms

        hall.exits = { "N" : None, "E" : livingroom, "S" : None, "O" : diningroom , "U" : None, "D" : None}
        diningroom.exits = {"N" : kitchen, "E" : hall,  "S" : None,"O" : None, "U" : None, "D" : None}
        livingroom.exits = { "N" : None, "E" : None,  "S" : None, "O" : hall, "U" : None, "D" : None}
        cave.exits = { "N" : None , "E" : None,  "S" : None, "O" : coldroom,"U" : None, "D" : None}
        kitchen.exits = { "N" : coldroom , "E" : None, "S" : diningroom, "O" : None, "U" : None, "D" : None}
        coldroom.exits = { "N" : None,  "S" : kitchen, "O" : None, "U" : None, "D" : None}
        library.exits = { "N" : None , "E" : None,  "S" : None,  "O" : hall, "U" : None, "D" : None}
        stairs.exits = { "N" : None, "E" : None, "S" : hall, "O" : None, "U" : None, "D" : None}
        
        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = hall

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input(">"))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        
        # If the command is not recognized, print an error message
        if command_word=="":
            print(f"\n ")
        elif command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
