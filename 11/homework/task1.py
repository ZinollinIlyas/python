from datetime import datetime

current_date = datetime.now()

print("Enter your name :")
name = input().capitalize()
print("Enter your last name :")
last_name = input().capitalize()
print("When were you born?")
birth_date = int(input())
print("Where are you from?")
location = input().capitalize()


def age(birth_year):
    return current_date.year - birth_year


print("Hello, %s %s. You are %s years old. You are living in %s" % (name, last_name, age(birth_date), location))

