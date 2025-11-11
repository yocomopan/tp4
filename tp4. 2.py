"""
2025-11-11
Ivan Zheryakov
Exercice de classe 2
"""
import random


class NPC:
    def __init__(self, sides=6):
        self.sides = sides
        self.npc_strength = random.randint(1, 6)
        self.npc_dexterity = random.randint(1, 6)
        self.npc_con = random.randint(1, 6)
        self.npc_iq = random.randint(1, 6)
        self.npc_wisdom = random.randint(1, 6)
        self.npc_charisma = random.randint(1, 6)


