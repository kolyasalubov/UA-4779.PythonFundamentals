PI = 3.14159265359


def rectangle_area(width, height):
    return width * height



def triangle_area(base, height):
    return 0.5 * base * height


def circle_area(radius):
    return PI * radius ** 2

print("Choose a shape:")
print("1 - Rectangle")
print("2 - Triangle")
print("3 - Circle")

choice = input("Enter your choice (1/2/3):")

if choice == "1":
    width = int(input("Enter width:"))
    height = int(input("Enter height:"))
    print("Width:", width)
    print("Height:", height)
    print("Rectangle area:", rectangle_area(width, height))

elif choice == "2":
    base = int(input("Enter base:"))
    height = int(input("Enter height:"))
    print("Base:", base)
    print("Height:", height)
    print("Tringle area:",triangle_area(base, height))

elif choice == "3":
    radius = int(input("Enter radius:"))
    print("Radius:", radius)
    print("Radius area:", circle_area(radius))
else:
    print("Invalid input!")