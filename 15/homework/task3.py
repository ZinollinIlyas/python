from random import uniform

days = int(input("Enter number of days\n"))

exchange1 = []
exchange2 = []
exchange3 = []


def generate(day, a):
    for i in range(day):
        a.append(uniform(65.0, 70.0))


generate(days, exchange1)
generate(days, exchange2)
generate(days, exchange3)


result_list = exchange1 + exchange2 + exchange3

average = sum(result_list) / len(result_list)

print(f"Generated prices: \nExchange 1: {exchange1}\nExchange 2: {exchange2}\nExchange 3: {exchange3}\n\nAverage price:\
 {average:.7}")
