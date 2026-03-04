# Jenny's secret message 
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)
    
# Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    return round(((x2-x1)**2+(y2-y1)**2)**0.5, 2)
# No yelling!
def filter_words(st):
    st = " ".join(st.split())
    return st.lower().capitalize()
# Convert a Number to a String
def number_to_string(num):
    return str(num)
# Reversing Words in a String
def reverse(st):
    st_list = st.split()
    st = " ".join(st_list[::-1])
    return st 
# Reverse List Order
def reverse_list(l):
    return l[::-1]
    # l.reverse()
    # return l
# Multiples of 3 or 5
def solution(number):
    sum = 0
    if number < 0:
        return 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum+i
    return sum
# Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump <= mpg * fuel_left:
        return True
    else:
        return False
# Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0] == "r" or name[0] == "R":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
# Convert boolean values to strings 'Yes' or 'No'
def bool_to_word(boolean):
    return "Yes" if boolean else "No"
# Counting sheep
def count_sheeps(sheep):
    count = 0
    for item in sheep:
        if item:
            count +=1
    return count
# Is this my tail?
def correct_tail(body, tail):
    sub = body[len(body)-len(tail):]
    if sub == tail:
        return True
    else:
        return False