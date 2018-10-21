"""
Vasyl Zakharuk
Python Core 355
Class work 3: GCD and LCM
"""


def gcd(a,b):
    return a if b == 0 else gcd(b, a % b)
def lcm(a,b):
    return a * b / gcd(a, b)
a = int(input("Please input the number a="))
b = int(input("Please input the number b="))
print(gcd(a,b))
print(lcm(a,b))
