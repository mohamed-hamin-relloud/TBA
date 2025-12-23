import random
from copy import deepcopy

class Character:

    def __init__(self, name, description, current_room, msgs):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs

    def __str__(self):
        return f"{self.name} : {self.description}."

    def move(self):
        actual_room = self.current_room
        choice = ["True", "False"]
        random_choice = random.choice(choice)
        if random_choice == "True":
            l = []
            for i in actual_room.exits:
                if actual_room.exits.get(i) != None:
                    l.append(i)
                else:
                    continue
            
            if l == []:
                return False 
            
            r = random.choice(l)
            del actual_room.characters[self.name]
            actual_room.exits[r].characters[self.name] = self
            self.current_room = actual_room.exits[r]
            print("PNJ:", self.name)
            print("Salle actuelle:", self.current_room.name)
            print("Exits valides:", l)
            return True
        else :
            return False

        
    
  
    