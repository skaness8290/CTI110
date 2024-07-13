# Shanice Skanes
# 06/28/2024
# P3HW2
# This program calculates the gross pay of an employee based on hours worked, pay rate, and overtime hours.

# 1. Ask user to enter the name of the employee.
# 2. Ask user to enter the number of hours the employee worked this week.
# 3. Ask user to enter the employee's pay rate.
# 4. Evaluate if the employee has worked overtime (more than 40 hours).
# 5. If overtime, calculate the overtime hours and the amount owed for overtime.
# 6. Calculate the amount the employee should be paid for regular hours worked.
# 7. Calculate the total gross pay.
# 8. Display the employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours, and gross pay.

# Step 1
employee_name = input("Enter employee's name: ")

# Step 2
hours_worked = float(input("Enter number of hours worked: "))

# Step 3
pay_rate = float(input("Enter employee's pay rate: "))

overtime_hours = 0
overtime_pay = 0

# Step 4
if hours_worked > 40:
    # Step 5
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_hours = 40
else:
    regular_hours = hours_worked

# Step 6
regular_pay = regular_hours * pay_rate

# Step 7
gross_pay = regular_pay + overtime_pay

# Step 8
print("---------------------------------------")
print(f"Employee name: {employee_name}\n")
print("Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHourPay  Gross Pay")
print("-------------------------------------------------------------------------")
print(f"{hours_worked:<14.1f} {pay_rate:<10.2f} {overtime_hours:<10.1f} {overtime_pay:<14.2f} {regular_pay:<11.2f} {gross_pay:<10.2f}")
