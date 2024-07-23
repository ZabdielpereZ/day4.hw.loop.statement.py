# 1. The Range Riddle

# Objective: The aim of this assignment is to deepen your understanding of Python's range() function and its application in loops. You will correct a code snippet, simulate moods for different days, and create a countdown timer.

# Task 1: Every Other Day Write a program that prints each day of the week, but only if that day is on an even index.

#indicies        0    1    2   3    4    5    6
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

print("Even Days of the Week, from 0 to 6")
for num in range(0, len(days_of_week), 2):
    print(days_of_week[num])

print('='* 50)

# 2. Loop Condition Logic

# Objective: The aim of this assignment is to explore the importance of the loop condition in while loops. You will create loops with different conditions to see how they influence the behavior of the loop.

# Task 1: Loop Condition Exploration Write a while loop with a condition that will never be true (an infinite loop). Ask the user a question until their answer triggers a break statement (hint: use an if statement to evaluate their answer).

flag = True
while flag:
    user = input("Do you want to continue? (yes/no): ")
    if user == "no":
        break
    # flag = False  <---- # this works too!!

print('='* 50)

# Task 2: Conditional Exit Create a while loop that will terminate after 5 iterations, and each iteration you print which iteration it is on. (use a control variable)

people = []

while len(people) < 5:
    print("Letting person take a seat...")
    people.append('people')
    print(len(people), "left")
print(people)
