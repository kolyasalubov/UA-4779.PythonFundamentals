def count_letters(my_str):
    """
    The function returns dictionary with unique symbols
    """
    my_dict = {}
    for letter in my_str:
        if letter in my_dict:
            my_dict[letter] = my_dict[letter] + 1
        else:
            my_dict[letter] = 1
    return my_dict


string = input("Enter string: ")
print(count_letters(string))
