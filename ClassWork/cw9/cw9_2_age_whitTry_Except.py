"""
Vasyl Zakharuk
Python Core 355
Class work 9. Age with 'try: except:'
"""


def enterage(age):
    if age <= 0:
        raise ValueError("Age can't be negative or even zero!")
    if age%2 == 0:
        print("age is even")
    else:
        print("age is odt")
try:
    num = int(input("Enter your age: "))
    enterage(num)
    
except ValueError:
    print("Age can't be negative or even zero!")
except Exception:
    print("something is wrong")
