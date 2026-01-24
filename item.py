"""Module définissant la classe Item utilisée par le jeu."""

from __future__ import annotations


class Item:
    """Représente un objet dans le jeu.

    Attributes:
        name (str): nom de l'objet
        description (str): description affichée
        weight (float): poids en kilogrammes
    """

    def __init__(self, name: str, description: str, weight: float):
        self.name = name
        self.description = description
        self.weight = weight

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

    - attribut `lit` (bool) : état de la torche
    - `use(player)` : allume/éteint la torche et modifie `player.current_room.dark` si nécessaire
    """

    def __init__(self, name: str = "torch", description: str = "une torche en bois qui éclaire faiblement", weight: float = 1.5):
        super().__init__(name, description, weight)
        self.lit = False

    def use(self, player):
        """Allume ou éteint la torche.

        Si la torche est allumée, la pièce courante est éclairée (dark=False).
        Si elle est éteinte, la pièce redevient sombre (dark=True).
        """
        self.lit = not self.lit
        if self.lit:
            player.current_room.dark = False
            return "Vous allumez la torche. La pièce est désormais éclairée."
        else:
            # Éteindre rend la pièce sombre (comportement simple)
            player.current_room.dark = True
            return "Vous éteignez la torche. Il fait maintenant plus sombre ici."

class Key(Item):
    """Une clé attachée à une porte identifiée par `door_id`."""

    def __init__(self, door_id: str):
        # Nom simple pour faciliter la saisie par le joueur
        name = "key"
        description = f"clé pour la porte {door_id}"
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
    
    def __init__(self, name: str, description: str, weight: float, damage : int):
        super().__init__(name,description,weight)
        self.damage = damage

    def isequipped(self):
        return True
    
    def isnot_equipped(self):
        return False

    def __str__(self):
        return f"{self.name} : {self.description} ({self.weight} kg) ({"Equipé" if self.isequipped() else "Pas équipé"}) "

    

    

        

