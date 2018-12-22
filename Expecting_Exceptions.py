import math

def split_check(total, number_of_people):
    return math.ceil(total / number_of_people)

try:  # TRY
    total_due = float(input("What is the total? "))
    number_of_people = int(input("How many people? "))
except ValueError: # except
    print("Oh no that no value !!!!!")

amount_due = split_check(total_due, number_of_people)

print("Each person owes $ {}".format(amount_due))
