"""
Vasyl Zakharuk
Python Core 355
Class work 10. color.
"""


color_list = ['red', 'yellow', 'blue', 'green', 'red', 'green', 'red', 'brown', 'red', 'yellow']
sort_red = list(filter(lambda x: x == 'red', color_list))
print(len(sort_red), sort_red)