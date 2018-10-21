"""
Vasyl Zakharuk
Python Core 355
Class work 5. even / 2, odd / 3, nymber not / 2 and not / 3
"""


for x in  range(1,11):
    if x % 2 == 0:
        print(x, 'is even multiple of 2')
    elif x % 3 == 0:
        print(x, 'is odd multiple of 3')
    else:
        print(x, 'not divdsible  by 2 and 3')
