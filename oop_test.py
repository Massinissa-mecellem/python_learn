
from datetime import date
import math
class Students:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student_info(self):
        return f'Student name is {self.name} has {self.age} '

class Man(Students):
    gender = 'male'
    number = 0
    def __init__(self, name, age, voice):
        super().__init__(name, age)
        self.voice = voice
        self.number +=1
    def Man_info(self):
        string = super().student_info()
        return string + f'his voice is {self.voice} and is a {self.gender}'



man = Man('massi', 25, 'hard')
print(man.Man_info())
print(man.number)










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

    





