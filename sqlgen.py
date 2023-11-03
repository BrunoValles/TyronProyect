import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('employee_database.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Define the table structure for the employees
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    active BOOLEAN NOT NULL,
    employee_type TEXT NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
