"""
2025-11-11
Ivan Zheryakov
Exercice de classe 2
"""
import random

play_game = True
k_list = []
h_list = []


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

    def attaquer(self, cible):
        capable = random.randint(1, 20)

        if capable == 20:
            cible.subir_degats(random.randint(1, 8))
            print("GODLIKE -k")

        elif capable == 1:
            print("Il est miserables...")

        else:
            cible.subir_degats(random.randint(1, 6))
            print("touche! -k")
        print("\n")

    def subir_degats(self, dommage):
        self.npc_health -= dommage


class Hero(NPC):
    def __init__(self, race="humain"):
        super().__init__(Name="Bob", Race=race, Species="Ape")

    def show_hero(self):
        print(f"HP: {self.npc_health}\n"
              f"Strength: {self.npc_strength}\n")

    def attaquer(self, cible):
        capable = random.randint(1, 20)

        if capable == 20:
            cible.subir_degats(random.randint(1, 8))
            print("GODLIKE -h")

        elif capable == 1:
            print("Tu es miserables...")

        else:
            cible.subir_degats(random.randint(1, 6))
            print("touche! -h")


    def subir_degats(self, dommage):
        self.npc_health -= dommage


n = NPC("A", "B", "C", "D")
h = Hero()
k = Kobold()
for i in range(50):
    h.attaquer(k)
    k.attaquer(h)

# while play_game:
#     OPS = int(input("Roulez ou Mourez\n"
#                     "1 - Debuter\n"
#                     "2 - Quitter\n"))
#
#     if OPS == 1:
#         h_list.append(h.npc_health)
#         k_list.append(k.npc_health)
#         n.show_info()
#
#         combat = True
#
#         while combat:
#             die_kobold = random.randint(1, 12)
#             die_hero = random.randint(1, 20)
#
#             if h.npc_health <= 0 and k.npc_health <= 0:
#                 print("Nulle. Vous et Kobold etes mort.\n"
#                       f"{h_list} - HERO HP evolution\n"
#                       f"{k_list} - KOBOLD HP evolution")
#                 play_game = False
#                 exit()
#
#             if h.npc_health <= 0:
#                 print("Vous etes mort! Kobold gagne.\n"
#                       f"{h_list} - HERO HP evolution\n"
#                       f"{k_list} - KOBOLD HP evolution")
#                 play_game = False
#                 exit()
#             if k.npc_health <= 0:
#                 print("Kobold est mort. Vous gagnez!\n"
#                       f"{h_list} - HERO HP evolution\n"
#                       f"{k_list} - KOBOLD HP evolution")
#                 play_game = False
#                 exit()
#             print("Ennemi: ")
#
#             k.show_kobold()
#             print("Vous: ")
#
#             h.show_hero()
#             input("")
#
#             if die_hero == 20:
#                 crit_hero = random.randint(6, 8)
#                 print(f"Attaque critique!\n"
#                       f"Vous tapez le kobold pour {crit_hero} degats\n ")
#                 k.npc_health -= crit_hero
#                 k_list.append(k.npc_health)
#
#
#             elif die_hero > k.npc_armor:
#                 die_hp_hero = random.randint(1, 6)
#                 print(f"Vous tapez Kobold pour {die_hp_hero}")
#                 k.npc_health -= die_hp_hero
#                 k_list.append(k.npc_health)
#
#             elif die_hero < k.npc_armor or die_hero == 1:
#                 print("Vous ratez votre coup.")
#                 k_list.append(k.npc_health)
#
#             if die_kobold > h.npc_armor:
#                 die_hp_kobold = random.randint(1, 6)
#                 print(f"Kobold vous tape pour {die_hp_kobold}\n")
#                 h.npc_health -= die_hp_kobold
#                 h_list.append(h.npc_health)
#
#             else:
#                 print("Kobold rate son coup.\n")
#                 h_list.append(h.npc_health)
#
#     elif OPS == 2:
#         play_game = False
#         print("LOADING COMPLETE\n"
#               "EXITING PROGRAM")
