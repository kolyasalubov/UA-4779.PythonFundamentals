
def calc_area_r(a, b):
    """
    Calculates the area of a rectangle given its height and width.
    """
    area_r = a * b
    return (area_r)

def calc_area_t(ht, bt):
    """
    Calculates the area of a triangle given its height and base.
    """
    area_t = (ht * bt) / 2
    return (area_t)

def calc_area_c(r):
    """
    Calculates the area of a circle given its radius.
    """
    area_c = 3.14*r*2
    return (area_c)

choice = (input("Type 1 to calculate area of rectangle, 2 " \
                "— for triangle, 3 for circle: "))

if choice == "1":
    x = int(input("Enter height: "))
    y = int(input("Enter width: "))
    print("Area of rectangle is", calc_area_r(x,y))
elif choice == "2":
    x = int(input("Enter height: "))
    y = int(input("Enter base: "))
    print("Area of triangle is", calc_area_t(x,y))
elif choice == "3":
    x = int(input("Enter radius: "))
    print("Area of circle is", calc_area_c(x))
else:
    print("Error")
