def numbers_compare (first : int , second: int ) -> int: 
    """
    Function compares two int numbers and returns the largest one
    Input: two int numbers
    Output: int number
    """
    return first if first >= second else second

# print (numbers_compare(66, 99))