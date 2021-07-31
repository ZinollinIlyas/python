print("Enter pyramid height")
height = int(input())


def build_pyramid(a):
    for i in range(a + 1):
        print(f"{'*' * (i * 2 - 1):^{a * 2}}")


def build_rhombus(a):
    for i in range(a + 1):
        print(f"{'*' * (i * 2 - 1):^{a * 2}}")

    for i in range(a, 0, -1):
        print(f"{'*' * ((i * 2 - 1) - 2):^{a * 2}}")


build_rhombus(height)
build_pyramid(height)
