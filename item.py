class Item:

    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight
    
    def __str__(self):
        return f"{self.name} : {self.description} ({self.weight} kg)"

    def get_inventory(self):
        inventory = self.inventory
        if inventory == {}:
            print("votre inventaire est vide")
            return False
        else:
            return f"Vous disposez des items suivants :\n {inventory.get()}"