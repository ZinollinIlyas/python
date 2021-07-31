from .shape import Shape
import turtle


class Rectangle(Shape):
    def __init__(self, border, fill, heading, length, width, coordinates=[]):
        super().__init__(border, fill, heading, coordinates)
        self.length = length
        self.width = width

    def draw(self):
        super().draw()
        turtle.pendown()
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(self.length)
            turtle.left(90)
            turtle.forward(self.width)
            turtle.left(90)
        turtle.end_fill()

    def __str__(self):
        return f"Shape - Rectangle, length = {self.length}, width = {self.width}, Position - {turtle.pos()}," \
               f" Heading - {turtle.heading()}, Border color and filling - {turtle.color()}"
