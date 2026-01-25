# Define the Player class.
from item import Item, Beamer, Weapon, Book, Key, Desintegrator
from door import Door
from quest import QuestManager




class Player():

    # Define the constructor.
    def __init__(self, name, current_room=None, history=None, max_weight=10.0, weapons = None, hp=35, invisible = False):
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
        self.move_count = 0
        self.quest_manager = QuestManager(self)
        self.rewards = []  # List to store earned rewards
        self.weapons = weapons
        self.hp = hp
        self.game = None
        self.invisible = invisible
        self.equiped_weapons = []
    
   
    
    def equip(self, weapons):
        if isinstance(weapons, Desintegrator):
            if weapons not in self.equiped_weapons:
                print(f'Vous vous êtes équipé de {weapons.name}!')
                weapons.equiped = True
                self.equiped_weapons.append(weapons)
                return True
            else:
                print(f"Vous êtes déjà équipé de {weapons.name}")
            return True
            

        if isinstance(weapons, Weapon):
            if weapons not in self.equiped_weapons:
                print(f"Vous vous êtes équipé de {weapons.name}!")
                weapons.isequipped()
                self.equiped_weapons.append(weapons)
                return True
            else:
                print(f"Vous êtes déjà équipé de {weapons.name}")
            return True
        
        else:
            print(f"{weapons.name} n'est pas une arme, vous ne pouvez l'équiper comme une arme.")
            print(self.equiped_weapons)
            return False

            
    def get_history(self):
        print("vous avez visité les lieux suivant :\n")
        for i in self.history[:len(self.history)-1]:
            if i is not None:
                print(f"\t {i.description}")
        return ""
    


    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        direction_map = {
            'nord': 'N', 'north': 'N', 'n': 'N',
            'sud': 'S', 'south': 'S', 's': 'S',
            'ouest': 'O', 'west': 'O', 'o': 'O',
            'est': 'E', 'east': 'E', 'e': 'E',
            'up': 'U', 'u': 'U',
            'down': 'D', 'd': 'D',
        }
        canonical = direction_map.get(direction.lower())
        if canonical is None:
            print(f"la commande {direction} n'est pas valide ! Vous ne vous déplacez.")
            return None
       
        
        direction = direction.lower()[0].upper()
        next_exit = self.current_room.exits.get(direction)   
        
        

        if self.history == []:
            self.history.append(self.current_room)
            

        # If the next exit is None, print an error message and return False.
        if next_exit is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Check room visit objectives
        self.quest_manager.check_room_objectives(self.current_room.name)

        # Increment move counter and check movement objectives
        self.move_count += 1
        self.quest_manager.check_counter_objectives("Se déplacer", self.move_count)
         
        # If the exit is a Door, check its lock state and get the target room
        next_room = next_exit
         
        # Check if there's a locked door to the next room
        for porte in self.current_room.door:
            if porte.room_to == next_room:
                if porte.locked:
                    print("\nLa porte est verrouillée.\n")
                    return False
                break
        
        self.current_room = next_room
        
        #if isinstance(self.current_room, Door):
            #next_room = self.current_room.room_to
        #else:
            #next_room = self.current_room

        # Record visit in history and move
        self.history.append(next_room)
        self.current_room = next_room
        print(self.current_room.get_long_description())
        print(self.get_history())
        return True
    
    def get_inventory(self):
        if not self.inventory:
            return f"Votre inventaire est vide. Poids actuel: {self.current_weight}/{self.max_weight} kg."
        items_str = "\n".join(f"    - {self.inventory[item]}" for item in self.inventory)
        return f"Vous disposez des items suivants :\n{items_str}\nPoids actuel: {self.current_weight}/{self.max_weight} kg." 
    
    def use_beamer(self):
        for item in self.inventory:
            if isinstance(item, Beamer):
                return item.use(self)
        return "Vous ne possédez pas de beamer."


    def add_reward(self, reward):
            """
            Add a reward to the player's rewards list.
            
            Args:
                reward (str): The reward to add.
                
            Examples:
            
            >>> player = Player("Bob")
            >>> player.add_reward("Épée magique") # doctest: +NORMALIZE_WHITESPACE
            <BLANKLINE>
            🎁 Vous avez obtenu: Épée magique
            <BLANKLINE>
            >>> "Épée magique" in player.rewards
            True
            >>> player.add_reward("Épée magique") # Adding same reward again
            >>> len(player.rewards)
            1
            """
            if reward and reward not in self.rewards:
                self.rewards.append(reward)
                print(f"\n🎁 Vous avez obtenu: {reward}\n")


    def show_rewards(self):
            """
            Display all rewards earned by the player.
            
            Examples:
            
            >>> player = Player("Charlie")
            >>> player.show_rewards() # doctest: +NORMALIZE_WHITESPACE
            <BLANKLINE>
            🎁 Aucune récompense obtenue pour le moment.
            <BLANKLINE>
            >>> player.add_reward("Bouclier d'or") # doctest: +NORMALIZE_WHITESPACE
            <BLANKLINE>
            🎁 Vous avez obtenu: Bouclier d'or
            <BLANKLINE>
            >>> player.show_rewards() # doctest: +NORMALIZE_WHITESPACE
            <BLANKLINE>
            🎁 Vos récompenses:
            • Bouclier d'or
            <BLANKLINE>
            """
            if not self.rewards:
                print("\n🎁 Aucune récompense obtenue pour le moment.\n")
            else:
                print("\n🎁 Vos récompenses:")
                for reward in self.rewards:
                    print(f"  • {reward}")
                print()
    
    def weapons_attack(self, weapon = None):
        if weapon:
            print(f"Vous attaquez avec {weapon.name}!")
        else:
            print("Vous n'avez pas choisi d'arme pour attaquer.")
    
    def choose_weapon(self):
        # 1. On transforme le dictionnaire d'inventaire en liste pour avoir un ordre
    
        if not self.equiped_weapons:
            print("Votre inventaire est vide.")
            return None

        print("\nChoisissez un objet :")
        # 2. enumerate(..., 1) commence à compter à 1 au lieu de 0 pour l'utilisateur
        for i, weapons_select in enumerate(self.equiped_weapons, 1):
            print(f"{i}. {weapons_select.name}")

        # 3. Récupération du choix avec sécurité
        try:
            choice = int(input("\nEntrez le numéro de l'objet : "))
        
        # Vérification si l'indice est bien dans la liste
            if 1 <= choice <= len(self.equiped_weapons):
                selected_item = self.equiped_weapons[choice - 1]   
                print(f"Vous avez choisi : {selected_item.name}")
                return selected_item
            else:
                print("Numéro invalide.")
        except ValueError:
            print("Veuillez entrer un chiffre.")
        except AttributeError:
            print("L'arme choisie n'existe pas.")
    
        return False
        
        
    def fighting(self, target):
        in_fight = True
        print("Le combat commence !")
        print("Avec quelle arme voulez-vous attaquer ? Choississez le numéro correspondant :")
        self.weapons = self.choose_weapon()
        if not self.weapons or not isinstance(self.weapons, (Weapon, Desintegrator)):
            print("Vous n'avez pas d'arme équipée, vous ne pouvez pas combattre.")
            self.game.lose()
            return False
        while in_fight:
            attack = input(">")
            self.weapons_attack(self.weapons)
            target.fighting()
            target.health-= self.weapons.damage 
            self.hp -= target.attack_damage
            
            if self.hp < 0:
                self.hp = 0
            if target.health < 0:
                target.health = 0   

            if (self.hp <= 0 and target.health > 0) or (self.hp == 0 and target.health <= 0):
                self.game.lose()
                self.hp -= self.hp
                in_fight = False
            
            if target.health <= 0 and self.hp > 0:
                self.game.win(target)
                target.health -= target.health
                in_fight = False
            
            print(f"Vous avez maintenant {self.hp} PV!")
            print(f"{target.name} à maintenant {target.health} PV!")
        
            
        

    def fight(self, target):
        """
        Docstring for fight

        description : player fight with monster
        
        
        """
        print("Appuyez sur la touche 1 pour combattre sinon sur la touche 0 pour fuir")
        print("\t   -  0  :  fuir\n\t   -  1  :  attaquer")
        on = True
        while on:
            decision = input(">")
            if decision.isdigit():
                if decision == "0":
                    print(f"vous sortez de {self.current_room.name}")
                    self.history.pop()
                    self.current_room = self.history[-1]
                    print(self.current_room.get_long_description())
                    on = False

                if decision == "1":
                    self.fighting(target)
                    on = False
            
            else:
                print("commandes non valides")
    
    def resolve_enigma(self):
        resolving = True
        while resolving:
            answer = input(">")
            
            if answer.lower() == "le démon" or answer.lower() == "un démon":
                resolving = False
                print("Vous avez trouvé le mot mystère!")
                self.quest_manager.check_action_objectives("resoudre", "enigma")
                self.quest_manager.check_action_objectives("prendre", "clé_en_argent")
                self.inventory["clé_en_argent"] = Key("clé_en_argent", "Clé en Argent poussièreux", 0.5, 0x01)
                
            else:
                print("Ca ne semble pas être correcte...")
    
    def read(self, book):
        if book == None:
            return False
        if book.name.lower() == 'livre_marron':
            print(book.enigma_description_begin())
            print(book.enigma_description())
            self.resolve_enigma()
            return True
        else:
            print(book.read_description())
            return True

    def health_status(self):
        print("\nStatut de santé :")
        print(f"\t PV : {self.hp}")
        for weapon in self.equiped_weapons:
            print(f"\t Arme équipée : {weapon.name} (Dégâts : {weapon.damage})")
        return True         
    
   
            

    




