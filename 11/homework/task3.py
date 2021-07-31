print("Enter two strings:")
first_str = input()
second_str = input()


def calculate_difference(string1, string2):
    result = len(string1) - len(string2)
    return abs(result)


if len(first_str) > len(second_str):
    print("First string is longer by %s characters" % calculate_difference(first_str, second_str))
elif len(first_str) == len(second_str):
    print("Strings are equal length")
else:
    print("Second string is longer by %s characters" % calculate_difference(first_str, second_str))