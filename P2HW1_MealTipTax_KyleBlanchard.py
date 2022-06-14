#Calculate the total amount of a meal puchased at a resturant
#06/14/2022
#CTI-110 P2HW1 - Meal Tip Tax Calculator
#Kyle Blanchard
#prompt the user for the cost of the food, the tip percentage, and the tax percentage. divide each percentage by 100 to get the decimal value, multiply each by the food cost to get the proper amount, and return the amount to tip, the amount for tax, and sum of the cost, tip, and tax to the user.
food_cost=float(input("Enter Food Cost: "))
tip_amount=float(input("Enter Tip Percentage: "))*food_cost/100.0
tax_amount=float(input("Enter Tax Percentage: "))*food_cost/100.0
total_amount = food_cost+tip_amount+tax_amount
print(f"Calculated Tip: ${tip_amount:.2f}")
print(f"Calculated Tax: ${tax_amount:.2f}")
print(f"\nTotal cost including tip and tax: ${total_amount:.2f}")
