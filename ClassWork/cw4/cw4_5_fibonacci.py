'''
Vasyl Zakharuk
Python Core 355
Class work 4. Fibonacci sequences using generators
'''
max_f = int(input("Plese input last namber of Fibonacci sequences: "))
def fibonacci(max_f):
    a, b = 0, 1
    while a < max_f:
        yield a
        a, b = b, a+b
for n in fibonacci(max_f):
    print(n)
input ("\n\nHaтисни Enter, щоб вийти. ")
