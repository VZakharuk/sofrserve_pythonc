
nums = []
k = int(input("Pease enter the count of the elements of segence: "))
for i in range(k):
    n = int(input("Please enter the element: "))
    nums.append(n)
print(nums)
max = nums[0]
min = nums[0]
for i in range(k):
    if nums[i] > max:
        max = nums[i]
    if nums[i] < min:
        min = nums[i]
#print("Maximum number = %d. Minimum number = %d." %(max, min))
print("Maximum number = {}. Minimum number = {}.".format(max, min))
