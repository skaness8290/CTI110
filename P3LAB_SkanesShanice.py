# Shanice Skanes
# 06/28/2024
# P3LAB
# This program calculates the most efficient number of dollars, quarters, dimes, nickels, and pennies needed to make a given amount of money.

def calculate_change(amount):
    amount_in_cents = int(round(amount * 100))
    
    dollars = amount_in_cents // 100
    amount_in_cents %= 100
    
    quarters = amount_in_cents // 25
    amount_in_cents %= 25
    
    dimes = amount_in_cents // 10
    amount_in_cents %= 10
    
    nickels = amount_in_cents // 5
    amount_in_cents %= 5
    
    pennies = amount_in_cents

    result = []
    
    if dollars > 0:
        result.append(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        result.append(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        result.append(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        result.append(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        result.append(f"{pennies} Penn{'ies' if pennies > 1 else 'y'}")
    
    if not result:
        result.append("No change")
    
    for line in result:
        print(line)

amount = float(input("Enter the amount of money as a float: $"))
calculate_change(amount)
