#######################################################################################

import math 

def area_rectangle (length, width):
    return length * width
def area_triangle (base, height):
    return 0.5 * base * height
def area_circle (radius):
    return math.pi * radius * 2

figure = input("figure (rectangle, triangle, circle): ").lower()

if figure == "rectangle":
   print ("Area: ", area_rectangle(float(input("length: ")), float(input("width: "))))
elif figure == "triangle":
   print ("Area: ", area_triangle(float(input("base: ")), float(input("height: "))))
elif figure == "circle":
   print ("Area: ", area_circle(float(input("radius: "))))
else:
   print ("unknown figure")

#########################################################################################