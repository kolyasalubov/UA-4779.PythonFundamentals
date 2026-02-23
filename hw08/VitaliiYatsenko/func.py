def addition(*args):
    return sum(args)

def substraction(*args):
    s = args[0]
    for a in args[1:]:
        res = s - a
        s = res
    return s

def multiplication(*args):
    s = args[0]
    for a in args[1:]:
        res = s * a
        s = res
    return s

def division(*args):
    s = args[0]
    for a in args[1:]:
        res = s / a
        s = res
    return round(s,3)



