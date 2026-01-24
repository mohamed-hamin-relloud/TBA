# Define the Player class.
from item import Item, Beamer, Weapon
from door import Door
from quest import QuestManager


class Player():

    # Define the constructor.
    def __init__(self, name, current_room=None, history=None, max_weight=10.0, weapons = None, hp=60):
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

    
        
    def equip(self, weapons):
        print(f"Vous vous êtes équipé de {weapons.name}!")
        weapons.isequipped()

            
    def get_history(self):
        print("vous avez visité les lieux suivant :\n")
        for i in self.history[:len(self.history)-1]:
            if i is not None:
                print(f"\t {i.description}")
        return ""
       

    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        Directions = ['NORD','Nord','nord','n','N', "S", 'sud','s','Sud','SUD', "O", 'o', 'ouest', 'Ouest','OUEST','E', 'e','est','EST', 'Est', "U", 'u', 'up', 'Up', 'UP',"D", 'd','down','Down', 'DOWN']
        if direction not in Directions:
            print(f"la commande {direction} n'est pas valide ! Vous ne vous déplacez.")
            return None
        direction = direction[0].upper()
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
        if isinstance(next_exit, Door):
            if next_exit.locked:
                print("\nLa porte est verrouillée.\n")
                return False
            next_room = next_exit.room
        else:
            next_room = next_exit

        # Record visit in history and move
        self.history.append(next_room)
        self.current_room = next_room
        print(self.current_room.get_long_description())
        print(self.get_history())
        print([i.name for i in self.history])
        return True
    
    def get_inventory(self):
        if not self.inventory:
            return f"Votre inventaire est vide. Poids actuel: {self.current_weight}/{self.max_weight} kg."
        items_str = "\n".join(f"    - {item}" for item in self.inventory)
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
    
    def weapons_attack(self, weapon):
        print(f"Vous attaquez avec {weapon.name}!")

    def fighting(self, target):
        self.weapons_attack(self.weapons)
        target.fighting(self)
        target.health-= self.weapons.damage
        self.hp -= target.attack_damage

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


    
    




