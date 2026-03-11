##############################################
# I. Jenny's secret message

# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     return "Hello, {name}!".format(name=name)

###############################################
# II. Find The Distance Between Two Points

# def distance(x1, y1, x2, y2):
#      return round(((x2-x1)**2+(y2-y1)**2)**0.5, 2)

###############################################
# III. No yelling!

def filter_words(st):
    st = st.split () 
    return ' '.join (st).capitalize() 

###############################################
# IV. Convert a Number to a String

# def number_to_string(num):
#     return str(num)

###############################################
# V. Reversing Words in a String

# def reverse(st):
#     words = st.split(' ')
#     rev = words[::-1]
#     return ' '.join(rev)

###############################################
# VI. Reverse List Order

# def reverse_list(l):
#     return l [:: -1]

###############################################
# VII. Multiples of 3 or 5

# def solution(number):
#     if number < 0: 
#         return 0
    
#     total = 0 
#     for i in range(number):
#         if i % 3 == 0 or i % 5 == 0:
#             total += i         

#     return total

###############################################
# VIII. Will you make it?

# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     return mpg * fuel_left >= distance_to_pump

###############################################
# IX. Are You Playing Banjo?

# def are_you_playing_banjo(name):
#     if name[0] == 'R' or name[0] == 'r':
#         return name + " plays banjo"
#     else:
#         return name + " does not play banjo"

###############################################
# X. Convert boolean values to strings 'Yes' or 'No’

# def bool_to_word(boolean):
#     if boolean:
#         return "Yes"
#     else:
#         return "No"

###############################################
# XI. Counting sheep

# def count_sheeps(sheep_list):
#     if not sheep_list:
#         return 0 
#     count = 0 
#     for sheep in sheep_list:
#         if sheep is True:
#             count += 1
#     return count

###############################################
# XII. Is this my tail?

# def correct_tail(body, tail):
#     return body[-1] == tail

###############################################