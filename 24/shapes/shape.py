import turtle


class Shape:
    def __init__(self, border, fill, heading, coordinates=[]):
        self.border = border
        self.fill = fill
        self.coordinates = coordinates
        self.heading = heading

    def draw(self):
        turtle.penup()
        turtle.color(self.border, self.fill)
        turtle.goto(self.coordinates[0], self.coordinates[1])
        turtle.setheading(self.heading)

    def __str__(self):
        return f"Position - {turtle.pos()}, Heading - {turtle.heading()}, Border color and filling - {turtle.color()}"
