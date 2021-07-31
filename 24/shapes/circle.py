from .shape import Shape
import turtle


class Circle(Shape):
    def __init__(self, border, fill, heading, radius, coordinates=[]):
        super().__init__(border, fill, heading, coordinates)
        self.radius = radius

    def draw(self):
        super().draw()
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.radius)
        turtle.end_fill()

    def __str__(self):
        return f"Shape - Circle, Radius = {self.radius}, Position - {turtle.pos()}," \
               f" Heading - {turtle.heading()}, Border color and filling - {turtle.color()}"



