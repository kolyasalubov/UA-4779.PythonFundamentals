print('Hi! This program will help you perform standard mathematical operations ' \
'such as:\naddition, subtraction, multiplication and division. \n')

print('You need to select the required mathematical operation using the buttons: "+", "-", "*", "/" '
'\nand enter the numbers with which you need to perform the selected operation.')

operator = input('Enter operator as like("+", "-", "*", "/"): ')
operator_list = ["+", "-", "*", "/"]

if operator not in operator_list:
    print('Oops, this operation is not supported.')
else:
    numbers = input('Enter the numbers with which you want to perform the ' \
    'selected operation, separated by commas: ')
    if numbers == " ":
        print('You need to enter at least 2 numbers')
    else:
        tuple_numbers = tuple(int(n) for n in numbers.split(','))
        if operator == '+':
            from func import addition
            print(f"\tThe result of this operation is: {addition(*tuple_numbers)}")
        if operator == '-':
            from func import substraction
            print(f"\tThe result of this operation is: {substraction(*tuple_numbers)}")
        if operator == '*':
            from func import multiplication
            print(f"\tThe result of this operation is: {multiplication(*tuple_numbers)}")
        if operator == '/':
            from func import division
            print(f"\tThe result of this operation is: {division(*tuple_numbers)}")



