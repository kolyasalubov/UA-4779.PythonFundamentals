# class Ball:
#     def __init__(self, ball_type='regular'):
#         self.ball_type = ball_type


# -----------------------------------------------

# class Ghost:
#     def __init__(self, color=None):
#         import random
#         self.color = random.choice(['yellow','white','red','purple'])


# -----------------------------------------------

# class Human:
#     pass

# class Man(Human):
#     pass

# class Woman(Human):
#     pass

# a = Man()
# e = Woman()


# def God():
#     return [a,e] 


# -----------------------------------------------

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age

#     @property
#     def info(self):
#         return f'{self.name}s age is {self.__age}'


# -----------------------------------------------

# class Block:
#     def __init__(self, params=['width', 'length', 'height']):
#         self.width = params[0]
#         self.length = params[1]
#         self.height = params[2]

#     def get_width(self):
#         return self.width
    
#     def get_length(self):
#         return self.length
    
#     def get_height(self):
#         return self.height
    
#     def get_volume(self):
#         volume = self.width * self.length * self.height
#         return volume
    
#     def get_surface_area(self):
#         s = 2 * (self.width * self.length + self.length * self.height + self.height * self.width)
#         return s

# import math

# class Sphere:
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass

#     def get_radius(self):
#         return self.radius
    
#     def get_mass(self):
#         return self.mass
    
#     def get_volume(self):
#         volume = 4/3 * round(math.pi, 4) * self.radius ** 3
#         return round(volume, 5)
    
#     def get_surface_area(self):
#         s = 4 * round(math.pi, 4) * self.radius ** 2
#         return round(s, 5)
    
#     def get_density(self):
#         d = self.mass / (4/3 * round(math.pi, 4) * self.radius ** 3)
#         return round(d, 5)


# -----------------------------------------------

# import re

# def class_name_changer(cls, new_name):
#     template = r'^[A-Z][A-Za-z0-9]*$'
#     t = re.compile(template)

#     if re.fullmatch(t, new_name):
#         cls.__name__ = new_name
#         return cls.__name__
#     raise ValueError('opps')

