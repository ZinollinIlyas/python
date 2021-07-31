items = ['Milk', 'Bread', 'Cheese', 'Chocolate', 'Water']
prices = [10, 5, 20.5, 7.15, 2.99]

print(f"{'Name:':20}{'Price:'}")

for i in range(len(items)):
    items[i] = '{:20}'.format(items[i])
    prices[i] = '{:.2f}'.format(prices[i])
    print(f"{items[i]:.20}{prices[i]:.6}")

