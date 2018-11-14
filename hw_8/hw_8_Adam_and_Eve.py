"""
Vasyl Zakharuk
Python Core 355
Codewars Kata. Adam And Eve.
"""


def God():
    return [Man(), Woman()]  # on 'Code wars'-site must to write: Man('Adam'), Woman('Eve')


class Human:
    def __init__(self, name):
        self.name = name


class Man(Human):
    def __init__(self, name):
         super().__init__(name)


class Woman(Human):
    def __init__(self, name):
        super().__init__(name)


men_humen = Human('Adam')
woman_human = Human('Eve')
print(men_humen.name)
print(woman_human.name)


#  This code is for 'codewars'
# def God():
#     return [Man('Adam'), Woman('Eve')]
#
#
# class Human:
#     def __init__(self, name):
#         self.name = name
#
#
# class Man(Human):
#     def __init__(self, name):
#          super().__init__(name)
#
#
# class Woman(Human):
#     def __init__(self, name):
#         super().__init__(name)
