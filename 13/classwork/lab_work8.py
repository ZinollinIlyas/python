print("Enter integer or float numbers")
a = float(input("Enter first number\n"))
b = float(input("Enter second number\n"))

max_number = max(a, b)
min_number = min(a, b)
m = max_number / min_number
n = min_number / max_number
d = abs(a - b)
relationship = {
    'max_to_min': m,
    'min_to_max': n,
    'difference': d
}

if max_number.is_integer():
    print(f"Max = {round(max_number)}")
else:
    print(f"Max = {max_number}")

if min_number.is_integer():
    print(f"Min = {round(min_number)}")
else:
    print(f"Min = {min_number}")
print(f"Max to Min = {relationship['max_to_min']}")
print(f"Min to Max = {'{:.1f}'.format(relationship['min_to_max'])}")
print(f"Difference = {round(relationship['difference'])}")
