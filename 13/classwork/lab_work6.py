from random import randint

A = []
B = []

for i in range(0, 10):
    A.append(randint(1, 100))
    B.append(randint(1, 100))


C = [x+y for x, y in zip(A, B)]
max_number = max(C)

print(f"Массив А: {A}")
print(f"Массви B: {B}")
print(f"Массив C: {C}")
print(f"MAX = {max_number}")
