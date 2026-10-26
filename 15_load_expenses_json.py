
import json

file_name = "expenses.json"

try:
    # Open the saved JSON file and convert it into Python data.
    with open(file_name, "r", encoding="utf-8") as file:
        expenses = json.load(file)

    print("SAVED EXPENSES")
    print("==============")

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

    print("==============")
    print(f"Total expenses: UGX {total_expenses:,}")
    print(f"Records loaded: {len(expenses)}")

except FileNotFoundError:
    print("No expense file found. Save some expenses first.")

except json.JSONDecodeError:
    print("The expense file contains invalid JSON.")
