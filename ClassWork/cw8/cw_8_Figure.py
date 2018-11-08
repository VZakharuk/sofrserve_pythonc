"""
Vasyl Zakharuk
Python Core 355
Class work 8. Rectangle's color in class figure'
"""


class Figure:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def info(self):
        print("Figure")
        print("Color: " + self.color)

class Rectangle(Figure):
    def __init__(self, color, width=100, height=100):
        super().__init__(color)
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

    def info(self):
        print("Rectangle")
        print("Color: " + self.color)
        print("Width: " + str(self.width))
        print("Height: " + str(self.height))
        print("Square: " + str(self.square()))

fig1 = Figure("green")
fig1.info()
fig2 = Rectangle("red", 89, 65)
fig2.info()



