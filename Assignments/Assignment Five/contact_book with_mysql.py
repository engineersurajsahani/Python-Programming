# Contact book using MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="mydatabase"
)

cursor = connection.cursor()

# Assuming 'contacts' table with columns 'name' and 'number'
cursor.execute("INSERT INTO contacts (name, number) VALUES (%s, %s)", ("John Doe", "123-456-7890"))

cursor.execute("SELECT * FROM contacts")
for row in cursor.fetchall():
    print(row)

connection.close()
