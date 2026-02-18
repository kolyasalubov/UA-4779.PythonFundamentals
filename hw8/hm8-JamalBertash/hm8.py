import re
password = input("Введіть пароль: ")
if len(password) < 6:
    print("Пароль повинен містити не менше 6 символів.")
elif len(password) > 16:
    print("Пароль повинен містити не більше 16 символів.")
elif not re.search(r'[A-Z]', password):
    print("Пароль повинен містити хоча бы одну велику букву.")
elif not re.search(r'[a-z]', password):
    print("Пароль повинен містити хоча бы одну маленьку букву.")
elif not re.search(r'[$#@]', password):
    print("Пароль повинен містити хоча бы один символ із $#@")
elif not re.search(r'[0-9]', password):
    print("Пароль повинен містить хотя бы одну цифру.")
else:
    print("Пароль відповідає всім вимогам.")

############################################################################



import area_func

value = input("Enter the shape whose area you want to calculate (rectangle, triangle, circle): ")


if value == "rectangle" or value == "Rectangle":

    area_func.area_of_rectangle()

elif value == "triangle" or value == "Triangle":

    area_func.area_of_triangle()

elif value == "circle" or value == "Circle":

    area_func.area_of_circle()

else:
    print("Incorrect name!")