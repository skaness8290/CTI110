# Shanice Skanes
# 07/05/2024
# P4HW2
# This program calculates the gross pay of multiple employees based on hours worked, pay rate, and overtime hours, and calculates total payments for all employees.

# 1. Totals for overtime pay, regular pay, gross pay, and employee count.
# 2. Use a loop to repeatedly ask for employee details until the user enters "Done".
# 3. For each employee, get the number of hours worked and the pay rate.
# 4. Calculate overtime hours and pay, regular hours and pay, and gross pay.
# 5. Update the totals with the current employee's values.
# 6. Display the employee's pay details.
# 7. After the loop ends, display the totals.

# Step 1
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

while True:
    employee_name = input("Enter employee's name or 'Done' to terminate: ")

    if employee_name.lower() == "done":
        break

    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    overtime_hours = 0
    overtime_pay = 0

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * pay_rate * 1.5
        regular_hours = 40
    else:
        regular_hours = hours_worked

    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    print(f"\nEmployee name: {employee_name}\n")
    print(f"Hours Worked    Pay Rate   OverTime   OverTime Pay   RegHourPay     Gross Pay")
    print("---------------------------------------------------------------------------------------")
    print(f"{hours_worked:<15.1f} {pay_rate:<10.2f} {overtime_hours:<10.1f} {overtime_pay:<15.2f} {regular_pay:<15.2f} {gross_pay:<15.2f}\n")


print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")