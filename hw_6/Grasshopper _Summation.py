num = int(input("Please input the number of numbers: "))
def summation(num):
    sum_1 = 1
    while(num > 1):
        sum_1 += num
        num -= 1
    return sum_1
print("The sum of integer numbers from 1 will be: sum_1=", summation(num))
