
from datetime import date
import math
class Students:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student_info(self):
        return f'l\'etudiant {self.name} a {self.age} '

    @classmethod
    def initbirthday(cls, name, birthday):
        return cls(name, date.today().year - birthday)



class Pizza:
    def __init__(self, ingredians, radius):
        self.ingredians = ingredians
        self.radius = radius

    def dir_pizza(self):
        return f'les ingredians sont {self.ingredians} '
    def self_radius(self):
        return Pizza.get_radius(self.radius)

    @classmethod
    def veg(cls):
        return cls(['tomate', 'onions', 'olives'])
    @classmethod
    def margurite(cls):
        return cls(['tomate', 'fromage', 'olives'])
    @classmethod
    def viande(cls):
        return cls(['viande_hachée', 'fromages', 'souce_tomate', 'olives'])
    @staticmethod
    def get_radius(r):
        return r ** 2 * math.pi

    


p1 = Pizza(['tomates', 'olives'], 6)
print(p1.self_radius())
print(p1.get_radius(4))



