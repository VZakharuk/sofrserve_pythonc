'''
Vasyl Zakharuk
Python Core 355
Class work 3'''
# Factorial
def fact(n):
    if n == 0:
        return 1
    return fact(n - 1) * n
number=int(input("Please input the number n="))
print("The factorial of the number n={0} is the number n!={1}"\
      .format(str(number),str(fact(number))))
