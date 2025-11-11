"""
2025-11-06
Ivan Zheryakov
Exercices de classe 1 #5
"""
import random


class Human:
    def __init__(self):
        """
        Variables / 'stats' de l'humain.
        """
        self.human_strength = random.randint(1, 20)
        self.human_dexterity = random.randint(1, 20)
        self.human_con = random.randint(1, 20)
        self.human_iq = random.randint(1, 20)
        self.human_wisdom = random.randint(1, 20)
        self.human_charisma = random.randint(1, 20)

    def show_info(self):
        print(
            f"Force {self.human_strength}\n"
            f"Dextérité {self.human_dexterity}\n"
            f"Constitution {self.human_con}\n"
            f"Intelligence {self.human_iq}\n"
            f"Sagesse {self.human_wisdom}\n"
            f"Charisme {self.human_charisma}\n")


Execute = Human()
Execute.show_info()
