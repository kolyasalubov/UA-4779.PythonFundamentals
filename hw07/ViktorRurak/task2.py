import math


def find_area_of_rectangle(a, b):
    return a*b

def find_area_of_triangle(a, b, c):
    if a < b + c and b < a + c and c < a +b:
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5
    else:
        print("Not possible")
        

def find_area_of_circle(r):
    return math.pi * (r**2)

print(find_area_of_rectangle(2,5))
print(find_area_of_triangle(1,5,7))
print(find_area_of_circle(5))


