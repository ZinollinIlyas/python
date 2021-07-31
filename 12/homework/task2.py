import math

marks = {
    "Bill": None,
    "Jane": None,
    "John": None,
    "Mary": None
}
avg_result = 0

print("Enter mark for Bill:")
marks["Bill"] = int(input())
print("Enter mark for Jane:")
marks["Jane"] = int(input())
print("Enter mark for John:")
marks["John"] = int(input())
print("Enter mark for Mary:")
marks["Mary"] = int(input())

avg_result = (marks["Bill"] + marks["Jane"] + marks["John"] + marks["Mary"]) / len(marks)

print(f"Average mark : {math.ceil(avg_result)}")


