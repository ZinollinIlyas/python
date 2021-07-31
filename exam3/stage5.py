from random import shuffle


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


class Hand:
    def __init__(self, deck):
        self.hand = []
        self.deck = deck

    def take_card(self):
        self.hand.append(self.deck.give_card())

    def change_card(self, index):
        self.take_card()
        self.hand[index - 1].rank = self.hand[len(self.hand) - 1].rank
        self.hand[index - 1].suit = self.hand[len(self.hand) - 1].suit
        self.hand.remove(self.hand[len(self.hand) - 1])

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
            elif (self.player_hand.hand[i].rank == '10' or self.player_hand.hand[i].rank == 'J' or
                  self.player_hand.hand[
                      i].rank == 'Q'
                  or self.player_hand.hand[i].rank == 'K'
                  or self.player_hand.hand[i].rank == 'A') and self.player_hand.hand[i].suit == "\u2660":
                rank_count += 1
                spades += 1
            elif (self.player_hand.hand[i].rank == '10' or self.player_hand.hand[i].rank == 'J' or
                  self.player_hand.hand[
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
        if pair == 1 and three_of_kind == 0:
            return 1
        elif three_of_kind == 1 and pair == 0:
            return 3
        elif pair == 1 and three_of_kind == 1:
            return 5
        elif pair == 2:
            return 2
        elif four_of_kind == 1:
            return 4


class Application:
    def __init__(self):
        self.deck = None
        self.hand = None
        self.checker = None

    def run(self):
        while True:
            self.deck = Deck()
            self.hand = Hand(self.deck)
            self.checker = Checker(self.hand)
            self.deck.shuffle()
            for _ in range(5):
                self.hand.take_card()
            print(self.hand)
            change = input("What cards do you want to change?\n")
            if change == '':
                pass
            else:
                change_list = change.split(' ')
                for i in change_list:
                    self.hand.change_card(int(i))
                print(self.hand)
            if self.checker.check_royal_flush():
                print("ROYAL FLUSH")
                choice = input("Do you want to play again?\n")
                if choice == 'yes' or choice == "Yes":
                    self.run()
                else:
                    print('Goodbye')
                    break
            elif self.checker.check_pairs() == 1:
                print("Pair")
                choice = input("Do you want to play again?\n")
                if choice == 'yes' or choice == "Yes":
                    self.run()
                else:
                    print('Goodbye')
                    break
            elif self.checker.check_pairs() == 2:
                print("Two pairs")
                choice = input("Do you want to play again?\n")
                if choice == 'yes' or choice == "Yes":
                    self.run()
                else:
                    print('Goodbye')
                    break
            elif self.checker.check_pairs() == 5:
                print("Pair and three of a kind")
                choice = input("Do you want to play again?\n")
                if choice == 'yes' or choice == "Yes":
                    self.run()
                else:
                    print('Goodbye')
                    break
            elif self.checker.check_pairs() == 4:
                print("Four of a kind")
                choice = input("Do you want to play again?\n")
                if choice == 'yes' or choice == "Yes":
                    self.run()
                else:
                    print('Goodbye')
                    break
            elif self.checker.check_pairs() == 3:
                print("Three of a kind")
                choice = input("Do you want to play again?\n")
                if choice == 'yes' or choice == "Yes":
                    self.run()
                else:
                    print('Goodbye')
                    break
            else:
                print("No combination")
                choice = input("Do you want to play again?\n")
                if choice == 'yes' or choice == "Yes":
                    self.run()
                else:
                    print('Goodbye')
                    break


game = Application()
game.run()
