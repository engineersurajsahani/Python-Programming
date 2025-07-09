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

# Replace 'your_table_name' with the name of the table from which you want to retrieve data
table_name = 'users'

# SQL query to select data from the table
select_data_query = f"SELECT * FROM {table_name}"

try:
    # Execute the query
    cursor.execute(select_data_query)

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
