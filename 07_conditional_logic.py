
# Conditional logic for a personal expense tracker

monthly_income = 800000
total_expenses = 650000

balance = monthly_income - total_expenses
expense_ratio = (total_expenses / monthly_income) * 100

print("MONTHLY BUDGET ANALYSIS")
print("-----------------------")
print(f"Monthly income: UGX {monthly_income:,}")
print(f"Total expenses: UGX {total_expenses:,}")
print(f"Remaining balance: UGX {balance:,}")
print(f"Income spent: {expense_ratio:.1f}%")

if balance < 0:
    print("Status: Overspending")
elif balance == 0:
    print("Status: All income has been spent")
elif expense_ratio >= 80:
    print("Status: High spending")
else:
    print("Status: Within budget")
