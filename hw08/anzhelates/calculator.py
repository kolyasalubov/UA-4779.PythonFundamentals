import calculator_functions

choice = input("Enter the operation (+,-,*,/): ")

match choice:
    case "+":
        a = int(input("a: "))
        b = int(input("b: "))
        print(calculator_functions.addition(a, b))
    case "-":
        a = int(input("a: "))
        b = int(input("b: "))
        print(calculator_functions.subtraction(a, b))
    case "*":
        a = int(input("a: "))
        b = int(input("b: "))
        print(calculator_functions.multiplication(a, b))
    case "/":
        a = int(input("a: "))
        b = int(input("b: "))
        if (b != 0):
            print(calculator_functions.division(a, b))
        else:
            print("Cannot divide by 0")
    case _:
        "Invalid input"