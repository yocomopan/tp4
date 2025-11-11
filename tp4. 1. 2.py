"""
2025-11-03
Ivan Zheryakov
Exercice de Classe 1 #2
"""


class Rectangle:
    def __init__(self, largeur, longueur):
        self.surface_rectangle = None
        self.length = longueur
        self.width = largeur

    def solving_surface_rectangle(self):
        self.surface_rectangle = self.length * self.width

    def show_info(self):
        if self.surface_rectangle is None:
            self.solving_surface_rectangle()
        print(f"This rectangle's surface is {self.surface_rectangle}")


r = Rectangle(9, 8)
r.show_info()
