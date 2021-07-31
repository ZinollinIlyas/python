from shapes import *


class Drawing:
    def __init__(self, shapes=[]):
        self.shapes = shapes

    def draw(self):
        for shape in self.shapes:
            turtle.speed(10)
            print(shape)
            shape.draw()


house = Square('black', 'orange', 90, 300, [100, -250])
roof = Triangle('black', 'brown', 120, 300, [100, 50])
door = Rectangle('black', '#591209', 90, 250, 100, [-50, -220])
roof_window = Circle('black', '#15c6e6', 90, 50, [0, 150])
doorhandle = Circle('black', '#e6a715', 90, 10, [-120, -100])
window = Square('black', '#15c6e6', 90, 100, [70, -100])
window_beam1 = Rectangle('black', '#591209', 90, 100, 10, [25, -100])
window_beam2 = Rectangle('black', '#591209', 90, 10, 100, [70, -60])
if __name__ == '__main__':
    draw = Drawing([house, roof, door, roof_window, doorhandle, window, window_beam1, window_beam2])
    draw.draw()
    turtle.done()
