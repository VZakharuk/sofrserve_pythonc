"""
Vasyl Zakharuk
Python Core 355
Class work 13. Split output: Square rectangle,
Triangle area and Circle Area,
using pow and pi from math
"""


from math import pow

from math import pi

def figure():
    # 'fig' is parameter of function 'figure'. And user must input and name it himself
    fig = input("1 - rectangle, 2 - triangle, 3 - circle: ")
    if fig == '1':
        rectangle()
    elif fig == '2':
        triangle()
    elif fig == '3':
        circle()
    else:
        print("Please input valid digit from 1 to 3")


def rectangle():
    a = float(input("Please input side a="))
    b = float(input("Please input side b="))
    print("Square rectangle = {}".format(a*b))


def triangle():
    c = float(input("Please input the basis of the triadle c="))
    h = float(input("Please input the triangle height h="))
    print("Triangle area = {}".format(c*h/2))


def circle():
    r = float(input("Please input the radius of the circle r="))
    print("Circle_area = {}".format(pi*pow(r, 2)))


figure()

