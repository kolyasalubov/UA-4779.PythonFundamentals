def count_sheeps(sheep):
    count = 0
    for s in sheep:
        if s == True:
            count += 1
        else:
            continue
    return count
