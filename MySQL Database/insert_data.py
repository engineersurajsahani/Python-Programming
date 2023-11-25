import mysql.connector

# Replace these values with your MySQL server and database information
host = "your_host"
user = "your_username"
password = "your_password"
database_name = "your_database_name"

# Connect to MySQL server and select the database
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database_name
)

# Create a cursor object to interact with the MySQL server
cursor = connection.cursor()

# Replace 'your_table_name' with the name of the table where you want to insert data
table_name = 'your_table_name'

# SQL query to insert data into the table
insert_data_query = f"""
INSERT INTO {table_name} (name, age, email)
VALUES (%s, %s, %s)
"""

# Replace these values with the actual data you want to insert
data_to_insert = [
    ("John Doe", 25, "john@example.com"),
    ("Jane Smith", 30, "jane@example.com"),
    ("Bob Johnson", 22, "bob@example.com")
]

try:
    # Execute the query for each set of data
    cursor.executemany(insert_data_query, data_to_insert)

    # Commit the changes
    connection.commit()

    print("Data inserted successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
