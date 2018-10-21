"""
Vasyl Zakharuk
Python Core 355
Codewars Kata: Will you make it?
"""


def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left >= distance_to_pump / mpg:
        return True
    else:
        return False
print(zero_fuel(50,25,2))
