numbers = []
total = 0
average = 0

print("Enter numbers")

while True:
    number = input()
    if number == "end":
        break
    numbers.append(number)

print("You entered: " + ', '.join(numbers))
for i in numbers:
    total += int(i)

print("Total: " + str(total))
average = total / len(numbers)
print("Average: " + str(average))
