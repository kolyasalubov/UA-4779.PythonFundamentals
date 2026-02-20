"""module implements task 7.1"""
import math

def get_largest_number(a:int, b:int) -> int:
    """Returns the largest of two numbers"""
    return max(a, b)

def get_rectangle_area(a: float, b: float) -> float:
    """Calculate the area of a rectangle"""
    return a * b

def get_triangle_area(base: float, height: float) -> float:
    """Calculate the area of a triangle"""
    return (base * height) / 2

def get_circle_area(radius: float) -> float:
    """Calculate the area of a circle"""
    return math.pi * radius ** 2

def get_shape_area(shape_name: str, *args) -> float:
    """Calculate the area of a shape based on its name."""
    shape_name = shape_name.lower()
    match shape_name:
        case 'rectangle':
            return get_rectangle_area(args[0], args[1])
        case 'triangle':
            return get_triangle_area(args[0], args[1])
        case 'circle':
            return get_circle_area(args[0])
        case _:
            raise ValueError(f"Unknown shape: {shape_name}")


def count_characters(s: str) -> dict[str, int]:
    """Calculate the number of characters in a given string."""
    char_count = {}
    for char in s:
        char_count[char] = char_count[char] + 1 if char in char_count else 1
    return char_count
