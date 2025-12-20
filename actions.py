# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.



# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

from copy import deepcopy

class Actions:

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
        if len(player.history)==0:
            print("\nvous ne pouvez plus revenir en arrière ou alors vous n'avez rien visité.\n")
            return False
        else:
            try:
                player.history.pop()
                print(player.history[-1].get_long_description())
                player.current_room = player.history[-1]
                player.get_history()
            except IndexError :
                print("\nvous êtes revenu au hall.\n")
                return False

    def look(game, list_of_words, number_of_parameter):
        player = game.player
        actual_room = game.player.current_room
        pnj_room = game.player.character.current_room
        if actual_room.inventory == {} :
            print("\nvous ne voyez rien de particulier dans cette pièce.\n")
            return False
        else:
            print("\nvous voyez :")
            for i in actual_room.inventory:
                print(f"\t - {actual_room.inventory.get(i).name} : {actual_room.inventory.get(i).description}")
            for i in pnj_room:
                print(f"\t - {pnj_room.inventory.get(i).name} : {pnj_room.inventory.get(i).description}")

            return True
    
    def take(game, list_of_words, number_of_parameter):
        actual_room_object = game.player.current_room.inventory
        stuff = game.player.inventory
        actual_room_copy = deepcopy(actual_room_object)
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
                    del actual_room_copy[items]
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
                del actual_room_copy[items]
                print(f"\nvous avez récuperé l'objet {items}.\n")
            weight_max += actual_room_object.get(items).weight
        game.player.current_room.inventory = actual_room_copy
        game.player.inventory = stuff
    
    def drop(game, list_of_words, number_of_paramater):
        actual_room_object = game.player.current_room.inventory
        stuff = game.player.inventory
        if stuff == {}:
            print("\nvous n'avez aucun objet.\n")
            return False
        
        items = list_of_words[1]
        
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
            
           
      

            
    
        


        
    


            

                   
            

                   

                    

        



        

