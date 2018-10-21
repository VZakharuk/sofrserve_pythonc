"""
Vasyl Zakharuk
Python Core 355
Class work 4. Check Odt with 'for ... break'
"""


list_number=[2,4,6,8,9,10]
contain_odd=False
for item in list_number:
    if not item % 2 == 0:
        contain_odd=True
        break
if contain_odd:
    print("There are odd number in the list")
else:
    print("There are only even number in the list")
