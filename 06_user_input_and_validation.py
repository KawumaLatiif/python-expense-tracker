
# User input and validation

def get_positive_amount(prompt):
    """Ask for a positive amount and reject invalid input."""
    while True:
        try:
            amount = float(input(prompt))

            if amount <= 0:
                print("Enter an amount greater than zero.")
                continue

            return amount

        except ValueError:
            print("Invalid input. Enter a number, such as 50000.")


monthly_income = get_positive_amount(
    "Enter your monthly income (UGX): "
)

expenses = []

number_of_expenses = int(
    input("How many expenses do you want to record? ")
)

for number in range(1, number_of_expenses + 1):
    amount = get_positive_amount(
        f"Enter expense {number} (UGX): "
    )
    expenses.append(amount)

total_expenses = sum(expenses)
balance = monthly_income - total_expenses

print("\nMONTHLY FINANCIAL REPORT")
print("------------------------")
print(f"Income: UGX {monthly_income:,.0f}")
print(f"Total expenses: UGX {total_expenses:,.0f}")
print(f"Remaining balance: UGX {balance:,.0f}")
