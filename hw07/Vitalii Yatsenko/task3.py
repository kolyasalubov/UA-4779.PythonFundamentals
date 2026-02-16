def number_of_char(str):
    res = {s: str.count(s) for s in str}
    return res


print(number_of_char('hello'))