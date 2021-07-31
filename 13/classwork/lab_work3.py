digit = int(input("Enter number between 1000 and 9999\n"))
if digit < 1000 or digit > 9999:
    print("Entered value must be between 1000 and 9999")


def justify(a):
    if isinstance(a, int):
        for i in str(a):
            print(i)
    else:
        print("Entered value must be integer")


justify(digit)


# 2 способ

def justify_2(a):
    if not isinstance(a, int):
        print("Entered value must be integer")
    else:
        print(str(a)[0] + '000')
        print(str(a)[1] + '00')
        print(str(a)[2] + '0')
        print(str(a)[3])


justify_2(digit)
