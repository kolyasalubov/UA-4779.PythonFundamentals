"""Write a function that returns the largest number of two numbers
(use DocStrings documentation strings in the function)."""

def largest_num(a, b:int) -> int:
    """The function returns the largest 
    of two numbers entered"""
    return a if a > b else b

###################################################################

"""Write a program that calculates the area of a rectangle, triangle and circle 
(write three functions to calculate the area. And call them in the main 
program depending on the user's choice)."""


PI = 3.141592653589793

print("This function will help you find the area of ​​a rectangle, triangle, or circle.") 
name_figure = input("Enter the name of the shape you want to find the area of: ")
    
def area_of_rectangle(arg1=0,arg2=0):
    print('To find the area of ​​a rectangle, enter the following data:')
    arg1 = int(input("Specify width: "))
    arg2 = int(input("Specify the length: "))
    result = arg1 * arg2
    print(result)


def area_of_triangle(arg1=0,arg2=0):
    print('To find the area of ​​a triangle, enter the following data:')
    arg1 = int(input("Specify width: "))
    arg2 = int(input("Specify base length: "))
    result = 0.5 * arg1 * arg2
    print(result)
    


def area_of_circle(arg=0):
    global PI
    print('To find the area of ​​a circle, enter the following data:')
    arg = int(input("Specify radius: "))
    result = PI * arg**2
    print(round(result, 2))

if name_figure == "rectangle" or name_figure == "Rectangle":

    area_of_rectangle()

elif name_figure == "triangle" or name_figure == "Triangle":

    area_of_triangle()

elif name_figure == "circle" or name_figure == "Circle":

    area_of_circle()

else:
    print("Incorrect name!")

###########################################################################

"""Write a function that calculates the number of characters included in given string"""


def kri(arg):
    result = {}
    for i in arg:
        if i in result:
            result[i] = result[i] + 1  
        else:
            result[i] = 1 
    return result