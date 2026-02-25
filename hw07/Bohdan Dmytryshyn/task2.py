PI = 3.14159265359


def area_rectangle(width, height):
    area = width * height
    return area


def area_triangle(base, height):
    area = 0.5 * base * height
    return area


def area_circle(radius):
    area = PI * radius * radius
    return round(area, 2)


def main():
    choice = input(
        "To calculate the area of a rectangle, press R; for a triangle, press T; and for a circle, press C: ")
    choice = choice.upper()

    if choice == "R":
        width = int(input("Enter Rectangle width: "))
        height = int(input("Enter Rectangle height: "))
        print(f"Rectangle area = {area_rectangle(width, height)}")
    elif choice == "T":
        base = int(input("Enter Triangle base: "))
        height = int(input("Enter Triangle height: "))
        print(f"Triangle area = {area_triangle(base, height)}")
    elif choice == "C":
        radius = int(input("Enter Circle radius: "))
        print(f"Circle area = {area_circle(radius)}")
    else:
        print("Wrong parameter")


if __name__ == "__main__":
    main()
