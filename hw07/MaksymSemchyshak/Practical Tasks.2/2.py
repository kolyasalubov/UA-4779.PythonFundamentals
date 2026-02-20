# II. Find The Distance Between Two Points

def distance(x1, y1, x2, y2):
    a = (x1 - x2)**2 + (y2 -y1)**2
    d = a ** 0.5

    return round(d, 2)

print(distance(1, 2, 3, 4))