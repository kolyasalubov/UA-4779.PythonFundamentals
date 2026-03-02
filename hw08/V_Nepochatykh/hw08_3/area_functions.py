import math

def rectangle_area (side1: float, side2: float) -> float | None:
    """
    function calculates the area of a rectangle given its two sides
    returns None if either value is not positive
    """
    return  side1*side2 if side1 > 0 and side2 > 0 else None

def triangle_area (base: float, height: float) -> float | None:
    """
    function calculates the area of a triangle given its base and height 
    returns None if either value is not positive
    """
    return 0.5*base*height if base > 0 and height > 0 else None

def  circle_area (radius: float) -> float | None:
    """
    function calculates the area of a circle given its radius
    returns None if either value is not positive
    """
    return math.pow(radius, 2)*math.pi if radius > 0 else None
