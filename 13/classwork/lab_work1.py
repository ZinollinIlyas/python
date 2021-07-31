def compare(a, b):
    if not (a.isdigit() and b.isdigit()):
        print("number must be integer")
    else:
        if int(a) > int(b):
            print(">")
        elif int(a) < int(b):
            print("<")
        else:
            print("=")


first_digit = input("Enter first number\n")
second_digit = input("Enter second number\n")

compare(first_digit, second_digit)
