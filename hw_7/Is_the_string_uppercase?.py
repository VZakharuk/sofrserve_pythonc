"""
Vasyl Zakharuk
Python Core 355
Codewars Kata: Is the string uppercase
"""

inp = input("Please input the text: ")
def is_uppercase(inp):
    caps = inp.upper()
    if caps == inp:
        return True
    else :
        return False
print(is_uppercase(inp))

