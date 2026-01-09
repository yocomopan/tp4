"""
2025-11-11
Ivan Zheryakov
Exercice de classe 2
"""
import random

play_game = True


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
              f"- {self.npc_health} health and {self.npc_armor} armor\n")


# h = NPC("Yvan", "Programmeur", "Humain", "Humain")
# h.show_info()


class Kobold(NPC):
    def __init__(self, race="Kobold"):
        super().__init__(Name="Bob", Race=race, Species="Reptile")

    def show_kobold(self):
        print(f"HP: {self.npc_health}\n"
              f"Strength: {self.npc_strength}\n")


class Hero(NPC):
    def __init__(self, race="humain"):
        super().__init__(Name="Bob", Race=race, Species="Ape")

    def show_hero(self):
        print(f"HP: {self.npc_health}\n"
              f"Strength: {self.npc_strength}\n")


# he = Hero
# he.show_hero()

while play_game:
    OPS = int(input("Roulez ou Mourez\n"
                    "1 - Debuter\n"
                    "2 - Quitter\n"))
    if OPS == 1:
        n = NPC("A", "B", "C", "D")
        n.show_info()
        combat = True
        die_kobold = random.randint(1, 12)
        die_hero = random.randint(1, 20)
        while combat:
            if h.npc_health == 0
                print()

            print("Ennemi: ")
            k = Kobold()
            k.show_kobold()
            print("Vous: ")
            h = Hero()
            h.show_hero()
            input("")

            if die_hero == 20:
                crit_hero = random.randint(6, 8)
                print(f"Attaque critique!\n"
                      f"Vous tapez le kobold pour {crit_hero} degats\n ")

            elif die_hero > k.npc_armor:
                die_hp_hero = random.randint(1, 6)
                print(f"Vous tapez Kobold pour {die_hp_hero}")

            elif die_hero < k.npc_armor or die_hero == 1:
                print("Vous ratez votre coup.")

            if die_kobold > h.npc_armor:
                die_hp_kobold = random.randint(1, 6)
                print(f"Kobold vous tape pour {die_hp_kobold}\n")

            else:
                print("Kobold rate son coup.\n")

    elif OPS == 2:
        play_game = False
        print("LOADING COMPLETE\n"
              "EXITING PROGRAM")
