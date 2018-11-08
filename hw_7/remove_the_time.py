"""
Vasyl Zakharuk
Python Core 355
Codewars Kata. Remove the time.
"""


long_date = input("Please input the date: ")
def shorten_to_date(long_date):
    short_date = ' '.join(long_date.split(',')[0:1])
    return short_date
print(shorten_to_date(long_date))
#print(shorten_to_date("Sunday April 1, 10am"))
