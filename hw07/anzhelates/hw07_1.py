def largest_number(n1, n2):
    """
    A function that returns the largest number of two numbers
    """
    if n1 > n2:
        return n1
    else:
        return n2

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

print("The largest number is: ", largest_number(number1, number2))

# # or:
# def largest_number(n1, n2):
#     return max(n1, n2)