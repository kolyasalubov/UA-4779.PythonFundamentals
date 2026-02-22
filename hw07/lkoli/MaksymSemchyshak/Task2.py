def rectangle_area(a, b):
    return a * b

def circle_area(r):
    return 3.14 * r**2

area = int(input('Whitch area you wanna calculate? (1 - rectangle_area, 2 - circle_area): '))
if area == 1:
    a = float(input('a: '))
    b = float(input('b: '))
    print(rectangle_area(a, b))
elif area == 2:
    r = float(input('r: '))
    print(circle_area(r))
else:
    print('Wrong choice')