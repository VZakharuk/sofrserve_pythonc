"""
Vasyl Zakharuk
Python Core 355
Codewars Kata: Are You playing Banjo?
"""


def areYouPlayingBanjo(name):
    return ("{0} plays banjo" if name[0].lower() == 'r'\
            else "{0} does not play banjo").format(name)

name = input("Are You playing Banjo ")

print(areYouPlayingBanjo(name))
