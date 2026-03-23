# Ball-super-ball
class Ball(object):
    def __init__(self, type = 'regular'):
        self.ball_type = type
# Color-ghost
import random
class Ghost(object):
    def __init__(self):
        colors = ['white', 'yellow', 'purple', 'red']
        self.color = random.choice(colors)
# Basic-subclasses-Adam-and-Eve
class Human:
    pass
class Man(Human):
    pass
class Woman(Human):
    pass

man = Man()
woman = Woman()

def God():
    return [man, woman]
# Classy-classes
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age  
        self.info=f"{name}s age is {age}"
# Building Spheres
from math import pi
class Sphere():
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_volume(self):
        return 4/3*pi*self.radius**3
    def get_surface_area(self):
        return 4*pi*self.radius**2
    def get_density(self):
        return self.mass/self.get_volume()
# Dynamic Classes
import re
def class_name_changer(cls, new_name):
    pattern = r"^[A-Z][A-Za-z0-9]*$"
    if re.match(pattern, new_name):
        cls.__name__ = new_name
    else:
        raise ValueError("Invalid class name")