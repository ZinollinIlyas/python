days = int(input("Enter your age in days\n"))

year = days // 365
month = (days % 365) // 30
day = (days % 365) % 30

age = {
    'years': year,
    'months': month,
    'days': day
}

print(age)
