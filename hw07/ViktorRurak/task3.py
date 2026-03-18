def count_characters(sting):
    counter = {}
    for letter in sting:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
    print(counter)

count_characters('gfddfgwerw')