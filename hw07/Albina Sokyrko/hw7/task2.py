from math import pi

def area_of_rectangle(length, width):
    return length * width

def area_of_triangle(base, height):
    return 0.5 * base * height

def area_of_circle(radius):
    return pi * radius ** 2

choice = int(input("Choose shape (1 - rectangle, 2 - triangle, 3 - circle): "))

match choice:
    case 1:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        print("Area of rectangle:", area_of_rectangle(length, width))

    case 2:
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print("Area of triangle:", area_of_triangle(base, height))

    case 3:
        radius = float(input("Enter radius: "))
        print("Area of circle:", area_of_circle(radius))
    case _:
        print("Invalid choice")