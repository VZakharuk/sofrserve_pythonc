"""
Vasyl Zakharuk
Python Core 355
Codewars Kata: Will you make it?
"""


def zero_fuel(distance_to_pump, mpg, fuel_left):
    return ("We got to the pump" if fuel_left >= distance_to_pump / mpg else "A few miles we were pushing the car to the pump(((").format(distance_to_pump, mpg, fuel_left)
distance_to_pump = int(input("Please input distanse to pump: "))
mpg = int(input("Please input miles per gallon: "))
fuel_left = int(input("Please input fuel left: "))

print(zero_fuel(distance_to_pump, mpg, fuel_left))
