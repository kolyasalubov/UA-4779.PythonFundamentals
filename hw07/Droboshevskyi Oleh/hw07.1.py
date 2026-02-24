def count_symbols_in_row(word):
    result = {}
    for item in word:
        result[item] = result.get(item, 0) + 1
    return result

print(count_symbols_in_row("hello"))