# Regular Ball Super Ball
class Ball(object):
    def __init__(self, ball_type = 'regular'):
        self.ball_type = ball_type


# Color-ghost
import random

class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


# Basic subclasses - Adam and Eve
def God():
    return[m, w]

class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

m = Man()
w = Woman()


# Classy Classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def info(self):
        return f"{self.name}s age is {self.age}"
    
    def getInfo(self):
        return f"{self.name}s age is {self.age}"


# Building Spheres
from math import pi

class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = float(radius)
        self.mass = float(mass)
    
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return round((4/3)*pi*self.radius**3, 5)
    
    def get_surface_area(self):
        return round(4*pi*self.radius**2, 5)
    
    def get_density(self):
        return round(self.mass / self.get_volume(), 5)

ball = Sphere(2,50)
print(ball.get_radius())
print(ball.get_mass())
print(ball.get_volume())
print(ball.get_surface_area())
print(ball.get_density())


# Python's Dynamic Classes #1
import re

def class_name_changer(cls, new_name):
    pattern = r"^[A-Z][A-Za-z0-9]*$"
    if re.match(pattern, new_name):
        cls.__name__ = new_name
    else:
        raise ValueError("Invalid")