
# Representing one expense with a dictionary

expense = {
    "description": "Monthly rent",
    "category": "Housing",
    "amount": 200000,
    "date": "2026-10-01"
}

print("EXPENSE RECORD")
print("--------------")

print(f"Description: {expense['description']}")
print(f"Category: {expense['category']}")
print(f"Amount: UGX {expense['amount']:,}")
print(f"Date: {expense['date']}")

# Add a new field to the record.
expense["payment_method"] = "Mobile Money"

# Update an existing field.
expense["amount"] = 220000

print("\nUpdated expense:")
print(expense)
