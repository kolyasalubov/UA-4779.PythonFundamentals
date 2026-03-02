import area_functions



choice = int(input ("Enter a number corresponding to the shape whose area you would like to calculate:\n 1 — rectangle, 2 — triangle, 3 — circle  "))

match choice:
    case 1:
        try:
            side1 = float(input("Enter first side length, m: "))
            side2 = float(input("Enter second side length, m: "))
        except ValueError:
            print ("Invalid input")
        else:
            area = area_functions.rectangle_area (side1, side2)
            print(f"The area of your rectangle is: {round(area,2)} square meters" if area is not None else "Invalid input")
    case 2:
        try:
            base = float(input("Enter base length, m: "))
            height = float(input("Enter height length, m: "))
        except ValueError:
            print ("Invalid input")
        else:
            area = area_functions.triangle_area(base, height)
            print(f"The area of your triangle is: {round(area,2) } square meters" if area is not None else "Invalid input")
    case 3:
        try:
            radius = float(input("Enter radius length, m: "))
        except ValueError:
            print ("Invalid input")
        else:
            area = area_functions.circle_area (radius)
            print(f"The area of your circle is: {round(area,2)} square meters" if area is not None else "Invalid input")
    case _:
        print ("Invalid choice")