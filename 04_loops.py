
# For loops and while loops

expenses = [50000, 30000, 25000, 40000]

print("Using a for loop:")

for expense in expenses:
    print(f"Expense: UGX {expense:,}")

print("\nUsing a loop with range:")

for number in range(1, 4):
    print(f"Expense number {number}")

print("\nUsing a while loop:")

count = 1

while count <= 3:
    print(f"Count: {count}")
    count = count + 1

print("Loop completed.")
