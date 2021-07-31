class Cat:
    def __init__(self, name, age=None, color="White"):
        self.name = name
        self.age = age
        self.color = color

    def meow(self, something):
        print("Meow", something)

    def purr(self):
        print("Purrr")

    def ask_food(self):
        for i in range(3):
            self.meow("asd")
        self.purr()


murka = Cat("Murka", color="white", age=5)
print(murka.name)
