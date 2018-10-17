'''
Vasyl Zakharuk
Python Core 355
Codewars Kata: Will there be enough space?
universal code''' 
cap = int(input("Please input the amount of people the can hold excluding the driver, cap="))
on = int(input("Please input the number of people on the bus, on="))
wait = int(input("Please input the number of people waiting to get to the bus, wait="))
all_pass = on + wait
can_t_fit = all_pass - cap
def enough(cap, on, wait):
    if cap >= all_pass:
        print("He can fit all", wait, "passengers.")
        return 0
    else:
        print("He can't fit only ", can_t_fit, "out of", wait, "waiting.")
        return can_t_fit
print(enough(cap, on, wait))
