import re
from geometry import area_of_circle
from geometry import area_of_rectangle
from geometry import area_of_triangle

print('This program will help you calculate area of rectangle, triangle and circle\n')
print('To continue, you need to select a figure and enter the required parameters.\n')
figure = input('Prompt:\n\tTo select a triangle enter "t".' \
'\n\tTo select a rectangle, enter "r".' \
'\n\tTo select a circle, enter "c".' \
'\nEnter the symbol of the selected figure: ')

template = r'^[trc]$'
entered_char = re.compile(template)

if entered_char.search(figure):
    if figure.lower() == 't':
        h = int(input('Enter the height of the triangle: '))
        a = int(input('Enter the side of the triangle: '))
        print(f'Area of triangle is: {area_of_triangle(h,a)}')
    if figure.lower() == 'r':
        a = int(input('Enter the first side of the rectangle: '))
        b = int(input('Enter the second side of the rectangle: '))
        print(f'Area of rectangle is: {area_of_rectangle(a,b)}')
    if figure.lower() == 'c':
        r = int(input('Enter the radius of the circle: '))
        print(f'Area of circle is: {area_of_circle(r)}')
else:
    print('You have entered an incorrect parameter.')

      

