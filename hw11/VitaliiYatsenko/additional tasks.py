# def check_age(age :int):

#     if age <= 0:
#         raise ValueError ('Age must be greater than 0')
#     else:
#         if age % 2 == 0:
#             return f'Your age: {age} is even.'
#         else:
#             return f'Your age: {age} is odd.'

# try:
#     age = int(input('Enter your age: '))
# except ValueError:
#     print('Enter integer')
# else:
#     try:
#         print(check_age(age))
#     except ValueError as e:
#         print(e)



days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

def return_day(number):
    if number not in days:
        raise ValueError('There are only 7 days in a week. Enter a number from 1 to 7.')
    else:
        result = days[number]
        return(result)


try:
    number = int(input('Enter number: '))
except ValueError:
    print("Enter integer from 1 to 7.")
else:
    try:
        (print(return_day(number)))
    except ValueError as e:
        print(e)






