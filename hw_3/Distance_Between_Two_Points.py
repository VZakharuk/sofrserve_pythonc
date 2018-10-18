'''
Vasyl Zakharuk
Python Core 355
Codewars Kata: Simple: Find The Distance Between Two Points
'''
def distance(x1, y1, x2, y2):
    import math
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)
x1 = int(input("Input x1="))
y1 = int(input("Input y1="))
x2 = int(input("Input x2="))
y2 = int(input("Input y2="))
print(distance(x1, y1, x2, y2))
