import math


def area_rectangle(width, height):
    area = width * height
    return area


def area_triangle(base, height):
    area = 0.5 * base * height
    return area


def area_circle(radius):
    area = math.pi * math.pow(radius,2)
    return round(area, 2)
