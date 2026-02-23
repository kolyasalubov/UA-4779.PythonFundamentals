import math

def area_of_rectangle(a, b):
    """
    Returns the area of a rectangle
    """
    return a * b

def area_of_triangle(a, h):
    """
    Returns the area of a triangle
    """
    return 0.5 * a * h

def area_of_circle(r):
    """
    Returns the area of a circle
    """
    return math.pi * r ** 2

print("Choose the shape: rectangle, triangle, circle")
choice = input("Enter: ").lower()

match choice:
    case "rectangle":
        a = float(input("Enter length: "))
        b = float(input("Enter width: "))
        print("Area = ", area_of_rectangle(a, b))
    case "triangle":
        a = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print("Area = ", area_of_triangle(a, h))
    case "circle":
        r = float(input("Enter radius: "))
        print("Area = ", area_of_circle(r))
    case _:
        print("Error")