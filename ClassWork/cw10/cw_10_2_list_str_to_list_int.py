"""
Vasyl Zakharuk
Python Core 355
Class work 10. List string to list integer with: 1) .append; 2) map.
"""


# Всі ці числа в списку мають стрічковий тип даних,
#  наприклад  [‘1’,’2’,’3’,’4’,’5’,’7’], перетворити цей список  в список всі числа якого мають тип даних integer:
# 1)  використовуючи метод  append
# 2)  використовуючи метод  map

# 1)  використовуючи метод  append:

list_str = ['1', '2', '3', '4', '5', '7']
list_int = []
for n in list_str:
    list_int.append(int(n))
#    print(list_int)  # If print() in this place - printing to column of list
print(list_int)  # don't need function list(). If print() in this place - printing to one list


# 2)  використовуючи метод  map:

# list_str = ['1', '2', '3', '4', '5', '7']
# list_int = map(int, list_str)
# print(list(list_int))  # need function list()
