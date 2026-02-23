# # #Jenny's secret message
# # def greet(name):
# #     if name == "Johnny":
# #         return "Hello, my love!"
# #     return "Hello, {name}!".format(name=name)


# #Simple: Find The Distance Between Two Points
# import math

# def distance(x1, y1, x2, y2):
#     return round(math.dist((x1, y1), (x2, y2)), 2)


#  #No yelling!
# def filter_words(text):
#     cleaned = " ".join(text.split())
#     return cleaned.capitalize()


#Convert a Number to a String!
# def number_to_string(num):
#     return str(num)


#Reversing Words in a String
# def reverse(st):
#     return " ".join(st.split()[::-1])   

#Reverse List Order
# def reverse_list(l):
#     'return a list with the reverse order of l'
#     return l[::-1]


# Multiples of 3 or 5
# def solution(number):
#     if number < 0:
#         return 0
#     total = 0
#     for i in range(number):
#         if i % 3 == 0 or i % 5 == 0:
#             total += i
#     return total


# Will you make it?
# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     return distance_to_pump <= mpg * fuel_left



# Are You Playing Banjo?
# def are_you_playing_banjo(name):
#     return name + " plays banjo" if name[0].lower() == "r" else name + " does not play banjo"


# Convert boolean values to strings 'Yes' or 'No'.
# def bool_to_word(boolean):
#     return "Yes" if boolean else "No"



# Counting sheep...
# def count_sheeps(sheep):
#     return sheep.count(True)



# Is this my tail?
# def correct_tail(body, tail):
#     return body[-1] == tail