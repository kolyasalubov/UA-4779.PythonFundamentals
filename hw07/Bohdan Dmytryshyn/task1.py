def max_two(a, b):
    """
    The function returns the larger of the two numbers
    """
    if a > b:
        return a
    else:
        return b


first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
print(max_two(first, second))
