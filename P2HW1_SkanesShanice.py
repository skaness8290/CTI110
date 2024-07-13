# Shanice Skanes
# 06/21/2024
# P2LAB2
# This program calculates and displays travel expenses

# 1. Prompt user to enter their budget and store it in as a number.
# 2. Prompt user to enter their travel destination and store it in as a number.
# 3. Prompt user to enter the amount for gas and store it in as a number.
# 4. Prompt user to enter the amount for accommodation and store it in as a number.
# 5. Prompt user to enter the amount for food and store it in as a number.
# 6. Calculate total amount by summing gas, accommodation, and food.
# 7. Calculate remaining balance by subtracting total amount from the budget.
# 8. Display the travel destination, initial budget, individual expenses, and remaining balance.

budget = float(input("Enter Budget: "))

destination = input("Enter your travel destination: ")

gas = float(input("How much do you think you will spend on gas? "))

accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))

food = float(input("Last, how much do you need for food? "))

total_expenses = gas + accommodation + food

remaining_balance = budget - total_expenses

print("\n-----------Travel Expenses------------")
print(f"Location:          {destination}")
print(f"Initial Budget:    ${budget:.2f}")
print(f"Fuel:              ${gas:.2f}")
print(f"Accommodation:     ${accommodation:.2f}")
print(f"Food:              ${food:.2f}")
print("--------------------------------------")
print(f"Remaining Balance: ${remaining_balance:.2f}")