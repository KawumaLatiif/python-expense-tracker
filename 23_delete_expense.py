
import sqlite3
from pathlib import Path

database_path = Path(__file__).with_name("expenses.db")


def delete_expense():
    try:
        with sqlite3.connect(database_path) as connection:
            cursor = connection.cursor()

            # Display the available expenses.
            cursor.execute("""
                SELECT id, description, category, amount, expense_date
                FROM expenses
                ORDER BY id
            """)

            expenses = cursor.fetchall()

            if not expenses:
                print("There are no expenses to delete.")
                return

            print("\n========== EXISTING EXPENSES ==========")

            for expense in expenses:
                print(
                    f"ID: {expense[0]} | "
                    f"{expense[1]} | "
                    f"{expense[2]} | "
                    f"UGX {expense[3]:,} | "
                    f"{expense[4]}"
                )

            # Get the ID of the expense to delete.
            try:
                expense_id = int(
                    input("\nEnter the ID of the expense to delete: ")
                )
            except ValueError:
                print("Please enter a valid numeric ID.")
                return

            # Check that the expense exists.
            cursor.execute("""
                SELECT id, description, category, amount
                FROM expenses
                WHERE id = ?
            """, (expense_id,))

            expense = cursor.fetchone()

            if expense is None:
                print("No expense found with that ID.")
                return

            # Ask for confirmation before deleting.
            print("\nYou selected:")
            print(f"Description: {expense[1]}")
            print(f"Category: {expense[2]}")
            print(f"Amount: UGX {expense[3]:,}")

            confirmation = input(
                "\nAre you sure you want to delete this expense? (yes/no): "
            ).strip().lower()

            if confirmation != "yes":
                print("Deletion cancelled. No expense was deleted.")
                return

            # Delete only the selected record.
            cursor.execute("""
                DELETE FROM expenses
                WHERE id = ?
            """, (expense_id,))

            if cursor.rowcount == 1:
                print("Expense deleted successfully.")
            else:
                print("No expense was deleted.")

    except sqlite3.Error as error:
        print(f"Database error: {error}")


if __name__ == "__main__":
    delete_expense()
