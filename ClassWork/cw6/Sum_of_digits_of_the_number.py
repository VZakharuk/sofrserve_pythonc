numb = int(input("Please input the number: "))
def sum_numb():
    str_numb = str(numb)
    digits = str_numb.split()
    s_numb = sum(digits)
    print("The sum of digits of the number = {}".format(s_numb))
sum_numb()
