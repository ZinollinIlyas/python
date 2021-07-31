from random import randint

print("Enter number of samples")
sample = int(input())
iterator = 1


groups = {
    "Group 0-9": 0,
    "Group 10-19": 0,
    "Group 20-29": 0,
    "Group 30-39": 0,
    "Group 40-49": 0,
    "Group 50-59": 0,
    "Group 60-69": 0,
    "Group 70-79": 0,
    "Group 80-89": 0,
    "Group 90-99": 0
}

while iterator <= sample:
    random_number = randint(0, 99)

    if 0 <= random_number <= 9:
        groups["Group 0-9"] += 1
    elif 10 <= random_number <= 19:
        groups["Group 10-19"] += 1
    elif 20 <= random_number <= 29:
        groups["Group 20-29"] += 1
    elif 30 <= random_number <= 39:
        groups["Group 30-39"] += 1
    elif 40 <= random_number <= 49:
        groups["Group 40-49"] += 1
    elif 50 <= random_number <= 59:
        groups["Group 50-59"] += 1
    elif 60 <= random_number <= 69:
        groups["Group 60-69"] += 1
    elif 70 <= random_number <= 79:
        groups["Group 70-79"] += 1
    elif 80 <= random_number <= 89:
        groups["Group 80-89"] += 1
    else:
        groups["Group 90-99"] += 1

    iterator += 1

print(f"Number of samples: {sample}")
for key in groups:
    print(f"{key}: {groups[key]}")
