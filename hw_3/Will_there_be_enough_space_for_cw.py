'''
Vasyl Zakharuk
Python Core 355
Codewars Kata: Will there be enough space?
''' 
def enough(cap, on, wait):
    if cap >= on+wait:
        print("He can fit all", wait, "passengers.")
        return 0
    else:
        print("He can't fit only ", on+wait-cap, "out of", wait, "waiting.")
        return on+wait-cap
print(enough(10, 5, 5))
