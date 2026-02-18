def count_chars(s: str) -> dict:
    """
    Calculates the number of characters in a given string.
    """

    counts = {}
    for ch in s:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts

string = input("Enter a string: ")
print(count_chars(string))