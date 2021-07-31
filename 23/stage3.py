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


field = Field()
bot = Bot('x', field)
bot.move()
print(bot.field)
