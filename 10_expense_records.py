
# A collection of expense records

expenses = [
    {
        "description": "Monthly rent",
        "category": "Housing",
        "amount": 200000,
        "date": "2026-10-01"
    },
    {
        "description": "Groceries",
        "category": "Food",
        "amount": 85000,
        "date": "2026-10-03"
    },
    {
        "description": "Taxi fare",
        "category": "Transport",
        "amount": 25000,
        "date": "2026-10-04"
    },
    {
        "description": "Electricity",
        "category": "Utilities",
        "amount": 40000,
        "date": "2026-10-05"
    }
]

print("EXPENSE REGISTER")
print("================")

for expense in expenses:
    print(
        f"{expense['date']} | "
        f"{expense['category']} | "
        f"{expense['description']} | "
        f"UGX {expense['amount']:,}"
    )

total_expenses = sum(
    expense["amount"] for expense in expenses
)

print("================")
print(f"Total expenses: UGX {total_expenses:,}")
print(f"Number of records: {len(expenses)}")
