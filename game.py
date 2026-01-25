# Description: Game class

# Import modules

from room import Room
from player import Player
from item import Item, Beamer, Key, Torch, Weapon, Book, InvisibilityCloak, Desintegrator
from command import Command
from actions import Actions
from character import Character, Monster
from quest import Quest
from door import Door


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
        back = Command("back", "revenir en arriere", Actions.back, 0)
        talk = Command('talk', ' <PNJ> : parler avec un PNJ', Actions.talk, 1)
        help = Command("help", " : afficher cette aide", Actions.help, 0)
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        look = Command("look", " : regarder autour de vous", Actions.look, 0)
        take = Command("take", " <item> : prendre un objet", Actions.take, 1)
        drop = Command("drop", " <item> : déposer un objet", Actions.drop, 1)
        check= Command("check", " : vérifier l'inventaire", Actions.check, 0)
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
        self.commands["fight"] = Command("fight"
                                         , " <ennemi>: combattre l'ennemi"
                                         , Actions.fight
                                         , 1)
        self.commands["equip"] = Command("equip"
                                         , " <weapon> : s'équiper de l'arme weapon"
                                         , Actions.equip
                                         , 1)
        self.commands["read"] = Command("read"
                                         , " <livre> : lire un livre"
                                         , Actions.read
                                         , 1)
        self.commands["status"] = Command("status",
                                          " : afficher l'état de santé du joueur",
                                          Actions.status, 0)

        
             
       
    

        
       
        
        
        
        
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
        clearence = Room("Clearence", "un débarras sombre et rempli d'objets, vous entendez du bruit, sûrement des rats...")
        self.rooms.append(clearence)
        laboratory = Room('Laboratory', "un laboratoire de science avec des machines, ordinateurs, celui à qui appartenait ce laboratoire devait être brillant...")
        self.rooms.append(laboratory)
        
        
        #Create doors
        door_1 = Door(0x01, library, clearence, locked=True)
        library.door.append(door_1)
        clearence.door.append(door_1)
        door_2 = Door(0x02, hall, diningroom, locked=True)
        hall.door.append(door_2)
        diningroom.door.append(door_2)
        door_3 = Door(0x03, coldroom, cave, locked=True)
        coldroom.door.append(door_3)
        cave.door.append(door_3)
        door_4 = Door(0x04, livingroom, laboratory, locked=True)
        livingroom.door.append(door_4)
        laboratory.door.append(door_4)

        hall.exits = { "N" : library, "E" : livingroom, "S" : None, "O" : diningroom , "U" : None, "D" : None}
        diningroom.exits = {"N" : kitchen, "E" : hall,  "S" : None,"O" : None, "U" : None, "D" : None}
        livingroom.exits = { "N" : None, "E" : laboratory,  "S" : None, "O" : hall, "U" : None, "D" : None}
        cave.exits = { "N" : None , "E" : None,  "S" : None, "O" : coldroom,"U" : None, "D" : None}
        kitchen.exits = { "N" : coldroom , "E" : None, "S" : diningroom, "O" : None, "U" : None, "D" : None}
        coldroom.exits = { "N" : None,  "S" : kitchen, "O" : None, "E" : cave, "U" : None, "D" : None}
        library.exits = { "N" : None , "E" : clearence,  "S" : hall,  "O" : None, "U" : None, "D" : None}
        clearence.exits = { "N" : None, "E" : None, "S" : None, "O" : library, "U" : None, "D" : None}
        laboratory.exits = { "N" : None, "E" : None, "S" : None, "O" : livingroom, "U" : None, "D" : None}

        


        #Create Item

        orbe_de_vie = Item("orbe de vie", "orbe rayonnant une énergie vitale débordante...",9)
        grimoire = Book("grimoire", "gros livre poussièreux en cuire", 1.2, 600, "Ce grimoire ancien contient des sorts puissants et des connaissances oubliées depuis longtemps.")
        chandelier = Item("chandelier","un grand chandelier en fer forgé suspendu au plafond", 5.0)
        ancient_book = Book("ancient_book", "il y a plein d'anciens livres déposés sur des étagères", 0.95, 300, "Ce livre ancien parle des mystères de l'univers et des civilisations perdues.")
        silver_knife = Weapon("silver_knife", "un couteau en argent finement ouvragé", 0.3, 9)
        rusty_key = Key("rusty_key", "une clé rouillée qui semble ancienne", 0.1, 0x04)
        wooden_chest = Item("wooden_chest", "un coffre en bois verrouillé", 10.0)
        wine_bottle = Item("wine_bottle", "une bouteille de vin scellée, étiquetée d'une année lointaine", 1.2)
        old_map = Item("old_map", "une carte dessiné à la main, montrant des lieux inconnus", 0.2)
        candle = Item("candle", "une bougie à moitié consumée", 0.1)
        frying_pan = Item("frying_pan", "une poêle en fonte lourde et bien usée", 2.5)
        frozen_meat = Item("frozen_meat", "un morceau de viande gelée, encore comestible", 1.8)
        painting = Item("painting", "un tableau représentant un paysage mystérieux", 1.0)
        fireplace_poker = Item("fireplace_poker", "un tisonnier en métal pour la cheminée", 1.5)
        beamer = Beamer()
        torch = Torch() 
        explosive_orb = Weapon("rock_orb", "une orbe qui paraît normale très petite", 0.2, 67)
        samourai_sword = Weapon("samourai_sword", "une épée japonaise traditionnelle, tranchante et élégante", 3.0, 56)
        stick = Weapon("stick", "un bâton solide dégageant une énergie mystérieuse", 2.0, 133)
        wick_sword = Weapon("wick_sword", "une épée faite de cire durcie, étonnamment résistante", 2.5, 12)


        #important items for game
        goldenkey = Key("clé_en_or", "Clé en Or et Semble Ancienne", 0.55, 0x02)
        #silverkey = Key("clé_en_argent", "Clé en Argent poussièreux", 0.5, 0x01)#
        #diamondkey = Key("clé_en_diamant", "Clé en Diamand Etincellant", 0.5, 0x03)#
        sword = Weapon("sword", "épée lourde ressemblant à celle des rois d'antan...",5, 19)
        Enigmabook = Book("livre_marron", "livre épais semblant être ordinaire", 1.2, 260)
        #philosopher_stone = Item("pierre_philosophale", "Pierre incruster de minerais aux reflets oranges donnant l'immortalité", 1.5)
        colt = Weapon("colt", "un revolver de calibre .45, classique mais efficace", 1.0, 25)
        desintegrator = Desintegrator("desintegrator", "un pistolet laser futuriste capable de désintégrer la matière", 2.0, 200, 1)
        invisibility_cloak = InvisibilityCloak("long_cloak", "une longue cape qui semble à première vue ordinaire", 1.0)
        
        
        # Add Item to Room
        hall.add_item(chandelier)
        hall.add_item(old_map)
        
        # Add Item to Hall
        
        # Add Item to Coldroom
        coldroom.add_item(frozen_meat)
        coldroom.add_item(samourai_sword)
        
        # Add Item to Diningroom
        diningroom.add_item(silver_knife)
        diningroom.add_item(wine_bottle)
        diningroom.add_item(goldenkey)

        # Add Item to Cave
        
        
        cave.add_item(wooden_chest)

        # Add Item to Clearence
        clearence.add_item(sword)
        clearence.add_item(colt)
        clearence.add_item(explosive_orb)
        clearence.add_item(rusty_key)


        # Add Item to Laboratory
        laboratory.add_item(torch)
        laboratory.add_item(desintegrator)
        laboratory.add_item(beamer)
        laboratory.add_item(goldenkey)
        
        # Add Item to Kitchen
        kitchen.add_item(frying_pan)               
        kitchen.add_item(candle)
        kitchen.add_item(orbe_de_vie)
        kitchen.add_item(stick)

        # Add Item to Livingroom
        livingroom.add_item(fireplace_poker)
        livingroom.add_item(painting)
        livingroom.add_item(invisibility_cloak)
        livingroom.add_item(wick_sword)

        # Add Item to Library
        library.add_item(ancient_book)
        library.add_item(grimoire)
        library.add_item(Enigmabook)


        # Create characters
        chief = Character("Chief-cook", "un homme avec une toque", kitchen, ['bonjour cher convive',"à vos fourneaux !", "donnez la poule !"])
        jardiner = Character("Gardener", "un homme avec une salopette verte", hall, ["le jardin est magnifique aujourd'hui.","avez-vous vu mes outils ?","je dois arroser les plantes."])
        major_domo = Character("Major-domo", "un homme en costume noir", diningroom, ["Bienvenue dans cette demeure.","puis-je vous aider ?","le dîner sera servi bientôt."])
        kids = Character("Kids", "des enfants joueurs et curieux", livingroom, ["voulez-vous jouer avec nous ?","attrape-moi si tu peux !","regardez ce que j'ai trouvé !"])
        dog = Character("Dog", "un chien fidèle et joueur", kitchen, ["woof woof !","le chien remue la queue.","le chien aboie joyeusement."])
        tall_guard = Character("Tall-guard", "un grand garde imposant", laboratory, ["rien ne passe ici sans ma permission.","je surveille ce laboratoire.","restez loin d'ici."])

        # Add Characters in Rooms
        kitchen.characters[chief.name] = chief
        hall.characters[jardiner.name] = jardiner
        diningroom.characters[major_domo.name] = major_domo
        livingroom.characters[kids.name] = kids
        kitchen.characters[dog.name] = dog
        laboratory.characters[tall_guard.name] = tall_guard


        # Define monster
        humanbird = Monster('humanbird', 'Oiseau humanoïde entièrement noir avec une tête et des ailes de Pygarde ', 95, "boule de feu", "une vague de feu ardente ", 25, 100)
        gargouille = Monster('gargouille', "Petit dragon bleu avec des griffes acérées et des yeux rouges", 25, 'griffure',"coups de griffres acérées", 10, 14)
        demon = Monster("demon", "entitée malveillante aux yeux rouges et entièrement recouverte d'une fumée sombre", 200, "Poings explosifs", "Coup de poing de ténébre laissant s'echapper des éclairs violets", 50, 190)

        # Add monsters in rooms
        cave.monsters["demon"] = demon
        coldroom.monsters["humanbird"] = humanbird
        livingroom.monsters["gargouille"] = gargouille


       

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
        self.player.game = self

    def _setup_quests(self):
        """Initialize all quests."""
        key_quest = Quest(
            title="Dénicheur de Clés",
            description="Trouvez les Differentes Clés.",
            objectives=["prendre clé_en_or",
                        "prendre clé_en_argent",
                        "prendre clé_en_diamant"],
            reward="Le dénicheur de Clés"
        )

        gargouille_quest = Quest(
            title="Le Petit Combattant",
            description="Vaincre la Gargouille dans le salon",
            objectives=["vaincre gargouille"],
            reward="Un Chasseur est Né !"
        )

        enigme_quest = Quest(
            title="En Quête d'Enigme",
            description="Resolvez une énigme.",
            objectives=["resoudre enigma"],
            reward="Clé en Argent"
        )

        laser_quest = Quest(
            title="Le désintégrateur",
            description="Trouvez un désintegrateur.",
            objectives=["prendre desintegrator"],
            reward="Soldat Prêt à Eradiquer les Monstres "
        )

        humanbird_quest = Quest(
            title="Le Gardien",
            description="Vaincre le Gardien.",
            objectives=["vaincre humanbird"],
            reward="clé_en_diamant"
        )

        demon_quest = Quest(
            title="Le Boss",
            description="Vaincre le Boss.",
            objectives=["vaincre demon"],
            reward="Pierre Philosophale"
        )

        pnj_quest = Quest(
            title="Le Cuisinier",
            description="Parler au Cuisinier.",     
            objectives=["parler Chief-cook"],
            reward="Poêle du Cuisinier")

       
       
       
        self.player.quest_manager.add_quest(key_quest)
        self.player.quest_manager.add_quest(gargouille_quest)
        self.player.quest_manager.add_quest(enigme_quest)
        self.player.quest_manager.add_quest(laser_quest)
        self.player.quest_manager.add_quest(demon_quest)
        self.player.quest_manager.add_quest(humanbird_quest)
        self.player.quest_manager.add_quest(pnj_quest)
        
        self.player.quest_manager.activate_quest("Dénicheur de Clés")
        self.player.quest_manager.activate_quest("Le Boss")  
        self.player.quest_manager.activate_quest("Le Gardien")    
        self.player.quest_manager.activate_quest("Le désintégrateur")    
        self.player.quest_manager.activate_quest("En Quête d'Enigme",)    
        self.player.quest_manager.activate_quest("Le Petit Combattant")      
        self.player.quest_manager.activate_quest("Le Cuisinier")

       

    def finalize_win(self):
        for quest in self.player.quest_manager.get_all_quests():
            if not quest.is_completed:
                return False
        print("\n\t ----------------------------------------------------------------------\n")
        print("\n\t ------------------------- FÉLICITATIONS --------------------------------\n")
        print("\n\t ----------------------------------------------------------------------\n")
        print("\n\t\tVous Avez Gagnez Le Jeu ! Vous Êtes Vraiment Très Fort Jeune Aventurier !")
        self.finished = True
        return True


        
    def win(self, target=None):
        if target:
            if target.name == 'demon':
                print("\n\t ----------------------------------------------------------------------\n")
                print("\n\t ------------------------- FÉLICITATIONS --------------------------------\n")
                print("\n\t ----------------------------------------------------------------------\n")
                print("\n\t\tVous avez vaincu le démon ! Victoire totale !")
                self.player.quest_manager.check_action_objectives("vaincre", f"{target.name}")
                self.player.inventory["philosopher_stone"] = Item("philosopher_stone", "Pierre incrustée de minerais aux reflets oranges donnant l'immortalité", 1.5)
                return True
            else:
                print("\n\t\tVous Avez Gagnez!\n")
                self.player.hp += target.exp
                self.player.max_weight += target.exp //2
                for i in self.player.equiped_weapons:
                    i.damage += 15
                    print(f"Vos armes {i.name} gagnent 15 points de dégats !")
                print(f"Vous Gagnez {target.exp} PV Supplémentaire ! Plus Vous Vainquerai, Plus Vous Deviendrai Fort Jeune Combattant !\n")

                self.player.quest_manager.check_action_objectives("vaincre", f"{target.name}")
                if target.name == 'humanbird':
                    self.player.inventory["clé_en_diamant"] = Key("clé_en_diamant", "Clé en Diamand Etincellant", 0.5, 0x03)
                    self.player.quest_manager.check_action_objectives("prendre", "clé_en_diamant")
                    return True
        else:
            return False

    def lose(self):
        print("\n\t ----------------------------------------------------------------------\n")
        print("\n\t ------------------------- GAME OVER ----------------------------------\n")
        print("\n\t ----------------------------------------------------------------------\n")
        self.player.current_room = self.rooms[0]
        self.player.inventory = {}
        self.player.history = []
        print("Vous avez été ramené au hall d'entrée. Votre inventaire est vidé.\nFaites attention désormais. Le danger rôde partout...\n")
        self.setup()
        self.print_welcome()
        return None


    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.finalize_win()
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

