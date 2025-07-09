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

# Replace 'your_table_name' with the desired table name
table_name = 'users'

# SQL query to create a new table
create_table_query = f"""
CREATE TABLE {table_name} (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    email VARCHAR(255)
)
"""

try:
    # Execute the query
    cursor.execute(create_table_query)
    print(f"Table '{table_name}' created successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
