
# Analyse spending by category

expenses = [
    {"description": "Monthly rent", "category": "Housing", "amount": 200000},
    {"description": "Groceries", "category": "Food", "amount": 85000},
    {"description": "Taxi fare", "category": "Transport", "amount": 25000},
    {"description": "Electricity", "category": "Utilities", "amount": 40000},
    {"description": "Lunch", "category": "Food", "amount": 30000},
    {"description": "Bus fare", "category": "Transport", "amount": 15000}
]

category_totals = {}

for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]

    if category not in category_totals:
        category_totals[category] = 0

    category_totals[category] += amount

print("SPENDING BY CATEGORY")
print("====================")

for category, total in category_totals.items():
    print(f"{category}: UGX {total:,}")

overall_total = sum(category_totals.values())

print("====================")
print(f"Overall total: UGX {overall_total:,}")
