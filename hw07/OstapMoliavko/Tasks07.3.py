#       I. Jenny's secret message

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


#       II. Find The Distance Between Two Points

import math

def distance_between_points(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)


#       III. No yelling

def filter_words(st):
    words = st.split()
    word_str = words[0].capitalize() + " "
    for x in range(1,len(words)):
        if x < len(words) - 1:
            word_str += (words[x]).lower() + " "
        else:
            word_str += (words[x]).lower()
    return(word_str)


#       IV. Convert a Number to a String

def number_to_string(num):
    return str(num)


#       V. Reversing Words in a String

def reverse(st):
    words = st.split(' ')
    rev = words[::-1]
    return ' '.join(rev)


#       VI. Reverse List Order  

def reverse_list(l):
    return l[::-1]


#       VII. Multiples of 3 or 5

def solution(number):
    snum = 0
    for i in range(0, number, 1):
        if i % 3 == 0 or i % 5 == 0:
            snum += i
    return(snum)


#       VIII. Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if mpg * fuel_left >= distance_to_pump else False


#       IX. Are You Playing Banjo?

def are_you_playing_banjo(name):
    if (name[0]).lower() == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


#       X. Convert boolean values to strings 'Yes' or 'No’

def bool_to_word(bool):
    return "Yes" if bool else "No"


#       XI. Counting sheep

def count_sheeps(sheep):
    return sum(x is True for x in sheep)


#       XII. Is this my tail?       

def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    else:
        return False