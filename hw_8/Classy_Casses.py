"""
Vasyl Zakharuk
Python Core 355
Codewars Kata. Classy Classes.
"""


class Person:
    def __init__(self, name, age):
        self.info = name + 's age is ' + str(age)

names = ["John", "Ann", "Bill", "Jack", "Susanna"]
ages = [25, 44, 17, 49, 33]
for i in range(5):
    name, age = names[i], ages[i]
    person = Person(name, age)
    print(person.info)
