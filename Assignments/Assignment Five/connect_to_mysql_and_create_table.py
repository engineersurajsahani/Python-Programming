# Connect to MySQL and create a table
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="mydatabase"
)

cursor = connection.cursor()
cursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")

connection.commit()
connection.close()
