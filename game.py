# Description: Game class

# Import modules

from room import Room
from player import Player, Item
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
        Directions = ['nord', 'sud', 'ouest', 'est', 'up','down']

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        look = Command("look", " : regarder autour de vous", Actions.look, 0)

        direction_description = "(N, S, E, O, U, D)" + str(Directions)
        go = Command("go", " <direction> : se déplacer dans une direction cardinale "+direction_description, Actions.go, 1)
        back = Command("back", "reviens en arriere", Actions.back, 0)
        directions = set(Directions)
        directions.add("go")
        # self.commands = dict([(Directions[i], go) for i in range(6)])
        self.commands["go"] = go
        self.commands["help"] = help
        self.commands["quit"] = quit
        self.commands["back"] = back
        self.commands["look"] = look
       

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

        self.rooms = [hall, diningroom, cave, kitchen, coldroom, livingroom, library, stairs]
        torch = Item("torch", "une torche en bois qui éclaire faiblement", 1.5)
        chandelier = Item("chandelier","un grand chandelier en fer forgé suspendu au plafond", 5.0)
        ancient_book = Item("ancient_book", "il y a plein d'anciens livres déposés sur des étagères", 10.0)
        silver_knife = Item("silver_knife", "un couteau en argent finement ouvragé", 0.3)
        rusty_key = Item("rusty_key", "une clé rouillée qui semble ancienne", 0.1)
        wooden_chest = Item("wooden_chest", "un coffre en bois verrouillé", 10.0)
        wine_bottle = Item("wine_bottle", "une bouteille de vin scellée, étiquetée d'une année lointaine", 1.2)
        old_map = Item("old_map", "une carte dessiné à la main, montrant des lieux inconnus", 0.2)
        candle = Item("candle", "une bougie à moitié consumée", 0.1)
        frying_pan = Item("frying_pan", "une poêle en fonte lourde et bien usée", 2.5)
        frozen_meat = Item("frozen_meat", "un morceau de viande gelée, encore comestible", 1.8)
        painting = Item("painting", "un tableau représentant un paysage mystérieux", 1.0)
        fireplace_poker = Item("fireplace_poker", "un tisonnier en métal pour la cheminée", 1.5)

        hall.add_item(chandelier)
        hall.add_item(old_map)

        diningroom.add_item(silver_knife)
        diningroom.add_item(wine_bottle)

        cave.add_item(torch)
        cave.add_item(rusty_key)
        cave.add_item(wooden_chest)

        kitchen.add_item(frying_pan)
        kitchen.add_item(candle)

        coldroom.add_item(frozen_meat)

        livingroom.add_item(fireplace_poker)
        livingroom.add_item(painting)

        library.add_item(ancient_book)


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
    
    def look(self):
        """Affiche les détails de la pièce actuelle."""
        if self.current_room:
            self.current_room.look()
        else:
            print("Vous n'êtes nulle part.")#Cela signifie que le joueur n'a pas encore été placé dans une pièce de la map.


    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()

