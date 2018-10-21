"""
Vasyl Zakharuk
Python Core 355
Codewars Kata: Are You playing Banjo?
"""


def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    areYouPlayingBanjo = "{0}".format(name)

name = input("Are You playing Banjo ")

print(areYouPlayingBanjo(name))
