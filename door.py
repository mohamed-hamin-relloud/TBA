class Door:
    def __init__(self, nom, room_from, room_to, locked=True):
        self.nom = nom
        self.room_from = room_from
        self.room_to = room_to
        self.locked = locked  # État verrouillé/déverrouillé
