#CTI-110
#P3HW2 - MealTipTax
#Blanchard Kyle
#06/21/2022
#building on a program to calculate tip, tax, and total to include validation for tip percentage and a hard coded tax value
food_cost=float(input("Enter Food Cost: "))
tip_amount=float(input("Enter tip percentage of 15, 18, or 20: "))
if tip_amount == 15 or tip_amount == 18 or tip_amount == 20:
    tip_amount = tip_amount * food_cost / 100
    tax_amount=.06*food_cost
    total_amount = food_cost+tip_amount+tax_amount
    print(f"Calculated Tip: ${tip_amount:.2f}")
    print(f"Calculated Tax: ${tax_amount:.2f}")
    print(f"\nTotal cost including tip and tax: ${total_amount:.2f}")
else:
    print("Enter a valid percentage")
