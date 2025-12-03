"""
2025-11-11
Ivan Zheryakov
Exercice de classe 2
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
    def __init__(self, Name="", Profession="", Race="", Species=""):
        self.npc_race = Race
        self.npc_name = Name
        self.npc_species = Species
        self.npc_profession = Profession
        self.npc_health = 20
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
              f"- {self.npc_health} health and {self.npc_armor} armor")


h = NPC("Yvan", "Programmeur", "Humain", "Humain")
h.show_info()


class Kobold(NPC):
    def __init__(self, Race):
        super().__init__(Name="Bob", Race="Kobold", Species="Kobold")
        self.npc_strength = stats()
        self.npc_health = 20
        self.npc_armor -= 3


class Hero(NPC):
    def __init__(self, Race):
        super().__init__(Name="Bob", Race="Humain", Species="humain")
        self.npc_strength = stats()


