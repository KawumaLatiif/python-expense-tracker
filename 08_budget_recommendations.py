# Budget recommendations based on spending percentage

monthly_income = 800000
total_expenses = 650000

print("MONTHLY BUDGET RECOMMENDATION")
print("------------------------------")
print(f"Monthly income: UGX {monthly_income:,}")
print(f"Total expenses: UGX {total_expenses:,}")

# Handle zero or negative income safely
if monthly_income <= 0:
    print("Cannot calculate spending percentage: income must be greater than zero.")
    if total_expenses > 0:
        print("Recommendation: Warning: You are overspending")
    else:
        print("Recommendation: No income and no expenses recorded.")
else:
    balance = monthly_income - total_expenses
    expense_ratio = (total_expenses / monthly_income) * 100

    print(f"Remaining balance: UGX {balance:,}")
    print(f"Income spent: {expense_ratio:.1f}%")
    print()

    # Prioritise the overspending warning before any ratio-based advice
    if total_expenses > monthly_income:
        print("Recommendation: Warning: You are overspending")
    elif expense_ratio < 50:
        print("Recommendation: Good spending control")
    elif expense_ratio < 80:
        print("Recommendation: Monitor your spending")
    else:
        print("Recommendation: Consider reducing expenses")