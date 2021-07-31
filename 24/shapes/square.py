from .shape import Shape
import turtle


class Square(Shape):
    def __init__(self, border, fill, heading, length, coordinates=[]):
        super().__init__(border, fill, heading, coordinates)
        self.length = length

    def draw(self):
        super().draw()
        turtle.pendown()
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(self.length)
            turtle.left(90)
        turtle.end_fill()

    def __str__(self):
        return f"Shape - Square, length = {self.length}, Position - {turtle.pos()}," \
               f" Heading - {turtle.heading()}, Border color and filling - {turtle.color()}"
