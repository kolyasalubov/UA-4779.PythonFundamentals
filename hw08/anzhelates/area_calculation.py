import area_functions

choice = (input("Enter the shape: ")).lower()
match choice:
    case "rectangle":
        a = int(input("a: "))
        b = int(input("b: "))
        print(area_functions.rectangle_area(a, b))
    case "triangle":
        a = int(input("a: "))
        h = int(input("h: "))
        print(area_functions.triangle_area(a, h))
    case "circle":
        r = int(input("r: "))
        print(area_functions.circle_area(r))
    case _:
        print("Invalid")