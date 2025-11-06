"""
2025-11-06
Ivan Zheryakov
Exercice de Classe 1 #6
"""
import random

class Hero:
    def __init__(self, name):
        self.hp = random.randint(2, 10)
        self.attack = random.randint(1, 6)
        self.defense = random.randint(1, 6)
        self.charisma = random.randint(1, 2)
        self.reducing = None
        self.reduction = None
        self.name = name

    def Damage_taken(self):

        self.reducing = self.attack / self.charisma
        self.reduction = self.attack - self.reducing

        if self.defense > self.reduction:
            self.hp -= 0
            print(f"{self.name} has {self.hp} hp after taking 0 dmg")
        else:
            self.hp -= self.reduction - self.defense
            print(f"{self.name} has {self.hp} hp after taking {self.reduction - self.defense} dmg")

    def Alive(self):
        return self.hp > 0


h = Hero("JacK")

h.Damage_taken()
if not h.Alive():
    print("They have Died")





