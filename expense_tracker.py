
# Personal Expense Tracker

def get_amount(prompt):
    """Collect a valid non-negative monetary amount."""
    while True:
        try:
            amount = float(input(prompt))

            if amount < 0:
                print("Amount cannot be negative.")
                continue

            return amount

        except ValueError:
            print("Please enter a valid number.")


def calculate_total(expenses):
    """Calculate the total of all recorded expenses."""
    return sum(expenses)


def display_summary(income, expenses):
    """Display the income, expenses and remaining balance."""
    total = calculate_total(expenses)
    balance = income - total

    print("\n========== FINANCIAL SUMMARY ==========")
    print(f"Monthly income:     UGX {income:,.0f}")
    print(f"Total expenses:     UGX {total:,.0f}")
    print(f"Remaining balance:  UGX {balance:,.0f}")

    if balance < 0:
        print("Warning: Your expenses exceed your income.")
    elif balance == 0:
        print("You have used all your income.")
    else:
        print("You have money remaining.")

    print("=======================================")


def main():
    """Run the expense tracker."""
    print("=======================================")
    print("          PERSONAL EXPENSE TRACKER")
    print("=======================================")

    income = get_amount("Enter your monthly income (UGX): ")
    expenses = []

    while True:
        try:
            count = int(input("How many expenses will you enter? "))

            if count < 0:
                print("Enter zero or a positive whole number.")
                continue

            break

        except ValueError:
            print("Enter a whole number, such as 3.")

    for number in range(1, count + 1):
        expense = get_amount(
            f"Enter expense {number} (UGX): "
        )
        expenses.append(expense)

    display_summary(income, expenses)


if __name__ == "__main__":
    main()
