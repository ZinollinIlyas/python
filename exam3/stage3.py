from random import randint, shuffle


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank:^2}{self.suit:^2}'


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
        shuffle(self.deck)

    def display(self):
        for card in self.deck:
            print(card)


class Hand:
    def __init__(self, deck):
        self.hand = []
        self.deck = deck

    def take_card(self, index):
        self.hand.append(self.deck.give_card(index))

    def change_card(self, index):
        self.hand.remove(index - 1)
        self.take_card(index)

    def __str__(self):
        hand = ''
        for i in range(len(self.hand)):
            hand += f"| {i + 1:^2} {'|':>2} "
        hand += '\n'
        for card in self.hand:
            hand += f"| {card}{'|'} "
        return hand


deck = Deck()
hand = Hand(deck)
hand.take_card()
hand.take_card()
hand.take_card()
hand.take_card()
hand.take_card()
print(hand)
