def my_numbers(num1, num2):
   return max(num1, num2)

result = my_numbers(45,34)   
print(result) 

def my_numbers(num1, num2):
    if num1 > num2:
        return num1
    else:
       return num2
result = my_numbers(33, 77)  
print(result)      

def area_rectangle(a, b):
   total = a * b
   return total
result = area_rectangle(3, 5)
print(result)

def area_triangle(a, b, c):
    total = a*b/c
    return total
result = area_triangle(6, 4, 2)
print(round(result))

import math
area_circle = lambda r: math.pi * (r**2)
print (round(area_circle(3)))

