from random import randint


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'-------\n|{self.suit}    |\n|  {self.rank}  |\n|    {self.suit}|\n-------'


class Deck:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["\u2660", "\u2665", "\u2666", "\u2663"]

    def __init__(self):
        self.deck = []
        for rank in self.RANKS:
            for suit in self.SUITS:
                self.deck.append(Card(rank, suit))

    def give_card(self):
        return self.deck.pop()

    def shuffle(self):
        for i in range(len(self.deck)):
            random_number = randint(0, 51)
            self.deck[i] = self.deck[random_number]

    def display(self):
        for card in self.deck:
            print(card)


deck = Deck()
deck.give_card()
deck.display()

