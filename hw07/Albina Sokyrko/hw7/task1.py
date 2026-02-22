def find_largest(x,y):
    '''Find the largest of two numbers.'''
    if x > y:
        return x
    else:
        return y

print(find_largest.__doc__)

input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))
largest = find_largest(input1, input2)
print("The largest number is:", largest)