def check_age(age):
    if age < 0:
        raise ValueError("Wrong input data: not positive number")
    if age % 2 == 0:
        print('Age is even number')
    else:
        print('Age is odd number')


def process_input():
    try:
        age = int(input("Enter age: "))
        check_age(age)
    except ValueError as e:
        print(e)


process_input()
