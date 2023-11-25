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

# Replace 'your_table_name' with the name of the table from which you want to retrieve data
table_name = 'your_table_name'

# SQL query to select specific data from the table
select_specific_data_query = f"SELECT * FROM {table_name} WHERE name = %s"

# Replace this value with the specific criteria for selecting data
criteria = ("John Doe",)

try:
    # Execute the query with the specified criteria
    cursor.execute(select_specific_data_query, criteria)

    # Fetch all the rows
    result = cursor.fetchall()

    # Print the retrieved data
    for row in result:
        print(row)
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
