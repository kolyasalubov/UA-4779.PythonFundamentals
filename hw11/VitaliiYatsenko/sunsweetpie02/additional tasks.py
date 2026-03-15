##########################################################################
#hw11.01

# def process_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative!")
#     if age % 2 == 0:
#         print(f"The age {age} is even.")
#     else:
#         print(f"The age {age} is odd.")

# try:
#     user_input = int(input("Enter your age: "))
#     process_age(user_input)
# except ValueError as e:
#     print("Error:", e)

###########################################################################
#hw11.02

# def number_to_day(number):
#     days = {
#         1: "Monday",
#         2: "Tuesday",
#         3: "Wednesday",
#         4: "Thursday",
#         5: "Friday",
#         6: "Saturday",
#         7: "Sunday"
#     }
#     if number not in days:
#         raise ValueError("Number must be between 1 and 7!")
#     return days[number]

# try:
#     user_input = int(input("Enter a number (1-7) for the day of the week: "))
#     day = number_to_day(user_input)
#     print(f"{user_input} is {day}.")
# except ValueError as e:
#     print("Error:", e)

############################################################################