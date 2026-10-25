
# Functions for calculating expenses

def calculate_total(expenses):
    """Return the sum of all expenses."""
    return sum(expenses)


def calculate_balance(income, total_expenses):
    """Return income minus expenses."""
    return income - total_expenses


def display_report(income, expenses):
    """Calculate and display a financial report."""
    total = calculate_total(expenses)
    balance = calculate_balance(income, total)

    print("MONTHLY FINANCIAL REPORT")
    print("------------------------")
    print(f"Income: UGX {income:,}")
    print(f"Total expenses: UGX {total:,}")
    print(f"Remaining balance: UGX {balance:,}")


monthly_income = 800000
monthly_expenses = [200000, 120000, 60000, 40000]

display_report(monthly_income, monthly_expenses)
