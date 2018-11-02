"""
Vasyl Zakharuk
Python Core 355
Class work 9. Even & Odd with 'try: except:'
"""


n = input("Input the number: ")
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("\n You entered incorrect data!\n")
        n = input("Input correct number:\n ")

if n %2 == 0:
    print("{0} is the even number.".format(n))
else:
    print("{0} is the odd number.".format(n))
