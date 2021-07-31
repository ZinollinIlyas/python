from random import randint


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
        else:
            print("There's no such command")





