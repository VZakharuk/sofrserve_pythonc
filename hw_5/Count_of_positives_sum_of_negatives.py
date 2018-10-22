"""
Vasyl Zakharuk
Python Core 355
Codewars Kata: Count of positives / sum of negatives
"""


arr = []
k = int(input("Pease enter the count of the elements of segence: "))
for i in range(k):
    n = int(input("Please enter the element: "))
    arr.append(n)
print(arr)


def count_positives_sum_negatives(arr):
    count_pos = [x for x in arr if x > 0]
    sum_neg = [x for x in arr if x < 0]
    if arr != []:
        result_arr = [len(count_pos), sum(sum_neg)]
        return result_arr
    else:
        return arr
print(count_positives_sum_negatives(arr))

