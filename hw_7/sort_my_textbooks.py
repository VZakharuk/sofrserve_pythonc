"""
Vasyl Zakharuk
Python Core 355
Codewars Kata. Sort my textbooks
"""

textbooks = input("Entry the list of books: ")

def sorter(textbooks):
    return(sorted(textbooks, key=lambda x: x[0].upper()))

print(sorter([textbooks])) # parametr textbooks must to have [] like a list!!!

