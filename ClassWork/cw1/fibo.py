# Fibonacci numbers module fibo.py
#n = int(input("Please input tne namber n="))
#def fib(n):    # write Fibonacci series up to n
#    a, b = 0, 1
#    while b < n:
#        print(b, end=' ')
#        a, b = b, a+b
#print(fib(n))

n = int(input("Please input tne namber n="))
def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
print(fib2(n))
