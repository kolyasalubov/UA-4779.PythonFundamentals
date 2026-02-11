def returns_number():
    """The function returns the largest 
    of two numbers entered by the user."""

    n1 = int(input(' Enter the first integer: '))
    n2 = int(input(' Enter the second integer: '))

    result = max(n1,n2)
    return f'The largest number you have entered is {result}.'


print(returns_number())