def calculate_areas():
    print('This program will help you calculate the area ' \
    'of ​​a triangle, rectangle or circle. \n') 
    print('To continue, use the prompts to select the desired ' \
    'shape and enter the necessary parameters\n')

    figure = input('If you choose a triangle, enter "t", if you choose a rectangle, ' \
    'enter "r", if you choose a circle, enter "c": ')

    if figure.lower() == "t":
        a = int(input('Enter the length of the base of the triangle(must be integer): '))
        h = int(input('Enter the height of the triangle(must be integer): '))
        area = 0.5 * a * h
        return f"The area of ​​the triangle is equal to: {area}"
    if figure.lower() == 'c':
        r = int(input('Enter the radius of the circle(must be integer): '))
        from math import pi
        area = pi * r**2
        return f"The area of ​​the circle is equal to: {round(area,2)}"
    if figure.lower() == 'r':
        a = int(input('Enter the length of the first side(must be integer): '))
        b = int(input('Enter the length of the second side(must be integer): '))
        area = a * b
        return f"The area of ​​the rectangle is equal to: {area}"
    else:
        return 'See you later'
    


print(calculate_areas())

