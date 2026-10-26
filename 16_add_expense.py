
import json
from pathlib import Path
from datetime import date

# Store the data file beside this Python script.
file_path = Path(__file__).with_name("expenses.json")


def load_expenses():
    """Load existing records, or return an empty list."""
    if not file_path.exists():
        return []

    with file_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("The expense file must contain a list.")

    return data


def save_expenses(expenses):
    """Write all expense records to the JSON file."""
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def get_positive_amount():
    """Ask for a valid amount greater than zero."""
    while True:
        try:
            amount = float(input("Enter expense amount (UGX): "))

            if amount <= 0:
                print("Enter an amount greater than zero.")
                continue

            return amount

        except ValueError:
            print("Please enter a valid number.")


def main():
    try:
        expenses = load_expenses()
    except (json.JSONDecodeError, ValueError) as error:
        print(f"Cannot load expenses: {error}")
        return

    description = input("Enter expense description: ").strip()
    category = input("Enter expense category: ").strip().title()

    if not description or not category:
        print("Description and category cannot be empty.")
        return

    amount = get_positive_amount()

    new_expense = {
        "description": description,
        "category": category,
        "amount": amount,
        "date": date.today().isoformat()
    }

    expenses.append(new_expense)
    save_expenses(expenses)

    print("\nExpense saved successfully.")
    print(f"Total records: {len(expenses)}")


if __name__ == "__main__":
    main()
