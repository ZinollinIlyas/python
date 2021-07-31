from .shape import Shape
import turtle


class Triangle(Shape):
    def __init__(self, border, fill, heading, length, coordinates=[]):
        super().__init__(border, fill, heading, coordinates)
        self.length = length

    def draw(self):
        super().draw()
        turtle.pendown()
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(self.length)
            turtle.left(120)
        turtle.end_fill()


    def __str__(self):
        return f"Shape - Triangle, Length = {self.length}, Position - {turtle.pos()}," \
               f" Heading - {turtle.heading()}, Border color and filling - {turtle.color()}"



