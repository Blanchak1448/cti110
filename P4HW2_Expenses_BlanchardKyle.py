#CTI-110
#P4HW2 - Expense Calculator
#Kyle Blanchard
#06/27/2022

additional_expense = ''
balance = int(input("Enter starting amount in account: $"))
while balance <= 0:
    balance = int(input("Balance must be greater than 0. Enter a real balance: $"))
starting_balance = balance
expense = int(input("\nEnter expense 1: $"))
while balance < expense:
    expense = int(input("ERROR: Expense cannot be larger than balance. Enter a smaller expense or come back with a higher balance: "))
balance -= expense
expense_count = 1

while True:
    if balance == 0:
        print("Out of money")
        break
    additional_expense = input("Do you want to enter another expense?(y/n) ").lower()
    while additional_expense != 'y' and additional_expense != 'n':
        additional_expense= input("ERROR: Invalid input. Enter \'y\' or \'n\' ").lower()
    if additional_expense == 'y':
        expense_count += 1
        expense = int(input(f"\nEnter expense {expense_count}: $"))
        while balance < expense:
            expense = int(input("ERROR: Expense cannot be larger than balance. Enter a smaller expense or come back with a higher balance: "))
        balance -= expense
    else:
        break

print(f"\nAmount in accound before expenses subtracted: ${starting_balance:.2f}")
print(f"Number of expenses entered: {expense_count}")
print(f"Amount in account after expenses subtracted is: ${balance:.2f}")
