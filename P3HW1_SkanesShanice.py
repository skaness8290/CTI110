# Shanice Skanes
# 06/28/2024
# P3HW1
# This program takes a number grade , determines min, max, sum, and average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
total_sum = sum(grades)
avg = total_sum / len(grades)

# Determine letter grade for average

if avg >= 90:
 letter_grade = 'A'
elif avg >= 80:
 letter_grade = 'B'
elif avg >= 70:
 letter_grade = 'C'
elif avg >= 60:
 letter_grade = 'D'
else:
 letter_grade = 'F'

# Display the results
print("---------Results----------")
print(f"Lowest Grade:            {low}")
print(f"Highest Grade:           {high}")
print(f"Sum of Grades:           {total_sum}")
print(f"Average:                 {avg:.2f}")
print("--------------------------")
print(f"Your grade is: {letter_grade}")





