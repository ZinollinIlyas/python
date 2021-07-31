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



def guess_number():
    hidden_number = randint(0, 100)
    count = 0
    while True:
        print("Try to guess the number from 0 to 100")
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
        count += 1


while True:
    print("Chose the game mode:\n1 - Computer vs human\n2 - Human vs computer")
    mode = input()
    if mode == '1':
        print("Got it in %s steps" % binary_search())
    elif mode == '2':
        guess_number()
    elif mode == 'exit':
        sys.exit("Good luck!))")
    else:
        print("No such mode")
