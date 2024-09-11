class Weapon:

    def __init__(self, attributes = {}):
        self.name = attributes['name']
        self.description = attributes['description']
        self.attack_power = attributes['attack_power']

    def __str__(self):
        return f"\nWeapon Details:\n> Name of Weapon: {self.name}\n> Description of Weapon: {self.description}\n> Attack Power of Weapon: {self.attack_power}"

class Dagger(Weapon):

    def int_attack_boost(self):
        return (self.attack_power * 5)

class Bow(Weapon):

    def int_attack_boost(self):
        return (self.attack_power * 3)
