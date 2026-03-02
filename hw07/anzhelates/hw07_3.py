def calc_num_of_chars(txt):
    """
    Returns the number of characters included in given string
    """
    calc_chars = {}
    for char in txt:
        if char in calc_chars:
            calc_chars[char] += 1
        else:
            calc_chars[char] = 1
    return calc_chars

text = input("Enter text: ")
print(calc_num_of_chars(text))

# # or:
# def calc_num_of_chars(txt):
#     calc_chars = {char: text.count(char) for char in text}
#     return calc_chars