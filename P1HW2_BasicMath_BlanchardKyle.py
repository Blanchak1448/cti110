# Calculates tax and shows a monthly and annual cost of an expense
# 06/08/2022
# CTI-110 P1HW2 - Basic Math
# Kyle Blanchard
#The program will prompt the user to enter the name and amount of the expense, it will output the name and total of the expense before tax, output the total monthly tax, then display the monthly and annual cost with tax.

expense_name = input("Enter name of expense: ")
expense_price = int(input("Enter monthly charge: "))
print("\nBill: %s ---------- Before Tax: $%1.2f"%(expense_name,expense_price))
print("Monthly Tax: $%1.2f"%(expense_price*.06))
print("Monthly Charge: $%1.2f"%(expense_price+expense_price*.06))
print("Annual Charge: $%1.2f"%((expense_price+expense_price*.06)*12))
