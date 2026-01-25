"""Module définissant la classe Item utilisée par le jeu."""

from __future__ import annotations


class Item:
    """Représente un objet dans le jeu.

    Attributes:
        name (str): nom de l'objet
        description (str): description affichée
        weight (float): poids en kilogrammes
    """

    def __init__(self, name: str, description: str, weight: float, equiped = False):
        self.name = name
        self.description = description
        self.weight = weight
        self.equiped = equiped

    def __str__(self):
        return f"{self.name} : {self.description} ({self.weight} kg)"

    def __repr__(self):
        return f"Item({self.name!r}, {self.description!r}, {self.weight!r})"
    
    def get_weight(self):
        """Retourne le poids de l'objet."""
        return self.weight


class Beamer(Item):
    """Un beamer : objet spécial capable de mémoriser une pièce et téléporter le joueur."""

    def __init__(self):
        super().__init__("beamer", "un appareil de téléportation (beamer)", 1.0)
        self.charged_room = None  # Pièce mémorisée

    def charge(self, room):
        """Mémorise la pièce actuelle."""
        self.charged_room = room
        return f"Le beamer a été chargé avec la pièce : {room.name}."

    def use(self, player):
        """Téléporte le joueur vers la pièce mémorisée."""
        if self.charged_room:
            player.current_room = self.charged_room
            return f"Vous avez été téléporté dans la pièce : {self.charged_room.name}."
        else:
            return "Le beamer n'a pas été chargé. Utilisez 'charge' pour mémoriser une pièce."


class Torch(Item):
    """Une torche que l'on peut allumer pour éclairer la pièce.

    - attribut `state` (bool) : état de la torche
    - `use(player)` : allume/éteint la torche et modifie `player.current_room.dark` si nécessaire
    """

    def __init__(self, name: str = "torch", description: str = "une torche en bois qui éclaire faiblement", weight: float = 1.5):
        super().__init__(name, description, weight)
        self.state = False

    def use(self, player):
        """Allume ou éteint la torche.

        Si la torche est allumée, la pièce courante est éclairée (dark=False).
        Si elle est éteinte, la pièce redevient sombre (dark=True).
        """
        
        if not self.state:
            player.current_room.dark = False
            return "Vous allumez la torche. La pièce est désormais éclairée."
        else:
            # Éteindre rend la pièce sombre (comportement simple)
            player.current_room.dark = True
            return "Vous éteignez la torche. Il fait maintenant plus sombre ici."

class Key(Item):
    """Une clé attachée à une porte identifiée par `door_id`."""

    def __init__(self, name, description, weight, door_id: str):
        description = f"{description} (clé pour la porte {door_id})"
        weight = 0.5
        super().__init__(name, description, weight)
        self.door_id = door_id  # Identifiant de la porte associée

    def use(self, door):
        """Ouvre une porte si la clé correspond.

        Attendu : `door` possède les attributs `id` et `locked`.
        """
        if getattr(door, "id", None) == self.door_id:
            door.locked = False
            return f"La porte {door.id} a été déverrouillée."
        else:
            return f"Cette clé ne correspond pas à la porte {getattr(door, 'id', '<inconnue>')}."
        
class Weapon(Item):
    
    def __init__(self, name: str, description: str, weight: float, damage : int, equiped = False):
        super().__init__(name,description,weight)
        self.damage = damage
        self.equiped = equiped

    def isequipped(self):
        self.equiped = True
        return True
        

    def isnot_equipped(self):
        self.equiped = False
        return True

    def __str__(self):
        return f"{self.name} : {self.description} ({self.weight} kg) ({"Pas équipé" if not self.equiped else "Équipé"}) "

    

    
class Book(Item):
    
    def __init__(self, name: str, description: str, weight: float, number_of_page : int, resume = None, open = False):
        super().__init__(name,description,weight)
        self.number_of_page = number_of_page
        self.open = open
        self.resume = resume if resume else "Ce livre n'est pas très intéressant"

    def read_description(self):
        return f"\n{self.resume}\n"
    
    def enigma_description_begin(self):
        a = "En Feuilletant les Pages Vous Remarquez que le mot Enigma est Entouré en Gras..."
        b = "En Allant à la Page dédié à Enigma, Vous Constatez qu'une Image à été Gribouillé et une énigme."
        return f"\n{a}\n{b}\n"
    
    def enigma_description(self):
        a = "Né dans les profondeurs, je ne verrai jamais les cimes. Je reste tapi dans l'ombre pour vous ramener, un jour, là d'où je viens."
        b = "Qui suis-je ?"
        return f"\n{a}\n{b}\n"
    
class InvisibilityCloak(Item):
    """Une cape d'invisibilité qui rend le joueur invisible aux monstres."""

    def __init__(self, name: str = "invisibility_cloak", description: str = "une cape qui semble à première vue ordinaire", weight: float = 1.0):
        super().__init__(name, description, weight)
        self.worn = False

    def use(self, player):
        """Active ou désactive la cape d'invisibilité.

        Lorsque la cape est portée, les monstres ne peuvent pas détecter le joueur.
        """
        if not self.worn:
            player.invisible = True
            return "Vous enfilez la cape d'invisibilité. Vous êtes maintenant invisible aux monstres."
        else:
            player.invisible = False
            return "Vous retirez la cape d'invisibilité. Vous êtes à nouveau visible aux monstres."


class Desintegrator(Weapon):
    """ Une arme de type désintegrateur futuriste"""

    def __init__(self, name = "desintegrator", description = "un pistolet laser futuriste", weight = 2.0, damage = 200, equiped = False, usable = 1):
        super().__init__(name, description, weight, damage, equiped)
        self.usable = usable # Nombre d'utilisation restante

    def attack(self, player, target):
        if self.usable > 0:
            target.health -= self.damage
            self.usable -= 1
            return f'Vous utilisez le desintegrateur sur {target.name} : il lui reste {target.health} PV. Le desintegrateur peut être utilisé {self.usable} fois.'
        else:
            return "Le désintegrateur ne fonctionne plus, reserve épuisée." 
            
        


        


        

