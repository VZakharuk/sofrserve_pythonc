"""
Vasyl Zakharuk
Python Core Lv-355
Codewars Kata: Reverse List Order
"""

l = []
k = int(input("Pease enter the count of the elements of list: "))
for i in range(k):
    n = int(input("Please enter the element: "))
    l.append(n)
print(l)


def reverse_list(l):
    return list(reversed(l))
print(reverse_list(l))
