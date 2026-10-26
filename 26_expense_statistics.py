
import sqlite3
from pathlib import Path

database_path = Path(__file__).with_name("expenses.db")


def show_expense_statistics():
    try:
        with sqlite3.connect(database_path) as connection:
            cursor = connection.cursor()

            cursor.execute("""
                SELECT
                    COUNT(*),
                    COALESCE(SUM(amount), 0),
                    AVG(amount),
                    MIN(amount),
                    MAX(amount)
                FROM expenses
            """)

            count, total, average, smallest, largest = cursor.fetchone()

            print("\n========== EXPENSE STATISTICS ==========")

            if count == 0:
                print("No expenses available for analysis.")
                return

            print(f"Number of expenses: {count}")
            print(f"Total expenditure: UGX {total:,}")
            print(f"Average expense: UGX {average:,.2f}")
            print(f"Smallest expense: UGX {smallest:,}")
            print(f"Largest expense: UGX {largest:,}")

            cursor.execute("""
                SELECT description, category, amount, expense_date
                FROM expenses
                ORDER BY amount DESC, id DESC
                LIMIT 1
            """)

            largest_expense = cursor.fetchone()

            print("\n------ LARGEST EXPENSE DETAILS ------")
            print(f"Description: {largest_expense[0]}")
            print(f"Category: {largest_expense[1]}")
            print(f"Amount: UGX {largest_expense[2]:,}")
            print(f"Date: {largest_expense[3]}")

            print("\n======================================")

    except sqlite3.Error as error:
        print(f"Database error: {error}")


if __name__ == "__main__":
    show_expense_statistics()
