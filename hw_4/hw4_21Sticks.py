"""
Vasyl Zakharuk
Python Core 355
Codewars Kata: 21 Stics
"""


#import random
#sticks = 21
def makeMove(sticks):
    if sticks == 1:
        return 1
    elif sticks == 2:
        return 2
    elif sticks == 3:
        return 3
    else:
        return sticks % 4 if sticks % 4 !=0 else 1

