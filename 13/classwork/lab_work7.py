radius = [12, 35, 4]
PI = 3.14
areas = []


def calculate_area(array):
    for i in array:
        areas.append(PI * pow(i, 2))


calculate_area(radius)

print(areas)
