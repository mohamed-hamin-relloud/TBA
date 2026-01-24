# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.

from door import Door
from item import Key
from character import Monster

# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

from copy import deepcopy

class Actions:

    @staticmethod
    def _print_room_state(game):
        """Affiche la description longue de la salle courante et son inventaire."""
        player = game.player
        player.current_room.get_long_description()
        player.current_room.get_inventory()

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        

        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        

        # Get the direction from the list of words.
        direction = list_of_words[1]
        
         # Move the player in the direction specified by the parameter
        if direction != list_of_words[1] and list_of_words[1].upper() and list_of_words[1].lower() and list_of_words[1][0] and list_of_words[1][0].upper() and list_of_words[1][0].lower():
            print(f"{direction} inacessible, vous n'avancez pas !")
        else:
            player.move(direction)
            return True

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
    
    def back(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        player = game.player
        
        if len(player.history) == 1:
            print("\nvous ne pouvez plus revenir en arrière ou alors vous n'avez rien visité.\n")
            print(player.history[0].name)
            return False
        
        else:
            player.history.pop()
            last = player.history[-1]
            # if not player.history:
            #     print("\nvous êtes revenu au hall.\n")
            # last = None
            # for r in reversed(player.history):
            #     if r is not None:
            #         last = r
            #         break
            # if last is None:
            #     print("\nErreur: aucune salle valide dans l'historique.\n")
            #     return False
        print()
        player.current_room = last
        print(last.get_long_description())
        player.get_history()
        print([i.name for i in player.history])
        
        return True
    
    def look(game, list_of_words, number_of_parameter):
        player = game.player
        actual_room = game.player.current_room
        if actual_room.inventory == {} :
            print("\nvous ne voyez rien de particulier dans cette pièce.\n")
            return False
        else:
            actual_room.get_inventory()
            return True




            #print("\nvous voyez :")
            #for i in actual_room.inventory:
                #print(f"\t - {actual_room.inventory.get(i).name} : {actual_room.inventory.get(i).description}")
            #return True
    
    def take(game, list_of_words, number_of_parameter):
        actual_room_object = game.player.current_room.inventory
        stuff = game.player.inventory
        if len(list_of_words) != number_of_parameter + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        if actual_room_object== {}:
            print("\nil n'y a rien ici.\n")
            return False
        
        items = list_of_words[1]
        

        if items == "":
            print('\nquel objet voulez vous prendre ?\n')
            return False
        
        if items not in actual_room_object:
            print("\nil n'y a pas d'objet de la sorte ici.\n")
            return False
        else:
            if stuff == {}:
                if actual_room_object.get(items).weight > game.player.max_weight:
                    print(f"\nl'objet {items} est trop lourd.\n")
                    return False
                else:
                    stuff[items] = actual_room_object.get(items)
                    del actual_room_object[items]
                    print(f"\nvous avez récuperé l'objet {items}.\n")
                    return True
            s = 0
            for ele in stuff:
                s+=stuff.get(ele).weight
            weight_max = s
            if actual_room_object.get(items).weight + weight_max > game.player.max_weight:
                print(f"\nl'objet {items} vous allourdi trop.\n")
                return False
            else:
                stuff[items] = actual_room_object.get(items)
                print(f"\nvous avez récuperé l'objet {items}.\n")
            weight_max += actual_room_object.get(items).weight
            del actual_room_object[items]
        game.player.current_room.inventory = actual_room_object
        game.player.inventory = stuff
    
    def drop(game, list_of_words, number_of_parameter):
        actual_room_object = game.player.current_room.inventory
        stuff = game.player.inventory
        if len(list_of_words) != number_of_parameter + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        if stuff == {}:
            print("\nvous n'avez aucun objet.\n")
            return False
        
        items = list_of_words[1]

        if items == "":
            print("\ncommande indisponible.\n")
            return False
        
        if items not in stuff:
            print("\nvous n'avez pas cette objet.\n")
            return False
        else:
            actual_room_object[items] = stuff.get(items)
            del stuff[items]
            print(f"\nvous avez déposé l'objet {items}.\n")
        game.player.current_room.inventory = actual_room_object
        game.player.inventory = stuff

    
    def check(game, list_of_words, number_of_parameter):
        player = game.player
        bag = player.inventory
        if  bag == {}:
            print("\nvous n'avez aucun objet sur vous.\n")
            return False
        else:
            print("\nvous disposez des objets suivant :")
            for i in bag:
                print(f"\t - {bag.get(i).name} : {bag.get(i).description}")
            return True
            
    def talk(game, list_of_words, number_of_parameter):
        player = game.player
        l = len(list_of_words)
       
        if l != number_of_parameter + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        perso_talking = list_of_words[1]
        
        if perso_talking == "":
            print("\nCommande indisponible.\n")
            return False

        if perso_talking not in player.current_room.characters:
            print(f"\n{perso_talking} n'est pas ici.\n")
            return False

        player.current_room.characters[perso_talking].get_msg()
        return True
                   

    def look(game, list_of_words, number_of_parameters):
        """
        Display the current room's description and inventory.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player = game.player
        player.current_room.get_long_description()
        player.current_room.get_inventory()
        return True

    def take(game, list_of_words, number_of_parameters):
        """Take an item from the current room and add it to the player's inventory,
        respecting the player's max_weight limit.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        player = game.player
        item_name = list_of_words[1]
        current_room = player.current_room

        # Find the item in the current room
        item = current_room.inventory.get(item_name.lower())

        if item is None:
            print(f"\nIl n'y a pas d'item nommé '{item_name}' ici.\n")
            return False
        
        game.player.quest_manager.check_action_objectives("prendre", item_name)

        # Check weight limit
        if player.current_weight + item.weight > player.max_weight:
            print(f"\nVous ne pouvez pas prendre '{item_name}' : capacité maximale ({player.max_weight} kg) dépassée.\n")
            return False

        # Transfer item and update weight
        if current_room.take(item_name, player):
            player.current_weight += item.weight
            print(f"\nVous avez pris {item_name} ({item.weight} kg). Poids actuel: {player.current_weight}/{player.max_weight} kg.\n")
            Actions._print_room_state(game)
        
            return True
        else:
            print(f"\nÉchec lors de la prise de l'item '{item_name}'.\n")
            return False
        
    def drop(game, list_of_words, number_of_parameters):
        """Drop an item from the player's inventory into the current room and
        update the player's carried weight."""
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        player = game.player
        item_name = list_of_words[1]
        current_room = player.current_room

        # Find the item in the player's inventory to get its weight
        item = player.inventory.get(item_name.lower())

        if item is None:
            print(f"\nVous n'avez pas d'item nommé {item_name} dans votre inventaire.\n")
            return False

        if current_room.drop(item_name, player):
            player.current_weight = max(0, player.current_weight - item.weight)
            print(f"\nVous avez déposé {item_name}. Poids actuel: {player.current_weight}/{player.max_weight} kg.\n")
            Actions._print_room_state(game)
            return True
        else:
            print(f"\nÉchec lors du dépôt de l'item '{item_name}'.\n")
            return False
        
    def check(game, list_of_words, number_of_parameters):
        """
        Check the player's inventory.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        player = game.player
        print(player.get_inventory())
        return True
        
    
    def use(game, list_of_words, number_of_parameters):
        """
        Use an item from the player's inventory.

        - If the item is a Key, attempt to unlock an adjacent Door with the same id.
        - Otherwise, if the item exposes a `use` method, call it.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        player = game.player
        item_name = list_of_words[1]

        # Find the item in the player's inventory (inventory stores name->Item)
        item = player.inventory.get(item_name.lower())

        if item is None:
            print(f"\nVous n'avez pas d'item nommé '{item_name}' dans votre inventaire.\n")
            return False

        # If it's a Key, attempt to unlock a Door adjacent to the player's current room
        if isinstance(item, Key):
            for exit in player.current_room.exits.values():
                if isinstance(exit, Door) and exit.id == item.door_id:
                    if not exit.locked:
                        print("\nLa porte est déjà déverrouillée.\n")
                        return False
                    exit.locked = False
                    # Unlock the reverse side if it exists
                    other = exit.room
                    for rev in other.exits.values():
                        if isinstance(rev, Door) and rev.room == player.current_room and rev.id == item.door_id:
                            rev.locked = False
                    print(f"\nVous avez déverrouillé la porte {exit.id} vers {exit.room.name}.\n")
                    Actions._print_room_state(game)
                    return True
            print("\nAucune porte associée à cette clé n'est accessible depuis cette pièce.\n")
            return False

        # Otherwise try to call a 'use' method on the item (beamer, etc.)
        if hasattr(item, 'use'):
            try:
                msg = item.use(player)
                print(f"\n{msg}\n")
                Actions._print_room_state(game)
                return True
            except TypeError:
                print("\nImpossible d'utiliser cet item dans ce contexte.\n")
                return False

        print("\nCet item ne peut pas être utilisé.\n")
        return False

    def use_beamer(game, list_of_words, number_of_parameters):
        """
        Use the beamer to teleport the player to the charged room.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        player = game.player
        msg = player.use_beamer()
        print(f"\n{msg}\n")
        Actions._print_room_state(game)
        return True

    def charge(game, list_of_words, number_of_parameters):
        """Charge le beamer avec la pièce courante (doit être dans l'inventaire)."""
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        player = game.player
        for item in player.inventory.values():
            # On cherche un item qui sait "charge" (le Beamer)
            if hasattr(item, "charge"):
                msg = item.charge(player.current_room)
                print(f"\n{msg}\n")
                Actions._print_room_state(game)
                return True
        print("\nVous ne possédez pas de beamer à charger.\n")
        return False

    def use_torch(self, item_name):
        for item in self.player.inventory.values():
            if isinstance(item, Torch) and item.name.lower() == item_name.lower():
                return True, item.use(self.player.current_room)
        return False, "Vous ne possédez pas de torche."



    @staticmethod
    def quests(game, list_of_words, number_of_parameters):
        """
        Show all quests and their status.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.quests(game, ["quests"], 0)
        <BLANKLINE>
        📋 Liste des quêtes:
          ❓ Grand Explorateur (Non activée)
          ❓ Grand Voyageur (Non activée)
          ❓ Découvreur de Secrets (Non activée)
        <BLANKLINE>
        True
        >>> Actions.quests(game, ["quests", "param"], 0)
        <BLANKLINE>
        La commande 'quests' ne prend pas de paramètre.
        <BLANKLINE>
        False

        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Show all quests
        game.player.quest_manager.show_quests()
        return True
    
    @staticmethod
    def quest(game, list_of_words, number_of_parameters):
        """
        Show details about a specific quest.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.quest(game, ["quest", "Grand", "Voyageur"], 1)
        <BLANKLINE>
        📋 Quête: Grand Voyageur
        📖 Déplacez-vous 10 fois entre les lieux.
        <BLANKLINE>
        Objectifs:
          ⬜ Se déplacer 10 fois (Progression: 0/10)
        <BLANKLINE>
        🎁 Récompense: Bottes de voyageur
        <BLANKLINE>
        True
        >>> Actions.quest(game, ["quest"], 1)
        <BLANKLINE>
        La commande 'quest' prend 1 seul paramètre.
        <BLANKLINE>
        False

        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n < number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the quest title from the list of words (join all words after command)
        quest_title = " ".join(list_of_words[1:])

        # Prepare current counter values to show progress
        current_counts = {
            "Se déplacer": game.player.move_count
        }

        # Show quest details
        game.player.quest_manager.show_quest_details(quest_title, current_counts)
        return True
    
    @staticmethod
    def activate(game, list_of_words, number_of_parameters):
        """
        Activate a specific quest.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.activate(game, ["activate", "Grand", "Voyageur"], 1) # doctest: +ELLIPSIS
        <BLANKLINE>
        🗡️  Nouvelle quête activée: Grand Voyageur
        📝 Déplacez-vous 10 fois entre les lieux.
        <BLANKLINE>
        True
        >>> Actions.activate(game, ["activate"], 1)
        <BLANKLINE>
        La commande 'activate' prend 1 seul paramètre.
        <BLANKLINE>
        False

        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n < number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the quest title from the list of words (join all words after command)
        quest_title = " ".join(list_of_words[1:])

        # Try to activate the quest
        if game.player.quest_manager.activate_quest(quest_title):
            return True

        msg1 = f"\nImpossible d'activer la quête '{quest_title}'. "
        msg2 = "Vérifiez le nom ou si elle n'est pas déjà active.\n"
        print(msg1 + msg2)
        # print(f"\nImpossible d'activer la quête '{quest_title}'. \
        #             Vérifiez le nom ou si elle n'est pas déjà active.\n")
        return False


    @staticmethod
    def rewards(game, list_of_words, number_of_parameters):
        """
        Display all rewards earned by the player.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.rewards(game, ["rewards"], 0)
        <BLANKLINE>
        🎁 Aucune récompense obtenue pour le moment.
        <BLANKLINE>
        True
        >>> Actions.rewards(game, ["rewards", "param"], 0)
        <BLANKLINE>
        La commande 'rewards' ne prend pas de paramètre.
        <BLANKLINE>
        False
        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Show all rewards
        game.player.show_rewards()
        return True
    


    def fight(game, list_of_words, number_of_parameter):
        player = game.player
        l = len(list_of_words)
       
        if l != number_of_parameter + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        monster_fighting_name = list_of_words[1]
        
        if monster_fighting_name == "":
            print("\nCommande indisponible.\n")
            return False

        if monster_fighting_name not in player.current_room.monsters:
            print(f"\n{monster_fighting_name} n'est pas ici.\n")
            return False
        
        print(game.player.current_room.monsters[monster_fighting_name].begin_attack())
        player.current_room.monsters[monster_fighting_name].fight(player)
        return True