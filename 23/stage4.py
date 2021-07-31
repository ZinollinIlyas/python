from random import randint


class Field:
    def __init__(self, size=3):
        self.size = size
        self.field_list = []
        for i in range(size):
            self.field_list.append([''] * size)

    def does_cell_exist(self, x, y):
        if x >= self.size or y >= self.size:
            return False
        else:
            return True

    def is_cell_empty(self, x, y):
        if not self.does_cell_exist(x, y):
            return False
        else:
            if self.field_list[x][y] == '':
                return True
            else:
                return False

    def set_cell(self, x, y, symbol):
        if not self.does_cell_exist(x, y):
            raise ValueError("Cell does not exist")
        elif not self.is_cell_empty(x, y):
            raise ValueError("Cell is already hired")
        else:
            self.field_list[x][y] = symbol

    def __str__(self):
        field = ''
        for i in range(self.size):
            field += f"{i:^5}"
        for i in range(self.size):
            row = f"{i:^2}"
            for j in range(self.size):
                row += f"{self.field_list[i][j]:^4}|"
            field += '\n' + row + '\n' + '-' * (self.size * 5)
        return field


class Player:
    def __init__(self, symbol, field):
        self.symbol = symbol
        self.field = field

    def move(self):
        x = int(input("Enter x coordinate\n"))
        y = int(input("enter y coordinate\n"))
        self.field.set_cell(x, y, self.symbol)


class Bot(Player):
    def move(self):
        x = randint(0, self.field.size)
        y = randint(0, self.field.size)
        if self.field.is_cell_empty(x, y):
            self.field.set_cell(x, y, self.symbol)
            print(f"I went on ({x}, {y}) cell")
        else:
            self.move()


class Checker:
    def __init__(self, field):
        self.field = field

    def check_horizontal(self, line_number):
        x = 0
        o = 0
        for i in range(self.field.size):
            if self.field.field_list[line_number][i] == 'x':
                x += 1
            elif self.field.field_list[line_number][i] == 'o':
                o += 1
        if x == self.field.size:
            return True
        elif o == self.field.size:
            return True
        else:
            return False

    def check_vertical(self, line_number):
        x = 0
        o = 0
        for i in range(self.field.size):
            if self.field.field_list[i][line_number] == 'x':
                x += 1
            elif self.field.field_list[i][line_number] == 'o':
                o += 1
        if x == self.field.size:
            return True
        elif o == self.field.size:
            return True
        else:
            return False

    def check_diagonal(self):
        x = 0
        o = 0
        for i in range(self.field.size):
            if self.field.field_list[i][i] == 'x':
                x += 1
            elif self.field.field_list[i][i] == 'o':
                o += 1
        if x == self.field.size:
            return True
        elif o == self.field.size:
            return True
        else:
            return False

    def check_reverse_diagonal(self):
        x = 0
        o = 0
        for i in range(self.field.size):
            if self.field.field_list[i][abs(i - (self.field.size - 1))] == 'x':
                x += 1
            elif self.field.field_list[i][abs(i - (self.field.size - 1))] == 'o':
                o += 1
        if x == self.field.size:
            return True
        elif o == self.field.size:
            return True
        else:
            return False

    def check(self):
        for i in range(self.field.size):
            if self.check_horizontal(i):
                print("win")
                return True
            elif self.check_vertical(i):
                return True
            elif self.check_diagonal():
                return True
            elif self.check_reverse_diagonal():
                print("win")
                return True
        print('f')
        return False


field = Field(5)
field.set_cell(0, 4, 'x')
field.set_cell(1, 3, 'x')
field.set_cell(2, 2, 'x')
field.set_cell(3, 1, 'x')
field.set_cell(4, 0, 'x')

print(field)
checker = Checker(field)
checker.check()
