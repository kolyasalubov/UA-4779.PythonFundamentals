#1. Jenny has written a function that returns a greeting for a user.
#  However, she's in love with Johnny, and would like to greet him slightly different.
#  She added a special case to her function, but she made a mistake.
#Can you help her?


def greet(name):
    if name == "Jhonny":
        return "Hello, my lovely Jhonny"
    else:
        return f"Hello, {name}!"
    

   #2. Given two ordered pairs calculate the distance between them.
   #Round to two decimal places. This should be easy to do in 0(1) timing. 


def distance(x1, y1, x2, y2):
    dist = ((x2 - x1)**2 + (y2-y1)**2) ** 0.5
    return round(dist, 2)


#3. Write a function taking in a string like
# WOW this is REALLY          amazing and returning Wow this is really amazing.
# String should be capitalized and properly spaced.


def format_string(i):
    words = i.split()
    low = " ".join(word.lower() for word in words)
    return low.capitalize()


#4. We need a function that can transform a number (integer) into a string.
#What ways of achieving this do you know?


def number_to_string(num):
    return str(num)


#5. You need to write a function that reverses the words in a given string. Words are always separated by a single space.
# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.


def reverse_words(i):
    words = i.split()
    reverse_words = word[::-1]
    return " ".join(reverse_words)


#6. In this kata you will create a function that takes in a list and returns a list with the reverse order.


def reverse_list(lst):
    return lst[::-1]


#7. If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
#Additionally, if the number is negative, return 0.
#Note: If a number is a multiple of both 3 and 5, only count it once.


def solution(number):
    if number < 0:
        return 0
    
    total = 0

    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i

    return total


#8. You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
# Considering these factors, write a function that tells you if it is possible to get to the pump or not.
# Function should return true if it is possible and false if not.


def can_reach_pump(distance, fuel, miles_per_gallon):
    max_distance = fuel * miles_per_gallon

    return max_distance >= distance


#9. Create a function which answers the question "Are you playing banjo?".
#If your name starts with the letter "R" or lower case "r", you are playing banjo!
#The function takes a name as its only argument, and returns one of the following strings:


def are_you_playing_banjo(name):
    if name[0].lower == "r":
        return f"{name} palys banjo!"
    else:
        return f"{name} does not play banjo!"
    

#10. Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.


def bool_to_word(boolean):
    if boolean == True:
        return 'Yes'
    else:
        return 'No'

print(bool_to_word(True))
print(bool_to_word(False))


#11. Consider an array/list of sheep where some sheep may be missing from their place.
#We need a function that counts the number of sheep present in the array (true means present).


def count_sheeep(sheep):
    count = 0
    for s in sheep:
        if s:
            count += 1
    return count


#12. Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right tails. To help her, you must correct the broken function to make sure that the second argument (tail), is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
#If the tail is right return true, else return false.
#The arguments will always be non empty strings, and normal letters.

def correct_tail(body, tail):
     sub = body[len(body) - len(tail):]
    
     if sub == tail:
        return True
     else:
        return False




