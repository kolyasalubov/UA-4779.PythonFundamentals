import calc_func

choice = int(input("""Type in digit to choose an operation to perform:\n1 - Addition;\n2 - Subtraction;\n3 - Multiplication;\n4 - Division.\n"""))
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

match choice:
    case 1: 
        print(f"{a} + {b} = {calc_func.addition(a,b)}")
    case 2: 
        print(f"{a} - {b} = {calc_func.subtraction(a,b)}")
    case 3: 
        print(f"{a} * {b} = {calc_func.multiplication(a,b)}")
    case 4:
        print(f"{a} / {b} = {calc_func.division(a,b)}" if b != 0 else "Don't try to divide by zero")
    case _:
        print ("Invalid choice")
