def show_largest(a, b):
    '''
    This function returns largest number 
    of two, entered by user
    '''
    l = 0
    if a > b:
        l = a
    else:
        l = b
    return(l)

ag = input("Enter first number: ")
bg = input("Enter second number: ")

print("Largest number is", show_largest(ag,bg))

