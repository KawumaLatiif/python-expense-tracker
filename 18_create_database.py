
import sqlite3
from pathlib import Path

# Store the database beside this Python file.
database_path = Path(__file__).with_name("expenses.db")

# Connect to the database.
connection = sqlite3.connect(database_path)

# Create a cursor to execute SQL statements.
cursor = connection.cursor()

# Create the expenses table if it does not already exist.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        category TEXT NOT NULL,
        amount INTEGER NOT NULL CHECK (amount > 0),
        expense_date TEXT NOT NULL
    )
""")

# Save database changes.
connection.commit()

# Close the database connection.
connection.close()

print(f"Database created successfully: {database_path}")
