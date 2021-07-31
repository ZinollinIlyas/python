from random import randint
import sys


class Field:
    def __init__(self, size=3):
        self.size = size
        self.field_list = []
        self.cell_quantity = size ** 2
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
            self.cell_quantity -= 1

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
        x = input("Enter x coordinate\n")
        y = input("enter y coordinate\n")
        if x == "exit" or y == "exit":
            sys.exit("Goodbye")
        else:
            self.field.set_cell(int(x), int(y), self.symbol)


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

    def check_horizontal(self, line_number, player):
        x = 0
        o = 0
        if self.field.size <= 5:
            for i in range(self.field.size):
                if self.field.field_list[line_number][i] == 'x':
                    x += 1
                elif self.field.field_list[line_number][i] == 'o':
                    o += 1
            if x == self.field.size and player.symbol == 'x':
                return True
            elif o == self.field.size and player.symbol == 'o':
                return True
            else:
                return False
        else:
            for i in range(self.field.size):
                if self.field.field_list[line_number][i] == 'x':
                    x += 1
                elif self.field.field_list[line_number][i] == 'o':
                    o += 1
            if x == 5 and player.symbol == 'x':
                return True
            elif o == 5 and player.symbol == 'o':
                return True
            else:
                return False

    def check_vertical(self, line_number, player):
        x = 0
        o = 0
        if self.field.size <= 5:
            for i in range(self.field.size):
                if self.field.field_list[i][line_number] == 'x':
                    x += 1
                elif self.field.field_list[i][line_number] == 'o':
                    o += 1
            if x == self.field.size and player.symbol == 'x':
                return True
            elif o == self.field.size and player.symbol == 'o':
                return True
            else:
                return False
        else:
            for i in range(self.field.size):
                if self.field.field_list[i][line_number] == 'x':
                    x += 1
                elif self.field.field_list[i][line_number] == 'o':
                    o += 1
            if x == 5 and player.symbol == 'x':
                return True
            elif o == 5 and player.symbol == 'o':
                return True
            else:
                return False

    def check_diagonal(self, player):
        x = 0
        o = 0
        if self.field.size <= 5:
            for i in range(self.field.size):
                if self.field.field_list[i][i] == 'x':
                    x += 1
                elif self.field.field_list[i][i] == 'o':
                    o += 1
            if x == self.field.size and player.symbol == 'x':
                return True
            elif o == self.field.size and player.symbol == 'o':
                return True
            else:
                return False
        else:
            for i in range(self.field.size):
                if self.field.field_list[i][i] == 'x':
                    x += 1
                elif self.field.field_list[i][i] == 'o':
                    o += 1
            if x == 5 and player.symbol == 'x':
                return True
            elif o == 5 and player.symbol == 'o':
                return True
            else:
                return False

    def check_reverse_diagonal(self, player):
        x = 0
        o = 0
        if self.field.size <= 5:
            for i in range(self.field.size):
                if self.field.field_list[i][abs(i - (self.field.size - 1))] == 'x':
                    x += 1
                elif self.field.field_list[i][abs(i - (self.field.size - 1))] == 'o':
                    o += 1
            if x == self.field.size and player.symbol == 'x':
                return True
            elif o == self.field.size and player.symbol == 'o':
                return True
            else:
                return False
        else:
            for i in range(self.field.size):
                if self.field.field_list[i][abs(i - (self.field.size - 1))] == 'x':
                    x += 1
                elif self.field.field_list[i][abs(i - (self.field.size - 1))] == 'o':
                    o += 1
            if x == 5 and player.symbol == 'x':
                return True
            elif o == 5 and player.symbol == 'o':
                return True
            else:
                return False

    def check(self, player):
        for i in range(self.field.size):
            if self.check_horizontal(i, player):
                return True
            elif self.check_vertical(i, player):
                return True
            elif self.check_diagonal(player):
                return True
            elif self.check_reverse_diagonal(player):
                return True
        return False


class Game:
    def __init__(self):
        self.field = None
        self.player1 = None
        self.player2 = None
        self.checker = None

    def choose_field_size(self):
        print("Choose field size")
        field_size = input()
        if field_size == "exit":
            sys.exit("Goodbye")
        elif int(field_size) < 3 or int(field_size) > 10:
            print("Field size must be from 3 to 10")
            self.run()

        elif 3 <= int(field_size) <= 10:
            self.field = Field(size=int(field_size))
            self.checker = Checker(self.field)
        else:
            print("Wrong input")
            self.run()

    def choose_mode(self):
        mode = input("Enter the game mode:\n1 - Player vs Bot\n2- Player vs Player\n")
        if mode == '1':
            self.player1 = Player(field=self.field, symbol='x')
            self.player2 = Bot(field=self.field, symbol='o')
        elif mode == '2':
            self.player1 = Player(field=self.field, symbol='x')
            self.player2 = Player(field=self.field, symbol='o')
        elif mode == 'exit':
            sys.exit("Goodbye")
        else:
            print("Wrong input")

    def choose_first_move(self):
        number = randint(1, 2)
        return number

    def run(self):
        self.choose_field_size()
        self.choose_mode()
        if self.choose_first_move() == 1:
            while True:
                print("Player1 moves first")
                print(self.field)
                self.player1.move()
                print(self.field)
                self.player2.move()
                print(self.field)
                if self.checker.check(player=self.player1):
                    print("Player1 wins")
                    print(self.field)
                    print("Want to play again?")
                    choice = input()
                    if choice == 'yes' or choice == 'Yes':
                        self.run()
                    else:
                        sys.exit("Goodbye")

                elif self.field.cell_quantity == 0:
                    print("No cells left. Game over")
                    print("Want to play again?")
                    choice = input()
                    if choice == 'yes' or choice == 'Yes':
                        self.run()
                    else:
                        sys.exit("Goodbye")
                else:
                    if self.checker.check(player=self.player2):
                        print("Player2 wins")
                        print(self.field)
                        print("Want to play again?")
                        choice = input()
                        if choice == 'yes' or choice == 'Yes':
                            self.run()
                        else:
                            sys.exit("Goodbye")
                    else:
                        print(self.field)

        else:
            while True:
                print('Player2 moves first')
                print(self.field)
                self.player2.move()
                print(self.field)
                self.player1.move()
                print(self.field)
                if self.checker.check(player=self.player2):
                    print("Player2 wins")
                    print(self.field)
                    print("Want to play again?")
                    choice = input()
                    if choice == 'yes' or choice == 'Yes':
                        self.run()
                    else:
                        sys.exit("Goodbye")
                else:
                    if self.checker.check(player=self.player1):
                        print("Player1 wins")
                        print(self.field)
                        print("Want to play again?")
                        choice = input()
                        if choice == 'yes' or choice == 'Yes':
                            self.run()
                        else:
                            sys.exit("Goodbye")
                    elif self.field.cell_quantity == 0:
                        print("No cells left")
                        print("Want to play again?")
                        choice = input()
                        if choice == 'yes' or choice == 'Yes':
                            self.run()
                        else:
                            sys.exit("Goodbye")
                    else:
                        print(self.field)


game = Game()
game.run()
