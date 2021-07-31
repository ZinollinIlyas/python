class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'-------\n|{self.suit}    |\n|  {self.rank}  |\n|    {self.suit}|\n-------'


card = Card(1, "\u2660")
print(card)
