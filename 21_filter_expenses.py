
import sqlite3
from pathlib import Path

database_path = Path(__file__).with_name("expenses.db")


def filter_expenses():
    category = input("Enter category to search for: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    try:
        with sqlite3.connect(database_path) as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT id, description, category, amount, expense_date
                FROM expenses
                WHERE LOWER(category) = LOWER(?)
                ORDER BY expense_date DESC, id DESC
                """,
                (category,)
            )

            expenses = cursor.fetchall()

            if not expenses:
                print(f"No expenses found in category: {category}")
                return

            total = 0

            print(f"\n========== {category.upper()} EXPENSES ==========")

            for expense in expenses:
                expense_id, description, expense_category, amount, expense_date = expense

                print(f"\nID: {expense_id}")
                print(f"Description: {description}")
                print(f"Category: {expense_category}")
                print(f"Amount: UGX {amount:,}")
                print(f"Date: {expense_date}")

                total += amount

            print("\n====================================")
            print(f"Matching records: {len(expenses)}")
            print(f"Category total: UGX {total:,}")

    except sqlite3.Error as error:
        print(f"Database error: {error}")


if __name__ == "__main__":
    filter_expenses()
