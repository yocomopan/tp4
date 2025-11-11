"""
2025-11-03
Ivan Zheryakov
Exercice de Classe 1 #3
"""
import math


class Circle:
    def __init__(self, ray):
        self.perimeter = None
        self.rayon = ray
        self.diameter = None
        self.surface_circle = None

    def solving_surface_circle(self):
        self.surface_circle = self.rayon * self.rayon * math.pi

    def solving_perimeter_circle(self):
        self.diameter = self.rayon * 2
        self.perimeter = self.diameter * math.pi

    def show_info(self):
        if self.perimeter is None:
            self.solving_perimeter_circle()
        if self.surface_circle is None:
            self.solving_surface_circle()
        print(f"Les variables de votre Cercle:\nPerimètre: {self.perimeter}\nAire: {self.surface_circle}\n")


c = Circle(10)
c.show_info()
