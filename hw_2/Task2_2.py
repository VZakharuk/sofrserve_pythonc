"""
Vasyl Zakharuk
Python Core 355
hw_2 Task2_2: four-digit number: multiplying, reversing, sorting
"""


fd=input('Enter a four-digit number: ')
fd_tuple=tuple(str(fd))
fd_product = eval('*'.join(fd))
fd_list = list(fd_tuple)
fd_list.reverse()
fd_reverse = int(''.join(fd_list))
fd_sort = int(''.join(sorted(str(fd))))


print("The product of the digits of the number, is: ", fd_product)


print('Recording numbers in reverse: ', fd_reverse)


print('Sort digits from less to bigger: ', fd_sort)
