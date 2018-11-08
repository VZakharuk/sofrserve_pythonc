"""
Vasyl Zakharuk
Python Core 355
Home work 9. Days of week with 'try: except:'
"""


week_days = {1: 'Monday',
             2: 'Tuesday',
             3: 'Wednesday',
             4: 'Thursday',
             5: 'Friday',
             6: 'Saturday',
             7: 'Sunday'}
# This function has not sens if I can't print: The day of week is...
#def day_num(i):
#    if i >= 8 or i <= 0:
#        raise ValueError('You did not enter the right number. The week has seven days')
while True:
    try:
        i = int(input('Enter the day of week: '))
#        day_num(i)
    except ValueError:
        print('You did not enter the number!')
    else:
        print(week_days.get(i, 'You did not enter the right number. The week has seven days')) # .get is need that never return KeyError
#        print("The day of week is {}".format(week_days[i]))
