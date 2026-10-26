import json
from pathlib import Path

# Store the data file beside this Python script so the program works
# no matter which directory it is run from.
file_path = Path(__file__).with_name("expenses.json")


def load_expenses():
    """Load existing records, or return an empty list."""
    # If the file is missing (e.g. first run), return an empty list so the
    # rest of the program can handle "no data" gracefully.
    if not file_path.exists():
        return []

    # Open the file explicitly as UTF-8 so descriptions with non-ASCII
    # characters are read consistently across platforms.
    with file_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    # Guard against a valid-JSON file that isn't a list (e.g. a single dict),
    # which would break the loops below.
    if not isinstance(data, list):
        raise ValueError("The expense file must contain a list.")

    return data


def total_spent(expenses):
    """Sum the amount of every expense record."""
    # A generator expression keeps this to one line and avoids building an
    # intermediate list of amounts.
    return sum(expense["amount"] for expense in expenses)


def most_expensive(expenses):
    """Return the single expense with the highest amount."""
    # max() with a key returns the whole record, not just the amount, so the
    # caller can still access description and category.
    return max(expenses, key=lambda expense: expense["amount"])


def category_totals(expenses):
    """Build a dictionary mapping each category to its total spending."""
    totals = {}

    for expense in expenses:
        category = expense["category"]
        # totals.get(category, 0) returns 0 for a category seen for the first
        # time, avoiding a KeyError and giving a natural running total.
        totals[category] = totals.get(category, 0) + expense["amount"]

    return totals


def top_categories(totals):
    """Return every category that shares the highest total.

    Ties are resolved by returning a list of all tied categories, so the
    report can name each one rather than silently picking a single winner.
    """
    # Find the highest total across all categories.
    highest = max(totals.values())

    # Collect every category whose total equals that highest value, which
    # naturally includes all members of a tie.
    return [category for category, amount in totals.items() if amount == highest]


def display_report(expenses):
    """Print the four required summary figures."""
    print("EXPENSE REPORT")
    print("=" * 40)

    # Handle the empty case before calling max() or dividing anything, so the
    # report stays clean when there are no records yet.
    if not expenses:
        print("No expense records found.")
        return

    # 1. Total number of records.
    print(f"Total records: {len(expenses)}")

    # 2. Total amount spent across all records.
    print(f"Total amount spent: UGX {total_spent(expenses):,.2f}")

    # 3. The single most expensive expense, showing description and category.
    priciest = most_expensive(expenses)
    print(
        f"Most expensive expense: {priciest['description']} "
        f"({priciest['category']}) - UGX {priciest['amount']:,.2f}"
    )

    # 4. The category (or categories) with the highest total spending.
    totals = category_totals(expenses)
    winners = top_categories(totals)
    # Every winner has the same total, so reading any of them gives the value.
    highest_total = totals[winners[0]]

    if len(winners) == 1:
        # Single clear winner: print it on one line.
        print(f"Highest spending category: {winners[0]} - UGX {highest_total:,.2f}")
    else:
        # Tie: list each tied category so no winner is hidden.
        print("Highest spending categories (tie):")
        for category in winners:
            print(f"  - {category}: UGX {totals[category]:,.2f}")
        print(f"  Each tied at UGX {highest_total:,.2f}")


def main():
    # Load the data inside a try block so malformed JSON or a non-list file
    # produces a readable message instead of a traceback.
    try:
        expenses = load_expenses()
    except (json.JSONDecodeError, ValueError) as error:
        print(f"Cannot load expenses: {error}")
        return

    display_report(expenses)


# Only run the report when executed directly, not when imported as a module.
if __name__ == "__main__":
    main()