class Door:
    def __init__(self, id, room_from, room_to, locked=True):
        self.id = id
        self.room_from = room_from
        self.room_to = room_to
        self.locked = locked  # État verrouillé/déverrouillé
        self.player = None
    

    