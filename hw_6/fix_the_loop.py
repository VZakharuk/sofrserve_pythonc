"""
Vasyl Zakharuk
Python Core 355
Codewars Kata: fix the loop
"""


#i = input("Input the animals: ")
def list_animals(animals):
    list_a = ''
    for i in range(len(animals)):
        list_a += str(i + 1) + '. ' + ''.join(animals[i]) + '\n'
    return list_a
    
print(list_animals([ 'dog', 'monkey', 'elephant', 'cat', 'caw']))
#print(list_animals([i]))
