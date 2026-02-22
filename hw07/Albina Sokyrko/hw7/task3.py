def number_of_characters(word):
    counts = {}
    for char in word:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    for char, count in counts.items():
        print(f'"{char}": {count}', end=' ')

input_word = input("Enter a word: ")
number_of_characters(input_word)