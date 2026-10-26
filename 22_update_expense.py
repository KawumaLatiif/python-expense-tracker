
import sqlite3
from pathlib import Path

database_path = Path(__file__).with_name("expenses.db")


def update_expense():
    try:
        with sqlite3.connect(database_path) as connection:
            cursor = connection.cursor()

            # Display existing expenses first.
            cursor.execute("""
                SELECT id, description, category, amount, expense_date
                FROM expenses
                ORDER BY id
            """)

            expenses = cursor.fetchall()

            if not expenses:
                print("No expenses are available to update.")
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

            # Ask which record to update.
            try:
                expense_id = int(input("\nEnter the ID to update: "))
            except ValueError:
                print("Please enter a valid numeric ID.")
                return

            cursor.execute(
                "SELECT id, description, category, amount "
                "FROM expenses WHERE id = ?",
                (expense_id,)
            )

            existing_expense = cursor.fetchone()

            if existing_expense is None:
                print("No expense found with that ID.")
                return

            print("\nLeave a field blank to keep its current value.")

            current_description = existing_expense[1]
            current_category = existing_expense[2]
            current_amount = existing_expense[3]

            new_description = input(
                f"Description [{current_description}]: "
            ).strip()

            new_category = input(
                f"Category [{current_category}]: "
            ).strip()

            new_amount_text = input(
                f"Amount in UGX [{current_amount}]: "
            ).strip()

            # Keep the old values if the user leaves a field blank.
            if not new_description:
                new_description = current_description

            if not new_category:
                new_category = current_category
            else:
                new_category = new_category.title()

            if not new_amount_text:
                new_amount = current_amount
            else:
                try:
                    new_amount = int(new_amount_text)

                    if new_amount <= 0:
                        print("Amount must be greater than zero.")
                        return

                except ValueError:
                    print("Enter a valid whole-number amount.")
                    return

            # Update the selected database record.
            cursor.execute("""
                UPDATE expenses
                SET description = ?, category = ?, amount = ?
                WHERE id = ?
            """, (
                new_description,
                new_category,
                new_amount,
                expense_id
            ))

            if cursor.rowcount == 1:
                print("\nExpense updated successfully.")
            else:
                print("\nNo record was updated.")

    except sqlite3.Error as error:
        print(f"Database error: {error}")


if __name__ == "__main__":
    update_expense()
