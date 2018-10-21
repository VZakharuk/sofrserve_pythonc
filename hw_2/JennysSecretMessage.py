"""
Vasyl Zakharuk
Python Core 355
Codewars Kata: Jenny's Secret Message
"""


name=input("Write a name:  ")
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)
print(greet(name))
