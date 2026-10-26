
import sqlite3
from pathlib import Path

database_path = Path(__file__).with_name("expenses.db")


def show_expense_summary():
    try:
        with sqlite3.connect(database_path) as connection:
            cursor = connection.cursor()

            # Calculate the number of records and total expenditure.
            cursor.execute("""
                SELECT COUNT(*), COALESCE(SUM(amount), 0)
                FROM expenses
            """)

            total_records, total_amount = cursor.fetchone()

            print("\n========== EXPENSE SUMMARY ==========")
            print(f"Number of expenses: {total_records}")
            print(f"Total expenditure: UGX {total_amount:,}")

            # Calculate expenditure separately for each category.
            cursor.execute("""
                SELECT category, COUNT(*), SUM(amount)
                FROM expenses
                GROUP BY category
                ORDER BY SUM(amount) DESC
            """)

            category_summaries = cursor.fetchall()

            if category_summaries:
                print("\n------ EXPENDITURE BY CATEGORY ------")

                for category, count, amount in category_summaries:
                    print(
                        f"{category}: UGX {amount:,} "
                        f"({count} expense(s))"
                    )
            else:
                print("\nNo expenses have been recorded yet.")

            print("\n=====================================")

    except sqlite3.Error as error:
        print(f"Database error: {error}")


if __name__ == "__main__":
    show_expense_summary()
