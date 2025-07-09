import mysql.connector

# Replace these values with your MySQL server and database information
host = "localhost"
user = "root"
password = "root"
database_name = "instagram"

# Connect to MySQL server and select the database
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database_name
)

# Create a cursor object to interact with the MySQL server
cursor = connection.cursor()

# Replace 'your_table_name' with the name of the table where you want to update data
table_name = 'users'

# SQL query to update data in the table
update_data_query = f"""
UPDATE {table_name}
SET age = %s, email = %s
WHERE name = %s
"""

# Replace these values with the updated data
updated_data = (28, "john.doe@example.com", "John Doe")

try:
    # Execute the query
    cursor.execute(update_data_query, updated_data)

    # Commit the changes
    connection.commit()

    print("Data updated successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
