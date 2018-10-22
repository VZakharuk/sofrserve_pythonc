"""
Vasyl Zakharuk
Python Core 355
Codewars Kata: Multiples of 3 or 5
"""

number = 10

def solution(number):
    return sum(n for n in range(number) if n % 3 == 0 or n % 5 == 0)

print(solution(number))


#def solution(number):
#    sum = 0
#    for n in range(number):
#        if n % 3 is 0 or n % 5 is 0:
#            sum += n
#    return sum
#print(solution(number))
