
# Lists: storing multiple values in one variable

expenses = [50000, 30000, 25000, 40000]

print("Individual expenses:")

for expense in expenses:
    print(f"UGX {expense:,}")

total_expenses = sum(expenses)
number_of_expenses = len(expenses)
average_expense = total_expenses / number_of_expenses

print("\nExpense statistics")
print(f"Number of expenses: {number_of_expenses}")
print(f"Total expenses: UGX {total_expenses:,}")
print(f"Average expense: UGX {average_expense:,.0f}")

# Add another expense to the list.
expenses.append(15000)

print(f"Updated number of expenses: {len(expenses)}")
