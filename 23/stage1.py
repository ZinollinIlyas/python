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

        if self.field_list[x][y] == '':
            return True
        else:
            return False

    def set_cell(self, x, y, symbol):
        if symbol == 'o':
            symbol = 'o'
        elif symbol == 'x':
            symbol = 'x'
        else:
            raise ValueError("Symbol must be either x or o")

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

field = Field(7)
field.set_cell(0,1,'x')
field.set_cell(0,2,'o')
print(field)
