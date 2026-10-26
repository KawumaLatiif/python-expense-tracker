
# Writing and reading a text file

file_name = "expense_notes.txt"

# Write text to a file.
with open(file_name, "w", encoding="utf-8") as file:
    file.write("Monthly expense report\n")
    file.write("Rent: UGX 200,000\n")
    file.write("Food: UGX 85,000\n")

print("Expense notes saved.")

# Read the file's contents.
with open(file_name, "r", encoding="utf-8") as file:
    contents = file.read()

print("\nSaved file contents:")
print(contents)
