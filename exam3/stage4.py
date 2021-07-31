from random import randint


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
        for i in range(len(self.deck)):
            random_number = randint(0, 51)
            self.deck[i] = self.deck[random_number]

    def display(self):
        for card in self.deck:
            print(card)


class Hand:
    def __init__(self, deck):
        self.hand = []
        self.deck = deck

    def take_card(self):
        self.hand.append(self.deck.give_card())

    def change_card(self, index):
        self.hand.remove(index - 1)
        self.take_card()

    def __str__(self):
        hand = ''
        for i in range(len(self.hand)):
            hand += f"| {i + 1:^2} {'|':>2} "
        hand += '\n'
        for card in self.hand:
            hand += f"| {card}{'|'} "
        return hand


class Checker:
    def __init__(self, player_hand):
        self.player_hand = player_hand

    def check_royal_flush(self):
        rank_count = 0
        hearts = 0
        diamonds = 0
        spades = 0
        clubs = 0
        for i in range(len(self.player_hand.hand)):
            if (self.player_hand.hand[i].rank == '10' or self.player_hand.hand[i].rank == 'J' or self.player_hand.hand[
                i].rank == 'Q'
                or self.player_hand.hand[i].rank == 'K'
                or self.player_hand.hand[i].rank == 'A') and self.player_hand.hand[i].suit == "\u2665":
                rank_count += 1
                hearts += 1
            elif (self.player_hand.hand[i].rank == '10' or self.player_hand.hand[i].rank == 'J' or
                  self.player_hand.hand[i].rank == 'Q'
                  or self.player_hand.hand[i].rank == 'K'
                  or self.player_hand.hand[i].rank == 'A') and self.player_hand.hand[i].suit == "\u2666":
                rank_count += 1
                diamonds += 1
            elif (self.player_hand.hand[i].rank == '10' or self.player_hand.hand[i].rank == 'J' or self.player_hand.hand[
                i].rank == 'Q'
                or self.player_hand.hand[i].rank == 'K'
                or self.player_hand.hand[i].rank == 'A') and self.player_hand.hand[i].suit == "\u2660":
                rank_count += 1
                spades += 1
            elif (self.player_hand.hand[i].rank == '10' or self.player_hand.hand[i].rank == 'J' or self.player_hand.hand[
                i].rank == 'Q'
                or self.player_hand.hand[i].rank == 'K'
                or self.player_hand.hand[i].rank == 'A') and self.player_hand.hand[i].suit == "\u2663":
                rank_count += 1
                clubs += 1
        if rank_count == 5 and hearts == 5:
            return True
        elif rank_count == 5 and diamonds == 5:
            return True
        elif rank_count == 5 and spades == 5:
            return True
        elif rank_count == 5 and clubs == 5:
            return True
        else:
            return False
    def check_pairs(self):
        counts = {
            'first_card': 0,
            'second_card': 0,
            'third_card': 0,
            'fourth_card': 0,
            'fifth_card': 0
        }
        for i in range(len(self.player_hand.hand)):
            if self.player_hand.hand[0].rank == self.player_hand.hand[i].rank:
                counts['first_card'] += 1
            elif self.player_hand.hand[1].rank == self.player_hand.hand[i].rank:
                counts['second_card'] += 1
            elif self.player_hand.hand[2].rank == self.player_hand.hand[i].rank:
                counts['third_card'] += 1
            elif self.player_hand.hand[3].rank == self.player_hand.hand[i].rank:
                counts['fourth_card'] += 1
            elif self.player_hand.hand[4].rank == self.player_hand.hand[i].rank:
                counts['fifth_card'] += 1

        pair = 0
        three_of_kind = 0
        four_of_kind = 0
        for value in counts.values():
            if value == 2:
                pair += 1
            elif value == 3:
                 three_of_kind += 1
            elif value == 4:
                four_of_kind += 1
        print(pair, three_of_kind, four_of_kind)
        if pair == 1 and three_of_kind == 0:
            return 1
        elif pair == 1 and three_of_kind == 1:
            return 5
        elif pair == 2:
            return 2
        elif four_of_kind == 1:
            return 4





deck = Deck()
deck.shuffle()
hand = Hand(deck)
hand.take_card()
hand.take_card()
hand.take_card()
hand.take_card()
hand.take_card()
print(hand)
checker = Checker(hand)
checker.check_pairs()
