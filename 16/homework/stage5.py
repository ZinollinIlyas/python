from random import randint
import sys


def binary_search():
    some_list = [i for i in range(101)]
    count = 0
    is_found = False
    start_idx = 0
    end_idx = len(some_list) - 1
    while not is_found:
        count += 1
        mid_idx = (end_idx + start_idx) // 2
        element = some_list[mid_idx]
        print("Is it %s?" % element)
        answer = input()
        if answer == 'yes' or answer == 'Yes':
            is_found = True
            return count
        elif answer == 'greater':
            start_idx = mid_idx
        elif answer == 'less':
            end_idx = mid_idx
        elif answer == 'exit':
            sys.exit("Good luck!))")
        else:
            print("There's no such command")

def linear_search():
    max = 100
    min = 0
    count = 0
    while True:
        count += 1
        hidden_number = randint(min, max)
        print("Is it %s" % hidden_number)
        answer = input()
        if answer == 'yes' or answer == 'Yes':
            return count
        elif answer == 'less':
            max = hidden_number
        elif answer == 'greater':
            min = hidden_number
        elif answer == 'exit':
            sys.exit("Good luck!))")
        else:
            print("There's no such command")


def guess_number():
    hidden_number = randint(0, 100)
    count = 0
    print("Try to guess the number from 0 to 100")
    while True:
        count += 1
        answer = input()
        if answer == 'exit':
            sys.exit("Good luck!))")
        elif int(answer) < hidden_number:
            print("less")
        elif int(answer) > hidden_number:
            print("greater")
        elif int(answer) == hidden_number:
            print("yes")
            return count
        else:
            print("There's no such command")


def play_in_turn():
    rounds = 3
    iterator = 0
    player = 0
    computer = 0
    is_draw = False
    print("Enter quantity of rounds form 1 to 10")
    quantity_rounds = input()
    if quantity_rounds == '':
        rounds = 3
    elif quantity_rounds == "exit":
        sys.exit("Good luck!))")
    elif int(quantity_rounds) >= 1 and int(quantity_rounds) <= 10:
        rounds = int(quantity_rounds)
    elif int(quantity_rounds) < 1 or int(quantity_rounds) > 10:
        print("Impossible quantity of rounds")
        return 0

    while iterator != rounds:
        print(f"Computer's playing {iterator + 1} round")
        print("Choose the level of difficulty: easy or difficult")
        choice = input()
        if choice == 'easy':
            computer_count = linear_search()
        elif choice == 'difficult':
            computer_count = binary_search()
        else:
            print("No such level of difficulty")
            return 0
        print(f"Human's playing {iterator + 1} round")
        player_count = guess_number()
        if player_count > computer_count:
            player += 1
        elif computer_count > player_count:
            computer += 1
        elif player_count == computer_count:
            is_draw = True
        iterator += 1
    if player < computer:
        print("Human wins!")
    elif computer < player:
        print("Computer wins!")
    elif is_draw:
        print("Draw!")


while True:
    print("Chose the game mode:\n1 - Computer vs human\n2 - Human vs computer\n3 - In turn")
    mode = input()
    if mode == '1':
        print("Choose the level of difficulty: easy or difficult")
        choice = input()
        if choice == 'easy':
            print("Got it in %s steps" % linear_search())
        elif choice == 'difficult':
            print("Got it in %s steps" % binary_search())
        else:
            print("No such level of difficulty")
    elif mode == '2':
        guess_number()
    elif mode == '3':
        play_in_turn()
    elif mode == 'exit':
        sys.exit("Good luck!))")
    else:
        print("No such mode")
