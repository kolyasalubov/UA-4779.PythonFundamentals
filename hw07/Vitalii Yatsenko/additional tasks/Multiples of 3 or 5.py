def solution(number):
    nums = [n for n in range(1, number)]
    nums2 = []
    for n in nums:
        if n % 3 == 0:
            nums2.append(n)
        elif n % 5 == 0:
            nums2.append(n)
        elif n % 3 == 0 and n % 5 == 0:
            continue
        else:
            continue
    print(nums2)  
    return(sum(nums2))
 


