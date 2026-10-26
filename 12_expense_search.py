expenses = [
    {"description": "Rent", "category": "Housing", "amount": 200000},
    {"description": "Groceries", "category": "Food", "amount": 85000},
    {"description": "Taxi", "category": "Transport", "amount": 25000},
    {"description": "Lunch", "category": "Food", "amount": 30000},
    {"description": "Electricity", "category": "Utilities", "amount": 40000}
]

search_category = input("Enter a category to search: ").strip().title()

matching_expenses = []

for expense in expenses:
    if expense["category"] == search_category:
        matching_expenses.append(expense)

if matching_expenses:
    print(f"\nExpenses in {search_category}:")

    total_amount = 0

    for expense in matching_expenses:
        print(
            f"{expense['description']}: "
            f"UGX {expense['amount']:,}"
        )
        total_amount += expense["amount"]

    print("-" * 30)
    print(f"Total: UGX {total_amount:,}")
else:
    print(f"No expenses found in {search_category}.")