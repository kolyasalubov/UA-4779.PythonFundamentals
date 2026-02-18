import math

def area_of_rectangle(arg1=0,arg2=0):
    print('To find the area of ​​a rectangle, enter the following data:')
    arg1 = int(input("Specify width: "))
    arg2 = int(input("Specify the length: "))
    result = arg1 * arg2
    return print(result)


def area_of_triangle(arg1=0,arg2=0):
    print('To find the area of ​​a triangle, enter the following data:')
    arg1 = int(input("Specify width: "))
    arg2 = int(input("Specify base length: "))
    result = 0.5 * arg1 * arg2
    return print(result)
    


def area_of_circle(arg=0):
    print('To find the area of ​​a circle, enter the following data:')
    arg = int(input("Specify radius: "))
    result = math.pi * pow(arg, 2)
    return print(round(result, 2))