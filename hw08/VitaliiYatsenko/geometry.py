def area_of_rectangle(a, b):
    s = a * b
    return s

def area_of_triangle(h, a):
    s = 0.5 * h * a
    return s

def area_of_circle(r):
    from math import pi
    from math import pow
    s = pi * pow(r,2)
    return round(s,2)

