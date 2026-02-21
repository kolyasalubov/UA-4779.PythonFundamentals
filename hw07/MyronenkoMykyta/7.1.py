#~~~~~~~~~~~~~~Task1~~~~~~~~~~~~~~~~~~~~~~
# def get_max_number(a, b):
#     """
#     Returns the larger of two numbers.
#     Params:
#     a (int or float): First number
#     b (int or float): Second number
#     Return:
#     int or float: The larger number
#     """
#     if a > b:
#         return a
#     else:
#         return b

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# result = get_max_number(num1, num2)
# print("Larger number:", result)


#~~~~~~~~~~~~~~Task2~~~~~~~~~~~~~~~~~~~~~~
# import math


# def rectangle_area(length, width):
#     return length * width


# def triangle_area(base, height):
#     return 0.5 * base * height


# def circle_area(radius):
#     return math.pi * radius ** 2


# print("Choose a shape:")
# print("1 - Rectangle")
# print("2 - Triangle")
# print("3 - Circle")

# choice = input("Enter your choice (1/2/3): ")

# if choice == "1":
#     length = float(input("Enter length: "))
#     width = float(input("Enter width: "))
#     print("Rectangle area:", rectangle_area(length, width))

# elif choice == "2":
#     base = float(input("Enter base: "))
#     height = float(input("Enter height: "))
#     print("Triangle area:", triangle_area(base, height))

# elif choice == "3":
#     radius = float(input("Enter radius: "))
#     print("Circle area:", circle_area(radius))

# else:
#     print("Invalid choice!")

#~~~~~~~~~~~~~~Task3~~~~~~~~~~~~~~~~~~~~~~
# def count_characters(text):
#     """
#     Counts the number of each character in a string.
#     Params:
#     text (str): Input string
#     Returns:
#     dict: Dictionary with character counts
#     """
#     char_count = {}

#     for char in text:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1

#     return char_count


# input_text = input("Enter a string: ")
# result = count_characters(input_text)

# print(result)
