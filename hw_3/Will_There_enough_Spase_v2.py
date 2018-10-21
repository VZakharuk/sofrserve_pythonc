"""
Vasyl Zakharuk
Python Core 355
Codewars Kata: Will there be enough space?
"""
# universal code


def enough(cap, on, wait):
    all_pass = on + wait
    can_t_fit = all_pass - cap
    return "He can fit all", (wait), "passengers." if cap >= all_pass else "He can't fit only ", (can_t_fit), "out of", (wait), "waiting."
cap = int(input("Please input the amount of people the can hold excluding the driver, cap="))
on = int(input("Please input the number of people on the bus, on="))
wait = int(input("Please input the number of people waiting to get to the bus, wait="))

print(enough(cap, on, wait))

