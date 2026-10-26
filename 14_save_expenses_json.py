
import json

# Store several expenses as structured records.
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
    }
]

file_name = "expenses.json"

# Convert the Python data into JSON and save it.
with open(file_name, "w", encoding="utf-8") as file:
    json.dump(expenses, file, indent=4)

print(f"Saved {len(expenses)} expenses to {file_name}.")
