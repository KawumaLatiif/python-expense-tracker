
import sqlite3
from pathlib import Path
from datetime import date

DATABASE_PATH = Path(__file__).with_name("expenses.db")


def connect_database():
    """Connect to the existing expense database."""
    return sqlite3.connect(DATABASE_PATH)


def add_expense():
    """Collect details and save a new expense."""
    description = input("Description: ").strip()
    category = input("Category: ").strip().title()

    if not description or not category:
        print("Description and category cannot be empty.")
        return

    try:
        amount = int(input("Amount (UGX): "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid whole-number amount.")
        return

    try:
        with connect_database() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO expenses
                    (description, category, amount, expense_date)
                VALUES (?, ?, ?, ?)
            """, (description, category, amount, date.today().isoformat()))

        print("Expense added successfully.")

    except sqlite3.Error as error:
        print(f"Database error: {error}")


def view_expenses():
    """Display all saved expenses."""
    try:
        with connect_database() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT id, description, category, amount, expense_date
                FROM expenses
                ORDER BY expense_date DESC, id DESC
            """)
            expenses = cursor.fetchall()

        if not expenses:
            print("No expenses found.")
            return

        total = 0
        print("\n========== ALL EXPENSES ==========")

        for expense_id, description, category, amount, expense_date in expenses:
            print(
                f"ID: {expense_id} | {description} | {category} | "
                f"UGX {amount:,} | {expense_date}"
            )
            total += amount

        print("----------------------------------")
        print(f"Records: {len(expenses)}")
        print(f"Total: UGX {total:,}")

    except sqlite3.Error as error:
        print(f"Database error: {error}")


def search_expenses():
    """Find expenses by category."""
    category = input("Enter category to search: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    try:
        with connect_database() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT id, description, category, amount, expense_date
                FROM expenses
                WHERE LOWER(category) = LOWER(?)
                ORDER BY expense_date DESC, id DESC
            """, (category,))
            expenses = cursor.fetchall()

        if not expenses:
            print("No expenses found in that category.")
            return

        total = 0
        for expense_id, description, expense_category, amount, expense_date in expenses:
            print(
                f"ID: {expense_id} | {description} | {expense_category} | "
                f"UGX {amount:,} | {expense_date}"
            )
            total += amount

        print(f"Category total: UGX {total:,}")

    except sqlite3.Error as error:
        print(f"Database error: {error}")


def update_expense():
    """Update an expense selected by ID."""
    try:
        expense_id = int(input("Enter the expense ID to update: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    try:
        with connect_database() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT description, category, amount
                FROM expenses
                WHERE id = ?
            """, (expense_id,))
            existing = cursor.fetchone()

            if existing is None:
                print("Expense not found.")
                return

            description, category, amount = existing
            print("Leave a field blank to keep its current value.")

            new_description = input(
                f"Description [{description}]: "
            ).strip() or description

            new_category = input(
                f"Category [{category}]: "
            ).strip()

            new_category = new_category.title() if new_category else category

            new_amount_text = input(f"Amount [{amount}]: ").strip()

            if new_amount_text:
                try:
                    new_amount = int(new_amount_text)
                    if new_amount <= 0:
                        print("Amount must be greater than zero.")
                        return
                except ValueError:
                    print("Please enter a valid whole-number amount.")
                    return
            else:
                new_amount = amount

            cursor.execute("""
                UPDATE expenses
                SET description = ?, category = ?, amount = ?
                WHERE id = ?
            """, (new_description, new_category, new_amount, expense_id))

        print("Expense updated successfully.")

    except sqlite3.Error as error:
        print(f"Database error: {error}")


def delete_expense():
    """Delete an expense after confirmation."""
    try:
        expense_id = int(input("Enter the expense ID to delete: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    try:
        with connect_database() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT description, category, amount
                FROM expenses
                WHERE id = ?
            """, (expense_id,))
            expense = cursor.fetchone()

            if expense is None:
                print("Expense not found.")
                return

            print(
                f"Selected: {expense[0]} | {expense[1]} | "
                f"UGX {expense[2]:,}"
            )

            confirmation = input("Confirm deletion? (yes/no): ").strip().lower()

            if confirmation != "yes":
                print("Deletion cancelled.")
                return

            cursor.execute(
                "DELETE FROM expenses WHERE id = ?",
                (expense_id,)
            )

        print("Expense deleted successfully.")

    except sqlite3.Error as error:
        print(f"Database error: {error}")


def show_summary():
    """Display total spending and spending by category."""
    try:
        with connect_database() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT COUNT(*), COALESCE(SUM(amount), 0), AVG(amount)
                FROM expenses
            """)
            count, total, average = cursor.fetchone()

            print("\n========== EXPENSE SUMMARY ==========")
            print(f"Number of expenses: {count}")
            print(f"Total expenditure: UGX {total:,}")

            if count:
                print(f"Average expense: UGX {average:,.2f}")

            cursor.execute("""
                SELECT category, SUM(amount)
                FROM expenses
                GROUP BY category
                ORDER BY SUM(amount) DESC
            """)
            categories = cursor.fetchall()

            print("\nSpending by category:")
            if categories:
                for category, amount in categories:
                    print(f"{category}: UGX {amount:,}")
            else:
                print("No expenses recorded.")

    except sqlite3.Error as error:
        print(f"Database error: {error}")


def main():
    """Display the menu and handle user choices."""
    while True:
        print("\n====== EXPENSE TRACKER ======")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Search by category")
        print("4. Update expense")
        print("5. Delete expense")
        print("6. Expense summary")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_expenses()
        elif choice == "4":
            update_expense()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            show_summary()
        elif choice == "0":
            print("Thank you for using Expense Tracker.")
            break
        else:
            print("Invalid choice. Please select an option from the menu.")


if __name__ == "__main__":
    main()
