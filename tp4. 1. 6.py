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
        self.dexterity = random.randint(1, 6)
        self.name = name

    def Damage_taken(self):
        if self.dexterity > self.attack:
            self.hp -= 0
            print(f"{self.name} a évité {self.attack} dégats")

        elif self.defense >= self.attack:
            self.hp -= 0
            print(f"{self.name} a {self.hp} hp après avoir reçu 0 dégats")
        else:
            self.hp -= self.attack - self.defense
            print(f"{self.name} a {self.hp} hp après avoir reçu {self.attack - self.defense} dégats")

    def Alive(self):
        return self.hp > 0


h = Hero("Jack")

h.Damage_taken()
if not h.Alive():
    print(f"Il/Elle est mort")
