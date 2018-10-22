"""
Vasyl Zakharuk
Python Core 355
Class work 3: maximum-minimum
"""


namber_1=int(input("Введіть перше число number_1="))
namber_2=int(input("Ведіть друге число namber_2="))
if namber_1 <= namber_2:
    minimum, maximum = namber_1, namber_2
else:
    minimum, maximum = namber_2, namber_1

string_min_max = "The namber namber_1={0} is minimal namber, the number number_2={1} is maximum number" .format(minimum, maximum)
print(string_min_max)
