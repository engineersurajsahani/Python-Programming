import sqlite3

def read_all_users():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

# Example usage
users = read_all_users()
for user in users:
    print(user)
