"""
Vasyl Zakharuk
Python Core 355
Codewars Kata: Double char
"""

s = input("Please input the data: ")
def double_char(s):
    return ''.join(list(map(lambda x: x*2, s)))
print(double_char(s))
