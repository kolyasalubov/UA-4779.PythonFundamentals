def count_chars(word):
    counts = {}

    for char in word:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts

print(count_chars('hello'))