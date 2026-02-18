def my_numbers(num1, num2):
   return max(num1, num2)

result = my_numbers(45,34)   
print(result) 

#####################################

def my_numbers(num1, num2):
    if num1 > num2:
        return num1
    else:
       return num2
result = my_numbers(33, 77)  
print(result)   

######################################

def area_rectangle(a, b):
   total = a * b
   return total
result = area_rectangle(3, 5)
print(result)

######################################

def area_triangle(a, b, c):
    total = a*b/c
    return total
result = area_triangle(6, 4, 2)
print(round(result))

#########################################

import math
area_circle = lambda r: math.pi * (r**2)
print (round(area_circle(3)))

##############################################

def greet(name):
    if name == "Johnny":
            return "Hello, my love!"
    return "Hello, {0}!".format(name) 

###############################################

def distance(x1, y1, x2, y2):
    return round(((x2 - x1)**2 + (y2 - y1)**2) ** 0.5, 2)

##########################################################

def filter_words(st):
    words = st.capitalize().split()
    return ' '.join(words)

#################################

def number_to_string(num):
    return str(num)

####################################

def reverse(st):
    
    return " ".join(st.split(" ")[::-1])

############################################


def reverse_list(l):
    'return a list with the reverse order of l'
    return l [::-1]

##########################################

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left

################################################

def are_you_playing_banjo(name):
    if name.startswith('R') or name.strartswith('r'):
        return name + ' plays banjo'

    else:
        return name + ' does not play banjo'
    
####################################################

def bool_to_word(boolean):
    if boolean == True:
        return 'Yes'
    else:
        boolean != True
        return 'No'
    
####################################

def count_sheeps(sheep):
    return sum(sheep)

######################################

def correct_tail(body, tail):
     #sub = bady[len(body)-len(tail)]
        if body[-1] == tail:
            return True
        else:
            return False
        
###################################### 

def array_diff(a, b):
    set_b = set(b)
    
    return [item for item in a if item not in set_b] 
    
