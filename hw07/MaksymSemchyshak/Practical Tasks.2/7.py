# VII. Multiples of 3 or 5

def solution(number):
    if number < 0:
        return 0
    
    total_sum = 0

    for i in range(number):
        if i %3 == 0 or i %5 == 0:
            total_sum = total_sum + i
    
    return total_sum

print(solution(10))