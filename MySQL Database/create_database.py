import mysql.connector

# Replace these values with your MySQL server information
host = "your_host"
user = "your_username"
password = "your_password"

# Connect to MySQL server
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password
)

# Create a cursor object to interact with the MySQL server
cursor = connection.cursor()

# Replace 'your_database_name' with the desired database name
database_name = 'your_database_name'

# SQL query to create a new database
create_database_query = f"CREATE DATABASE {database_name}"

try:
    # Execute the query
    cursor.execute(create_database_query)
    print(f"Database '{database_name}' created successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
