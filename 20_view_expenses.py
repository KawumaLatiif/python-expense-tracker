
import sqlite3
from pathlib import Path

# Locate the database in the same folder as this script.
database_path = Path(__file__).with_name("expenses.db")


def view_expenses():
    """Retrieve and display all expenses from the database."""

    try:
        with sqlite3.connect(database_path) as connection:
            cursor = connection.cursor()

            # Retrieve all expense records.
            cursor.execute("""
                SELECT id, description, category, amount, expense_date
                FROM expenses
                ORDER BY expense_date DESC, id DESC
            """)

            expenses = cursor.fetchall()

            if not expenses:
                print("No expenses found in the database.")
                return

            print("\n========== EXPENSE REPORT ==========")

            total = 0

            for expense in expenses:
                expense_id, description, category, amount, expense_date = expense

                print(f"\nID: {expense_id}")
                print(f"Description: {description}")
                print(f"Category: {category}")
                print(f"Amount: UGX {amount:,}")
                print(f"Date: {expense_date}")

                total += amount

            print("\n====================================")
            print(f"Number of expenses: {len(expenses)}")
            print(f"Total expenditure: UGX {total:,}")

    except sqlite3.Error as error:
        print(f"Database error: {error}")


if __name__ == "__main__":
    view_expenses()
