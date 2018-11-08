"""
Vasyl Zakharuk
Python Core 355
Class work 6. Split output: Sum of digits of the number
"""

numb = int(input("Please input the number: "))
print(sum(map(int, str(numb)[:numb])))


numb = int(input("Please input the number: "))
print(sum(map(int, str(numb)[:len(str(numb))])))


# def sum_numb():       # not working


#    print("The sum of digits of the number = {}".format(numb))
# sum_numb()
