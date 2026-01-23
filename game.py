# Description: Game class

# Import modules

from room import Room
from player import Player
from item import Item, Beamer, Key, Torch
from command import Command
from actions import Actions
from item import Item
from character import Character
from quest import Quest

DEBUG = True

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.character = None
        
    

    
    # Setup the game
    def setup(self, player_name=None):

        self._setup_commands()
        self._setup_rooms()
        self._setup_player(player_name)
        self._setup_quests()

        

    def _setup_commands(self):
        # Setup commands
        
        Directions = ['nord', 'sud', 'ouest', 'est', 'up','down']

        go = Command("go", " <direction> : se déplacer dans une direction cardinale <N,S,O,E,U,D>", Actions.go, 1)
        back = Command("back", "reviens en arriere", Actions.back, 0)
        talk = Command('talk', 'parler avec les PNJ', Actions.talk, 1)
        help = Command("help", " : afficher cette aide", Actions.help, 0)
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        look = Command("look", " : regarder autour de vous", Actions.look, 0)
        take = Command("take", " <item> : prendre un objet", Actions.take, 1)
        drop = Command("drop", " <item> : déposer un objet", Actions.drop, 1)
        check= Command("check", " : vérifier l'inventaire", Actions.check, 0)
        beamer= Command("beamer", " : utiliser le beamer pour se téléporter", Actions.use_beamer, 0)
        charge = Command("charge", " : charger le beamer dans la pièce courante", Actions.charge, 0)
        use = Command("use", " <item> : utiliser un objet (ex: use key, use beamer)", Actions.use, 1)

        
        # self.commands = dict([(Directions[i], go) for i in range(6)])
        self.commands["go"] = go
        self.commands["help"] = help
        self.commands["quit"] = quit
        self.commands["back"] = back
        self.commands["look"] = look
        self.commands["take"] = take
        self.commands["drop"] = drop
        self.commands["talk"] = talk
        self.commands["check"] = check
        self.commands["beamer"] = beamer
        self.commands["charge"] = charge
        self.commands["use"] = use
        self.commands["quests"] = Command("quests"
                                          , " : afficher la liste des quêtes"
                                          , Actions.quests
                                          , 0)
        self.commands["quest"] = Command("quest"
                                         , " <titre> : afficher les détails d'une quête"
                                         , Actions.quest
                                         , 1)
        self.commands["activate"] = Command("activate"
                                            , " <titre> : activer une quête"
                                            , Actions.activate
                                            , 1)
        self.commands["rewards"] = Command("rewards"
                                           , " : afficher vos récompenses"
                                           , Actions.rewards
                                           , 0)


        
             
       
     
        
        
        
        
    def _setup_rooms(self):    

        #Create Room 

        hall = Room("Hall", "dans une grande salle de receptions reliant beaucoup de piece entre elles.")
        self.rooms.append(hall)
        diningroom = Room("Diningroom", "dans une immense salle avec une grande table rectangulaire et des dizaines de chaises anciennes.")
        self.rooms.append(diningroom)
        cave = Room("Cave", "dans une cave où il fait très sombre et où l'atmosphère pensant, une menace à l'air de planer autour de nous.", dark=True)
        self.rooms.append(cave)
        kitchen = Room("Kitchen", "dans une cuisine où l'odeur des plats est reconfortant, on peut y voir des ustensiles en fonte et en bronze." )
        self.rooms.append(kitchen)
        coldroom = Room("Coldroom", "dans une chambre froide où la nourriture est stockée, l'endroit est assez préoccupant.")
        self.rooms.append(coldroom)
        livingroom = Room("Livingroom", "dans une grande salle avec des canapé, une cheminée et un endroit pour grignotter avec des meubles rustiques.")
        self.rooms.append(livingroom)
        library = Room("Library", "dans une énorme bibliothèque avec plusieurs étages et des livres qui paraissent très ancien.")
        self.rooms.append(library)
        stairs = Room("Stairs", "un grand esclalier reliant l'étage au hall d'entrée fait de marbre et de bois ancien.")
        self.rooms.append(stairs)


        hall.exits = { "N" : None, "E" : livingroom, "S" : None, "O" : diningroom , "U" : None, "D" : None}
        diningroom.exits = {"N" : kitchen, "E" : hall,  "S" : None,"O" : None, "U" : None, "D" : None}
        livingroom.exits = { "N" : None, "E" : None,  "S" : None, "O" : hall, "U" : None, "D" : None}
        cave.exits = { "N" : None , "E" : None,  "S" : None, "O" : None,"U" : None, "D" : None}
        kitchen.exits = { "N" : coldroom , "E" : None, "S" : diningroom, "O" : None, "U" : None, "D" : None}
        coldroom.exits = { "N" : None,  "S" : kitchen, "O" : None, "U" : None, "D" : None}
        library.exits = { "N" : None , "E" : None,  "S" : None,  "O" : hall, "U" : None, "D" : None}
        stairs.exits = { "N" : None, "E" : None, "S" : hall, "O" : None, "U" : None, "D" : None}

     #Create Item

        sword = Item("sword", "épée lourde ressemblant à celle des rois d'antan...",20)
        orbe_de_vie = Item("orbe de vie", "orbe rayonnant une énergie vitale débordante...",9)
        grimoire = Item("grimoire", "gros livre poussièreux en cuire", 6)
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
        goldenkey = Item("Clé", "Clé lourde et dorée", 0.5)
        beamer_item = Beamer()
        key_for_cave = Key('cave_door')
        torch = Torch() 
        
        # Add Item to Room
        hall.add_item(chandelier)
        hall.add_item(old_map)
        
        
        # Add Item to Hall
        hall.add_item(beamer_item)
        
        
        # Add Item to Coldroom
        coldroom.add_item(key_for_cave)
        coldroom.add_item(frozen_meat)

        
        # Add Item to Diningroom
        diningroom.add_item(silver_knife)
        diningroom.add_item(wine_bottle)
        diningroom.add_item(goldenkey)

        
        # Add Item to Cave
        cave.add_item(torch)
        cave.add_item(rusty_key)
        cave.add_item(wooden_chest)

        
        
        # Add Item to Kitchen
        kitchen.add_item(frying_pan)               
        kitchen.add_item(candle)
        kitchen.add_item(sword)
        kitchen.add_item(orbe_de_vie)

        
        # Add Item to Livingroom
        livingroom.add_item(fireplace_poker)
        livingroom.add_item(painting)

        # Add Item to Library
        library.add_item(ancient_book)
        library.add_item(grimoire)

        
        # Create characters
        chief = Character("Chief-cook", "un homme avec une toque", kitchen, ['bonjour cher convive',"à vos fourneaux !", "donnez la poule !"])
        kitchen.characters[chief.name] = chief
       

        # Création d'une porte verrouillée entre coldroom (N) et cave (S)

        
        # Setup player and starting room


        
    def pnj_move(self):
        for salle in list(self.rooms):
            for pnj in list(salle.characters):
                salle.characters.get(pnj).move()

    def _setup_player(self, player_name=None):
        """Initialize the player."""
        if player_name is None:
            player_name = input("\nEntrez votre nom: ")

        self.player = Player(player_name)
        self.player.current_room = self.rooms[0]  # swamp

    def _setup_quests(self):
        """Initialize all quests."""
        search_quest = Quest(
            title="Clé",
            description="Trouvez la Clé.",
            objectives=["prendre Clé"],
            reward="Le dénicheur de Clé"
        )

        fightmonster_quest = Quest(
            title="Le Combattant",
            description="Partez à la Recherche d'un Monstre",
            objectives=["Vaincre le Monstre"],
            reward="Le tueur de Monstre"
        )

        discovery_quest = Quest(
            title="Découvreur de Secrets",
            description="Découvrez les trois lieux les plus mystérieux.",
            objectives=["Visiter Cave"
                        , "Visiter Chambre Froide"
                        , "Visiter Library"],
            reward="Clé dorée"
        )

        # Add quests to player's quest manager
        self.player.quest_manager.add_quest(search_quest)
        self.player.quest_manager.add_quest(fightmonster_quest)
        self.player.quest_manager.add_quest(discovery_quest)

        # Activate quests by default
        self.player.quest_manager.activate_quest("Clé")
        self.player.quest_manager.activate_quest("Le Combattant")
        self.player.quest_manager.activate_quest("Découvreur de Secrets")



       
       

        
        


    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input(">"))
            self.pnj_move()

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

