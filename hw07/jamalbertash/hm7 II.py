"Задача 1:"
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


"Задача 2:"
import math
def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2-x1)2+(y2-y1)2)
    return round(dist,2)


"Задача 3:"
def filter_words(st):
    pra = st.capitalize()
    la = pra.split()
    gra = " ".join(la)
    return gra


"Задача 4:"
def number_to_string(num):
    return str(num)




"Задача 5:"
def reverse(st):
    g = list(st.split())
    g.reverse()
    res = " ".join(g)
    return res


"Задача 6:"
def reverse_list(l):
    'return a list with the reverse order of l'
    l.reverse()
    return l

"Задача 7:"
def solution(number):
    suma = []
    if number <=0:
        return 0
    else:
        for i in range(number):
            if i == 0:
                continue
            elif (i%3 == 0) and (i%5 == 0):
                suma.append(i)
            elif (i%3 == 0):
                suma.append(i)
            elif (i%5 == 0):
                suma.append(i)
    return sum(suma)


"Задача 8:"
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if mpg*fuel_left>=distance_to_pump else False



"Задача 9:"
def are_you_playing_banjo(name):
    k=name.lower()
    return name+" plays banjo"  if k.startswith("r") else name+" does not play banjo"



"Задача 10:"
def bool_to_word(boolean):
    return 'Yes' if boolean==True else "No"




"Задача 11:"
def count_sheeps(sheep):
    counter = 0
    for i in sheep:
        if i==True:
            counter+=i
    return counter



"Задача 12:"
def correct_tail(body, tail):
        if body[-1] == tail:
            return True
        else:
            return False

