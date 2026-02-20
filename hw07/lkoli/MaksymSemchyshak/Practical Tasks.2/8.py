# VIII. Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    a = mpg * fuel_left

    if a >= distance_to_pump:
        return True
    else:
        return False
    
print(zero_fuel(50, 25, 2))
