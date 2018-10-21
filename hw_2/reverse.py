"""
Vasyl Zakharuk
Python Core Lv-355
Codewars Kata: Reversing Words in a String
"""


st = input("Введіть фразу: ")

def reverse(st):
    line = st.split()
    line.reverse()
    st = ' '.join(line)
    return st

print(reverse(st))

