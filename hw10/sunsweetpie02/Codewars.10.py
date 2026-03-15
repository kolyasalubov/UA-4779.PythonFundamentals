##################################################################################
#I. Ball-super-ball

# class Ball(object):
#     def __init__(self, ball_type="regular"):
#         self.ball_type = ball_type
# ball1 = Ball()
# ball2 = Ball("super")
# print(ball1.ball_type)
# print(ball2.ball_type)

###################################################################################
# II. Color-ghost

# import random

# class Ghost:
#     def __init__(self):
#         self.color = random.choice(["white", "yellow", "purple", "red"])

###################################################################################
# III. Basic-subclasses-Adam-and-Eve

# class Human:
#     pass
# class Man(Human):
#     pass
# class Woman(Human):
#     pass
# def God():
#     return [Man(), Woman()]

###################################################################################
# IV. Classy-classes

# class Person:
#     def __init__(self,name,age):
#         self.info= f"{name}s age is {age}"
#     def getInfo(self):
#         return self.info

#     @property
#     def Info(self):
#         return self.info
# john = Person("john", 34)
# print(john.getInfo())
# print(john.Info) 

###################################################################################
# V. Building Spheres

# import math

# class Sphere(object):
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass

#     def get_radius(self):
#         return self.radius

#     def get_mass(self):
#         return self.mass

#     def get_volume(self):
#         volume = (4/3) * math.pi * self.radius ** 3
#         return round(volume, 5)

#     def get_surface_area(self):
#         area = 4 * math.pi * self.radius ** 2
#         return round(area, 5)

#     def get_density(self):
#         density = self.mass / ((4/3) * math.pi * self.radius ** 3)
#         return round(density, 5)

###################################################################################
# VI. Dynamic Classes

# def class_name_changer(cls, new_name):
#     if not new_name[0].isupper():
#         raise ValueError("Class name must start with an uppercase letter")
#     if not new_name.isalnum():
#         raise ValueError("Class name must be alphanumeric")
#     cls.__name__ = new_name
#     return cls

###################################################################################