"""
Vasyl Zakharuk
Python Core 355
Codewars Kata. Sort my textbooks
"""

#textbooks = input("Entry the list of books: ")

def sorter(textbooks):
    return sorted(textbooks, key=lambda x: x[0].upper())

#print(sorter([textbooks])) # not working properly. Not sort!!!


#def sorter(textbooks):
#    textbooks.sort(key=str.upper) 
#    return textbooks
print(sorter(['Algebra', 'history', 'Geometry', 'english']))

#print(sorter([textbooks]))
