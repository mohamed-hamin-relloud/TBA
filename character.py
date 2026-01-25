import random
from copy import deepcopy
from room import Door

class Character:

    def __init__(self, name, description, current_room, msgs, msgs_memory = None):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs
        if not msgs_memory:
            self.msgs_memory = []
        else:
            self.msgs_memory = msgs_memory

    def __str__(self):
        return f"{self.name} : {self.description}."

    def move(self):
        actual_room = self.current_room
        C = [True, False]
        Choice = random.choice(C)
        if Choice:
            directions = [ d for d in self.current_room.exits.keys() if self.current_room.exits[d] is not None]
            if directions:
                direction = random.choice(directions)
                old_room = self.current_room
                next_exit = self.current_room.exits[direction]
                # Si la sortie est une Door, vérifier si elle est verrouillée
                if isinstance(next_exit, Door):
                    if next_exit.locked:
                        return "\nLa porte est verrouillée.\n"
                    destination = next_exit.room
                else:
                    destination = next_exit

                self.current_room = destination
                if hasattr(old_room, 'characters') and self.name in old_room.characters:
                    del old_room.characters[self.name]
                self.current_room.characters[self.name] = self
                return True
            else:
                return "\nVide.\n"
        else:
            self.current_room = actual_room
            return True
        
    def get_msg(self):
        if self.msgs != []:
            self.msgs_memory.append(self.msgs[0])
            print(f"\n{self.msgs.pop(0)}\n")
            return True
        else:
            for i in self.msgs_memory:
                self.msgs.append(i)
            print(f"\n{self.msgs.pop(0)}\n")
        return True
        

class Monster:

    def __init__(self, name, description, health, attack_power, attack_power_description, attack_damage, exp):
        self.name = name
        self.description = description
        self.health = health 
        self.attack_power = attack_power
        self.attack_power_description = attack_power_description
        self.attack_damage = attack_damage
        self.exp = exp

    def __str__(self):
        return f"{self.name} : {self.description} (PV : {self.health}, Attaque : {self.attack_power})"
    
    def isliving(self):
        return self.health > 0
    
    def isdead(self):
        return self.health <= 0
    
    def attack_using(self):
        return f"{self.name} vous {self.attack_power_description}"
    
    def begin_attack(self):
        return f"{self.name} s'approche de vous dangereusement !"
    
    def fighting(self):
        self.attack_using()
        



        

    
    
    
                
        

            

        

        
    
