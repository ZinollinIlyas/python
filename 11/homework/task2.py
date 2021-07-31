from random import randint

first_digit = randint(1, 9)
second_digit = randint(1, 9)
result = first_digit * second_digit

print("How much is %s * %s" % (first_digit, second_digit))
answer = int(input())
if answer == result:
    print("Correct.")
else:
    print("Wrong. Correct answer is: %s" % result)

