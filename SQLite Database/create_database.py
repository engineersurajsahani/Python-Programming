import sqlite3

# This will create the database file if it doesn't exist
conn = sqlite3.connect('mydatabase.db')
conn.close()
print("Database created successfully.")
