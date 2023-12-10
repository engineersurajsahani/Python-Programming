# Query students from MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="mydatabase"
)

cursor = connection.cursor()
cursor.execute("SELECT name FROM students WHERE age >= 18")

for row in cursor.fetchall():
    print(row[0])

connection.close()
