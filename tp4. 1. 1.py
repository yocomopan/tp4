"""
2025-11-03
Ivan Zheryakov
Exercice de Classe 1 #1
"""


class StringFoo:
    def __init__(self):
        self.message = ""

    def set_string(self, msg):
        self.message = msg

    def print_string(self):
        print(self.message.upper())


s = StringFoo()
s.set_string(msg="Bienvenu à Python!")
s.print_string()
