# Shanice Skanes
# 06/22/2024
# P2HW2
# This program calculates the min, max, sum, and average of a student's grades

# 1. Create a list named 'module_grades'.
# 2. Prompt student to enter grades for Module 1 through 6.
# 3. Store each entered grade in the list created.
# 4. Calculate the lowest grade using the min() function.
# 5. Calculate the highest grade using the max() function.
# 6. Calculate the sum of grades using the sum() function.
# 7. Calculate the average of grades by dividing the sum of grades by the number of grades.
# 8. Display the results, ensuring proper alignment and formatting for decimal places.

module_grades = []

module_grades.append(float(input("Enter grade for Module 1: ")))
module_grades.append(float(input("Enter grade for Module 2: ")))
module_grades.append(float(input("Enter grade for Module 3: ")))
module_grades.append(float(input("Enter grade for Module 4: ")))
module_grades.append(float(input("Enter grade for Module 5: ")))
module_grades.append(float(input("Enter grade for Module 6: ")))

lowest_grade = min(module_grades)
highest_grade = max(module_grades)
sum_of_grades = sum(module_grades)
average_grade = sum_of_grades / len(module_grades) 

print("----------Results-----------")
print(f"Lowest Grade:           {lowest_grade}")
print(f"Highest Grade:          {highest_grade}")
print(f"Sum of Grades:          {sum_of_grades}")
print(f"Average:                {average_grade:.2f}")
print("----------------------------")