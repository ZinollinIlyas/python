class Good:
    def __init__(self, name, price, quantity=1):
        if quantity <= 0:
            print("Error, quantity must be greater than 0")
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_price(self):
        result = self.price * self.quantity
        return result

    def display(self):
        name = '{:.20}'.format(self.name)
        price = '{:.2f}'.format(self.price)
        print(f"{name:<25}{price:.7} * {self.quantity} = {self.calculate_price()}")


class DiscountGood(Good):
    def __init__(self, name, price, quantity=1, discount=0):
        super().__init__(name, price, quantity)
        self.discount = discount

    def calculate_price(self):
        if self.discount <= 0 or self.discount > 99:
            return super().calculate_price()
        else:
            result = super().calculate_price() - (super().calculate_price() * (self.discount / 100))
            return result

    def display(self):
        name = '{:.20}'.format(self.name)
        price = '{:.2f}'.format(self.price)
        if self.discount == 0:
            super().display()
        else:
            print(f"{name:<25}{price:.7} * {self.quantity} = {self.calculate_price()} (-{self.discount}%)")


class Cart:
    def __init__(self, goods_list):
        self.goods = goods_list

    def calculate_total_price(self):
        count = 0
        for good in self.goods:
            count += good.calculate_price()
        return count

    def display(self):
        print(f"{'Name:':<26}{'PPU':<7}{'CNT'}  {'Price'} {'Disc.'}")
        print("="*70)
        for good in self.goods:
            good.display()
        print("="*70)
        print(f"{'Total':<34} = {self.calculate_total_price()}")


good1 = Good("Bread", 17.00, 3)
good1.display()
good2 = DiscountGood('Juice', 80, discount=20)
good2.display()

goods = [
    Good('Bread', 17, 3),
    Good('Water', 19, 2),
    DiscountGood('Juice', 80, 1, 20),
    Good('Toilet Paper', 19, 10)
]

cart = Cart(goods)
cart.display()
