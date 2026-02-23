"""
Docstring for hw07.smaha_serhii.task2_codewars
"""


def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


def distance(x1, y1, x2, y2):
    raw_res = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return round(raw_res, 2)


def filter_words(st):
    words = st.split()
    result = ' '.join(words)
    return result.capitalize()

def number_to_string(num):
    return str(num)

def reverse(st):
    words = st.split()
    return ' '.join(reversed(words))

def reverse_list(items):
    return list(reversed(items))

def solution(number):
    if number < 0:
        return 0
    
    total = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump/mpg <= fuel_left

def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return f"{name} plays banjo"
    return f"{name} does not play banjo"

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

def count_sheeps(sheeps):
    return sheeps.count(True)

def correct_tail(body, tail):
    sub = body[-len(tail):]
    return sub == tail
