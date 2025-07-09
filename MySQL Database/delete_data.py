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

# Replace 'your_table_name' with the name of the table where you want to delete data
table_name = 'users'

# SQL query to delete data from the table
delete_data_query = f"""
DELETE FROM {table_name}
WHERE name = %s
"""

# Replace these values with the criteria for deleting data
data_to_delete = ("John Doe",)

try:
    # Execute the query
    cursor.execute(delete_data_query, data_to_delete)

    # Commit the changes
    connection.commit()

    print("Data deleted successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
