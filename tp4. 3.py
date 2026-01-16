"""
2025-11-11
Ivan Zheryakov
Exercice de classe 3
"""

import random


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


class Enum:
    def __init__(self):
        self.lawful_good = None
        self.lawful_neutral = None
        self.lawful_evil = None
        self.chaotic_good = None
        self.chaotic_neutral = None
        self.chaotic_evil = None
        self.true_neutral = None



class Kobold(NPC):
    def __init__(self, race="Kobold"):
        super().__init__(name="Pob Bob", race=race, species="Reptile")

    def show_kobold(self):
        print(f"HP: {self.npc_health}\n"
              f"Strength: {self.npc_strength}\n")

    def attaquer(self, cible):
        capable = random.randint(1, 20)

        if capable == 20:
            cible.subir_degats(random.randint(1, 8))
            print(f"GODLIKE {cible.npc_name}!")

        elif capable == 1:
            print("Il as manqué son coup, il est miserables...")

        else:
            if capable >= cible.npc_armor:
                cible.subir_degats(random.randint(1, 6))
                print(f"{cible.npc_name} touche!")
            else:
                print(f"Il as manqué son coup, l'armure de {cible.npc_name} l'a bloqué.")
        print("\n")

    def subir_degats(self, dommage):
        self.npc_health -= dommage


class Hero(NPC):
    def __init__(self, race="humain"):
        name = input("Quelle est votre nom? ")
        super().__init__(name, race=race, species="Ape")

    def show_hero(self):
        print(f"HP: {self.npc_health}\n"
              f"Strength: {self.npc_strength}\n"
              f"Name: {super()}")

    def attaquer(self, cible):
        capable = random.randint(1, 20)

        if capable == 20:
            cible.subir_degats(random.randint(1, 8))
            print(f"GODLIKE {cible.npc_name}!")

        elif capable == 1:
            print("Tu as manqué ton coup, tu es miserables...")

        else:
            if capable >= cible.npc_armor:
                cible.subir_degats(random.randint(1, 6))
                print(f"{cible.npc_name} touche!")
            else:
                print(f"Tu as manqué ton coup, l'armure de {cible.npc_name} l'a bloqué.")

    def subir_degats(self, dommage):
        self.npc_health -= dommage


n = NPC("A", "B", "C", "D")
h = Hero()
k = Kobold()
for i in range(40):
    h.attaquer(k)
    k.attaquer(h)
