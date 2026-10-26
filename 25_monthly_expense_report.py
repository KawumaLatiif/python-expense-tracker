
import sqlite3
from pathlib import Path
from datetime import datetime

database_path = Path(__file__).with_name("expenses.db")


def get_month_and_year():
    """Request and validate a month and year."""
    while True:
        month_year = input(
            "Enter the month and year (YYYY-MM), e.g. 2026-10: "
        ).strip()

        try:
            datetime.strptime(month_year, "%Y-%m")
            return month_year

        except ValueError:
            print("Invalid format. Please use YYYY-MM, such as 2026-10.")


def show_monthly_report():
    month_year = get_month_and_year()

    try:
        with sqlite3.connect(database_path) as connection:
            cursor = connection.cursor()

            # Calculate the number of expenses and total for the month.
            cursor.execute("""
                SELECT COUNT(*), COALESCE(SUM(amount), 0)
                FROM expenses
                WHERE substr(expense_date, 1, 7) = ?
            """, (month_year,))

            total_records, total_amount = cursor.fetchone()

            print(f"\n========== REPORT FOR {month_year} ==========")
            print(f"Number of expenses: {total_records}")
            print(f"Total expenditure: UGX {total_amount:,}")

            # Calculate spending by category for the selected month.
            cursor.execute("""
                SELECT category, COUNT(*), SUM(amount)
                FROM expenses
                WHERE substr(expense_date, 1, 7) = ?
                GROUP BY category
                ORDER BY SUM(amount) DESC
            """, (month_year,))

            category_summaries = cursor.fetchall()

            if category_summaries:
                print("\n------ CATEGORY BREAKDOWN ------")

                for category, count, amount in category_summaries:
                    print(
                        f"{category}: UGX {amount:,} "
                        f"({count} expense(s))"
                    )
            else:
                print("\nNo expenses were recorded for this month.")

            print("\n=====================================")

    except sqlite3.Error as error:
        print(f"Database error: {error}")


if __name__ == "__main__":
    show_monthly_report()
