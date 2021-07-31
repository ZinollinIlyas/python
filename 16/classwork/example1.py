some_list = [i for i in range(100)]


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
            return count, element
        elif value > element:
            start_idx = mid_idx
        else:
            end_idx = mid_idx


count, found_value = binary_search(98, some_list)
print("поиск отработал %s, со значением %s" % (count, found_value))
