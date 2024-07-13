# Shanice Skanes
# 07/05/2024
# P4HW1
#  This program collects a user-defined number of scores, validates the input, calculates the average after dropping the lowest score, and displays the corresponding letter grade.

# 1. Ask the user to enter the number of scores they want to input.
# 2. An empty list to store the scores.
# 3. Create a loop to collect the scores based on the number provided.
# 4. For each score:
#    a. Prompt the user to enter the score.
#    b. Check if the score is between 0 and 100.
#    c. If the score is invalid, notify the user and ask for a valid score.
#    d. If the score is valid, add it to the list.
# 5. Calculate the lowest score using min().
# 6. Remove the lowest score from the list.
# 7. Calculate the sum and average of the remaining scores.
# 8. Determine the letter grade based on the average.
# 9. Display the results in the specified format.

num_scores = int(input("How many scores do you want to enter? "))

grades = []

for i in range(num_scores):
    while True:
        score = float(input(f"Enter score#{i + 1}: "))
        if 0 <= score <=100:
            grades.append(score)
            break
        else:
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            print(f"Enter score #{i + 1} again:")

lowest_grade = min(grades)

grades.remove(lowest_grade)

sum_of_grades = sum(grades)

average_grade = sum_of_grades / len(grades)

if average_grade >= 90:
    letter_grade = 'A'
elif average_grade >= 80:
    letter_grade = 'B'
elif average_grade >= 70:
    letter_grade = 'C'
elif average_grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print("\n------------------Results------------------")
print(f"Lowest Score     :  {lowest_grade}")
print(f"Modified List    :  {grades}")
print(f"Scores Average   :  {average_grade:.2f}")
print(f"Grade            :  {letter_grade}")
print("--------------------------------------------")