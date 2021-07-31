some_list = [i for i in range(1000)]

def binary_search(value, list_for_found):
    count = 0
    is_found = False
    start_idx = 0
    end_idx = len(list_for_found) - 1
    while not is_found:
        count += 1
        mid_idx = (end_idx + start_idx) // 2
        element = list_for_found[mid_idx]
        if element == value:
            is_found = True
            return element, count
        elif value > element:
            start_idx = mid_idx
        else:
            end_idx = mid_idx

def linear_search(value, list_for_found):
    count = 0
    for i in range(len(list_for_found)):
        count += 1
        if value == list_for_found[i]:
            return value, count

print("Got %s in %s steps" % binary_search(215, some_list))
print("Got %s in %s steps" % linear_search(215, some_list))