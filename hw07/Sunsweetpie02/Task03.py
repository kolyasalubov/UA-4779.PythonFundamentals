###############################################################

from collections import Counter

def count_characters(s):
    return dict(Counter(s))

word = input("Enter the word: ")

print("Character counting:", count_characters(word))

###############################################################