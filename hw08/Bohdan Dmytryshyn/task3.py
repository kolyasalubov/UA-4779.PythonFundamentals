import module_area as area

def main():
    choice = input(
        "To calculate the area of a rectangle, press R; for a triangle, press T; and for a circle, press C: ")
    choice = choice.upper()

    if choice == "R":
        width = float(input("Enter Rectangle width: "))
        height = float(input("Enter Rectangle height: "))
        print(f"Rectangle area = {area.area_rectangle(width, height)}")
    elif choice == "T":
        base = float(input("Enter Triangle base: "))
        height = float(input("Enter Triangle height: "))
        print(f"Triangle area = {area.area_triangle(base, height)}")
    elif choice == "C":
        radius = float(input("Enter Circle radius: "))
        print(f"Circle area = {area.area_circle(radius)}")
    else:
        print("Wrong parameter")


if __name__ == "__main__":
    main()
