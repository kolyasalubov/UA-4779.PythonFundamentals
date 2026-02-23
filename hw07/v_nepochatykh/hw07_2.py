from math import pi

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
    return pi*radius**2 if radius > 0 else None

choice = int(input ("Enter a number corresponding to the shape whose area you would like to calculate:\n 1 — rectangle, 2 — triangle, 3 — circle  "))

match choice:
    case 1:
        try:
            side1 = float(input("Enter first side length, m: "))
            side2 = float(input("Enter second side length, m: "))
        except ValueError:
            print ("Invalid input")
        else:
            area = rectangle_area (side1, side2)
            print(f"The area of your rectangle is: {round(area,2)} square meters" if area is not None else "Invalid input")
    case 2:
        try:
            base = float(input("Enter base length, m: "))
            height = float(input("Enter height length, m: "))
        except ValueError:
            print ("Invalid input")
        else:
            area = triangle_area(base, height)
            print(f"The area of your triangle is: {round(area,2) } square meters" if area is not None else "Invalid input")
    case 3:
        try:
            radius = float(input("Enter radius length, m: "))
        except ValueError:
            print ("Invalid input")
        else:
            area = circle_area (radius)
            print(f"The area of your circle is: {round(area,2)} square meters" if area is not None else "Invalid input")
    case _:
        print ("Invalid choice")