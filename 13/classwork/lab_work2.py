first_segment = int(input("Enter first segment\n"))
second_segment = int(input("Enter second segment\n"))
third_segment = int(input("Enter third segment\n"))


def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "No"
    elif a + b < c or a + c < b or b + c < a:
        return "No"
    else:
        return "Yes"


print(is_triangle(first_segment, second_segment, third_segment))
