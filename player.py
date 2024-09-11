import items

class Player:

    def __init__(self, attributes):
        self.name = attributes['name']
        self.age = attributes['age']
        self.place_of_birth = attributes['place_of_birth']
        self.inventory = [items.Dagger({"name": "Widow Maker", "description": "Excellent for close combat", "attack_power": 50}), items.Bow({"name": "Flying Death", "description": "Devastation from above", "attack_power": 100}), "Cloak", "Berries"]

    def __str__(self):
        return f"Player Details:\n> Name: {self.name}\n> Age: {self.age}\n> Place of Birth: {self.place_of_birth}"

    def item_obj_best_weapon(self):
        best_weapon = None
        max_attack_power = 0

        for weapon in self.inventory:
            try:
                if weapon.attack_power > max_attack_power:
                    best_weapon = weapon
                    max_attack_power = weapon.attack_power
            except AttributeError:
                continue

        return best_weapon
