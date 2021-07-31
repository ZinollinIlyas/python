class Rectangle:
    def __init__(self, length, width):
        self.length = abs(length)
        self.width = abs(width)

    def get_perimeter(self):
        return (self.length + self.width) * 2

    def get_area(self):
        return self.length * self.width

    def describe(self):
        print(f"Длина - {self.length}, Ширина - {self.width}, Площадь - {self.get_area()}, Периметр -"
              f" {self.get_perimeter()}")


rect = Rectangle(7, 3)

rect.describe()
