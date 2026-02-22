def symbol_calc (phrase: str) -> dict:
    """
    Function counts the number of occurrences of each character in the input string 
    """
    result = {}
    for symb in phrase:
        if symb in result:
            result[symb] += 1
        else:
            result[symb] = 1
    return result

