"""
2025-11-11
Ivan Zheryakov
Exercice de classe 3
"""

import random
from collections import Counter
from dataclasses import dataclass
from enum import Enum


class Alignment(Enum):
    LAWFUL_GOOD = 0
    LAWFUL_NEUTRAL = 1
    LAWFUL_EVIL = 2
    CHAOTIC_GOOD = 3
    CHAOTIC_NEUTRAL = 4
    CHAOTIC_EVIL = 5
    NEUTRAL_GOOD = 6
    TRUE_NEUTRAL = 7
    NEUTRAL_EVIL = 8
    UNDEFINED = 9

def stats():
    """
    automatic function
    List captures 4 random generated numbers and stores them
    Reverse puts the list in order from biggest to smallest
    Pop() removes the last info stored in the list
    """
    donnees = []
    for x in range(4):
        donnees.append(random.randint(1, 6))
    donnees.sort(reverse=True)
    donnees.pop()
    return sum(donnees)


@dataclass
class Item:
    quantity: int
    name: str


class Bag:
    def __init__(self):
        # self.item_list = ["lamp oil", "rope", "bomb"]
        self.bag = []

    def adding_items(self, item_ajouter: Item):
        if len(self.bag) == 0:
            self.bag.append(item_ajouter)
        else:
            for item in self.bag:
                if item_ajouter.name == item.name:
                    item.quantity += item_ajouter.quantity

        #self.bag.append(item_ajouter)
        # Counter(self.bag)
        # if item_ajouter = None:
        # continue

    def removing_items(self, item_remove: Item):
        if len(self.bag) == 0:
            self.bag.pop()
        else:
            for item in self.bag:
                if item_remove.name == item.name:
                    item.quantity -= item_remove.quantity
# Counter(self.bag)


b = Bag()
b.adding_items(Item(2, "or"))
b.adding_items(Item(30, "argent"))
b.adding_items(Item(10, "argent"))
print(b.bag)


class NPC:
    def __init__(self, name="", profession="", race="", species=""):
        self.npc_race = race
        self.npc_name = name
        self.npc_species = species
        self.npc_profession = profession
        self.npc_health = random.randint(1, 12)
        self.npc_armor = random.randint(1, 12)
        self.npc_strength = stats()
        self.npc_dext = stats()
        self.npc_con = stats()
        self.npc_iq = stats()
        self.npc_wisdom = stats()
        self.npc_cha = stats()
        self.alignement = Alignment.UNDEFINED

    def show_info(self):
        print(f"{self.npc_name} the {self.npc_profession} NPC:\n"
              f"- Race, Species: {self.npc_race}, {self.npc_species}\n"
              f"- Strength {self.npc_strength}\n"
              f"- Dexterity {self.npc_dext}\n"
              f"- Constitution {self.npc_con}\n"
              f"- Intelligence {self.npc_iq}\n"
              f"- Wisdom {self.npc_wisdom}\n"
              f"- Charisma {self.npc_cha}\n"
              f"- {self.npc_health} health et {self.npc_armor} armure\n")


class Alignment(Enum):
    LAWFUL_GOOD = 0
    LAWFUL_NEUTRAL = 1
    LAWFUL_EVIL = 2
    CHAOTIC_GOOD = 3
    CHAOTIC_NEUTRAL = 4
    CHAOTIC_EVIL = 5
    NEUTRAL_GOOD = 6
    TRUE_NEUTRAL = 7
    NEUTRAL_EVIL = 8
    UNDEFINED = 9


# class Enum:
#     def __init__(self):  # [colonne;rangée]
#         #    self.lawful_good = None # [1;1]
#         #    self.lawful_neutral = None # [1;2]
#         #    self.lawful_evil = None # [1;3]
#         #    self.chaotic_good = None # [3;1]
#         #    self.chaotic_neutral = None # [3;2]
#         #    self.chaotic_evil = None # [3;3]
#         #    self.neutral_good = None # [2;1]
#         #    self.true_neutral = None # [2;2]
#         #    self.neutral_evil = None # [2;3]
#         self.alignement = ["lawful good", "lawful neutral", "lawful evil"
#             , "neutral good", "true neutral", "neutral evil"
#             , "chaotic good", "chaotic neutral", "chaotic evil"]


class Kobold(NPC):
    def __init__(self, race="Kobold"):
        super().__init__(name="Pob Bob", race=race, species="Reptile")
        self.alignement = Alignment.NEUTRAL_EVIL

    def show_kobold(self):
        print(f"Name: {self.npc_name}\n"
              f"HP: {self.npc_health}\n"
              f"Strength: {self.npc_strength}\n"
              f"Attribut: {self.alignement}\n")

    def attaquer(self, cible):
        capable = random.randint(1, 20)
        print(f"{self.npc_name} roule {capable} pour attaquer...")

        if capable == 20:
            cible.subir_degats(random.randint(1, 8))
            print(f"GODLIKE {self.npc_name}!")

        elif capable == 1:
            print("Il as manqué son coup, il est miserables...")

        else:
            if capable >= cible.npc_armor:
                cible.subir_degats(random.randint(1, 6))
                print(f"{self.npc_name} touche!")
            else:
                print(f"Il as manqué son coup, l'armure de {cible.npc_name} l'a bloqué.")
        print("\n")

    def subir_degats(self, dommage):
        self.npc_health -= dommage

    def alive(self):
        return self.npc_health > 0


class Hero(NPC):
    def __init__(self, race="humain"):
        name = input("Quelle est votre nom? ")
        super().__init__(name, race=race, species="Ape")

    def show_hero(self):
        print(f"Name: {self.npc_name}\n"
              f"HP: {self.npc_health}\n"
              f"Strength: {self.npc_strength}\n"
              f"Attribut: {self.alignement}\n")

    def attaquer(self, cible):
        capable = random.randint(1, 20)
        print(f"{self.npc_name} roule {capable} pour attaquer...")
        if capable == 20:
            cible.subir_degats(random.randint(1, 8))
            print(f"GODLIKE {self.npc_name}!")

        elif capable == 1:
            print("Tu as manqué ton coup, tu es miserables...")

        else:
            if capable >= cible.npc_armor:
                cible.subir_degats(random.randint(1, 6))
                print(f"{self.npc_name} touche!")
            else:
                print(f"Tu as manqué ton coup, l'armure de {cible.npc_name} l'a bloqué.")

    def subir_degats(self, dommage):
        self.npc_health -= dommage

    def alive(self):
        return self.npc_health > 0


n = NPC("A", "B", "C", "D")
h = Hero()
k = Kobold()
combat = True
while combat:
    # for i in range(40):
    h.attaquer(k)
    k.attaquer(h)
    if not h.alive():
        print(f"{h.npc_name} est mort")
        combat = False
    if not k.alive():
        print(f"{k.npc_name} est mort")
        combat = False
    h.show_hero()
    k.show_kobold()
