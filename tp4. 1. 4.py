"""
2025-11-03
Ivan Zheryakov
Exercice de Classe 1 #4
"""
import random

class Hero:
    def __init__(self, name):
        self.hp = random.randint(2, 10)
        self.attack = random.randint(1, 6)
        self.defense = random.randint(1, 6)
        self.name = name

    def Damage_taken(self):
        if self.defense > self.attack:
            self.hp -= 0
            print(f"{self.name} has {self.hp} hp after taking 0 dmg")
        else:
            self.hp -= self.attack - self.defense
            print(f"{self.name} has {self.hp} hp after taking {self.attack - self.defense} dmg")

    def Alive(self):
        return self.hp > 0


h = Hero("Jack")

h.Damage_taken()
if not h.Alive():
    print("They have Died")
