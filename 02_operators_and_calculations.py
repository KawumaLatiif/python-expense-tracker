
# Arithmetic operators and financial calculations

monthly_income = 800000

rent = 200000
food = 120000
transport = 60000
utilities = 40000

total_expenses = rent + food + transport + utilities
remaining_balance = monthly_income - total_expenses

print("MONTHLY FINANCIAL REPORT")
print("------------------------")
print(f"Income: UGX {monthly_income:,}")
print(f"Total expenses: UGX {total_expenses:,}")
print(f"Remaining balance: UGX {remaining_balance:,}")

# Check whether expenses are within the income.
within_budget = total_expenses <= monthly_income

print(f"Within budget: {within_budget}")
