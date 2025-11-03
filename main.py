"""
2025-11-03
Ivan Zheryakov
Classes
"""

#from math import pi
import math
import random

class StringFoo:
    def __init__(self):
        self.message = ""

    def set_string(self, msg):
        self.message = msg

    def print_string(self):
        print(self.message.upper())


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
        print(f"Your Circle's stats are:\nPerimeter: {self.perimeter}\nSurface: {self.surface_circle}\n")


c = Circle(10)
c.show_info()


class Hero:
    def __init__(self):
        self.hp = None
        self.Attack = None
        self.Defense = None
        self.Name = ""

    def rolling_hp(self):
        self.hp = random.randint(2, 10)

    def rolling_AnD(self):
        self.Attack = random.randint(1, 6)
        self.Defense = random.randint(1, 6)

    def Damage_taken(self):
        pass


