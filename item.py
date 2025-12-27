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

    def __str__(self) -> str:
        return f"{self.name} : {self.description} ({self.weight} kg)"

    def __repr__(self) -> str:
        return f"Item({self.name!r}, {self.description!r}, {self.weight!r})"
