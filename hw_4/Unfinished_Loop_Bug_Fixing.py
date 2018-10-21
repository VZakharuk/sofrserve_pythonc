"""
Vasyl Zakharuk
Python Core 355
Codewars Kata: Unfinished Loop - Bug Fixing #1
"""


n = int(input("Pease enter the count of the elements of sequence: "))
def create_array(n):
    res = []
    i = 1
    while i <= n: 
        res += [i]
        i += 1
    return res
print("{}".format(create_array(n)))
