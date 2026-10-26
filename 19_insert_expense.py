
import sqlite3
from pathlib import Path
from datetime import date

# Locate the database beside this Python file.
database_path = Path(__file__).with_name("expenses.db")


def get_positive_amount():
    """Ask for an expense amount greater than zero."""
    while True:
        try:
            amount = int(input("Enter expense amount (UGX): "))

            if amount <= 0:
                print("The amount must be greater than zero.")
                continue

            return amount

        except ValueError:
            print("Please enter a whole number, such as 25000.")


def main():
    description = input("Enter expense description: ").strip()
    category = input("Enter expense category: ").strip().title()

    if not description or not category:
        print("Description and category cannot be empty.")
        return

    amount = get_positive_amount()
    expense_date = date.today().isoformat()

    try:
        with sqlite3.connect(database_path) as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO expenses
                    (description, category, amount, expense_date)
                VALUES (?, ?, ?, ?)
                """,
                (description, category, amount, expense_date)
            )

            print("\nExpense saved successfully.")
            print(f"Expense ID: {cursor.lastrowid}")
            print(f"Description: {description}")
            print(f"Category: {category}")
            print(f"Amount: UGX {amount:,}")
            print(f"Date: {expense_date}")

    except sqlite3.Error as error:
        print(f"Database error: {error}")


if __name__ == "__main__":
    main()
