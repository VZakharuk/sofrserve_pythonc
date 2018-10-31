"""
Vasyl Zakharuk
Python Core 355
Codewars Kata: Grasshopper Summation
"""
num = int(input("Please input the number of numbers: "))
def summation(num):
    sum_1 = 1
    while(num > 1):
        sum_1 += num
        num -= 1
    print("The sum of integer numbers from 1 will be ={}".format(sum_1))
summation(num)
